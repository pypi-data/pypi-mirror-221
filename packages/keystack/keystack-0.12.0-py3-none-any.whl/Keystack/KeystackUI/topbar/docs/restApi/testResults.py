import os, json, traceback
from re import search
from shutil import rmtree, copytree
from pathlib import Path
from glob import glob 
from datetime import datetime 

from django.views import View
from django.http import JsonResponse, FileResponse, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from systemLogging import SystemLogsAssistant
from topbar.settings.accountMgmt.verifyLogin import verifyUserRole
from topbar.settings.accountMgmt.accountMgr import AccountMgr
from globalVars import GlobalVars, HtmlStatusCodes
from baseLibs import removeEmptyTestResultFolders
from keystackUtilities import makeFolder, mkdir2, readJson, readYaml, readFile, writeToJson, execSubprocessInShellMode
from topbar.docs.restApi.controllers import getMainAndRemoteControllerIp, executeRestApiOnRemoteController
from execRestApi import ExecRestApi


class Vars:
    webpage = 'testResults'
    

class SidebarTestResults(APIView):
    @verifyUserRole()
    def post(self, request):
        """
        For sidebar test resuls and archive results
        
        whichResults <str>: activeResults|archiveResults
        
        {% for group, playbookList in allPlaybookTestResultFoldersForSidebar.activeResults.items %}
            <span class="pb-2 pt-2 marginLeft10 textBlack fontSize12px">Group: {{group}}</span>

            {% for playbookPath in playbookList %}
                <!-- Notes: url testResults takes you to testResults.views -->
                <a class="collapse-item pt-2 pl-3 fontSize12px" href="{% url "testResults" %}?resultFolderPath={{playbookPath}}&typeOfResult=activeTestResults"><i class="fa-regular fa-folder pr-3 pt-1"></i>{% getPlaybookName playbookPath %}</a><br>
            {% endfor %}
            <br><br>
        {% endfor %}
        """
        remoteController = request.data.get('remoteController', None)
        mainControllerIp, remoteControllerIp, ipPort = getMainAndRemoteControllerIp(request, remoteController)
        user = AccountMgr().getRequestSessionUser(request)
        whichResult = request.data.get('whichResultType', None)
        htmlTestResults = ''
        status = 'success'
        statusCode = HtmlStatusCodes.success
        errorMsg = None
        
        if remoteControllerIp and remoteControllerIp != mainControllerIp:
            params = {'whichResultType': whichResult}
            restApi = '/api/v1/results/sidebarMenu'
            response, errorMsg = executeRestApiOnRemoteController('post', remoteControllerIp, ipPort, restApi, params, 
                                                                  user, webPage=Vars.webpage, action='SidebarTestResults')
            if errorMsg:
                status = 'failed'
                statusCode = HtmlStatusCodes.error
                Response(data={'testResults':htmlTestResults, 'status': 'failed', 'errorMsg': errorMsg}, status=HtmlStatusCodes.error)
            else:
                htmlTestResults = response.json()['testResults']
        else:        
            try:
                testResults = dict()
                testResults['activeResults'] = dict()
                testResults['archiveResults'] = dict()
                
                for groupPath in glob(f"{GlobalVars.resultsFolder}/GROUP*"):
                    group = groupPath.split('/')[-1].split('=')[-1]
                    testResults['activeResults'][group] = []
                    
                    # groupPath: /opt/KeystackTests/Results/GROUP=Default
                    for playbookPath in glob(f'{groupPath}/PLAYBOOK*'):
                        # /opt/KeystackTests/Results/GROUP=Default/PLAYBOOK=opt-KeystackTests-Playbooks-Samples-pythonSample.yml
                        testResults['activeResults'][group].append(playbookPath)
                        
                if os.path.exists(GlobalVars.archiveResultsFolder):
                    for groupPath in glob(f"{GlobalVars.archiveResultsFolder}/GROUP*"):
                        group = groupPath.split('/')[-1].split('=')[-1]
                        testResults['archiveResults'][group] = []
                        for playbookPath in glob(f'{groupPath}/PLAYBOOK*'):
                            testResults['archiveResults'][group].append(playbookPath)    
                
                htmlTestResults += '<center><p class="pt-3 pb-2 textBlack fontSize12px">Select a Playbook</p></center>'

                for group,playbookList in testResults[whichResult].items():
                    htmlTestResults += f'<p class="pl-2 pb-0 marginLeft10 textBlack fontSize12px">Test Group: {group}</p>'
                    htmlTestResults += '<p>'
                    
                    for playbookPath in playbookList:
                        # playbookPath -> /opt/KeystackTests/Results/GROUP=Default/PLAYBOOK=Samples-pythonSample
                        playbookName = playbookPath.split('/')[-1].split('=')[-1].replace('-', '/')
                        htmlTestResults += f'<a class="collapse-item fontSize12px" href="/testResults?resultFolderPath={playbookPath}&typeOfResult={whichResult}"><i class="fa-regular fa-folder pr-3"></i>{playbookName}</a>'
                        
                    htmlTestResults += '</p>'
                        
            except Exception as errMsg:
                erroMsg = str(errMsg)
                status = 'failed'
                statusCode = HtmlStatusCodes.error
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='GetTestResults', msgType='Error', msg=errMsg,
                                        forDetailLogs=f'{traceback.format_exc(None, errMsg)}')
        
        return Response(data={'status':status, 'errorMsg':errorMsg, 'testResults':htmlTestResults}, status=statusCode)


