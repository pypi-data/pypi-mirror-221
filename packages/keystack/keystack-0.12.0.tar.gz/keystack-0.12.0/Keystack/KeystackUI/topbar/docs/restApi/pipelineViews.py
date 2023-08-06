import os, json, traceback
from glob import glob
from datetime import datetime
from re import search, match

from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from systemLogging import SystemLogsAssistant
from topbar.settings.accountMgmt.verifyLogin import verifyUserRole
from topbar.docs.restApi.accountMgr import AccountMgr
from topbar.docs.restApi.controllers import getMainAndRemoteControllerIp, executeRestApiOnRemoteController
from execRestApi import ExecRestApi
from globalVars import GlobalVars, HtmlStatusCodes
from EnvMgmt import ManageEnv
from baseLibs import removeEmptyTestResultFolders, getGroupSessions
from keystackUtilities import readJson, readYaml, readFile, writeToJson, writeToYamlFile, mkdir2, chownChmodFolder, execSubprocessInShellMode

class Vars:
    """ 
    For logging the correct log topic.
    To avoid human typo error and be consistant
    """
    webpage = 'pipelines'
    

def getPipelines():
    return glob(f'{GlobalVars.pipelineFolder}/*.yml')

def getTableData(view="current", group='Default', user=''):
    """ 
    Get session status
    
    Parameters
        view: <str>: current | archive
    """
    tableData = ''
    
    if view == 'current':
        resultsPath = f'{GlobalVars.keystackTestRootPath}/Results'
    else:
        resultsPath = f'{GlobalVars.keystackTestRootPath}/ResultsArchive'
    
    index = 0
    overallDetails = dict()
    overallDetails['sessions'] = 0
    overallDetails['running'] = 0
    overallDetails['completed'] = 0
    overallDetails['pausedOnFailure'] = 0
    overallDetails['failed'] = 0
    overallDetails['passed'] = 0
    overallDetails['aborted'] = 0
    overallDetails['terminated'] = 0

    for playbookResults in glob(f'{resultsPath}/GROUP={group}/*'):
        # playbookResults: /opt/KeystackTests/ResultsArchive/GROUP=QA/PLAYBOOK=pythonSample
        if 'PLAYBOOK=' not in playbookResults:
            continue
        
        # ['/opt/KeystackTests/Results/GROUP=Default/PLAYBOOK=pythonSample/05-09-2023-18:19:06:538380_hgee', 
        #  '/opt/KeystackTests/Results/GROUP=Default/PLAYBOOK=pythonSample/05-09-2023-18:20:01:607913_hgee2']
        testResultTimestampFolders = glob(f'{playbookResults}/*')

        datetimeSortedList = list(reversed(sorted(testResultTimestampFolders, 
                                    key=lambda fileName: datetime.strptime(fileName.split('/')[-1].split('_')[0], "%m-%d-%Y-%H:%M:%S:%f"))))
                    
        for timestampResultsFullPath in datetimeSortedList:
            timestampResultFolder = timestampResultsFullPath.split('/')[-1]
            overallSummaryFile = f'{timestampResultsFullPath}/overallSummary.json'
            resultsMeta = f'{timestampResultsFullPath}/.Data/ResultsMeta'

            if os.path.exists(overallSummaryFile) == False:
                continue

            session = readJson(overallSummaryFile)
            index += 1
            
            try:
                processId = session['processId']
            except:
                processId = None    

            overallCurrentStatus = session['status']
            # /opt/KeystackTests/Playbooks/qa/pythonSample.yml
            playbookPath = session['playbook']
            # qa/pythonSample
            matchRegex = search(f'{GlobalVars.keystackTestRootPath}/Playbooks/(.+)\.y.+', playbookPath)
            if matchRegex:
                playbookNamespacePath = matchRegex.group(1)
            else:
                playbookNamespacePath = 'Unknown'

            resultsPath = session['topLevelResultFolder']
            timestampFolder = resultsPath.split('/')[-1]
            user = session['user']
            sessionId = timestampFolder
            holdEnvsIfFailed = session.get('holdEnvsIfFailed', False)
            setHoldEnvsIfFailed = False
            envIcon = ''
            
            overallDetails['sessions'] += 1
            if overallCurrentStatus == 'Completed':
                overallDetails['completed'] += 1
            if overallCurrentStatus in ['Aborted', 'StageFailAborted']:
                overallDetails['aborted'] += 1
            if overallCurrentStatus == 'Terminated':
                overallDetails['terminated'] += 1
            if overallCurrentStatus == 'Running':
                overallDetails['running'] += 1
            if session['result'] == 'Failed':
                overallDetails['failed'] += 1
            if session['result'] == 'Passed':
                overallDetails['passed'] += 1
                    
            # This runList will compare with ranList.
            # This is to show what is about to run and what already ran by comparing 
            # to the ranList created inside the for loop for moduleProperties below.
            runList = session['runList']
            
            # Start a new table row for each test
            tableData += '<tr class="bottomBorder">'
            tdProcessIdLink = ''
            tdStage  = '<td style="text-align:left;">'
            tdModule = '<td style="text-align:left;">'
            tdEnv =    '<td style="text-align:left;">'
            tdCurrentlyRunning = '<td style="text-align:left;">'
            tdProgress = '<td>'
            tdStatus =   '<td>'
            tdResult =   '<td>'
            tdLogs =     '<td>'
            
            # Get exception errors if any exists
            if os.path.exists(overallSummaryFile):
                overallSummaryData = readJson(overallSummaryFile)
                prestestErrors = ''

                if len(overallSummaryData["pretestErrors"]) > 0:
                    for line in overallSummaryData["pretestErrors"][0].split('\n'):
                        line = line.replace('"', '&quot;')
                        prestestErrors += f"{line}<br>"
            
            testAborted = False            
            # Getting in here means the test aborted.
            if len(glob(f'{timestampResultsFullPath}/STAGE=*')) == 0 or \
                prestestErrors != '':
                    testAborted = True                                                    
                    currentStatus = 'Aborted'   
                    tdProcessIdLink = f'<input type="checkbox" name="deleteSessionId" testResultsPath={timestampResultsFullPath} />'
                    tdStage    += ''
                    tdModule   += ''
                    tdEnv      += ''
                    tdProgress += ''
                    tdStatus   += f'<a href="#" exceptionError="{prestestErrors}" testLogResultPath="{timestampResultsFullPath}" onclick="openTestLogsModal(this)" data-bs-toggle="modal" data-bs-target="#testLogsModalDiv" class="blink">Aborted</a>'
                    tdResult   += ''
            
            ranList = []
            # Don't keep showing stage for all the modules. Just show stage name one time.
            stageTrackingForDisplay = ['']

            for eachRunningModule in glob(f'{timestampResultsFullPath}/STAGE=*'):
                # eachRunningModule:/opt/KeystackTests/Results/PLAYBOOK=pythonSample/07-08-2022-16:10:03:744673_qt8/STAGE=Test_MODULE=CustomPythonScripts_ENV=qa-pythonSample
                stageFolder = eachRunningModule.split('/')[-1]
                match = search('STAGE=(.+)_MODULE=(.+)_ENV=(.+)', eachRunningModule)
                if match is None:
                    continue

                currentStage = match.group(1)
                currentModule = match.group(2)
                currentEnv = match.group(3)
                if currentEnv in ['None', 'none', '']:
                    currentEnv = None

                try:
                    stage = currentStage
                    progress = ''
                    currentlyRunning = ''
                    env = ''
                    testToolSessionIdUrl = None
                    result = ''
                    resultReport = ''
                    deleteButton = ''
                    viewLogs = ''
                    processIdLink = ''
                    holdEnvOnFailure = 'No'
                    currentStatus = None
                    moduleSummaryData = ''
                    
                    # /KeystackTests/TestResults/SanityScripts/03-19-2022-16:48:02:764723_8598
                    moduleTestResultsPath = eachRunningModule
                    if os.path.exists(f'{moduleTestResultsPath}/moduleTestReport'):
                        testReportPath = f'{moduleTestResultsPath}/moduleTestReport'
                    else:
                        testReportPath = ''
                        
                    moduleSummaryFile = f'{moduleTestResultsPath}/moduleSummary.json'

                    if os.path.exists(moduleSummaryFile):
                        # Test might have started, but it aborted before the testcase began running
                        try:
                            moduleSummaryData = readJson(moduleSummaryFile)
                        except Exception as errMsg:  
                            #print('\nPipeline getTableData() ERROR:', traceback.format_exc(None, errMsg)) 
                            SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='GetPipelineData', msgType='Error',
                                                      msg=f'Pipeline aborted. Module summary file is malformed: {moduleSummaryFile}<br><br>{moduleSummaryData}', 
                                                      forDetailLogs=traceback.format_exc(None, errMsg))

                            exceptionMsg = f'Opening json moduleSummaryFile error: {moduleSummaryFile}: {errMsg}' 
                            addExceptionList = f'{prestestErrors}\n\n{exceptionMsg}'                   
                            currentStatus = 'Aborted'   
                            tdProcessIdLink = f'<input type="checkbox" name="deleteSessionId" testResultsPath={timestampResultsFullPath} />'
                            tdStage    += ''
                            tdModule   += ''
                            tdEnv      += ''
                            tdProgress += ''
                            tdStatus   += f'<a href="#" exceptionError="{addExceptionList}" testLogResultPath="{timestampResultsFullPath}" onclick="openTestLogsModal(this)" data-bs-toggle="modal" data-bs-target="#testLogsModalDiv">Aborted</a>'
                            tdResult   += ''
                            continue
                        
                        # Get all the module exception errors here so below areas could use it
                        moduleExceptionErrors = ''
                        if len(moduleSummaryData["exceptionErrors"]) > 0:
                            for line in moduleSummaryData["exceptionErrors"][0].split('\n'):
                                line = line.replace('"', '&quot;')
                                moduleExceptionErrors += f"{line}<br>"
                        addedExceptionErrors = f'Overall Exception:<br>{prestestErrors}<br><br>Module Exceptions:<br>{moduleExceptionErrors}'
                        addedExceptionErrors = f'Overall Exception:<br>{prestestErrors}'
                                                        
                        stage = currentStage
                        # env: qa/pythonSample
                        env = moduleSummaryData['env']
                        envFullPath = moduleSummaryData['envPath']
                        ranList.append({'stage': currentStage, 'module':currentModule, 'env': env})
                        
                        if moduleSummaryData['status'] == 'Did-Not-Start' and moduleSummaryData['loadBalanceGroup']:
                            # Waiting for an env from the load balance group.  Could be because all the envs are occupied.
                            env = 'Waiting-For-Env'
                        
                        isEnvParallelUsed = moduleSummaryData.get('isEnvParallelUsed', False)
                        
                        if env:
                            envIcon = ''
                            
                            if isEnvParallelUsed:
                                envIcon += f'<i class="fa-regular fa-circle-pause" title="parallelUsage=True" style="transform:rotate(90deg);"></i>&ensp;'
                                #envIcon += f'<i class="fa-solid fa-equals"></i>&ensp;'
                            else:
                                #envIcon += f'<i class="fa-solid fa-minus" ></i>&ensp;'
                                #envIcon += f'<i class="fa-solid fa-circle-minus" style="transform:rotate(90deg);"></i>&ensp;'
                                envIcon += f'<i class="fa-regular fa-circle-dot" title="parallelUsage=False"></i>&ensp;'
                            
                            if moduleSummaryData['loadBalanceGroup']:
                                envIcon += f'<i class="fa-solid fa-circle-half-stroke" title="LoadBalance=True"></i>'
                            else:
                                envIcon += f'<i class="fa-regular fa-circle" title="LoadBalance=False"></i>'
                        else:
                            envIcon = ''
                            env = ''
                                            
                        if 'progress' in moduleSummaryData:
                            progress = moduleSummaryData['progress']
                            
                        if 'currentlyRunning' in moduleSummaryData:
                            currentlyRunning = moduleSummaryData['currentlyRunning']
                            if currentlyRunning:
                                # /opt/KeystackTests/Modules/CustomPythonScripts/Samples/BridgeEnvParams/dynamicVariableSample.yml
                                currentlyRunning = currentlyRunning.split('/')[-1].split('.')[0] 
                            else:
                                currentlyRunning = ''
                        else:
                            currentlyRunning = ''
                            
                        if 'stopped' in moduleSummaryData and moduleSummaryData['stopped']:
                            stopped = ':'.join(moduleSummaryData['stopped'].split(':')[:-1])
                                                
                        result = moduleSummaryData['result']
                        resultReport = moduleSummaryData['result']
                        processIdLink = ''
                            
                        # Overall Status: Started | Did-Not-Start | Rebooting Agents | Loading Config File | Reconfiguring Config | Running 
                        #         Collecting Artifacts | Deleting Test Session
                        #         Completed | Aborted | Terminated
                        
                        if overallCurrentStatus not in ['Completed', 'Aborted', 'StageFailAborted', 'Terminated']:
                            currentlyRunningTestcase = moduleSummaryData['currentlyRunning']
                            if currentlyRunningTestcase:
                                # currentlyRunningTestcase could be None. There could be a ymal file error.
                                # /opt/KeystackTests/Modules/CustomPythonScripts/Samples/Testcases/bgp.yml
                                tcFile = f'{resultsMeta}{currentlyRunningTestcase}'
                                
                                for testcaseIterationFile in glob(f'{tcFile}/*'):
                                    testcaseIteration = readJson(tcFile)
                                    if testcaseIteration['status'] == 'Running':
                                        totalRunning += 1
                                        testToolSesisonIdUrl = testcaseIteration['testSessionId']
                                                                        
                            # Terminate is displayed because the is still running
                            processIdLink = f'<a href="#" style="text-decoration:none" sessionId={session["sessionId"]} playbook={session["playbook"]} module={currentModule} processId={processId} statusJsonFile={overallSummaryFile} onclick="terminateProcessId(this)">Terminate</a>'

                        if overallCurrentStatus in ['Completed', 'Aborted', 'StageFailAborted', 'Terminated']:            
                            if result in ['Failed', 'Error']:
                                resultColor = 'red'
                                setHoldEnvsIfFailed = True
                            else:
                                resultColor = 'blue'
                            
                            resultReport = f'<a href="#" style="color:{resultColor}" testReportPath={testReportPath} onclick="openTestResultModal(this)" data-bs-toggle="modal" data-bs-target="#testReportModalDiv">{result}</a>'                                
                        
                            # Delete is displayed because the test has stopped
                            processIdLink = f'<input type="checkbox" name="deleteSessionId" testResultsPath={timestampResultsFullPath} />'
                                                
                        if overallCurrentStatus in ['Aborted', 'StageFailAborted'] and result in ['Incomplete', 'Error']:
                            if os.path.exists(testReportPath):
                                with open(testReportPath, 'w') as fileObj:
                                    fileObj.write(str(json.dumps(moduleSummaryData, indent=4)))
                            
                            setHoldEnvsIfFailed = True
                            
                        viewLogs = f'<a href="#" exceptionError="" testLogResultPath="{moduleSummaryData["moduleResultsFolder"]}" onclick="openTestLogsModal(this)" data-bs-toggle="modal" data-bs-target="#testLogsModalDiv">Logs</a>'
                            
                        # Status
                        if testToolSessionIdUrl:
                            if moduleSummaryData["status"] not in ['Completed', 'Aborted', 'StageFailAborted', 'Did-Not-Start']:
                                if overallCurrentStatus != 'Terminated':
                                    currentStatus = f'<a class="blink" href={testToolSessionIdUrl} target="_blank" style="text-decoration:none;">{moduleSummaryData["status"]}</a>'
                                if overallCurrentStatus == 'Terminated' and moduleSummaryData["status"] == 'Running':
                                    currentStatus = 'Aborted'      
                            else:
                                if prestestErrors != '' or moduleExceptionErrors != '':
                                    currentStatus = f'<a href="#" exceptionError="{addedExceptionErrors}" testLogResultPath="{timestampResultsFullPath}" onclick="openTestLogsModal(this)" data-bs-toggle="modal" data-bs-target="#testLogsModalDiv">{moduleSummaryData["status"]}</a>'
                                else: 
                                    currentStatus = f'<a href={testToolSessionIdUrl} target="_blank">{moduleSummaryData["status"]}</a>'
                                setHoldEnvsIfFailed = True
                        else:
                            if moduleSummaryData["status"] not in ['Completed', 'Aborted', 'StageFailAborted', 'Did-Not-Start']:
                                # status = Running | Started
                                if overallCurrentStatus != 'Terminated':
                                    if testAborted:
                                        # Don't 
                                        currentStatus = f'<span class="blink">-{moduleSummaryData["status"]}</span>'
                                    else:
                                        currentStatus = f'<span class="blink">{moduleSummaryData["status"]}</span>'
                                        
                                if overallCurrentStatus == 'Terminated' and moduleSummaryData["status"] == 'Running':
                                    currentStatus = 'Aborted'
                            else:
                                if prestestErrors != '' or moduleExceptionErrors != '':
                                    currentStatus = f'<a href="#" exceptionError="{addedExceptionErrors}" testLogResultPath="{timestampResultsFullPath}" onclick="openTestLogsModal(this)" data-bs-toggle="modal" data-bs-target="#testLogsModalDiv">{moduleSummaryData["status"]}</a>'
                                else:   
                                    currentStatus = f'{moduleSummaryData["status"]}'
                                    
                                setHoldEnvsIfFailed = True
                    
                            # If paused-on-error, overwrite above status
                            if moduleSummaryData["status"] == 'paused-on-error':
                                overallDetails['pausedOnFailure'] += 1
                                currentStatus = f'<a href="#" class="blink" pausedOnErrorFile="{moduleTestResultsPath}/pausedOnError" onclick="resumePausedOnError(this)">Resume PausedOnError</a>'
                                
                        # If the test is terminated, moduleSummary.json status won't be set to Terminated.
                        # Use overallSummary data and get the moduleSummary['currentlyRunning'] to set the testcase status to terminated 
                        if overallCurrentStatus == 'Terminated':
                            if currentlyRunning or moduleSummaryData['status'] == 'Waiting-For-Env':
                                currentStatus = f'<span style="color:red">Terminated</span>'
                            
                except Exception as errMsg:
                    print('\nGetSession Exception:', traceback.format_exc(None, errMsg))
                    SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='GetPipelineData', msgType='Error',
                                            msg=f'getTableData(): {errMsg}', 
                                            forDetailLogs=traceback.format_exc(None, errMsg))

                tdProcessIdLink = f'{processIdLink}'

                if stageTrackingForDisplay[-1] != currentStage:
                    # <i class="fa-solid fa-circle-check"></i> | <i class="fa-solid fa-circle-xmark"></i> 
                    # <i class="fa-regular fa-circle">  | <i class="fa-solid fa-person-running"></i>
                    # <i class="fa-solid fa-dash"></i>  |  <i class="fas fa-circle-exclamation"></i>
                    # <i class="fa-solid fa-circle-notch"></i>
                    if session['stages'][stage]['result'] in ['Failed', 'Incomplete', 'Aborted']:
                        tdStage += '<strong><i class="fa-solid fa-circle-xmark textRed" title="Failed, Incomplete, Aborted"></i></strong>&emsp;'
                    elif session['stages'][stage]['result'] == 'Passed':
                        tdStage += '<i class="fa-solid fa-circle-check mainTextColor" title="Passed"></i>&emsp;' 
                    elif session['stages'][stage]['result'] == '':
                        # Running
                        #tdStage += '<i class="fa-solid fa-person-running"></i>'
                        tdStage += '<i class="sessionSpinningProgress"></i>'
                    else:
                        # Aborted
                        tdStage += '<i class="fa-solid fa-circle-notch" title="Not-Started, skipped or aborted"></i></i>&emsp;'
                            
                    tdStage  += f'{stage}<br>'
                else:
                    # Don't show the stage name again
                    tdStage  += '<br>'
                
                stageTrackingForDisplay.append(currentStage)
                if moduleSummaryData:
                    tdModule += f'<a style="text-decoration:none" href="/sessionMgmt/sessionDetails?testResultsPath={moduleSummaryData["moduleResultsFolder"]}">{currentModule}</a><br>'
                else:
                    tdModule += f'{currentModule}<br>'
                                            
                if currentStatus == "Completed" and 'Failed' in resultReport and holdEnvsIfFailed:
                    envMgmtDataFile = f'{timestampResultsFullPath}/.Data/EnvMgmt/STAGE={currentStage}_MODULE={currentModule}_ENV={currentEnv}.json'
                    envMgmtData = readJson(envMgmtDataFile)
                    
                    # envMgmtData:  {'user': 'hgee', 'sessionId': '05-25-2023-15:43:49:755851_2058', 'stage': 'Test', 'module': 'Demo2', 'env': 'Samples/hubert', 'envIsReleased': True, 'holdEnvsIfFailed': True, 'result': 'Failed'}
                    if isEnvParallelUsed == False and envMgmtData['envIsReleased'] == False:
                        # These envs failed and need to be released                        
                        # [{'user': 'hgee', 'sessionId': '11-15-2022-12:01:30:521184_hubogee', 'stage': 'Bringup', 'module': 'CustomPythonScripts', 'env': 'None'}, {'user': 'hgee', 'sessionId': '11-15-2022-12:01:30:521184_hubogee', 'stage': 'Test', 'module': 'CustomPythonScripts', 'env': 'pythonSample'},]
                        
                        # setups.views.ReleaseEnvsOnFailure() will clear out the Envs by pressing the releaseEnv button
                        tdEnv += f'<a href="#" class="blink" style="color:blue" user="{user}" sessionId="{timestampResultFolder}" stage="{currentStage}" module="{currentModule}" env="{env}" resultTimestampPath="{timestampResultsFullPath}" onclick="releaseEnvOnFailure(this)">{envIcon} ReleaseEnvOnHold:</a><span style="color:black">{env}</span><br>'
                    else:
                        #Passed | Aborted | Waiting
                        tdEnv += f'<a href="#" data-bs-toggle="modal" data-bs-target="#showEnvModal" onclick="showEnv(this)" envPath="{envFullPath}">{envIcon} {env}</a><br>'
                else:
                    tdEnv += f'<a href="#" data-bs-toggle="modal" data-bs-target="#showEnvModal" onclick="showEnv(this)" envPath="{envFullPath}">{envIcon} {env}<br></a>'
                
                tdCurrentlyRunning += f'{currentlyRunning}<br>'
                tdProgress += f'{progress}<br>'
                tdStatus   += f'{currentStatus}<br>'
                tdResult   += f'{resultReport}<br>'
                tdLogs     += f'{viewLogs}<br>'

            # print('\n--- runList:', runList)
            # print('\n---- ranList:', ranList)
            remainingList = [currentRuns for currentRuns in runList if currentRuns not in ranList]

            for x in remainingList:
                # Show what is about to run
                tdStage  += f'<i class="fa-solid fa-circle-notch" title="Aborted, Skipped or Did-Not-Start"></i></i>&emsp;{x["stage"]}<br>'
                tdModule += f'{x["module"]}<br>'
                tdEnv    += f'{envIcon} {x["env"]}<br>'
                if 'Aborted' not in tdStatus:
                    tdStatus += 'Not-Started<br>'
                
            # Create the pipeline        
            # processIdLink replaces Delete when it's active
            tableData += f'<td>{tdProcessIdLink}</td>'
            tableData += f'<td style="text-align:left;">{user}</td>'
            tableData += f'<td style="text-align:left;">{sessionId}</td>'
            tableData += f'<td style="text-align:left;" title={playbookNamespacePath}><a href="#" data-bs-toggle="modal" data-bs-target="#showPlaybookModal" id="playbookPath" onclick="showPlaybook(this)" playbookPath="{playbookPath}">{playbookNamespacePath}</a></td>'
            tableData += f'{tdStage}</td>'
            tableData += f'{tdModule}</td>'
            tableData += f'{tdEnv}</td>'
            tableData += f'{tdCurrentlyRunning}</td>'
            tableData += f'{tdProgress}</td>'
            tableData += f'{tdStatus}</td>' 
            tableData += f'{tdResult}</td>'
            tableData += '</tr>'

            # Add a blank row to separate the test for better visibility
            #tableData += f'<tr><td></td></tr>'     
                    
    tableData += '</tbody></table>' 
    return tableData, overallDetails