'''
class GetTestResultFileContents(APIView):
    @verifyUserRole()
    def get(self, request):
        """
        Selected to open a PDF file. Open PDF in a new tab. 
        The PDF link is created in the TestResult() class treewalk() function.
        """
        remoteController = request.data.get('remoteController', None)
        mainControllerIp, remoteControllerIp, ipPort = getMainAndRemoteControllerIp(request, remoteController)
        user = request.session['user']
        filePath = request.GET.get('testResultFile')
        filePath2 = request.data.get('testResultFile', None)
        from django.http import FileResponse
        
        if 'pdf' in filePath:
            #return FileResponse(open(filePath, 'rb'), content_type='application/pdf')
            return HttpResponse(open(filePath, 'rb'), content_type='application/pdf')
        else:
            #return FileResponse(open(filePath, 'rb'), content_type='text/plain')
            return HttpResponse(open(filePath, 'rb'), content_type='text/plain')
    
    @verifyUserRole()   
    def post(self, request):
        """
        Get file contents.
        This post is called by testResult.hmtl template in the readTestResultFile() <scripts>.
        
        The <a href="#" data=value="$file">

        Expect: <file path> and <file name> separated by dash
                Ex: /Keystack/Modules/LoadCore/GlobalVariables&globalVariables.yml
        """
        body = json.loads(request.body.decode('UTF-8'))
        filePath = body['testResultFile']
        fileExtension = filePath.split('/')[-1].split('.')[-1]
        user = AccountMgr().getRequestSessionUser(request)
        statusCode = HtmlStatusCodes.success
        error = None
        
        try:
            if fileExtension == 'zip':
                fileContents = ''
            
            elif fileExtension == 'pdf':
                from django.http import FileResponse
                return FileResponse(open(filePath, 'rb'), content_type='application/pdf', status=HtmlStatusCodes.success)
        
            else:
                with open(filePath) as fileObj:
                    contents = fileObj.read()
                    
                # Use <pre> to render the file format
                fileContents = f'<pre>{contents}</pre>'
            
        except Exception as errMsg:
            statusCode = HtmlStatusCodes.error
            status = 'failed'
            error = str(errMsg)
            SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='GetTestResultsContents', msgType='Error',
                            msg=f'Failed to open file contents for viewing: {filePath}', forDetailLogs=f'{traceback.format_exc(None, errMsg)}')


        
        return JsonResponse(data={'fileContents': fileContents, 'status': status, 'errorMsg': error}, content_type='application/json', status=statusCode)    
'''


class GetNestedFolderFiles(APIView):
    @verifyUserRole()
    def post(self, request):
        user = AccountMgr().getRequestSessionUser(request)
        remoteController = request.data.get('remoteController', None)
        mainControllerIp, remoteControllerIp, ipPort = getMainAndRemoteControllerIp(request, remoteController)
        
        nestedFolderPath = request.data.get('nestedFolderPath', None)
        insertToDivId = request.data.get('insertToDivId', None)
        status = 'success'
        errorMsg = None
        statusCode = HtmlStatusCodes.success
        html = ''
        caretName = None
        nestedFolderUniqueCounter = 200000
        
        import random
        randomNumber = str(random.sample(range(100,10000), 1)[0])
        caretName = f"caret{randomNumber}"
        
        if remoteControllerIp and remoteControllerIp != mainControllerIp:
            params = {'nestedFolderPath':nestedFolderPath, 'insertToDivId':insertToDivId}
            restApi = '/api/v1/results/nestedFolderFiles'
            response, errorMsg = executeRestApiOnRemoteController('post', remoteControllerIp, ipPort, restApi, params, 
                                                                  user, webPage=Vars.webpage, action='GetNestedFolderFiles')
            if errorMsg:
                return Response({'status': 'failed', 'errorMsg': errorMsg}, status=HtmlStatusCodes.error)
            else:
                html = response.json()['folderFiles']
                caretName = response.json()['caretName']
  
        else:                        
            for eachFile in glob(f'{nestedFolderPath}/*'):
                if os.path.isfile(eachFile):
                    filename = eachFile .split('/')[-1]
                    # Open the modifyFileModal and get the file contents                  
                    html += f'<li><a class="nav-link" href="#" onclick="getFileContents(this)" filePath="{eachFile}"  data-bs-toggle="modal" data-bs-target="#openFileModal"><i class="fa-regular fa-file pr-2"></i> {filename} </a></li>'
                
                if os.path.isdir(eachFile):
                    filename = eachFile.split('/')[-1]
                    nestedFolderDivId = f'insertNestedFolderFiles_{str(nestedFolderUniqueCounter)}'

                    html += f'<li><span class="{caretName}"><a class="nav-link" href="#" onclick="getNestedFolderFiles(this)" insertToDivId="#{nestedFolderDivId}" nestedFolderPath="{eachFile}"><i class="fa-regular fa-folder pr-2"></i> {filename}</a></span>'
                                    
                    html += f'<ul class="nested" id="{nestedFolderDivId}"></ul>'
                    html += '</li>'
                    nestedFolderUniqueCounter += 1

        return JsonResponse(data={'folderFiles':html, 'caretName': caretName, 'newVarName': f'newVar_{randomNumber}',
                            'status':status, 'errorMsg':errorMsg}, status=statusCode)
        