def getPipelines():
    return glob(f'{GlobalVars.pipelineFolder}/*.yml')

def getArtifacts(topLevelFolderFullPath):
    """
    Get result logs
    
    https://www.w3schools.com/howto/howto_js_treeview.asp

    <ul id="testResultFileTree">
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
    
    Requirements:
        - CSS: <link href={% static "commons/css/testResultsTreeView.css" %} rel="stylesheet" type="text/css">
        - html template needs to call addListeners() and getFileContents()
    """
    class getPagesVars:
        counter = 0
        
    timestampResultFolder = topLevelFolderFullPath.split('/')[-1]
    getPagesVars.html = f'<ul id="testResultFileTree">'

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
            path = topLevelFolderFullPath
            getPagesVars.html += f'<li style="margin-left:17px"> <span class="caret2"><i class="fa-regular fa-folder pr-2"></i>{timestampResultFolder}</span>' 
        
        if init == False:
            # FOLDER
            folderName = path.split('/')[-1]
            getPagesVars.html += f'<li style="margin-left:17px"> <span class="caret2"><i class="fa-regular fa-folder pr-2"></i>{folderName}</span>'  
                
        getPagesVars.html += '<ul class="nested">'
        getPagesVars.counter += 1
                    
        # FILE
        for eachFile in glob(f'{path}/*'):
            if os.path.isfile(eachFile): 
                filename = eachFile .split('/')[-1]

                # Open the modifyFileModal and get the file contents                  
                #getPagesVars.html += f'<li><a class="nav-link" href="#" onclick="getFileContents(this)" filePath="{eachFile}"  data-bs-toggle="modal" data-bs-target="#openFileModal"><i class="fa-regular fa-file pr-2"></i> {filename} </a></li>'
        
                # JS format:
                #    <object data="data/test.pdf" type="application/pdf" width="300" height="200">
                #    <a href="data/test.pdf">test.pdf</a>
                #    </object>
                # 
                # html
                # <iframe src="http://docs.google.com/gview?
                #     url=http://infolab.stanford.edu/pub/papers/google.pdf&embedded=true"
                #     style="width:600px; height:500px;" frameborder="0">
                # </iframe>
                if '.pdf' in eachFile:
                    # ${{window.location.host}}
                    # User clicks on pdf file, getTestResultFileContents uses Django's FileResponse to read the PDF file
                    getPagesVars.html += f'<i class="fa-regular fa-file pr-2"></i><a href="/testResults/getTestResultFileContents?testResultFile={eachFile}" target="_blank">{filename}</a>'
                else:
                    # getFileContents() is a JS function in sessionMgmt.html. It shows the file contents in a new web browser tab.
                    getPagesVars.html += f'<li><a href="#" onclick="getFileContents(this)" filePath="{eachFile}"><i class="fa-regular fa-file pr-2"></i>{filename}</a></li>'
                                                        
        # FOLDER
        for eachFolder in glob(f'{path}/*'):        
            if os.path.isdir(eachFolder):
                loop(eachFolder, init=False)
                getPagesVars.html += '</li></ul>'
                getPagesVars.counter -= 1
        
    loop(topLevelFolderFullPath, init=True)
    
    for x in range(0, getPagesVars.counter):
        getPagesVars.html += '</ul></li>'
        
    getPagesVars.html += '</ul>'

    return getPagesVars.html


class GetSessions(APIView):
    @verifyUserRole()
    def post(self, request):
        """ 
        Step to add a remote controller:
           - On the main controller, add "remote controller"
             (This will generate an Access-Key)
           - Go on the remote controller, add "Access Key" with the above main controller IP
        """ 
        remoteController = request.data.get('remoteController', None)
        mainControllerIp, remoteControllerIp, ipPort = getMainAndRemoteControllerIp(request, remoteController)       
        user = AccountMgr().getRequestSessionUser(request)
        status = 'success'
        errorMsg = None
        statusCode = HtmlStatusCodes.success
        tableData = '' 
        # view: current | archive
        view = request.data.get('view', None)
        group = request.data.get('group', None)
        
        # remoteController:192.168.28.17  mainControllerIp:192.168.28.7
        #print(f'\n---- pipelineViews: remoteController:{remoteControllerIp}  ipPort:{ipPort}  mainControllerIp:{mainControllerIp}')
                 
        try:
            overallDetailsHtml = ''
            
            # 28.7 = iNP29xnXdlnsfOyausD_EQ
            # 28.17 = da3XzmXRitPueJr4uPgBog
            if remoteControllerIp and remoteControllerIp != mainControllerIp:
                params = {"view":view, "group":group}
                restApi = '/api/v1/pipeline/getPipelines'
                response, errorMsg = executeRestApiOnRemoteController('post', remoteControllerIp, ipPort, restApi, params, 
                                                                      user, webPage=Vars.webpage, action='GetSessions')
                if errorMsg:
                    return Response({'status': 'failed', 'errorMsg': errorMsg, 'tableData': '', 'overallDetailsHtml':''}, status=HtmlStatusCodes.error)
                else:
                    tableData = response.json()['tableData']
                    overallDetailsHtml = response.json()['overallDetails']
                
            else:
                # Execute on local controller
                tableData, overallDetails = getTableData(view, group, user)
                settings.KEYSTACK_SESSIONS_CONNECTIVITY = True
                
                # overallDetails is from getTableData()
                overallDetailsHtml += '<center>'
                overallDetailsHtml += f'Total-Pipelines: {overallDetails["sessions"]}&emsp;&emsp;&emsp; Running: {overallDetails["running"]}&emsp;&emsp;&emsp;'
                overallDetailsHtml += f'Completed: {overallDetails["completed"]}&emsp;&emsp;&emsp; Aborted: {overallDetails["aborted"]}&emsp;&emsp;&emsp;'
                overallDetailsHtml += f'Terminated: {overallDetails["terminated"]}&emsp;&emsp;&emsp; Paused-On-Failure: {overallDetails["pausedOnFailure"]}&emsp;&emsp;&emsp;'
                overallDetailsHtml += f'Passed: {overallDetails["passed"]}&emsp;&emsp;&emsp; Failed: {overallDetails["failed"]}'
                overallDetailsHtml += '</center>'
                
        except Exception as errMsg:
            status = 'failed'
            errorMsg = str(errMsg)
            statusCode = HtmlStatusCodes.error
            SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='GetPipelines', msgType='Error', msg=errorMsg,
                                      forDetailLogs=f'{traceback.format_exc(None, errMsg)}')

        return Response(data={'status':status, 'errorMsg':errorMsg, 
                              'tableData':tableData, 'overallDetails':overallDetailsHtml}, 
                        status=statusCode)


class GetSessionDetails(APIView):        
    @verifyUserRole()
    def post(self, request):
        """ 
        Get the session details
        
        The folder toggler works in conjuntion with an addListener in getTestcaseData() 
        and keystackDetailedLogs CSS
        """
        user = AccountMgr().getRequestSessionUser(request)
        remoteController = request.data.get('remoteController', None)
        mainControllerIp, remoteControllerIp, ipPort = getMainAndRemoteControllerIp(request, remoteController)
        status = 'success'
        errorMsg = None
        statusCode = HtmlStatusCodes.success
        testResultsPath = request.data.get('testResultsPath', None)

        class getPagesVars:
            counter = 0
            html = ''
                
        if remoteControllerIp and remoteControllerIp != mainControllerIp:
            params = {"testResultsPath": testResultsPath}
            restApi = '/api/v1/pipeline/getSessionDetails'
            response, errorMsg = executeRestApiOnRemoteController('post', remoteControllerIp, ipPort, restApi, params, 
                                                                  user, webPage=Vars.webpage, action='GetSessionDetails')
            if errorMsg:
                status = 'failed'
                statusCode = HtmlStatusCodes.error 
                sessionData = None
                stageModuleEnv = None 
            else:    
                sessionData = response.json()['sessionData']
                stageModuleEnv = response.json()['stageModuleEnv']
                getPagesVars.html = response.json()['testcaseData']
                                  
        else:            
            try:
                status = readJson(f'{testResultsPath}/moduleSummary.json')
                
                # Verify if the overall test is terminated
                overallSummaryFile = f'{testResultsPath.split("STAGE")[0]}/overallSummary.json'
                overallStatus = readJson(overallSummaryFile)
                playbookFullPath = status['playbook']
                match = search(f'{GlobalVars.keystackTestRootPath}/Playbooks/([^ ]+)\.', playbookFullPath)
                if match:
                    playbook = match.group(1)
                else:
                    playbook = 'Unknown'
                    
                # STAGE=Tests_MODULE=CustomPythonScripts_ENV=loadcoreSample
                match = search('(STAGE=.*)_MODULE.*', testResultsPath)
                if match:
                    stage = match.group(1).replace('=', ': ')
                    
                match = search('STAGE=.*_(MODULE=.*)_ENV', testResultsPath)
                if match:
                    module = match.group(1).replace('=', ': ')

                match = search('STAGE=.*_MODULE=.*_(ENV.*)', testResultsPath)
                if match:
                    env = match.group(1).replace('=', ': ')
                
                statusCode = HtmlStatusCodes.success

            except Exception as errMsg:
                statusCode = HtmlStatusCodes.error
                status = 'failed'
                errorMsg = str(errMsg)
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='GetSessionDetails', msgType='Error',
                                        msg=errorMsg, forDetailLogs=traceback.format_exc(None, errMsg))

            testTime = f"Playbook: {playbook}<br>Started: {status['started']}<br>Stopped: {status['stopped']}<br>"
            
            try:
                testTime += f"Duration: {status['testDuration']}<br>"
            except:
                # test time may not be ready yet
                pass
            
            def createCard(inserts, col="col-xl-4"):
                data = f"""<div class="{col} col-md-6 mb-4">
                                <div class="card border-left-primary h-100 py-0">
                                    <div class="card-body">
                                        <div class=f"row no-gutters align-items-center">
                                            {inserts}
                                        </div>
                                    </div>
                                </div>
                            </div>
                        """  
                return data

            stageModuleEnv = f'{stage}&ensp;&emsp;{module}&ensp;&emsp;{env}'
            sessionData = '<div class="row">'
            sessionData += createCard(testTime)
            
            if status['status'] not in ['Completed', 'Terminated', 'Aborted']:
                if overallStatus['status'] == 'Terminated':
                    status2 = f'<span style="color:blue">Terminated</span>'
                else:
                    status2 = f'<span class="blink"><span style="color:blue">{status["status"]}</span></span>'
                
                sessionData += createCard(f"""<div style="font-size:20px; padding-left:0px">Status: {status2}</span></div><br>
                                        Total Testcases: {status['totalCases']}&emsp;&emsp; 
                                        Total Passed: {status['totalPassed']}&emsp;&emsp;
                                        Total Failed: {status['totalFailed']}&emsp;&emsp;<br>
                                        Progress: {status['progress']}
                                        """)
            else:
                # #10b332 = Green
                sessionData += createCard(f"""<div style="font-size:20px; padding-left:0px">Status: <span style="color:blue">{status['status']}</div><br>
                                        Total Testcases: {status['totalCases']}&emsp;&emsp; 
                                        Total Passed: {status['totalPassed']}&emsp;&emsp;
                                        Total Failed: {status['totalFailed']}&emsp;&emsp;<br>
                                        Progress: {status['progress']}
                                        """)

            if status['result'] in ['Failed', 'Incomplete']:
                status2 = f'<span style="color:red">{status["result"]}</span>'
            elif status['result'] == 'Passed':
                status2 = f'<span style="color:#10b332">{status["result"]}</span>'
            else:
                # Not-Ready
                status2 = f'<span style="color:blue">{status["result"]}</span>'
                    
            sessionData += createCard(f"""<div style="font-size:20px; padding-left:0px">Result: {status2}</div><br>
                                        Test Cases Aborted: {status['totalTestAborted']}&emsp;&emsp;
                                        Test Cases Skipped: {status['totalSkipped']}&emsp;&emsp;
                                        """)
            sessionData += "</div>"

            """
            The folder toggler works in conjuntion with an addListener in getTestcaseData() 
            
            <nav class="keystackDetailedLogs card py-0 mb-0">
                <ul class="nav flex-column" id="nav_accordion">
                    <li class="nav-item has-submenu">
                        <a class="nav-link" href="#"> resultFolder </a>
                        <ul class="submenu collapse">
                            <li><a class="nav-link" href="#"> File 1 </a></li>
                            <li><a class="nav-link" href="#"> File 2 </a></li>
                            <li><a class="nav-link" href="#"> File 3 </a> </li>
                        </ul>
                    </li>
                </ul>
            </nav>
            """
    
            if status['currentlyRunning']:
                sessionData += '<div class="row">'
                sessionData += createCard(f"Currently Running: {status['currentlyRunning']}", col="col-xl-12")       
                sessionData += "</div>"     

            if status.get('playlistExclusions', []):
                sessionData += 'Playlist Exclusions:<br>'
                for eachExclusion in status['playlistExclusions']:
                    sessionData += f'&emsp;&emsp;- {eachExclusion}<br>'
                    
                sessionData += '<br>'
            # Testcases begin here
            
            # class getPagesVars:
            #     counter = 0
                
            timestampResultFolder = testResultsPath.split('/')[-1]
            getPagesVars.html = f'<ul id="testResultFileTree">'

            def loop(path, init=False, status=None, result=None, isTestcaseFolder=False):
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
                if result in ['Failed', 'Aborted']:
                    result = f'<span class="textRed">{result}</span>'
                
                if init == True:
                    path = testResultsPath
                    getPagesVars.html += f'<li style="margin-left:17px"> <span class="caret2"><i class="fa-regular fa-folder pr-2"></i>{stage}&emsp;&ensp; {module}&emsp;&ensp; {env}</span>'
                    
                if init == False:
                    # FOLDER
                    folderName = path.split('/')[-1]
                    if isTestcaseFolder:
                        getPagesVars.html += f'<li style="margin-left:17px"> <span class="caret2"><i class="fa-regular fa-folder pr-2"></i>{folderName} &emsp;Status:{status} &emsp;Result:{result}</span>'
                    else:
                        getPagesVars.html += f'<li style="margin-left:17px"> <span class="caret2"><i class="fa-regular fa-folder pr-2"></i>{folderName}</span>'  
                        
                getPagesVars.html += '<ul class="nested">'
                getPagesVars.counter += 1
                            
                # FILE
                for eachFile in glob(f'{path}/*'):
                    if os.path.isfile(eachFile): 
                        filename = eachFile .split('/')[-1]
                
                        # JS format:
                        #    <object data="data/test.pdf" type="application/pdf" width="300" height="200">
                        #    <a href="data/test.pdf">test.pdf</a>
                        #    </object>
                        # 
                        # html
                        # <iframe src="http://docs.google.com/gview?
                        #     url=http://infolab.stanford.edu/pub/papers/google.pdf&embedded=true"
                        #     style="width:600px; height:500px;" frameborder="0">
                        # </iframe>
                        if '.pdf' in eachFile:
                            # ${{window.location.host}}
                            # User clicks on pdf file, getTestResultFileContents uses Django's FileResponse to read the PDF file
                            getPagesVars.html += f'<i class="fa-regular fa-file pr-2"></i><a href="/testResults/getTestResultFileContents?testResultFile={eachFile}" target="_blank">{filename}</a>'
                        else:
                            # getFileContents() is a JS function in sessionMgmt.html. It shows the file contents in a new web browser tab.
                            getPagesVars.html += f'<li><a href="#" onclick="getFileContents(this)" filePath="{eachFile}"><i class="fa-regular fa-file pr-2"></i>{filename}</a></li>'
                                                                
                # FOLDER
                for index,eachFolder in enumerate(glob(f'{path}/*')):
                    if os.path.isdir(eachFolder):
                        # The the testcase results first so results could be shown next to the testcase folder
                        for eachFile in glob(f'{eachFolder}/*'):
                            if 'testSummary.json' in eachFile:
                                testcaseSummary = readJson(eachFile)
                                status = testcaseSummary['status']
                                result = testcaseSummary['result']
                        
                        if index == 1:
                            isTestcaseFolder = True
                        else:
                            isTestcaseFolder = False
                                    
                        loop(eachFolder, init=False, status=status, result=result, isTestcaseFolder=isTestcaseFolder)
                        getPagesVars.html += '</li></ul>'
                        getPagesVars.counter -= 1
                
            loop(testResultsPath, init=True)
            
            for x in range(0, getPagesVars.counter):
                getPagesVars.html += '</ul></li>'
                
            getPagesVars.html += '</ul>'        

        return Response(data={'sessionData': sessionData, 'testcaseData': getPagesVars.html,
                              'stageModuleEnv':stageModuleEnv, 'errorMsg':errorMsg}, status=statusCode) 

    