class GetTestResultPages(APIView):
    @verifyUserRole()
    def post(self, request):
        """
        When users go to a test results page, show page number buttons.
        The buttons will contain the amount of pages to show.
        
        The return html code goes in conjunction with getTestResultTreeView.css.
        
        Requirements:
            - CSS: <link href={% static "commons/css/testResultsTreeView.css" %} rel="stylesheet" type="text/css">
            - html template needs to call addListeners() and getFileContents()
        """        
        user = AccountMgr().getRequestSessionUser(request)
        statusCode = HtmlStatusCodes.success
        status = 'success'
        errorMsg = None

        # 192.168.28.17:443
        remoteController = request.data.get('remoteController', None)
        mainControllerIp, remoteControllerIp, ipPort = getMainAndRemoteControllerIp(request, remoteController)

        # /opt/KeystackTests/Results/GROUP=Default/PLAYBOOK=pythonSample
        # /opt/KeystackTests/ResultsArchive/GROUP=ho/PLAYBOOK=pythonSample
        resultFolderPath = request.data.get('resultFolderPath', None)
        
        # ['0:2'] <-- In a list
        pageIndexRangeOriginal = request.data.get('pageIndexRange')
        pageIndexRange = pageIndexRangeOriginal[0]
        
        # The page number to get
        getPageNumber = request.data.get('getPageNumber')
        
        getResultsPerPage = request.data.get('getResultsPerPage', 25)
        
        # ADDED
        pageIndex = request.data.get('pageIndex', None)
        pageIndex = int(pageIndex)
        
        indexStart = int(pageIndexRange.split(':')[0])
        indexEnd = int(pageIndexRange.split(':')[1])
        testResultTimestampFolders = []
        startingRange = pageIndexRange.split(":")[0]
        
        if remoteControllerIp and remoteControllerIp != mainControllerIp:
            params = {'resultFolderPath':resultFolderPath, 'pageIndexRange':pageIndexRangeOriginal, 'getPageNumber':getPageNumber,
                      'getResultsPerPage':getResultsPerPage, 'pageIndex':pageIndex}
            restApi = '/api/v1/results/pages'
            response, errorMsg = executeRestApiOnRemoteController('post', remoteControllerIp, ipPort, restApi, params, 
                                                                  user, webPage=Vars.webpage, action='GetTestResultPages')
            if errorMsg:
                return Response({'status': 'failed', 'errorMsg': errorMsg, 'pages': ''}, status=HtmlStatusCodes.error)
        
            return JsonResponse(data={'pages': response.json()['pages'], 'status':status, 'errorMsg':errorMsg}, status=statusCode)
            
        else:
                            
            try:
                testResultTimestampFolders = glob(f'{resultFolderPath}/*')
            except:
                errorMsg = f'The result folder path is removed: {resultFolderPath}'
                status = HtmlStatusCodes.error

            # Get test results in a reversed list
            datetimeList = []
            for eachTimestampFolder in testResultTimestampFolders:
                datetimeList.append(eachTimestampFolder)
                
            # Got a sorted list
            datetimeList = list(reversed(sorted(datetimeList, key=lambda fileName: datetime.strptime(fileName.split('/')[-1].split('_')[0], "%m-%d-%Y-%H:%M:%S:%f"))))

            totalResults = len(testResultTimestampFolders)
            # Get round rounter
            #resultsPerPage =  round(totalResults / getResultsPerPage)
            # Get remainders using %.  Remainders go on the last page.
            #remainders = totalResults % getResultsPerPage        

            ''' 
            getTestResultsPages: totalResults: 5
            resultsPerPage: 2
            remainders: 1
            --- Page:1  0:2
            --- Page:2  2:4
            --- Page:3  4:6
            {1: (0, 2), 2: (2, 4), 3: (4, -1)}
            '''
            # Create the page buttons
            pages = dict()
            
            if pageIndex == int(pageIndexRange.split(":")[0]):
                resultsPerPageDropdown = f'<label for="resultsPerPage">Results Per Page: </label> <select id="resultsPerPage" onchange="setResultsPerPage(this)">'
                for option in [10, 25, 50, 100]:
                    #selectOption = f'<option value="{option}" abc>{option}</option>'
                    
                    if int(option) == int(getResultsPerPage):
                        resultsPerPageDropdown += f'<option value="{option}" selected="selected">{option}</option>'
                    else:
                        resultsPerPageDropdown += f'<option value="{option}">{option}</option>'
        
                resultsPerPageDropdown += f'</select>'

                pageButtons = f'{resultsPerPageDropdown} &emsp; Current Page: {getPageNumber} &emsp; Pages: &ensp;'
            else:
                pageButtons = ''
                
            if pageIndex == int(pageIndexRange.split(":")[0]):
                for index,startingIndex in enumerate(range(0, totalResults, getResultsPerPage)):
                    pageNumber = index+1
                    endingIndex = startingIndex + getResultsPerPage

                    if pageNumber > 1 and endingIndex == totalResults:
                        # Don't create a 2nd page button if there's only 1 page of results to show
                        #pages[pageNumber] = (startingIndex, -1)
                        pages[pageNumber] = (startingIndex, totalResults)
                        pageButtons += f'<button type="button" class="btn btn-outline-primary" onclick="getTestResultPages(this)" getPageNumber="{pageNumber}" pageIndexRange="{startingIndex}:{totalResults}">{pageNumber}</button>&ensp;'
                    else:
                        # if endingIndex != totalResults:
                        pages[pageNumber] = (startingIndex, endingIndex)
                        pageButtons += f'<button type="button" class="btn btn-outline-primary" onclick="getTestResultPages(this)" getPageNumber="{pageNumber}" pageIndexRange="{startingIndex}:{endingIndex}">{pageNumber}</button>&ensp;' 

                    
            class getPagesVars:
                counter = 0
                jsonCounter = 0
                htmlPageButtons = f'{pageButtons}<br><br>'
                
                if pageIndex == int(pageIndexRange.split(":")[0]):
                    html = f'{pageButtons}<br><br> <ul id="testResultFileTree">'
                else:
                    html = f'<ul id="testResultFileTree">'
                            
            """
            https://www.w3schools.com/howto/howto_js_treeview.asp
            
            <ul id="myUL">
                <li><span class="caret">Beverages</span>
                    <ul class="nested">
                        <li>Water</li>
                        <li>Coffee</li>
                        <li><span class="caret">Tea</span>
                            <ul class="nested">
                                <li>Black Tea</li>
                                <li>White Tea</li>
                                <li><span class="caret">Green Tea</span>
                                    <ul class="nested">
                                        <li>Sencha</li>
                                        <li>Gyokuro</li>
                                        <li>Matcha</li>
                                        <li>Pi Lo Chun</li>
                                    </ul>
                                </li>
                            </ul>
                        </li>
                    </ul>
                </li>
            </ul>
            """
            
            for index in range(indexStart, indexEnd):
                if pageIndex != index:
                    continue
                
                # The last page could have less than the calculated pages.
                # Just break out of the loop if there is no more results left to get.
                try:
                    eachResultFolderFullPath = datetimeList[index]
                except:
                    break
                        
                # eachResultFolderFullPath: /opt/KeystackTests/Results/GROUP=Default/PLAYBOOK=pythonSample/12-20-2022-18:00:49:300483_2054
                timestampResultFolder = eachResultFolderFullPath.split('/')[-1]
                started = ''
                stopped = ''
                testResult = ''
                testStatus = ''
                totalTestAborted = 0
                totalCases = ''
                totalFailed = 0
                user = ''
                
                getPagesVars.counter = 0
                                    
                if os.path.exists(f'{eachResultFolderFullPath}/overallSummary.json'):
                    statusJsonFile = readJson(f'{eachResultFolderFullPath}/overallSummary.json')
                    getPagesVars.jsonCounter += 1
                    
                    started = statusJsonFile['started']
                    stopped = statusJsonFile['stopped']
                    testResult = statusJsonFile['result']
                    testStatus = statusJsonFile['status']
                    totalTestAborted = statusJsonFile['totalTestAborted']
                    totalCases = statusJsonFile['totalCases']
                    totalFailed = statusJsonFile['totalFailed']
                    user = statusJsonFile['user']

                # Starting <li>:  Top-level timestamp result folders

                # When user clicks on the download button, the <form action="{% url 'testResults' %}" method="post"> will be directed.
                # Using name="downloadTestResults" to get the value
                getPagesVars.html += f'\n\t\t\t<li><input type="checkbox" name="testResultCheckbox" value="{eachResultFolderFullPath}" />&emsp;<button type=submit class="btn btn-sm btn-outline-primary p-0 px-2" style="height:20px" id="getSelectedTestResult" name="downloadTestResults" value={eachResultFolderFullPath}><i class="fas fa-cloud-arrow-down"></i></button><span class="caret2">&ensp;<a class="nav-link" style="display:inline-block" href="#"><i class="fa-regular fa-folder pr-2"></i>{timestampResultFolder}&emsp;User:{user}&emsp;Result:{testResult}&emsp;Status:{testStatus}&emsp;TotalCases:{totalCases}&emsp;TotalFailed:{totalFailed}&emsp;TotalAborted:{totalTestAborted}</a></span>'
                                
                def loop(path, init=False):
                    """ 
                    Create nested menu tree.  var.counter keeps track
                    of the amount of nested menus so it knows the 
                    amount of </li></ul> to close at the end.
                    
                    <li><span class="caret">Green Tea</span>
                        <ul class="nested">
                            <li>Sencha</li>
                            <li>Gyokuro</li>
                            <li>Matcha</li>
                            <li>Pi Lo Chun</li>
                    """
                    if init == True:
                        path = eachResultFolderFullPath
                    
                    if init == False:
                        folderName = path.split('/')[-1]
                        getPagesVars.html += f'<li style="margin-left:17px"><span class="caret2"><i class="fa-regular fa-folder pr-2"></i>{folderName}</span>'  
                        
                    getPagesVars.html += '<ul class="nested">'
                    getPagesVars.counter += 1
                                
                    for eachFile in glob(f'{path}/*'):
                        if os.path.isfile(eachFile):
                            filename = eachFile .split('/')[-1]
                            # Open the modifyFileModal and get the file contents 
                            if '.pdf' in eachFile:
                                # User clicks on pdf file, getTestResultFileContents uses Django's FileResponse to read the PDF file and display it in a new tab
                                getPagesVars.html += f'<li><a class="nav-link" href="/testResults/getTestResultFileContents?testResultFile={eachFile}" target="_blank"><i class="fa-regular fa-file pr-2"></i>{filename}</a></li>'
                            else:                 
                                getPagesVars.html += f'<li><a class="nav-link" href="#" onclick="getFileContents(this)" filePath="{eachFile}" data-bs-toggle="modal" data-bs-target="#openFileModal"><i class="fa-regular fa-file pr-2"></i> {filename} </a></li>'
                    
                    for eachFolder in glob(f'{path}/*'):        
                        if os.path.isdir(eachFolder):
                            loop(eachFolder, init=False)
                            getPagesVars.html += '</li></ul>'
                            getPagesVars.counter -= 1
                    
                loop(eachResultFolderFullPath, init=True)
                
                for x in range(0, getPagesVars.counter):
                    getPagesVars.html += '</ul></li>'
                    
                getPagesVars.html += '</li>'
                        
            getPagesVars.html += '</ul>'
                
            return JsonResponse(data={'pages':getPagesVars.html, 'status':status, 'errorMsg':errorMsg}, status=statusCode)
        
            
class DeleteResults(APIView):
    @verifyUserRole(webPage=Vars.webpage, action='DeleteTestResults', exclude=['engineer'])
    def post(self,request):
        """
        Delete test results
        
        Delete is called by Javascript fetch.
        
        TODO: Don't delete active test
        """
        remoteController = request.data.get('remoteController', None)
        mainControllerIp, remoteControllerIp, ipPort = getMainAndRemoteControllerIp(request, remoteController)
        user = AccountMgr().getRequestSessionUser(request)
        status = 'success'
        errorMsg = None
        statusCode = HtmlStatusCodes.success

        try:
            # Using json.loads() to convert into a list
            deleteTestResults = request.data.get('deleteTestResults')
        except:
            deleteTestResults = False

        if remoteControllerIp and remoteControllerIp != mainControllerIp:
            params = {"deleteTestResults": deleteTestResults}
            restApi = '/api/v1/results/delete'
            response, errorMsg = executeRestApiOnRemoteController('post', remoteControllerIp, ipPort, restApi, params, 
                                                                  user, webPage=Vars.webpage, action='DeleteResults')
            if errorMsg:
                status = 'failed'
                statusCode = HtmlStatusCodes.error
        
        else:  
            if deleteTestResults:
                # {'deleteTestResults': ['/opt/KeystackTests/Results/GROUP=QA/PLAYBOOK=pythonSample/10-15-2022-17:42:49:516252_qa']}
                statusCode = self.deleteTestResultFolders(deleteTestResults, user)
                
                if statusCode == HtmlStatusCodes.error:
                    status = 'failed'
                else:
                    status = 'success'
                    
        return Response({'status':status, 'errorMsg': errorMsg}, status=statusCode)

    def deleteTestResultFolders(self, deleteTestResults, user):            
        try:
            deletedResultList = []
            for resultFolder in deleteTestResults:
                # resultFolder: /opt/KeystackTests/Results/GROUP=Default/PLAYBOOK=pythonSample/10-26-2022-14:42:25:471305_809                
                rmtree(resultFolder)
                deletedResultList.append(resultFolder)
                removeEmptyTestResultFolders(user, resultFolder)

            HtmlStatusCodes.success
            if deletedResultList:
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='DeleteTestResults',
                                          msgType='Info', msg=f'Deleted results: {deletedResultList}')
            
            statusCode = HtmlStatusCodes.success 
            
        except Exception as errMsg:
            statusCode = HtmlStatusCodes.error
            SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='DeleteTestResults', 
                                      msgType='Error', msg=errMsg, 
                                      forDetailLogs=f'DeleteTestResults: {traceback.format_exc(None, errMsg)}')
            
        return statusCode        
 