class GetPipelines(APIView):
    @swagger_auto_schema(tags=['/api/v1/pipelines'], manual_parameters=[], 
                         operation_description="Get list of pipeline names")
    @verifyUserRole()
    def get(self, request, data=None):
        """
        Description:
            Get a list of saved pipelines names to play
        
        GET /api/vi/pipelines
        
        ---
        Examples:
            curl -H "API-Key: iNP29xnXdlnsfOyausD_EQ" -X GET http://192.168.28.7:8000/api/v1/pipelines
            
            curl -H "API-Key: iNP29xnXdlnsfOyausD_EQ" -H "Content-Type: application/x-www-form-urlencoded" -X GET http://192.168.28.7:8000/api/v1/pipelines/ 
            
            curl -H "API-Key: iNP29xnXdlnsfOyausD_EQ" -H "Content-Type: application/json" -X GET http://192.168.28.7:8000/api/v1/pipelines
            
            session = requests.Session()
            response = session.request('get', 'http://localhost:8000/api/v1/pipelines')
        """
        statusCode = HtmlStatusCodes.success
        errorMsg = None
        pipelines = []
        user = AccountMgr().getRequestSessionUser(request)
        remoteController = request.data.get('remoteController', None)
        mainControllerIp, remoteControllerIp, ipPort = getMainAndRemoteControllerIp(request, remoteController)
        
        if remoteControllerIp and remoteControllerIp != mainControllerIp:
            params = {}
            restApi = '/api/v1/pipelinesUI'
            response, errorMsg = executeRestApiOnRemoteController('get', remoteControllerIp, ipPort, restApi, params, 
                                                                  user, webPage=Vars.webpage, action='GetPipelines')  
            if errorMsg:
                status = 'failed'
                statusCode = HtmlStatusCodes.error
                pipelines = '' 
            else:
                pipelines = response.json()['pipelines']
            
        else:                           
            pipelineFile = f'{GlobalVars.pipelineFolder}'
            for eachPipeline in glob(f'{GlobalVars.pipelineFolder}/*.yml'):
                eachPipeline = eachPipeline.split('/')[-1].split('.')[0]
                pipelines.append(eachPipeline)
                
            return Response(data={'pipelines':pipelines, 'errorMsg': errorMsg, 'status': 'success'}, status=statusCode)

        
class RunPipeline(APIView):
    pipeline = openapi.Parameter(name='pipeline', description="Name of the pipeline to run",
                                 required=True, in_=openapi.IN_QUERY, type=openapi.TYPE_STRING) 
    @swagger_auto_schema(tags=['/api/v1/pipeline/run'], manual_parameters=[pipeline], 
                         operation_description="Run a pipeline")
    @verifyUserRole()
    def post(self, request, data=None):
        """
        Description:
            A webhook for CI/CT/CD to run a pipeline
        
        POST /api/vi/pipeline/run
        ---
        Examples:
            
            curl -H "API-Key: iNP29xnXdlnsfOyausD_EQ" -X POST http://192.168.28.7:8000/api/v1/pipeline/run?pipeline=pipelineName
            
            curl -H "API-Key: iNP29xnXdlnsfOyausD_EQ" -d "pipeline=pipelineName" -H "Content-Type: application/x-www-form-urlencoded" -X POST http://192.168.28.7:8000/api/v1/pipeline/run 
            
            curl -H "API-Key: iNP29xnXdlnsfOyausD_EQ" -d '{"pipeline": "pipelineName"}' -H "Content-Type: application/json" -X POST http://192.168.28.7:8000/api/v1/pipeline/run
            
            session = requests.Session()
            response = session.request('post', 'http://localhost:8000/api/v1/pipeline/run')
        """
        status = HtmlStatusCodes.success
        playbookDetails = None
        playbookName = None
        errorMsg = None
        user = AccountMgr().getRequestSessionUser(request)
        remoteController = request.data.get('remoteController', None)
        mainControllerIp, remoteControllerIp, ipPort = getMainAndRemoteControllerIp(request, remoteController)
        
        # http://ip:port/api/v1/pipeline/run?pipeline=pipelineName
        if request.GET:
            # Rest APIs with inline params come in here
            try:
                pipeline = request.GET.get('pipeline')
            except Exception as error:
                errorMsg = f'Expecting key pipeline, but got: {request.GET}'
                return Response(data={'status': 'failed', 'errorMsg': errorMsg}, status=HtmlStatusCodes.error)
            
        # JSON format
        if request.data:
            # <QueryDict: {'playbook': pythonSample}
            try:
                pipeline = request.data['pipeline']
            except Exception as errMsg:
                errorMsg = f'Expecting key pipeline, but got: {request.data}'
                return Response(data={'status': 'failed', 'errorMsg': errorMsg}, status=HtmlStatusCodes.error)

        if remoteControllerIp and remoteControllerIp != mainControllerIp:
            params = {"pipeline": pipeline}
            restApi = '/api/v1/pipeline/run'
            response, errorMsg = executeRestApiOnRemoteController('post', remoteControllerIp, ipPort, restApi, params, 
                                                                  user, webPage=Vars.webpage, action='RunPipeline')
            if errorMsg:
                status = 'failed'
                statusCode = HtmlStatusCodes.error 
                   
        else: 
            # 'HTTP_HOST': '192.168.28.7:8000'
            httpHost= request.META.get('HTTP_HOST')
            
            print('\n--- runPipeline:', httpHost)
            
            if ':' in httpHost:
                controllerIp = httpHost.split(':')[0]
                port = httpHost.split(':')[-1]
            else:
                controllerIp = httpHost
                port = None
                
            wsgiScheme = request.META.get('wsgi.url_scheme')
            if wsgiScheme.lower() == 'http':
                https = False
            else:
                https = True
    
            pipelineFile = f'{GlobalVars.pipelineFolder}/{pipeline}'
            if '.yml' not in pipelineFile:
                pipelineFile = f'{pipelineFile}.yml'
            
            # The issue is that to run a pipeline by the pipeline name, this function
            # calls runPlaybook rest api.  The runPlaybook Rest API checks verifyApiKey. To bypass 
            # checking verifyApiKey, include webhook param.
            # Getting in this function already validated user API-Key. So now calling 
            # runPlaybook is done internally and using webhook to bypass verifying api-key.
            params = {'pipeline': pipelineFile, 
                      'controller': httpHost,
                      'webhook': True}
            
            # Note: CI/CT/CD webhook already specified the controller's ip address with http://ip:port
            #       No need to look up remote_controllerIp
            restObj = ExecRestApi(ip=controllerIp, port=port, https=https)
            response = restObj.post('/api/v1/playbook/run', params=params)
            del restObj 
        
            if str(response.status_code).startswith('2') == False:
                #  {"sessions": {}, "status": "failed", "errorMsg": "GET Exception error 2/2 retries: HTTPSConnectionPool(host='192.168.28.17', port=88028): Max retries exceeded with url: /api/v1/sessions?view=current&group=Default (Caused by SSLError(SSLError(1, '[SSL: WRONG_VERSION_NUMBER] wrong version number (_ssl.c:997)')))"}
                error = json.loads(response.content.decode('utf-8'))
                errorMsg = error['errorMsg']
                
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='runPipeline', msgType='Error',
                                        msg=errorMsg, forDetailLogs='')
                
                # TODO: Display the failure message on UI topbar
                return Response({'status': 'failed', 'errorMsg': errorMsg}, status=HtmlStatusCodes.error)
            else:
                return Response({'status': 'success', 'errorMsg': None}, status=HtmlStatusCodes.success)
            

class DeletePipelineSessions(APIView):
    pipelines = openapi.Parameter(name='pipelines', description="Delete pipeline sessions",
                                 required=True, in_=openapi.IN_QUERY, type=openapi.TYPE_ARRAY, 
                                 items=openapi.Items(type=openapi.TYPE_STRING)) 
    
    @swagger_auto_schema(tags=['/api/v1/pipeline/deletePipelineSessions'], manual_parameters=[pipelines], 
                         operation_description="Delete pipeline sessions")
    @verifyUserRole(webPage=Vars.webpage, action='DeletePipelineSessions', exclude=['engineer'])
    def post(self, request, data=None):
        """
        Description:
            Delete pipeline test sessions
        
        POST /api/v1/pipeline/delete
        ---
        Examples:
            
            curl -H "API-Key: iNP29xnXdlnsfOyausD_EQ" -X POST http://192.168.28.7:8000/api/v1/pipeline/deletePipelineSessions?pipelines=pipelines
            
            curl -H "API-Key: iNP29xnXdlnsfOyausD_EQ" -H "Content-Type: application/x-www-form-urlencoded" -d "pipelines=session1" -d "pipelines=session2"  -X POST http://192.168.28.7:8000/api/v1/pipeline/deletePipelineSessions
            
            curl -H "API-Key: iNP29xnXdlnsfOyausD_EQ" -H "Content-Type: application/json" -d '{"pipelines": ["session1", "session2"]}'  -X POST http://192.168.28.7:8000/api/v1/pipeline/deletePipelineSessions
            
            session = requests.Session()
            response = session.request('post', 'http://localhost:8000/api/v1/pipeline/deletePipelineSessions')
        """
        user = AccountMgr().getRequestSessionUser(request)
        remoteController = request.data.get('remoteController', None)
        mainControllerIp, remoteControllerIp, ipPort = getMainAndRemoteControllerIp(request, remoteController)
        statusCode = HtmlStatusCodes.success
        errorMsg = None
        status = 'success'
        sessionId = None
        
        if request.GET:
            # Rest APIs with inline params come in here
            try:
                pipelines = request.GET.get('pipelines')
            except Exception as error:
                error = f'Expecting key pipelines, but got: {request.GET}'
                return Response(data={'status': 'failed', 'errorMsg': errorMsg}, status=HtmlStatusCodes.error)
            
        # JSON format
        if request.data:
            # <QueryDict: {'playbook': pythonSample}
            try:
                pipelines = request.data['pipelines']
            except Exception as errMsg:
                errorMsg = f'Expecting key pipelines, but got: {request.data}'
                return Response(data={'status': 'failed', 'errorMsg': errorMsg}, status=HtmlStatusCodes.error)

        if remoteControllerIp and remoteControllerIp != mainControllerIp:
            params = {"pipelines": pipelines}
            restApi = '/api/v1/pipelines/deletePipelineSessions'
            response, errorMsg = executeRestApiOnRemoteController('post', remoteControllerIp, ipPort, restApi, params, 
                                                                  user, webPage=Vars.webpage, action='DeletePipelineSessions')
            if errorMsg:
                status = 'failed'
                statusCode = HtmlStatusCodes.error
  
        else:
            try:
                # If "Delte results" checkbox is unchecked: 
                #    {'sessions': [{'sessionId': 'hgee3', 'testResultsPath': None}]}
                # If "Delte results" checkbox is checked:
                #    {'sessions': [{'sessionId': 'hgee3', 'testResultsPath': None}, {'sessionId': 'hgee3', 'testResultsPath': '/opt/KeystackTests/Results/PLAYBOOK=pythonSample/09-24-2022-15:55:58:091405_hgee3'}]}
                # [{'sessionId': 'hgee3', 'testResultsPath': None}, {'sessionId': 'hgee3', 'testResultsPath': None}]
                additionalMessage = ''
                
                # Users could select multiple sessions to delete
                for eachSession in pipelines:
                    # eachSession {'testResultsPath': '/opt/KeystackTests/Results/GROUP=Default/PLAYBOOK=pythonSample/11-16-2022-15:25:11:957919_hubogee'}
                    
                    # /opt/KeystackTests/Results/GROUP=Default/PLAYBOOK=pythonSample/10-26-2022-14:54:49:859583_1600
                    testResultsPath    = eachSession['testResultsPath']
                    overallSummaryFile = f'{testResultsPath}/overallSummary.json'
                    envMgmtPath        = f'{testResultsPath}/.Data/EnvMgmt'
                    envList = []
                    
                    if os.path.exists(overallSummaryFile):
                        overallSummaryData = readJson(overallSummaryFile)
                        envMgmtObj = ManageEnv()
                        for envMgmtFile in glob(f'{envMgmtPath}/*.json'):
                            envMgmtData = readJson(envMgmtFile)
                            env = envMgmtData['env']
                            if env is None:
                                continue
                            
                            stage = envMgmtData['stage']
                            module = envMgmtData['module']
                            user = envMgmtData['user']
                            sessionId = envMgmtData['sessionId']
                            envMgmtObj.setenv = env
                            session = {'user':user, 'sessionId':sessionId, 'stage':stage, 'module':module}
                            envMgmtObj.removeFromActiveUsersList([session])
                            envMgmtObj.removeFromWaitList(sessionId, user, stage, module)
                            envList.append(env)
                            
                            SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='removeFromActiveUsersList', msgType='Info', msg=session) 
                            
                        additionalMessage = f'Released Envs: {envList}'
                                                
                    from shutil import rmtree
                    try:
                        # When deleting a session, remove the result timestamp folder.
                        # If user wants to save the result, they could archive it.
                        if os.path.exists(testResultsPath):
                            rmtree(testResultsPath)
                            SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='DeletePipelineSessions', msgType='Info', msg=f'Deleted results {testResultsPath}. {additionalMessage}')   
                            
                        removeEmptyTestResultFolders(user, testResultsPath)

                    except Exception as errMsg:
                        #print('\n--- deletePipelines error:', traceback.format_exc(None, errMsg))
                        errorMsg = str(errMsg)
                        status = 'failed'
                        statusCode = HtmlStatusCodes.error
                        SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='DeletePipelineSessions', msgType='Error',
                                                msg=f'Failed to delete results & logs {testResultsPath}<br>{errorMsg}', 
                                                forDetailLogs=traceback.format_exc(None, errMsg))
                
            except Exception as errMsg:
                errorMsg = str(errMsg)
                status = 'failed'
                statusCode = HtmlStatusCodes.error
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='DeletePipelines', msgType='Error', msg=errorMsg,
                                        forDetailLogs=traceback.format_exc(None, errMsg))
            
        return Response(data={'status':status, 'errorMsg':errorMsg}, status=statusCode)