class DeleteAllInGroup(APIView):
    @verifyUserRole(webPage=Vars.webpage, action='DeleteAllInGroup', exclude=['engineer'])
    def post(self, request):
        """
        Delete all test results in GROUP=<groupName>
        
        TODO: Don't delete active test
        """
        remoteController = request.data.get('remoteController', None)
        mainControllerIp, remoteControllerIp, ipPort = getMainAndRemoteControllerIp(request, remoteController)
        user = AccountMgr().getRequestSessionUser(request)
        statusCode = HtmlStatusCodes.success
        status = 'success'
        errorMsg = None
        
        # /opt/KeystackTests/Results/GROUP=Default
        group = request.data.get('group', None)
        
        if remoteControllerIp and remoteControllerIp != mainControllerIp:
            params = {"group":group}
            restApi = '/api/v1/results/deleteAllInGroup'
            response, errorMsg = executeRestApiOnRemoteController('post', remoteControllerIp, ipPort, restApi, params, 
                                                                  user, webPage=Vars.webpage, action='DeleteAllInGroup') 
            if errorMsg:
                status = 'failed'
                statusCode = HtmlStatusCodes.error           
        else:
            try:
                cmd = f'rm -rf {GlobalVars.keystackTestRootPath}/Results/GROUP={group}'
                execSubprocessInShellMode(cmd)
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='DeleteAllInGroup', msgType='Info',
                                        msg=cmd, forDetailLogs='')
            except Exception as errMsg:
                statusCode = HtmlStatusCodes.error
                erroMsg = str(errMsg)
                status = 'failed'
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='DeleteAllInGroup', msgType='Error',
                                        msg=cmd, forDetailLogs=errorMsg)
                
        return JsonResponse({'status':status, 'errorMsg':errorMsg}, status=statusCode)