class DeletePipelines(APIView):
    @verifyUserRole(webPage=Vars.webpage, action='DeletePipelines', exclude=['engineer'])
    def post(self, request):
        statusCode = HtmlStatusCodes.success
        status = 'success'
        errorMsg = None
        user = AccountMgr().getRequestSessionUser(request)
        remoteController = request.data.get('remoteController', None)
        mainControllerIp, remoteControllerIp, ipPort = getMainAndRemoteControllerIp(request, remoteController)

        if request.GET:
            # Rest APIs with inline params come in here
            try:
                pipelines = request.GET.get('pipelines')
            except Exception as error:
                errorMsg = f'Expecting key pipelines, but got: {request.GET}'
                return Response(data={'status': 'failed', 'errorMsg': errorMsg}, status=HtmlStatusCodes.error)
            
        # JSON format
        if request.data:
            # <QueryDict: {'playbook': pythonSample}
            try:
                pipelines = request.data['pipelines']
            except Exception as errMsg:
                errorMsg = f'Expecting key pipelines, but got: {request.data}'
                return Response(data={'status': 'failed', 'errorMsg': errorMsg}, status=HtmlStatusCodes.error)
 
        if remoteControllerIp and remoteControllerIp != mainControllerIp:
            params = {"pipelines": pipelines}
            restApi = '/api/v1/pipelines/delete'
            response, errorMsg = executeRestApiOnRemoteController('post', remoteControllerIp, ipPort, restApi, params, 
                                                                  user, webPage=Vars.webpage, action='DeletePipelines')
            if errorMsg:
                status = 'failed'
                statusCode = HtmlStatusCodes.error 
                   
        else:                
            try:
                for eachPipeline in pipelines:
                    if os.path.exists(eachPipeline):
                        os.remove(eachPipeline)
                        pipelineName = eachPipeline.split('/')[-1].split('.')[0]
                        SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='DeletePipelines', msgType='Info',
                                                msg=f'Pipeline name: {pipelineName}', forDetailLogs='')
                    
            except Exception as errMsg:
                status = 'failed'
                statusCoe = HtmlStatusCodes.error
                errorMsg = str(errMsg)
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='DeletePipelines', msgType='Error',
                                          msg=f'Pipeline:{pipelineName}: {errorMsg}', forDetailLogs=traceback.format_exc(None, errMsg))
       
        return Response(data={'status':status, 'errorMsg': errorMsg}, status=statusCode)  
    

class GetPipelinesDropdown(APIView):
    @verifyUserRole()
    def post(self,request):
        """ 
        Dropdown menu for user to select a pipeline to run
        """
        user = AccountMgr().getRequestSessionUser(request)
        remoteController = request.data.get('remoteController', None)
        mainControllerIp, remoteControllerIp, ipPort = getMainAndRemoteControllerIp(request, remoteController)
        statusCode = HtmlStatusCodes.success
        status = 'success'
        errorMsg = None
        pipelines = []
                
        if remoteControllerIp and remoteControllerIp != mainControllerIp:
            params = {}
            restApi = '/api/v1/pipelines/dropdown'
            response, errorMsg = executeRestApiOnRemoteController('post', remoteControllerIp, ipPort, restApi, params, 
                                                                  user, webPage=Vars.webpage, action='GetPipelinesDropdown')
            if errorMsg:
                status = 'failed'
                statusCode = HtmlStatusCodes.error 
                pipelines = ''
            else:
                pipelines = response.json()['pipelines']
                  
        else:           
            try:
                pipelines = '<ul class="dropdown-menu dropdownSizeSmall dropdownFontSize">'
                        
                for eachPipeline in getPipelines():
                    pipeline = eachPipeline.replace(f'{GlobalVars.pipelineFolder}/', '').split('.')[0]
                    pipelines += f'<li class="dropdown-item" pipeline="{eachPipeline}" onclick="playPipeline(this)">{pipeline}</li>'
                
                pipelines += '</ul>'
                            
            except Exception as errMsg:
                statusCode = HtmlStatusCodes.error
                status = 'failed'
                errorMsg = str(errMsg)
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='GetPipelines', msgType='Error',
                                        msg=errMsg,
                                        forDetailLogs=f'error: {traceback.format_exc(None, errMsg)}')
        
        return Response({'pipelines': pipelines, 'status':status, 'errorMsg': errorMsg}, status=statusCode)
    

class SavePipeline(APIView):
    @verifyUserRole(webPage=Vars.webpage, action='SavePipeline', exclude=['engineer'])
    def post(self,request):
        """ 
        Create a new pipeline
        """
        user = AccountMgr().getRequestSessionUser(request)
        remoteController = request.data.get('remoteController', None)
        mainControllerIp, remoteControllerIp, ipPort = getMainAndRemoteControllerIp(request, remoteController)
        statusCode = HtmlStatusCodes.success
        status = 'success'
        errorMsg = None

        pipelineName = request.data.get('pipelineName', None)
        playbook     = request.data.get('playbook', None)

        if remoteControllerIp and remoteControllerIp != mainControllerIp:
            params = {"pipelineName": pipelineName, "playbook":playbook}
            restApi = '/api/v1/pipelines/save'
            response, errorMsg = executeRestApiOnRemoteController('post', remoteControllerIp, ipPort, restApi, params, 
                                                                  user, webPage=Vars.webpage, action='SavePipeline')
            if errorMsg:
                status = 'failed'
                statusCode = HtmlStatusCodes.error 
                   
        else:                    
            try:
                pipelineFilename = f'{GlobalVars.pipelineFolder}/{pipelineName}.yml'
            
                if playbook == '':
                    statusCode = HtmlStatusCodes.error
                    status = 'failed'
                    errorMsg = 'You must select a playbook'
                    SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='SavePipeline', msgType='Failed',
                                              msg=errorMsg, forDetailLogs='')
                    return Response({'status':status, 'errorMsg': errorMsg}, status=statusCode)
                
                for eachPipelineName in getPipelines():
                    if bool(match(pipelineName, eachPipelineName)):
                        status = 'failed'
                        statusCode = HtmlStatusCodes.error
                        errorMsg = f'Pipeline name already exists: {pipelineName}'
                        SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='SavePipeline', msgType='Error',
                                                msg=errorMsg, forDetailLogs='')
                
                if errorMsg is None:                    
                    if os.path.exists(GlobalVars.pipelineFolder) == False:
                        mkdir2(GlobalVars.pipelineFolder, stdout=False)
                    
                    writeToYamlFile({'pipeline':pipelineName, 'playbook':playbook}, pipelineFilename, mode='w')
                    chownChmodFolder(GlobalVars.pipelineFolder,
                                    user=GlobalVars.user, userGroup=GlobalVars.userGroup, permission=770, stdout=False)
                
                    SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='SavePipeline', msgType='Info',
                                              msg=f'playbook={playbook}  pipelineName={pipelineName}', forDetailLogs='')
                            
            except Exception as errMsg:
                statusCode = HtmlStatusCodes.error
                status = 'failed'
                errorMsg = str(errMsg)
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='SavePipeline', msgType='Error',
                                        msg=errorMsg, forDetailLogs=traceback.format_exc(None, errMsg))
        
        return Response({'status':status, 'errorMsg': errorMsg}, status=statusCode)
    

class GetPipelineTableData(APIView):
    @verifyUserRole()
    def post(self, request):
        """ 
        Get detailed Pipeline data table 
        """
        user = AccountMgr().getRequestSessionUser(request)
        remoteController = request.data.get('remoteController', None)
        mainControllerIp, remoteControllerIp, ipPort = getMainAndRemoteControllerIp(request, remoteController)
        statusCode = HtmlStatusCodes.success
        status = 'success'
        errorMsg = None
        html = ''
        
        if remoteControllerIp and remoteControllerIp != mainControllerIp:
            params = {"remoteController": remoteController}
            restApi = '/api/v1/pipelines/tableData'
            response, errorMsg = executeRestApiOnRemoteController('post', remoteControllerIp, ipPort, restApi, params, 
                                                                  user, webPage=Vars.webpage, action='GetPipelineTableData')
            if errorMsg:
                status = 'failed'
                statusCode = HtmlStatusCodes.error 
            else:
                html = response.json()['pipelineTableData']
                  
        else:        
            #html = '<table class="table table-sm table-bordered table-fixed tableFixHead">'
            html = '<table class="tableMessages table-bordered">'
            html += '<thead>'
            html += '<tr>'
            html += '<th>Delete</th>'
            html += '<th>Existing Pipelines</th>'
            html += '<th>Parameters</th>'
            html += '</tr>'
            html += '</thead>'

            try:
                for eachPipeline in glob(f'{GlobalVars.pipelineFolder}/*.yml'):
                    pipelineParams = readYaml(eachPipeline)
                    pipelineName = eachPipeline.split('/')[-1].split('.')[0]
                    paramsInStrFormat = ''
                    for key,value in pipelineParams.items():
                        paramsInStrFormat += f'{key}:{value}&emsp;'

                    html += '<tr>'
                    html += f'<td><center><input type="checkbox" name="deletePipeline" pipelineFullPath={eachPipeline} /></center></td>'
                    html += f'<td>{pipelineName}</td>'
                    html += f'<td class="marginLeft0">{paramsInStrFormat}</td>'
                    html += '</tr>'
            except Exception as errMsg:
                status = 'failed'
                errorMsg = str(errMsg)
                statusCode = HtmlStatusCodes.error
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='GetPipelineTableData', msgType='Error',
                                          msg=errorMsg, forDetailLogs='')
                        
            html += '</table>'
                          
        return Response({'pipelineTableData':html, 'status':status, 'errorMsg': errorMsg}, status=statusCode)
    
            
class GetTestReport(APIView):
    @verifyUserRole()
    def post(self,request):
        user = AccountMgr().getRequestSessionUser(request)
        remoteController = request.data.get('remoteController', None)
        mainControllerIp, remoteControllerIp, ipPort = getMainAndRemoteControllerIp(request, remoteController)
        statusCode = HtmlStatusCodes.success
        status = 'success'
        errorMsg = None
        
        if request.GET:
            # Rest APIs with inline params come in here
            try:
                testReportPath = request.GET.get('testReportPath')
            except Exception as error:
                errorMsg = f'Expecting key testReportPath, but got: {request.GET}'
                return Response(data={'status': 'failed', 'errorMsg': errorMsg}, status=HtmlStatusCodes.error)
            
        # JSON format
        if request.data:
            # <QueryDict: {'playbook': pythonSample}
            try:
                testReportPath = request.data['testReportPath']
            except Exception as errMsg:
                error = f'Expecting key testReportPath, but got: {request.data}'
                return Response(data={'status': 'failed', 'errorMsg': error}, status=HtmlStatusCodes.error)
 
        if remoteControllerIp and remoteControllerIp != mainControllerIp:
            params = {"testReportPath": testReportPath}
            restApi = '/api/v1/pipelines/getTestReport'
            response, errorMsg = executeRestApiOnRemoteController('post', remoteControllerIp, ipPort, restApi, params, 
                                                                  user, webPage=Vars.webpage, action='GetTestReport')
            if errorMsg:
                status = 'failed'
                statusCode = HtmlStatusCodes.error 
                testReport = ''
            else:
                testReport = response.json()['testReportInsert']
                       
        else:                    
            try:
                testReport = readFile(testReportPath)
                statusCode = HtmlStatusCodes.success
            except Exception as errMsg:
                errorMsg = str(errMsg)
                statusCode = HtmlStatusCodes.error
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='GetTestReport', msgType='Error',
                                          msg=errorMsg, forDetailLogs=traceback.format_exc(None, errMsg))
                testReport = f'Error: {errMsg}'

        return Response(data={'testReportInsert':testReport, 'status':status, 'errorMsg':errorMsg}, status=statusCode)
    
    