class DeleteAllInPlaybook(APIView):
    @verifyUserRole(webPage=Vars.webpage, action='DeleteAllInPlaybook', exclude=['engineer'])
    def post(self, request):
        """
        Delete all test results in GROUP=<groupName>/PLAYBOOK=<playbookName>

        """
        user = AccountMgr().getRequestSessionUser(request)
        statusCode = HtmlStatusCodes.success
        status = 'success'
        errorMsg = None
        remoteController = request.data.get('remoteController', None)
        mainControllerIp, remoteControllerIp, ipPort = getMainAndRemoteControllerIp(request, remoteController)
        
        # /opt/KeystackTests/Results/GROUP=Default
        path = request.data.get('path', None)
        
        if remoteControllerIp and remoteControllerIp != mainControllerIp:
            params = {"path":path}
            restApi = '/api/v1/results/deleteAllInPlaybook'
            response, errorMsg = executeRestApiOnRemoteController('post', remoteControllerIp, ipPort, restApi, params, 
                                                                  user, webPage=Vars.webpage, action='DeleteAllResultsInPlaybook') 
            if errorMsg:
                status = 'failed'
                statusCode = HtmlStatusCodes.error   
        else:    
            try:
                cmd = f'rm -rf {path}'
                execSubprocessInShellMode(cmd)
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='DeleteAllResultsInPlaybook', msgType='Info',
                                        msg=cmd, forDetailLogs='')
            except Exception as errMsg:
                statusCode = HtmlStatusCodes.error
                erroMsg = str(errMsg)
                status = 'failed'
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='DeleteAllResultsInPlaybook', msgType='Error',
                                        msg=cmd, forDetailLogs=errorMsg)
             
        return JsonResponse(data={'status':status, 'errorMsg':errorMsg}, status=statusCode)
    
    
class DownloadResults(APIView):
    @verifyUserRole(webPage=Vars.webpage, action='DownloadTestResults')
    def post(self,request):
        """
        Download test results
        
        Download is called by <form action={% url "downloadResults" %}? method="POST">. 
        Get the getSelectedTestResult value from the <button name= value=>
        """
        user = AccountMgr().getRequestSessionUser(request)
        status = 'success'
        statusCode = HtmlStatusCodes.success
        errorMsg = None 
        
        # <form action="{% url 'downloadResults' %}" method="post"> style
        downloadTestResults = request.POST.get('downloadTestResults')
        remoteController = request.data.get('remoteController', None)
        mainControllerIp, remoteControllerIp, ipPort = getMainAndRemoteControllerIp(request, remoteController)
            
        if remoteControllerIp and remoteControllerIp != mainControllerIp:
            params = {"downloadTestResults": downloadTestResults}
            restApi = '/api/v1/results/downloadResults'
            response, errorMsg = executeRestApiOnRemoteController('post', remoteControllerIp, ipPort, restApi, params, 
                                                                  user, webPage=Vars.webpage, action='DownloadResults')  
            if errorMsg:
                status = 'failed'
                statusCode = HtmlStatusCodes.error  
            
            return response
        else:
            try:    
                # JS style
                return self.downloadTestResultFolder(downloadTestResults, user)
                
            except Exception as errMsg:
                errorMsg = str(errMsg)
                status = 'success'
                statusCode = HtmlStatusCodes.success
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='DownloadResults', msgType='Error', 
                                        msg=errorMsg, forDetailLogs=traceback.format_exc(None, errMsg))
                            
        #return Response({'status':status, 'errorMsg': errorMsg}, status=statusCode, content_type='application/json')
    
    def downloadTestResultFolder(self, downloadTestResults, user):
        """ 
        Download files to the client is done inside <form action="{% url 'testResults' %}" method="post"></form>
        It is a direct response back to the client.
        """
        import mimetypes
        import zipfile
        from shutil import make_archive
        
        tempFolderIsCreated = False
        currentDir = os.path.abspath(os.path.dirname(__file__))
        # /opt/Keystack/KeystackUI/sidebar/testResults/tempFolderToStoreZipFiles
        tempFolderToStoreZipFiles = f'{currentDir}/tempFolderToStoreZipFiles'

        # Create a temp folder first
        if os.path.exists(tempFolderToStoreZipFiles) == False:
            try:
                path = Path(tempFolderToStoreZipFiles)
                originalMask = os.umask(000)
                path.mkdir(mode=0o770, parents=True, exist_ok=True)
                os.umask(originalMask)
            except Exception as errMsg:
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='DownloadTestResults', msgType='Error', 
                                          msg="Internal failure: Create temp folder for storing zip file. Check detail logs.", 
                                          forDetailLogs=f'downloadTestResultsFolder(): {traceback.format_exc(None, errMsg)}')
                tempFolderIsCreated = False
        else:
            tempFolderIsCreated = True
            
        if tempFolderIsCreated:     
            try:
                filename = downloadTestResults.split('/')[-1]
                pathToResultFolder = downloadTestResults.replace(filename, '')  # For FileResponse()
                destZipFilename = f'{tempFolderToStoreZipFiles}/{filename}'     # No .zip extension
                zipFileFullPath = f'{destZipFilename}.zip'                      # /full_path/file.zip for os.remove()
                zipFilename = f'{filename}.zip'                                 # zip file name for download filename
                make_archive(destZipFilename, 'zip', downloadTestResults)
                fileType, encoding = mimetypes.guess_type(zipFilename)
                
                if fileType is None:
                    fileType = 'application/octet-stream'

                #response = FileResponse(open(zipFileFullPath, 'rb'))
                response = HttpResponse(open(zipFileFullPath, 'rb'))
                response['Content-Type'] = fileType
                response['Content-Length'] = str(os.stat(zipFileFullPath).st_size)
                if encoding is not None:
                    response['Content-Encoding'] = encoding
                    
                response['Content-Disposition'] = f'attachment; filename={zipFilename}'
                
                #os.remove(zipFileFullPath)
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='DownloadTestResults', msgType='Info',
                                          msg=f'Downloaded results: {zipFilename}')
                return response
            
            except Exception as errMsg:
                SystemLogsAssistant().log(user=user, webPage='results', action='DownloadTestResults', msgType='Error', 
                                msg="Failed to create downloadable zip file. Check detail logs.", 
                                forDetailLogs=f'{traceback.format_exc(None, errMsg)}')
                statusCode = HtmlStatusCodes.error
        else:
            statusCode = HtmlStatusCodes.error
                    
           