class GetTestLogs(APIView):
    @verifyUserRole()
    def post(self,request):
        user = AccountMgr().getRequestSessionUser(request)
        remoteController = request.data.get('remoteController', None)
        mainControllerIp, remoteControllerIp, ipPort = getMainAndRemoteControllerIp(request, remoteController)
        statusCode = HtmlStatusCodes.success
        status = 'success'
        errorMsg = None
        testLogs = ''
        
        if request.GET:
            # Rest APIs with inline params come in here
            try:
                testResultPath = request.GET.get('testResultPath')
            except Exception as error:
                error = f'Expecting key testResultPath, but got: {request.GET}'
                return Response(data={'status': 'failed', 'errorMsg': error}, status=HtmlStatusCodes.error)
            
        # JSON format
        if request.data:
            # <QueryDict: {'playbook': pythonSample}
            try:
                testResultPath = request.data['testResultPath']
            except Exception as errMsg:
                error = f'Expecting key testResultPath, but got: {request.data}'
                return Response(data={'status': 'failed', 'errorMsg': error}, status=HtmlStatusCodes.error)

        if remoteControllerIp and remoteControllerIp != mainControllerIp:
            params = {"testResultPath": testResultPath}
            restApi = '/api/v1/pipelines/getTestLogs'
            response, errorMsg = executeRestApiOnRemoteController('post', remoteControllerIp, ipPort, restApi, params, 
                                                                  user, webPage=Vars.webpage, action='GetTestLogs')
            if errorMsg:
                status = 'failed'
                statusCode = HtmlStatusCodes.error 
                testLogs = ''
                testResultsPath = ''
            else:
                testLogs = response.json()['testLogsHtml']
                testResultPath = response.json()['test'].split('/')[-1]
     
        else:         
            try:
                testLogs = getArtifacts(testResultPath)
            except Exception as errMsg:
                status = 'failed'
                errorMsg = str(errMsg)
                statusCode = HtmlStatusCodes.error
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='GetTestLogs', msgType='Error',
                                          msg=errMsg, forDetailLogs=f'{traceback.format_exc(None, errMsg)}')
                testlogs = f"Error: {errMsg}"

        return Response(data={'status':status, 'errorMsg':errorMsg, 'testLogsHtml': testLogs, 
                              'test': testResultPath.split('/')[-1]}, status=statusCode, safe=False)

# ---- Job Scheduler ----

class JobSchedulerAssistant():                  
    def getCurrentCronjobs(self):
        """ 
        Get the as-is /etc/crontab file
        """
        cronJobs = ''
        if os.path.exists('/etc/crontab'):
            with open('/etc/crontab', 'r') as cronObj:
                currentCron = cronObj.readlines()
        
            for line in currentCron:
                line = line.strip()
                if not line:
                    continue
                
                if line.startswith('#'):
                    continue
                
                if 'playbook' not in line:
                    continue
                
                cronJobs += f'{line}\n'

        return cronJobs        
    
    def getCurrentCronjobList(self):
        """ 
        Create a crontab list
        """
        cronjobs = self.getCurrentCronjobs()

        from re import search
        
        cronlist = []
        for job in cronjobs.split('\n'):
            if job == '':
                continue 
            
            if bool(search('.*SHELL', job)) or bool(search('.*PATH', job)):
                continue

            cronlist.append(job)
 
        return cronlist
     
    def isCronExists(self, playbook, min, hour, day, month, dayOfWeek):
        currentCronList = self.getCurrentCronjobList()
        if len(currentCronList)  == 0:
            return False
        
        for eachCron in self.getCurrentCronjobList():
            match = search(' *([0-9\*]+) *([0-9\*]+) *([0-9\*]+) *([0-9\*]+) *([0-9\*]+).*playbook=([^ &]+).*-H', eachCron)
            if match:
                cronMin       = match.group(1)
                cronHour      = match.group(2)
                cronDay       = match.group(3)
                cronMonth     = match.group(4)
                cronDayOfWeek = match.group(5)
                cronPlaybook  = match.group(6)
                
                cronList = [cronPlaybook, cronMin, cronHour, cronDay, cronMonth, cronDayOfWeek]
                newList  = [playbook, min, hour, day, month, dayOfWeek]
                if set(cronList) == set(newList):
                    # Found existing cron
                    return True
     
        return False

    def removeCronJobs(self, listOfJobsToRemove, user):
        """
        Crontab example: 
            25 12 24 3 * root curl -d "playbook=goody&user=Hubert Gee" -H "Content-Type: application/x-www-form-urlencoded" -X POST http://172.16.1.16:8000/api/playbook
         
        listOfJobsToRemove: <list of dicts>:  
              [{'playbook': '/opt/KeystackTests/Playbooks/pythonSample.yml', 'month': '10', 'day': '6', 'hour': '11', 'minute': '42'}, {}, ...]
        """
        cronJobs = self.getCurrentCronjobList()
        if not cronJobs:
            return
        
        def deleteCron(min, hour, day, month, dayOfWeek, playbook):
            cronJobs = self.getCurrentCronjobList()
            
            for index,eachCron in enumerate(cronJobs):
                if playbook and bool(search(f'{min} *{hour} *{day} *{month} *{dayOfWeek}.*playbook={playbook}.*', eachCron)):
                    cronJobs.pop(index)
                    break            
                                    
        for removeJob in listOfJobsToRemove:
            # {'playbook': 'pythonSample', 'month': '*', 'day': '*', 'hour': '*', 'minute': '*', 'dayOfWeek': '*'}
            playbook =  removeJob['playbook']
            min =       removeJob["minute"]
            hour =      removeJob["hour"]
            day =       removeJob["day"]
            month =     removeJob["month"]
            dayOfWeek = removeJob["dayOfWeek"]
            
            for cronProperty in [{'min':min}, {'hour':hour}, {'day':day}, {'month':month}, {'dayOfWeek':dayOfWeek}]:
                for key,value in cronProperty.items():
                    if value == "*":
                        # The template already added slashes.  runPlaybook does not add slashes.
                        if key == 'min': min = '\\*'
                        if key == 'hour': hour = '\\*'
                        if key == 'day': day = '\\*'
                        if key == 'month': month = '\\*'
                        if key == 'dayOfWeek': dayOfWeek = '\\*'

            for index,eachCron in enumerate(cronJobs):
                # each cron: * * * * * keystack curl -d "sessionId=&playbook=pythonSample&awsS3=False&jira=False&pauseOnError=False&debug=False&group=Default&scheduledJob="minute=* hour=* dayOfMonth=* month=* dayOfWeek=*"&webhook=true" -H "Content-Type: application/x-www-form-urlencoded" -X POST http://192.168.28.7:8000/api/v1/playbook/run
                
                # eachCron: 18 19 24 3 * root curl -d "playbook=playbookName&user=user" 
                if bool(search(f'{min}\s+{hour}\s+{day}\s+{month}\s+{dayOfWeek}.*playbook={playbook}&.*', eachCron)):
                    cronJobs.pop(index)
                    break
                    
        if cronJobs:
            updatedCronJobs = ''
            for cron in cronJobs:
                # The crontab file may contain some unknown Linux OS cron jobs. Exclude them.
                if 'playbook' in cron:
                    updatedCronJobs += f'{cron}\n'
        
            try:
                execSubprocessInShellMode(f"sudo echo '{updatedCronJobs}' | sudo tee /etc/crontab", showStdout=False)
                    
            except Exception as errMsg:
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='removeScheduledJob', msgType='Error',
                                          msg=cronJobs.replace('\\'), forDetailLogs=f'removeScheduledJob: {traceback.format_exc(None, errMsg)}')
        else:
            try:
                execSubprocessInShellMode('sudo echo "" | sudo tee /etc/crontab', showStdout=False)

            except Exception as errMsg:
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='removeScheduledJob', msgType='Error',
                                          msg=cronJobs.replace('\\'), forDetailLogs=f'clearAllScheduledJob: {traceback.format_exc(None, errMsg)}')
 
 
class AddJobSchedule(APIView):                                           
    @verifyUserRole(webPage=Vars.webpage, action='AddJobSchedule', exclude=['engineer'])
    def post(self, request):
        """ 
        Schedule a cron job
        
            # Example of job definition:
            # .---------------- minute (0 - 59)
            # |  .------------- hour (0 - 23)
            # |  |  .---------- day of month (1 - 31)
            # |  |  |  .------- month (1 - 12) OR jan,feb,mar,apr ...
            # |  |  |  |  .---- day of week (0 - 6) (Sunday=0 or 7) OR sun,mon,tue,wed,thu,fri,sat
            # |  |  |  |  |
            # *  *  *  *  * user-name command to be executed
        """
        # body: {'minute': '*', 'hour': '*', 'dayOfMonth': '*', 'month': '*', 'dayOfWeek': '*', 'removeJobAfterRunning': False, 'controller': '192.168.28.7:8000', 'playbook': '/opt/KeystackTests/Playbooks/pythonSample.yml', 'debug': False, 'emailResults': False, 'awsS3': False, 'jira': False, 'pauseOnError': False, 'holdEnvsIfFailed': False, 'abortTestOnFailure': False, 'includeLoopTestPassedResults': False, 'sessionId': '', 'group': 'Default'}
        user = AccountMgr().getRequestSessionUser(request)
        remoteController = request.data.get('remoteController', None)
        mainControllerIp, remoteControllerIp, ipPort = getMainAndRemoteControllerIp(request, remoteController)
    
        cronjobUser = GlobalVars.user
        statusCode = HtmlStatusCodes.success
        status = 'success'
        errorMsg = None

        # 2022-03-23T02:00:00-07:00
        # minute = body['minute']
        # hour = body['hour']
        # dayOfMonth = body['dayOfMonth']
        # month = body['month']
        # dayOfWeek = body['dayOfWeek']
        # removeJobAfterRunning = body['removeJobAfterRunning']


        # 2022-03-23T02:00:00-07:00
        minute                       = request.data.get('minute', None)
        hour                         = request.data.get('hour', None)
        dayOfMonth                   = request.data.get('dayOfMonth', None)
        month                        = request.data.get('month', None)
        dayOfWeek                    = request.data.get('dayOfWeek', None)
        removeJobAfterRunning        = request.data.get('removeJobAfterRunning', None)
        group                        = request.data.get('group', 'Default')
        sessionId                    = request.data.get('sessionId', None)
        playbook                     = request.data.get('playbook', None)
        debugMode                    = request.data.get('debugMode', None)
        awsS3                        = request.data.get('awsS3', None)
        jira                         = request.data.get('jira', None)
        emailResults                 = request.data.get('emailResults', None)
        pauseOnError                 = request.data.get('pauseOnError', None)
        holdEnvsIfFailed             = request.data.get('holdEnvsIfFailed', None)
        abortTestOnFailure           = request.data.get('abortTestOnFailure', None)
        includeLoopTestPassedResults = request.data.get('includeLoopTestPassedResults', None)
                                            
        schedule = f'playbook={playbook} minute={minute} hour={hour} day={dayOfMonth} month={month} dayOfWeek={dayOfWeek}'

        if remoteControllerIp and remoteControllerIp != mainControllerIp:
            params = {"minute": minute, "hour": hour, "dayOfMonth": dayOfMonth, "month": month, "dayOfWeek": dayOfWeek, "removeJobAfterRunning": removeJobAfterRunning, "group": group, "sessionId": sessionId, "playbook": playbook, "debugMode": debugMode, "awsS3": awsS3, "jira": jira, "emailResults": emailResults, "pauseOnError": pauseOnError, "holdEnvsIfFailed": holdEnvsIfFailed, "abortTestOnFailure": abortTestOnFailure, "includeLoopTestPassedResults": includeLoopTestPassedResults, }
            
            restApi = '/api/v1/pipelines/jobScheduler/add'
            response, errorMsg = executeRestApiOnRemoteController('post', remoteControllerIp, ipPort, restApi, params, 
                                                                  user, webPage=Vars.webpage, action='AddScheduledJob')
            if errorMsg:
                status = 'failed'
                statusCode = HtmlStatusCodes.error 
                   
        else:
            try: 
                localHostIp = os.environ.get('keystack_localHostIp', 'localhost')
                keystackIpPort = os.environ.get('keystack_keystackIpPort', '88028')
                   
                if JobSchedulerAssistant().isCronExists(playbook, minute, hour, dayOfMonth, month, dayOfWeek):
                    SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='AddJobSchedule', msgType='Info', msg='Cron already exists: {schedule}')
                    return Response({'status':'failed', 'errorMsg':'Job already exists'}, status=HtmlStatusCodes.error)
                
                # REST API: Run playbook function is in Playbook apiView.py
                # For job scheduling, include the param -webhook to bypass verifying api-key
                #newJob = f'{minute} {hour} {dayOfMonth} {month} {dayOfWeek} keystack curl -d "sessionId={sessionId}&playbook={playbook}&awsS3={awsS3}&jira={jira}&pauseOnError={pauseOnError}&debug={debugMode}&group={group}&holdEnvsIfFailed={holdEnvsIfFailed}&abortTestOnFailure={abortTestOnFailure}&includeLoopTestPassedResults={includeLoopTestPassedResults}&scheduledJob=\'{schedule}\'&removeJobAfterRunning={removeJobAfterRunning}&webhook=true" -H "Content-Type: application/x-www-form-urlencoded" -X POST http://{localHostIp}:{keystackIpPort}/api/v1/playbook/run'
                
                newJob = f'{minute} {hour} {dayOfMonth} {month} {dayOfWeek} {cronjobUser} curl -d "sessionId={sessionId}&playbook={playbook}&awsS3={awsS3}&jira={jira}&pauseOnError={pauseOnError}&debug={debugMode}&group={group}&holdEnvsIfFailed={holdEnvsIfFailed}&abortTestOnFailure={abortTestOnFailure}&includeLoopTestPassedResults={includeLoopTestPassedResults}&scheduledJob=\'{schedule}\'&removeJobAfterRunning={removeJobAfterRunning}&webhook=true" -H "Content-Type: application/x-www-form-urlencoded" -X POST http://{localHostIp}:{keystackIpPort}/api/v1/playbook/run'
                
                cronJobs = JobSchedulerAssistant().getCurrentCronjobs()
                cronJobs += f'{newJob}\n'
                
                # Leaving behind for debugging purpose
                #cronJobs = f"""
                #{newJob}
                #* * * * * root date > /proc/1/fd/1 2>/proc/1/fd/2
                #* * * * * root echo "Hello World! 8" >/proc/1/fd/1 2>/proc/1/fd/2
                #"""

                execSubprocessInShellMode(f"sudo echo '{cronJobs}' | sudo tee /etc/crontab", showStdout=False)
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='AddJobSchedule', msgType='Info', msg=newJob.replace('&webhook=true', ''))            
            
            except Exception as errMsg:
                status = 'failed'
                statusCode = HtmlStatusCodes.error
                errorMsg = str(errMsg)
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='AddJobSchedule', msgType='Error',
                                          msg=errMsg, forDetailLogs=traceback.format_exc(None, errMsg))

        return Response(data={'status':status, 'errorMsg':errorMsg}, status=statusCode)