class ArchiveResults(APIView):
    @verifyUserRole()
    def post(self,request):
        """ 
        Archive results
        """
        user = AccountMgr().getRequestSessionUser(request)
        # /opt/KeystackTests/Results/PLAYBOOK=pythonSample/09-27-2022-08:17:44:760556_hgee2
        # resultsPathList: ['/opt/KeystackTests/Results/GROUP=QA/PLAYBOOK=pythonSample/10-14-2022-13:05:25:612106_hgee_debugMode']
        resultsPathList = request.data.get('results', [])
        playbookFolderName = None
        statusCode = HtmlStatusCodes.success
        status = 'success'
        errorMsg = None
        activeResultsPath = f"{GlobalVars.keystackTestRootPath}/Results"
        archiveResultsPath = f"{GlobalVars.keystackTestRootPath}/ResultsArchive"
        remoteController = request.data.get('remoteController', None)
        mainControllerIp, remoteControllerIp, ipPort = getMainAndRemoteControllerIp(request, remoteController)

        if remoteControllerIp and remoteControllerIp != mainControllerIp:
            params = {"results": resultsPathList}
            restApi = '/api/v1/results/archive'
            response, errorMsg = executeRestApiOnRemoteController('post', remoteControllerIp, ipPort, restApi, params, 
                                                                  user, webPage=Vars.webpage, action='ArchiveResults')
            if errorMsg:
                status = 'failed'
                statusCode = HtmlStatusCodes.error 
                   
        else:           
            if os.path.exists(archiveResultsPath) == False:
                makeFolder(targetPath=archiveResultsPath, permission=0o770, stdout=False)
                execSubprocessInShellMode(f'chown -R {GlobalVars.user}:{GlobalVars.userGroup} {archiveResultsPath}', showStdout=False)
                                    
            for resultsPath in resultsPathList:
                # ['/opt/KeystackTests/Results/GROUP=QA/PLAYBOOK=pythonSample/10-14-2022-13:05:25:612106_hgee_debugMode']
                try:
                    match = search('.*/(GROUP=.+)/(PLAYBOOK=.+)/(.+)', resultsPath)
                    if match:
                        group = match.group(1)
                        playbook = match.group(2)
                        timestampResults = match.group(3)
                        destination = f'{archiveResultsPath}/{group}/{playbook}/{timestampResults}'
                        
                        if os.path.exists(destination) == False:
                            mkdir2(destination)
                            
                        #print(f'\nArchiveResults: resultsPath={resultsPath} -> dest={destination}\n')   
                        
                        copytree(resultsPath, destination, dirs_exist_ok=True)
                        # Remove the results from the active test results
                        rmtree(resultsPath)
                        removeEmptyTestResultFolders(user, resultsPath)
                        execSubprocessInShellMode(f'chown -R {GlobalVars.user}:{GlobalVars.userGroup} {destination}', showStdout=False)

                        SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='ArchiveResults', 
                                                msgType='Info', msg=f'results:{resultsPath}')
                    
                except Exception as errMsg:
                    status = 'failed'
                    errorMsg = str(errMsg)
                    statusCode = HtmlStatusCodes.error
                    SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='ArchiveResults', msgType='Error',
                                            msg=f'results:{resultsPath}: {traceback.format_exc(None, errMsg)}')
                
        return Response(data={'status':status, 'errorMsg':errorMsg}, status=statusCode)