class DeleteScheduledJob(APIView):
    @verifyUserRole(webPage=Vars.webpage, action='DeleteScheduledJob', exclude=["engineer"])    
    def post(self, request):
        """ 
        Delete a scheduled job.  Called from template.
        """
        user = AccountMgr().getRequestSessionUser(request)
        remoteController = request.data.get('remoteController', None)
        mainControllerIp, remoteControllerIp, ipPort = getMainAndRemoteControllerIp(request, remoteController)
        removeScheduledJobs = request.data.get('removeScheduledJobs', None)
        status = 'success'
        statusCode = HtmlStatusCodes.success
        errorMsg = None
        
        if remoteControllerIp and remoteControllerIp != mainControllerIp:
            params = {"removeScheduledJobs": removeScheduledJobs}
            restApi = '/api/v1/pipelines/jobScheduler/delete'
            response, errorMsg = executeRestApiOnRemoteController('post', remoteControllerIp, ipPort, restApi, params, 
                                                                  user, webPage=Vars.webpage, action='DeleteScheduledJob')
            if errorMsg:
                status = 'failed'
                statusCode = HtmlStatusCodes.error 
                   
        else:        
            try:
                #  [{playbook, month, day, hour, min}, {}, ...]
                removeJobList = []
                
                for cron in removeScheduledJobs:
                    # eachJob: {'playbook': 'goody', 'month': '3', 'day': '26', 'hour': '17', 'minute': '29'}
                    #removeJobList.append({'playbook':cron['playbook'], 'month':cron['month]'], 'day':cron['day'], 'hour':cron['hour'], 'min':cron['minute']})
                    
                    # {'playbook': 'pythonSample', 'month': '*', 'day': '*', 'hour': '*', 'minute': '*', 'dayOfWeek': '*'}
                    removeJobList.append(cron)
                    SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='DeleteScheduledJob', msgType='Info',
                                              msg=cron, forDetailLogs='')
                        
                JobSchedulerAssistant().removeCronJobs(listOfJobsToRemove=removeJobList, user=user)
                statusCode = HtmlStatusCodes.success
                
            except Exception as errMsg:
                errorMsg = str(errMsg)
                status = 'failed'
                statusCode = HtmlStatusCodes.error
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='DeleteScheduledJob', msgType='Error',
                                          msg=errorMsg, forDetailLogs=traceback.format_exc(None, errMsg))            

        return Response(data={'status': status, 'errorMsg': errorMsg}, status=statusCode)


class ScheduledJobs(APIView):
    @verifyUserRole()
    def post(self, request):        
        """         
        Create a data table of scheduled jobs. Called by template.
        """
        user = AccountMgr().getRequestSessionUser(request)
        remoteController = request.data.get('remoteController', None)
        mainControllerIp, remoteControllerIp, ipPort = getMainAndRemoteControllerIp(request, remoteController)
        status = 'success'
        errorMsg = None
        statusCode = HtmlStatusCodes.success
            
        if remoteControllerIp and remoteControllerIp != mainControllerIp:
            params = {}
            restApi = '/api/v1/pipelines/jobScheduler/scheduledJobs'
            response, errorMsg = executeRestApiOnRemoteController('post', remoteControllerIp, ipPort, restApi, params, 
                                                                  user, webPage=Vars.webpage, action='ScheduledJobs')
            if errorMsg:
                status = 'failed'
                statusCode = HtmlStatusCodes.error
                html = '' 
            else:
                html = response.json()['jobSchedules']
                       
        else:    
            #html = '<table class="table table-sm table-bordered table-fixed tableFixHead">'
            html = '<table class="tableMessages table-bordered">'
            html += '<thead>'
            html += '<tr>'
            html += '<th>Delete</th>'
            html += '<th>Playbook</th>'
            html += '<th>Scheduled To Run</th>'
            html += '</tr>'
            html += '</thead>'

            try:
                cronjobs = JobSchedulerAssistant().getCurrentCronjobList()
                
                # 25 12 24 3 * root curl -d "playbook=goody&user=Hubert Gee" -H "Content-Type: application/x-www-form-urlencoded" -X POST http://172.16.1.16:8000/api/playbook
                # <a href="#" testLogResultPath="{moduleTestResultsPath}" onclick="openTestLogsModal(this)" data-bs-toggle="modal" data-bs-target="#testLogsModalDiv">View Logs</a>
                for eachCron in cronjobs:
                    # Handle the \t: '17 *\t* * *\troot    cd / && run-parts --report /etc/cron.hourly
                    eachCron = eachCron.replace('\t', ' ')
                    
                    # [{playbook, month, day, hour, min}]
                    # 00 14 31 3 * root curl -d "playbook=sanity&user=Hubert Gee"

                    # 42 11 6 10 * keystack curl -d "playbook=/opt/KeystackTests/Playbooks/pythonSample.yml&awsS3=False&jira=False&pauseOnError=False&debug=False" -H "Content-Type: application/x-www-form-urlencoded" -X POST http://192.168.28.7:8000/api/v1/playbook/run
                    #
                    match = search(' *([0-9\*]+) *([0-9\*]+) *([0-9\*]+) *([0-9\*]+) *([0-9\*]+).*playbook=([^ &]+).*-H', eachCron)
                    if match:
                        min       = match.group(1)
                        hour      = match.group(2)
                        day       = match.group(3)
                        month     = match.group(4)
                        dayOfWeek = match.group(5)
                        playbook  = match.group(6)

                        html += '<tr>'
                        html += f'<td class="textAlignCenter"><input type="checkbox" name="jobSchedulerMgmt" playbook={playbook} dayOfWeek={dayOfWeek} month={month} day={day} hour={hour} minute={min} /></td>'
                        html += f'<td>{playbook}</td>'
                        html += f'<td>Minute:{min}&emsp; Hour:{hour}&emsp; DayOfMonth:{day}&emsp; Month:{month}&emsp; DayOfWeek:{dayOfWeek}</td>'
                        html += '</tr>'
                    else:
                        match     = search(' *([0-9*]+) *([0-9*]+) *([0-9*]+) *([0-9*]+) *([0-9*]+).*', eachCron)
                        min       = match.group(1)
                        hour      = match.group(2)
                        day       = match.group(3)
                        month     = match.group(4)
                        dayOfWeek = match.group(5)
                        html += '<tr>'
                        html += f'<td class="textAlignCenter"><input type="checkbox" name="jobSchedulerMgmt" playbook="" dayOfWeek={dayOfWeek} month={month} day={day} hour={hour} minute={min} /></td>'
                        html += f'<td></td>'
                        html += f'<td>Minute:{min}&emsp; Hour:{hour}&emsp; DayOfMonth:{day}&emsp; Month:{month}&emsp; DayOfWeek:{dayOfWeek}</td>'
                        html += '</tr>'
                                            
                html += '</table>'
                
            except Exception as errMsg:
                errorMsg = str(errMsg)
                status = 'failed'
                statusCode = HtmlStatusCodes.error
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='GetScheduledJobs', msgType='Error',
                                          msg=errorMsg, forDetailLogs=traceback.format_exc(None, errMsg))
        
        return Response(data={'jobSchedules': html, 'status':status, 'errorMsg':errorMsg}, status=statusCode)
    
    
class GetCronScheduler(APIView):
    @verifyUserRole()
    def post(self, request):
        """
        Dropdowns for minute, hour, day, month, dayOfWeek
        """
        user = AccountMgr().getRequestSessionUser(request)
        remoteController = request.data.get('remoteController', None)
        mainControllerIp, remoteControllerIp, ipPort = getMainAndRemoteControllerIp(request, remoteController)
        statusCode = HtmlStatusCodes.success
        status = 'success'
        errorMsg = None

        if remoteControllerIp and remoteControllerIp != mainControllerIp:
            params = {}
            restApi = '/api/v1/pipelines/jobScheduler/getCronScheduler'
            response, errorMsg = executeRestApiOnRemoteController('post', remoteControllerIp, ipPort, restApi, params, 
                                                                  user, webPage=Vars.webpage, action='GetCronScheduler')
            if errorMsg:
                status = 'failed'
                statusCode = HtmlStatusCodes.error 
            else:
                minute     = response.json()['minute']
                hour       = response.json()['hour']
                dayOfMonth = response.json()['dayOfMonth']
                month      = response.json()['month']
                dayOfWeek  = response.json()['dayOfWeek']
                   
        else:        
            minute = f'<label for="minute">Minute:&emsp; </label>'
            minute += '<select id="minute">'
            minute += f'<option value="*" selected="selected">*</option>'
            for option in range(0, 61):            
                minute += f'<option value="{option}">{option}</option>'
            minute += f'</select> &emsp;&emsp;'
            
            hour = f'<label for="hour">Hour:&emsp; </label>'
            hour += '<select id="hour">'
            hour += f'<option value="*" selected="selected">*</option>'
            for option in range(0, 24):            
                hour += f'<option value="{option}">{option}</option>'
            hour += f'</select> &emsp;&emsp;'

            dayOfMonth = f'<label for="dayOfMonth">Day Of Month:&emsp; </label>'
            dayOfMonth += '<select id="dayOfMonth">'
            dayOfMonth += f'<option value="*" selected="selected">*</option>'
            for option in range(1, 32):            
                dayOfMonth += f'<option value="{option}">{option}</option>'
            dayOfMonth += f'</select> &emsp;&emsp;'

            month = f'<label for="month">Month:&emsp; </label>'
            month += '<select id="month">'
            month += f'<option value="*" selected="selected">*</option>'
            for option in ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']:            
                month += f'<option value="{option}">{option}</option>'
            month += f'</select> &emsp;&emsp;'

            dayOfWeek = f'<label for="dayOfWeek">Day Of Week:&emsp; </label>'
            dayOfWeek += '<select id="dayOfWeek">'
            dayOfWeek += f'<option value="*" selected="selected">*</option>'
            for option in ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat']:            
                dayOfWeek += f'<option value="{option}">{option}</option>'
            dayOfWeek += f'</select>'
                                                
        return Response(data={'minute':minute, 'hour':hour, 'dayOfMonth':dayOfMonth, 'month':month, 'dayOfWeek':dayOfWeek,
                              'status':status, 'errorMsg':errorMsg}, status=statusCode)


class GetJobSchedulerCount(APIView):
    @verifyUserRole()
    def post(self, request):
        """
        Get the total amount of scheduled jobs
        """
        user = AccountMgr().getRequestSessionUser(request)
        remoteController = request.data.get('remoteController', None)
        mainControllerIp, remoteControllerIp, ipPort = getMainAndRemoteControllerIp(request, remoteController)
        statusCode = HtmlStatusCodes.success
        status = 'success'
        errorMsg = None
        totalCronJobs = 0

        if remoteControllerIp and remoteControllerIp != mainControllerIp:
            params = {}
            restApi = '/api/v1/pipelines/jobScheduler/getJobSchedulerCount'
            response, errorMsg = executeRestApiOnRemoteController('post', remoteControllerIp, ipPort, restApi, params, 
                                                                  user, webPage=Vars.webpage, action='GetJobSchedulerCount')
            if errorMsg:
                status = 'failed'
                statusCode = HtmlStatusCodes.error
            else:
                totalCronJobs = response.json()['totalScheduledJobs']
                   
        else:         
            try:
                totalCronJobs = len(JobSchedulerAssistant().getCurrentCronjobList())
            except Exception as errMsg:
                errorMsg = str(errMsg)
                status = 'failed'
                statusCode = HtmlStatusCodes.error
            
        return Response(data={'totalScheduledJobs': totalCronJobs, 'status':status, 'errorMsg':errorMsg}, status=statusCode)

 
class TerminateProcessId(APIView):
    @verifyUserRole(webPage=Vars.webpage, action='Terminate')
    def post(self,request):
        """ 
        body: {'sessionId': 'awesomeTest2', 'playbook': '/opt/KeystackTests/Playbooks/pythonSample.yml', 'module': 'CustomPythonScripts2', 'processId': '36895', 'statusJsonFile': '/opt/KeystackTests/Results/PLAYBOOK=pythonSample/09-30-2022-15:31:36:496194_awesomeTest2/overallSummary.json'}
        """        
        sessionId      = request.data.get('sessionId', None)
        processId      = request.data.get('processId', None)
        playbook       = request.data.get('playbook', None)
        module         = request.data.get('module', None)
        statusJsonFile = request.data.get('statusJsonFile', None)
        
        timestampResultPath = '/'.join(statusJsonFile.split('/')[:-1])
        envMgmtPath = f'/{timestampResultPath}/.Data/EnvMgmt'
        user = AccountMgr().getRequestSessionUser(request)
        remoteController = request.data.get('remoteController', None)
        mainControllerIp, remoteControllerIp, ipPort = getMainAndRemoteControllerIp(request, remoteController)
        statusCode = HtmlStatusCodes.success
        status = 'success'
        errorMsg = None

        if remoteControllerIp and remoteControllerIp != mainControllerIp:
            params = {"sessionId": sessionId, "processId": processId, "playbook": playbook, 
                      "module": module, "statusJsonFile": statusJsonFile}
            restApi = '/api/v1/pipelines/terminateProcessId'
            response, errorMsg = executeRestApiOnRemoteController('post', remoteControllerIp, ipPort, restApi, params, 
                                                                  user, webPage=Vars.webpage, action='TerminateProcessId')
            if errorMsg:
                status = 'failed'
                statusCode = HtmlStatusCodes.error 
                   
        else:          
            # processIdLink: <a href="#" style="text-decoration:none" sessionId=hgee2 playbook=/opt/KeystackTests/Playbooks/pythonSample.yml module=CustomPythonScripts processId= statusJsonFile=/opt/KeystackTests/Results/PLAYBOOK=pythonSample/09-27-2022-08:04:59:982339_hgee2/STAGE=Test_MODULE=CustomPythonScripts_ENV=loadcoreSample/moduleSummary.json onclick="terminateProcessId(this)">Terminate</a>

            if statusJsonFile == 'None':
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='Terminate', msgType='Failed', 
                                        msg=f'No overallSummaryData.json result file for test: sessionId:{sessionId} playbook:{playbook} module:{module}')
                return Response(data={'status': 'failed', 'errorMsg': 'No overallSummaryData.json file found'}, status=HtmlStatusCodes.error)
            
            try:
                from datetime import datetime
                
                # Terminate the running the process
                if os.environ['keystack_platform'] == 'linux':
                    result, process = execSubprocessInShellMode(f'sudo kill -9 {processId}', showStdout=False)
                    
                if os.environ['keystack_platform'] == 'docker':
                    result, process = execSubprocessInShellMode(f'kill -9 {processId}', showStdout=False)
                    
                # Verify the termination
                result, process = execSubprocessInShellMode(f'ps -ef | grep keystack | grep {module} | grep {sessionId}', showStdout=False)

                # Update the test's overallSummary.json
                testStopTime = datetime.now()
                testStatusFile = readJson(statusJsonFile)
                testStatusFile['status'] = 'Terminated'
                testStatusFile['result'] = 'Incomplete'
                testStatusFile['stopped'] = testStopTime.strftime('%m-%d-%Y %H:%M:%S:%f')
                testStatusFile['currentlyRunning'] = ''

                # Don't remove the test session from the active user list.  
                # The user might have terminated the session for debugging. Just remove from the wait-list.
                if testStatusFile['holdEnvsIfFailed']:
                    for envMgmtDataFile in glob(f'{envMgmtPath}/*.json'):
                        envMgmtData = readJson(envMgmtDataFile)
                        env = envMgmtData['env']
                        envSessionId = envMgmtData['sessionId']
                        envUser = envMgmtData['user']
                        envStage = envMgmtData['stage']
                        envModule = envMgmtData['module']
                        envMgmtObj = ManageEnv()
                        envList = []
                        
                        # {'user': 'hgee', 'sessionId': '11-07-2022-12:37:30:802368_2280_debugMode', 'stage': 'Test', 'module': 'CustomPythonScripts', 'env': 'qa-rack1'}
                        envMgmtObj.setenv = env
                        envMgmtObj.removeFromWaitList(envSessionId, user=envUser, stage=envStage, module=envModule)
                        envList.append(env)
                else:
                    # Remove env from activeUserList
                    for envMgmtDataFile in glob(f'{envMgmtPath}/*.json'):
                        envMgmtData = readJson(envMgmtDataFile)
                        env = envMgmtData['env']
                        envSessionId = envMgmtData['sessionId']
                        envUser = envMgmtData['user']
                        envStage = envMgmtData['stage']
                        envModule = envMgmtData['module']
                        envMgmtObj = ManageEnv()
                        envList = []
                        
                        # {'user': 'hgee', 'sessionId': '11-07-2022-12:37:30:802368_2280_debugMode', 'stage': 'Test', 'module': 'CustomPythonScripts', 'env': 'qa-rack1'}
                        envMgmtObj.setenv = env
                        envMgmtObj.removeFromActiveUsersList([{'user':envUser, 'sessionId':envSessionId, 'stage':envStage, 'module':envModule}])
                    
                        envMgmtData['envIsReleased'] = True
                        writeToJson(jsonFile=envMgmtDataFile, data=envMgmtData)

                # Update overallSummary status with Terminated    
                writeToJson(jsonFile=statusJsonFile, data=testStatusFile)

                # "waitList": [{"module": "LoadCore", "sessionId": "11-01-2022-04:21:00:339301_rocky_200Loops",
                #               "stage": "LoadCoreTest", "user": "rocky"}
                for waitingSession in envMgmtObj.getWaitList():
                    # Remove sessionId in waitlist
                    if waitingSession['sessionId'] == envSessionId:
                        envMgmtObj.removeFromWaitList(sessionId=envSessionId, user=waitingSession['user'], 
                                                        stage=waitingSession['stage'], module=waitingSession['module'])
                        
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='Terminate', 
                                        msgType='Info', msg=f'sessionId:{sessionId} playbook:{playbook} module:{module}')
                
            except Exception as errMsg:                
                statusCode = HtmlStatusCodes.error
                status = 'failed'
                errorMsg = str(errMsg)
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='Terminate', msgType='Error',
                                        msg=f'sessionId:{sessionId} playbook:{playbook} module:{module}',
                                        forDetailLogs=traceback.format_exc(None, errMsg))

        return Response(data={'status':status, 'errorMsg':errorMsg}, status=statusCode)
    

class ResumePausedOnError(APIView):
    @verifyUserRole()
    def post(self,request):
        user = AccountMgr().getRequestSessionUser(request)
        remoteController = request.data.get('remoteController', None)
        mainControllerIp, remoteControllerIp, ipPort = getMainAndRemoteControllerIp(request, remoteController)
        statusCode = HtmlStatusCodes.success
        status = 'success'
        errorMsg = None
        pausedOnErrorFile = request.data.get('pausedOnErrorFile', None)
        
        if remoteControllerIp and remoteControllerIp != mainControllerIp:
            params = {'pausedOnErrorFile': pausedOnErrorFile}
            restApi = '/api/v1/pipelines/resumePausedOnError'
            response, errorMsg = executeRestApiOnRemoteController('post', remoteControllerIp, ipPort, restApi, params, 
                                                                  user, webPage=Vars.webpage, action='ResumePausedOnError')
            if errorMsg:
                status = 'failed'
                statusCode = HtmlStatusCodes.error 
                   
        else:        
            try:
                os.remove(pausedOnErrorFile)
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='ResumePausedOnError', msgType='Info',
                                        msg=pausedOnErrorFile, forDetailLogs='')
            except Exception as errMsg:
                statusCode = HtmlStatusCodes.error
                status = 'failed'
                errorMsg = str(errMsg)
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='ResumePausedOnError', msgType='Error',
                                        msg=errorMsg, forDetailLogs=traceback.format_exc(None, errMsg))
            
        return Response(data={'errorMsg': errorMsg, 'status': status}, status=statusCode)


class ShowGroups(APIView):
    @verifyUserRole()
    def post(self,request):
        user = AccountMgr().getRequestSessionUser(request)
        remoteController = request.data.get('remoteController', None)
        mainControllerIp, remoteControllerIp, ipPort = getMainAndRemoteControllerIp(request, remoteController)
        statusCode = HtmlStatusCodes.success
        status = 'success'
        errorMsg = None
        groupsRadioButtons = ''

        if remoteControllerIp and remoteControllerIp != mainControllerIp:
            params = {}
            restApi = '/api/v1/pipelines/showGroups'
            response, errorMsg = executeRestApiOnRemoteController('post', remoteControllerIp, ipPort, restApi, params, 
                                                                  user, webPage=Vars.webpage, action='ShowGroups')
            if errorMsg:
                status = 'failed'
                statusCode = HtmlStatusCodes.error
                groupsRadioButtons = '' 
            else:
                groupsRadioButtons = response.json()['groups']
                
        else:        
            try:
                testGroupsFile = GlobalVars.testGroupsFile
                if os.path.exists(testGroupsFile):
                    groupsData = readYaml(testGroupsFile)
                    
                    for group in groupsData.keys():
                        groupsRadioButtons += '<div class="pl-2 form-check form-check-inline" style="inline:block; color:black">'
                        if group == "Default":
                            groupsRadioButtons += f'<input class="form-check-input" type="radio" checked="checked" id="{group}" name="group" value="{group}">'
                        else:
                            groupsRadioButtons += f'<input class="form-check-input" type="radio" id="{group}" name="group" value="{group}" onclick="setSelectedTestGroup(this)">' 
                                            
                        groupsRadioButtons += f'<label for="{group}" class="form-check-label">{group}</label>'
                        groupsRadioButtons += '</div>'

            except Exception as errMsg:
                statusCode = HtmlStatusCodes.error
                errorMsg = str(errMsg)
                status = 'failed'
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='GetGroups', msgType='Error',
                                        msg=errMsg, forDetailLogs=traceback.format_exc(None, errMsg))
          
        return Response(data={'groups': groupsRadioButtons, 'status':status, 'errorMsg': errorMsg}, status=statusCode)
  
    
class GetSessionGroups(APIView):
    @verifyUserRole()
    def post(self,request):
        """
        Called by base.html
        
        For Pipelines dropdown:
            <GROUPNAME>: <total>
        """
        statusCode = HtmlStatusCodes.success
        errorMsg = None
        status = 'success'
        user = AccountMgr().getRequestSessionUser(request)
        remoteController = request.data.get('remoteController', None)
        mainControllerIp, remoteControllerIp, ipPort = getMainAndRemoteControllerIp(request, remoteController)
        html = ''

        if remoteControllerIp and remoteControllerIp != mainControllerIp:
            params = {}
            restApi = '/api/v1/pipelines/getSessionGroups'
            response, errorMsg = executeRestApiOnRemoteController('post', remoteControllerIp, ipPort, restApi, params, 
                                                                  user, webPage=Vars.webpage, action='GetSessionGroups')
            if errorMsg:
                status = 'failed'
                statusCode = HtmlStatusCodes.error
            else:
                html = response.json()['sessionGroups'] 
                   
        else:        
            try:
                # getGroupSessions gets test groups in the /KeystackTests/Results/GROUPS=?
                sessionGroups = getGroupSessions(user)
                # body = json.loads(request.body.decode('UTF-8'))
                # remoteController = body['remoteController']

                for groupName in sessionGroups:
                    totalPlaybookSessions = 0
                    for playbook in glob(f'{GlobalVars.keystackTestRootPath}/Results/GROUP={groupName}/PLAYBOOK=*'):
                        for timestampResult in glob(f'{playbook}/*'):
                            if os.path.exists(f'{timestampResult}/overallSummary.json'):
                                totalPlaybookSessions += 1
                        
                    html += f'<a class="collapse-item pl-3 textBlack" href="/sessionMgmt?group={groupName}"><i class="fa-regular fa-folder pr-3"></i>{groupName}: {totalPlaybookSessions}</a>'
                                            
            except Exception as errMsg:
                statusCode = HtmlStatusCodes.error
                errorMsg = str(errMsg)
                status = 'failed'
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='GetSessionGroups', msgType='Error',
                                          msg=errorMsg,
                                          forDetailLogs=traceback.format_exc(None, errMsg))

        return Response(data={'sessionGroups':html, 'status':status, 'errorMsg': errorMsg}, status=statusCode)
    
    