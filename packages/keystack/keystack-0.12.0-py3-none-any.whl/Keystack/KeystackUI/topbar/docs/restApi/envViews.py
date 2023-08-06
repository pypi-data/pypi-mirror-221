import os, sys, traceback
from glob import glob
from re import search
from shutil import rmtree

from systemLogging import SystemLogsAssistant
from topbar.settings.accountMgmt.verifyLogin import verifyUserRole
from topbar.settings.accountMgmt.accountMgr import AccountMgr
from topbar.docs.restApi.controllers import getMainAndRemoteControllerIp, executeRestApiOnRemoteController
import EnvMgmt
from execRestApi import ExecRestApi
from globalVars import HtmlStatusCodes
from keystackUtilities import readJson, writeToJson, readYaml, execSubprocessInShellMode, mkdir2, chownChmodFolder, writeToFile, getTimestamp
from EnvMgmt import ManageEnv
from db import DB
from globalVars import GlobalVars
from sidebar.sessionMgmt.views import SessionMgmt
from commonLib import getHttpMethodIpAndPort

from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets


class Vars:
    """ 
    For logging the correct topics.
    To avoid human typo error, always use a variable instead of typing the word.
    """
    webpage = 'envs'
    envMgmtDB = 'envMgmt'
    envLoadBalanceDB = 'envLoadBalanceGroups'
    
    keystackUIIpAddress, keystackIpPort, httpMethod = getHttpMethodIpAndPort()  

     
def getTableData(envGroup, user) -> str:
    """ 
    Get setup yml files from /$keystackTestRootPath/Setup folder.
    
    Setup groups are subfolder names
    """
    tableData: str = ''
    envPath = GlobalVars.envPath
    envMgmtPath = GlobalVars.envMgmtPath
    
    for rootPath,dirs,files in os.walk(envPath): 
        #  root=/opt/KeystackTests/Envs files=['pythonSample.yml', 'loadcoreSample.yml']          
        if bool(search(f'^{GlobalVars.keystackTestRootPath}/{envGroup}$', rootPath)) and files:
            # Just file names. Not path included.
            for envYmlFile in files:
                if envYmlFile.endswith('.yml'):
                    envYmlFileFullPath = f'{rootPath}/{envYmlFile}'
                    
                    try:
                        envData = readYaml(envYmlFileFullPath)
                    except Exception as errMsg:
                        # TODO: If there is an invisible tab in the yml file, no env will be shown
                        #       Must show the error to the user
                        print(f'setup: getTableData error: Problem found in yml file. Most likely tabs were used instead of spaces: {envYmlFileFullPath}: {errMsg}')
                        continue 

                    if envData is None:
                        continue
                    
                    if type(envData) != dict:
                        print(f'setup getTableData error: Yaml file contents is string type. Expecting dict type. Check the yaml file: {envYmlFileFullPath}')
                        continue
            
                    isParallelUsage = envData.get('parallelUsage', False) # Default to No if not exists
                    if isParallelUsage:
                        isParallelUsage = 'Yes'
                    if isParallelUsage == False:
                        isParallelUsage = 'No'
                
                    # Samples/loadcoreSample 
                    regexMatch = search(f'{GlobalVars.keystackTestRootPath}/Envs/(.+)\.y.+', envYmlFileFullPath)
                    if regexMatch:
                        envName = regexMatch.group(1)

                    envMgmtObj = ManageEnv(envName)
                    if envMgmtObj.isEnvExists() == False:
                        envMgmtObj.addEnv()

                    isAvailable = envMgmtObj.isEnvAvailable()
                    if isAvailable: isAvailable = 'Yes'
                    if isAvailable == False: isAvailable = 'No'
                    totalWaiting = len(envMgmtObj.getWaitList())
                    activeUsers = envMgmtObj.getActiveUsers()
                    totalActiveUsers = len(activeUsers)
                    
                    loadBalanceGroups = envMgmtObj.getLoadBalanceGroups()
                    if loadBalanceGroups:
                        lbgDropdown = '<div class="dropdown">'
                        lbgDropdown += '<a class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup=true aria-expanded=false>View</a>'
                        lbgDropdown += '  <ul class="dropdown-menu dropdownSizeSmall">'
                        for lbg in loadBalanceGroups:
                            lbgDropdown += f'<li class="dropdown-item">{lbg}</li>'
                        lbgDropdown += '</ul></div>' 
                    else:
                        lbgDropdown = 'None'
                        
                    tableData += '<tr>'
                    tableData += f'<td><input type="checkbox" name="envCheckboxes" value="{envYmlFileFullPath}"/></td>'
                    tableData += f'<td><button class="btn btn-sm btn-outline-primary" value="{envYmlFileFullPath}" onclick="getFileContents(this)" data-bs-toggle="modal" data-bs-target="#viewEditEnvModal">View / Edit</button></td>'
                    
                    tableData += f'<td style="text-align:left">{envName}</td>'
                    tableData += f'<td style="text-align:center">{lbgDropdown}</td>'
                    tableData += f'<td style="text-align:center">{isParallelUsage}</td>'
                    tableData += f'<td style="text-align:center">{isAvailable}</td>'

                    # data-toggle="modal" data-target="#modalId"
                    tableData += f'<td style="text-align:center"><a href="#" onclick="activeUsersList(this)" env={envName} data-bs-toggle="modal" data-bs-target="#activeUsersModal">ActiveUsers:{totalActiveUsers}&emsp;&ensp;Waiting:{totalWaiting}</a></td>'
                    
                    # The reserve button has no stage and module
                    tableData += f'<td><button onclick="reserveEnv(this)" env={envName} class="btn btn-sm btn-outline-primary">Reserve</button></td>'
                      
                    if isParallelUsage == 'No' and totalActiveUsers > 0: 
                        tableData += f'<td style="text-align:center"><button class="btn btn-sm btn-outline-primary" env={envName} onclick="releaseEnv(this)" >Release</button></td>'
                    else:
                        tableData += '<td></td>'
                        
                    tableData += f'<td><button onclick="resetEnv(this)" env={envName} class="btn btn-sm btn-outline-primary">Reset</button></td>'
                                                
                    tableData += '</tr>'
      
    return tableData


class GetEnvTableData(APIView):
    swagger_schema = None

    @verifyUserRole()
    def post(self, request):
        user = AccountMgr().getRequestSessionUser(request)
        remoteController = request.data.get('remoteController', None)
        mainControllerIp, remoteControllerIp, ipPort = getMainAndRemoteControllerIp(request, remoteController)
        errorMsg = None
        statusCode= HtmlStatusCodes.success
        status = 'success'
        tableData = ''

        if request.GET:
            # Rest APIs with inline params come in here
            try:
                envGroupToView = request.GET.get('envGroup')                
            except Exception as errMsg:
                errorMsg = str(errMsg)
                status = 'failed'
                statusCode = HtmlStatusCodes.error
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='getEnvDataTable', msgType='Error',
                                          msg=errorMsg, forDetailLogs=traceback.format_exc(None, errMsg))
                return Response(data={'status': status, 'errorMsg': errorMsg}, status=statusCode)
        
        # JSON format
        if request.data:
            # <QueryDict: {'env': 'loadcoreSample', 'sessionId': '02-04-2023-08:53:15:021768_7277', 'overallSummaryFile': '/opt/KeystackTests/Results/GROUP=Default/PLAYBOOK=pythonSample/02-04-2023-08:53:15:021768_7277/overallSummary.json', 'user': 'hgee', 'stage': 'Teardown', 'module': 'CustomPythonScripts', 'utilization': False, 'webhook': True}
            try:
                envGroupToView = request.data['envGroup']
            except Exception as errMsg:
                errorMsg = str(errMsg)
                status = 'failed'
                statusCode = HtmlStatusCodes.error
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='getEnvDataTable', msgType='Error',
                                          msg=errorMsg, forDetailLogs=traceback.format_exc(None, errMsg))
                return Response(data={'status': status, 'errorMsg': errorMsg}, status=statusCode)
        
        if remoteControllerIp and remoteControllerIp != mainControllerIp:
            params = {"envGroup": envGroupToView}
            restApi = '/api/v1/env/getEnvTableData'
            response, errorMsg = executeRestApiOnRemoteController('post', remoteControllerIp, ipPort, restApi, params, 
                                                                  user, webPage=Vars.webpage, action='GetEnvTableData')
            if errorMsg:
                status = 'failed'
                statusCode = HtmlStatusCodes.error 
            else:
                tableData = response.json()['tableData'] 
              
        else:                         
            try:            
                # Self cleanup on activeUsers
                # Users might have included -holdEnvsIfFailed and deleted the pipeline or test result
                # The env still has the active user. We need to automatically release the active-user from the env.
                #    1> Get all envs for the envGroupToView
                #    2> Get active users for all envs in this env group
                #    3> Check if test results exists.  If not, the user deleted the pipeline test results before
                #       releasing the env.

                envMgmtObj = ManageEnv(envGroupToView)                
                envGroupPath = f'{GlobalVars.keystackTestRootPath}/{envGroupToView}'

                for env in glob(f'{envGroupPath}/*'):
                    if bool(search('.+\.(yml|ymal)$', env)) == False:
                        continue 

                    envGroup = ''
                    envName = env.split('/')[-1].split('.')[0]
                    regexMatch = search('^Envs/(.+)', envGroupToView)
                    if regexMatch:
                        envGroup = regexMatch.group(1)

                    envMgmtObj.setenv = f'{envGroup}/{envName}'
                    activeUsers = envMgmtObj.getActiveUsers()
                    if activeUsers:
                        # Get test result path and check for path exists

                        # [{'sessionId': '05-17-2023-15:49:07:297406_5432', 'overallSummaryFile': '/opt/KeystackTests/Results/GROUP=Default/PLAYBOOK=Samples-pythonSample/05-17-2023-15:49:07:297406_5432/overallSummary.json', 'user': 'hgee', 'stage': 'Test', 'module': 'CustomPythonScripts2'}]
                        for activeUser in activeUsers:
                            overallSummaryFile = activeUser['overallSummaryFile']
                            if overallSummaryFile:
                                testResultPath = overallSummaryFile.split('/overallSummary.json')[0]
                                if os.path.exists(testResultPath) == False:
                                    # Release the env from activeUsers
                                    session = {'sessionId':activeUser['sessionId'], 'stage':activeUser['stage'],
                                            'module':activeUser['module'], 'user':activeUser['user']} 
                                    envMgmtObj.removeFromActiveUsersList([session])
                                    SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='AutoRemoveActiveUser', 
                                                            msgType='Info', msg=f'The env {envGroup}/{envName} has active user, but the pipeline and test results are deleted. Releasing active user on this env.',
                                                            forDetailLogs='')
                tableData = getTableData(envGroupToView, user)
                        
            except Exception as errMsg:
                errorMsg = str(errMsg)
                status = 'failed'
                statuCode = HtmlStatusCodes.error
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='GetEnvTableData', 
                                        msgType='Error', msg=errorMsg,
                                        forDetailLogs=traceback.format_exc(None, errMsg))
            
        return Response(data={'tableData': tableData, 'status': status, 'errorMsg': errorMsg}, status=statusCode)
    

class CreateEnv(APIView):
    @verifyUserRole(webPage=Vars.webpage, action='Create', exclude=['engineer'])
    def post(self, request):
        """
        Create a new Env file
        """
        user = AccountMgr().getRequestSessionUser(request)
        remoteController = request.data.get('remoteController', None)
        mainControllerIp, remoteControllerIp, ipPort = getMainAndRemoteControllerIp(request, remoteController)
        envPath = GlobalVars.envPath
        statusCode = HtmlStatusCodes.success
        status = 'success'
        errorMsg = None

        if request.GET:
            # Rest APIs with inline params come in here
            try:
                envNamespace = request.GET.get('newEnv')
                envGroup     = request.GET.get('envGroup') 
                textArea     = request.GET.get('textArea')                 
            except Exception as errMsg:
                errorMsg = str(errMsg)
                status = 'failed'
                statusCode = HtmlStatusCodes.error
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='createEnv', msgType='Error',
                                          msg=errorMsg, forDetailLogs=traceback.format_exc(None, errMsg))
                return Response(data={'status': status, 'errorMsg': errorMsg}, status=statusCode)
        
        # JSON format
        if request.data:
            # <QueryDict: {'env': 'loadcoreSample', 'sessionId': '02-04-2023-08:53:15:021768_7277', 'overallSummaryFile': '/opt/KeystackTests/Results/GROUP=Default/PLAYBOOK=pythonSample/02-04-2023-08:53:15:021768_7277/overallSummary.json', 'user': 'hgee', 'stage': 'Teardown', 'module': 'CustomPythonScripts', 'utilization': False, 'webhook': True}
            try:
                envNamespace = request.data['newEnv']
                envGroup     = request.data['envGroup']
                textArea     = request.data['textArea']
            except Exception as errMsg:
                errorMsg = str(errMsg)
                status = 'failed'
                statusCode = HtmlStatusCodes.error
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='createEnv', msgType='Error',
                                        msg=errorMsg, forDetailLogs=traceback.format_exc(None, errMsg))
                return Response(data={'status': status, 'errorMsg': errorMsg}, status=statusCode)

        if remoteControllerIp and remoteControllerIp != mainControllerIp:
            params = {"newEnv":envNamespace, "envGroup":envGroup, "textArea":textArea}
            restApi = '/api/v1/env/create'
            response, errorMsg = executeRestApiOnRemoteController('post', remoteControllerIp, ipPort, restApi, params, 
                                                                  user, webPage=Vars.webpage, action='Create')
            if errorMsg:
                status = 'failed'
                statusCode = HtmlStatusCodes.error    
        else:            
            if '-' in envNamespace:
                env = envNamespace.replace('-', '/')
            else:
                env = envNamespace
            
            try:
                if '.yml' not in env:
                    env = f'{env}.yml'
                
                if envGroup:
                    if envGroup[0] == '/':
                        envGroup = f'/{envGroup[1:]}'

                    envFullPath = f'{envPath}/{envGroup}'
                    mkdir2(envFullPath)
                    fullPathFile = f'{envFullPath}/{env}' 
                    chownChmodFolder(envFullPath, GlobalVars.user, GlobalVars.userGroup, stdout=False)
                    chownChmodFolder(fullPathFile, GlobalVars.user, GlobalVars.userGroup, stdout=False)
                            
                else:
                    envGroup = None
                    playbookGroup = None
                    fullPathFile = f'{envPath}/{env}'

                if os.path.exists(fullPathFile):
                    status = 'failed'
                    statusCode = HtmlStatusCodes.error
                    errorMsg = f'Env already exists: Group:{envGroup} Env:{env}'
                    
                    SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='CreateEnv', 
                                            msgType='Failed', msg=errorMsg, forDetailLogs='')
                    return Response({'status': status, 'errorMsg': errorMsg}, status=statusCode)
                
                writeToFile(fullPathFile, textArea, mode='w')
                            
                try:
                    # Verify for yaml syntax error
                    readYaml(fullPathFile)
                    SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='CreateEnv', 
                                            msgType='Info',
                                            msg=f'Env:{env} Group:{envGroup}', forDetailLogs='') 
                                
                except Exception as errMsg:
                    errorMsg = "Error: Yml syntax error."
                    status = "failed"
                    statusCode = HtmlStatusCodes.error
                    SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='CreateEnv', 
                                            msgType='Error',
                                            msg=errorMsg, forDetailLogs='') 

            except Exception as errMsg:
                statusCode = HtmlStatusCodes.error
                status = "failed"
                errorMsg = str(errMsg)
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='CreateEnv', msgType='Error',
                                        msg=errMsg, forDetailLogs=traceback.format_exc(None, errMsg)) 

        return Response(data={'status': status, 'errorMsg': errorMsg}, status=statusCode)

     
class DeleteEnvs(APIView):
    envs = openapi.Parameter(name='envs', description="A list of envs to delete",
                                          required=False, in_=openapi.IN_QUERY, type=openapi.TYPE_STRING)           
    @swagger_auto_schema(tags=['/api/v1/env/delete'], operation_description="Delete Envs",
                         manual_parameters=[envs])
    @verifyUserRole(webPage=Vars.webpage, action='DeleteEnv', exclude=['engineer'])
    def post(self, request):
        user = AccountMgr().getRequestSessionUser(request)
        remoteController = request.data.get('remoteController', None)
        mainControllerIp, remoteControllerIp, ipPort = getMainAndRemoteControllerIp(request, remoteController)
        error = None
        statusCode= HtmlStatusCodes.success
        status = 'success'

        if request.GET:
            # Rest APIs with inline params come in here
            try:
                deleteEnvs = request.GET.get('envs')                
            except Exception as errMsg:
                errorMsg = str(errMsg)
                status = 'failed'
                statusCode = HtmlStatusCodes.error
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='deleteEnv', msgType='Error',
                                          msg=errorMsg, forDetailLogs=traceback.format_exc(None, errMsg))
                return Response(data={'status': status, 'errorMsg': errorMsg}, status=statusCode)
        
        # JSON format
        if request.data:
            # <QueryDict: {'env': 'loadcoreSample', 'sessionId': '02-04-2023-08:53:15:021768_7277', 'overallSummaryFile': '/opt/KeystackTests/Results/GROUP=Default/PLAYBOOK=pythonSample/02-04-2023-08:53:15:021768_7277/overallSummary.json', 'user': 'hgee', 'stage': 'Teardown', 'module': 'CustomPythonScripts', 'utilization': False, 'webhook': True}
            try:
                deleteEnvs = request.data['envs']
            except Exception as errMsg:
                errorMsg = str(errMsg)
                status = 'failed'
                statusCode = HtmlStatusCodes.error
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='deleteEnv', msgType='Error',
                                        msg=errorMsg, forDetailLogs=traceback.format_exc(None, errMsg))
                return Response(data={'status': status, 'errorMsg': errorMsg}, status=statusCode)

        if remoteControllerIp and remoteControllerIp != mainControllerIp:
            params = {"envs": deleteEnvs}
            restApi = '/api/v1/env/delete'
            response, errorMsg = executeRestApiOnRemoteController('post', remoteControllerIp, ipPort, restApi, params, 
                                                                  user, webPage=Vars.webpage, action='DeleteEnvs')
            if errorMsg:
                status = 'failed'
                statusCode = HtmlStatusCodes.error    
        else:              
            try:  
                # deleteEnvs: ['/opt/KeystackTests/Envs/rack1.yml', '/opt/KeystackTests/Envs/rack3.yml']          
                for env in deleteEnvs:
                    # /opt/KeystackTests/Envs/hubert.yml
                    envName = env.split(f'{GlobalVars.envPath}/')[-1].split('.')[0]
                    os.remove(env)
                    
                    # Get the env load balance group name
                    envData = DB.name.getOneDocument(collectionName=Vars.envMgmtDB, fields={'env':envName})
                    
                    # Remove the env from the load balancer
                    if envData['loadBalanceGroups']:
                        DB.name.updateDocument(collectionName=Vars.envLoadBalanceDB, queryFields={'name':envData['loadBalanceGroups']}, 
                                            updateFields={'envs': envName}, removeFromList=True)
                        
                    DB.name.deleteOneDocument(collectionName=Vars.envMgmtDB, fields={'env': envName})
                    
                    SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='deleteEnv', 
                                            msgType='Info', msg=f'Deleted Env: {env}')
                    
            except Exception as errMsg:
                error = f'Error: {errMsg}'
                status = 'failed'
                statuCode = HtmlStatusCodes.error
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='deleteEnv', 
                                        msgType='Error', msg=error,
                                        forDetailLogs=traceback.format_exc(None, errMsg))
            
        return Response(data={'status': status, 'errorMsg': error}, status=statusCode)
 

class ViewEditEnv(APIView):
    @verifyUserRole(webPage=Vars.webpage, action='view/edit', exclude=["engineer"])
    def post(self, request):
        """
        Show the env yml file contents and allow editing
        """
        user = AccountMgr().getRequestSessionUser(request)
        remoteController = request.data.get('remoteController', None)
        mainControllerIp, remoteControllerIp, ipPort = getMainAndRemoteControllerIp(request, remoteController)
        envFile = request.data.get('envFile', None)
        envContents = dict()        
        statusCode = HtmlStatusCodes.success
        status = 'success'
        errorMsg = None

        if remoteControllerIp and remoteControllerIp != mainControllerIp:
            params = {"envFile": envFile}
            restApi = '/api/v1/env/viewEditEnv'
            response, errorMsg = executeRestApiOnRemoteController('post', remoteControllerIp, ipPort, restApi, params, 
                                                                  user, webPage=Vars.webpage, action='ViewEditEnv')
            if errorMsg:
                status = 'failed'
                statusCode = HtmlStatusCodes.error 
            else:
                envContents = response.json()['envContents']  
             
        else:
            if os.path.exists(envFile) == False:
                errorMsg = f'Env yml file not found: {envFile}'
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='ViewEditEnv', msgType='Error',
                                          msg=errorMsg, forDetailLogs='')  
                statusCode = HtmlStatusCodes.error
                status = 'failed'
            else:    
                envContents = readYaml(envFile)
            
        return Response(data={'envContents': envContents, 'status': status, 'errorMsg': errorMsg}, status=statusCode)
    
           
class GetEnvs(APIView):
    @swagger_auto_schema(tags=['/api/v1/env/list'], operation_description="Get a list of Envs",
                         manual_parameters=[])
    @verifyUserRole()
    def get(self, request):
        """
        Description: 
            Return a list of all the Environments in full path files
        
        No parameters required

        GET /api/v1/envs/list
        
        Example:
            curl -H "API-Key: iNP29xnXdlnsfOyausD_EQ" -X GET http://192.168.28.7:8000/api/v1/env/list
            
        Return:
            A list of environments
        """
        statusCode = HtmlStatusCodes.success
        status = 'success'
        envs = []
        error = None
        user = AccountMgr().getRequestSessionUser(request)
        remoteController = request.data.get('remoteController', None)
        mainControllerIp, remoteControllerIp, ipPort = getMainAndRemoteControllerIp(request, remoteController)

        if remoteControllerIp and remoteControllerIp != mainControllerIp:
            params = {}
            restApi = '/api/v1/env/list'
            # stream=False, showApiOnly=False, silentMode=False, 
            response, errorMsg = executeRestApiOnRemoteController('get', remoteControllerIp, ipPort, restApi, params, 
                                                                  user, webPage=Vars.webpage, action='GetEnvs', stream=False) 
            if errorMsg:
                status = 'failed'
                statusCode = HtmlStatusCodes.error 
            else:    
                envs = response.json()['envs']
              
        else:        
            try:
                envPath = GlobalVars.envPath
                for root,dirs,files in os.walk(envPath):
                    # /opt/KeystackTests/Envs/LoadCore
                    envGroup = root.split(envPath)[1]

                    if files:
                        for eachFile in files:
                            if eachFile.endswith('.yml'):
                                envs.append(f'{root}/{eachFile}')
                                    
            except Exception as errMsg:
                errorMsg = str(errMsg)
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='getEnvs', msgType='Error',
                                          msg=errorMsg, forDetailLogs=traceback.format_exc(None, errMsg))
                return Response(data={'status': 'failed', 'errorMsg': errorMsg}, status=HtmlStatusCodes.error)
        
        return Response(data={'envs': envs, 'status': status, 'errorMsg': errorMsg}, status=statusCode)


class EnvGroups(APIView):
    """
    Internal usage only: Get Env groups for sidebar Env dropdown menu
    
    /api/v1/env/groups
    """
    @verifyUserRole()
    def post(self, request):
        """
        Get Env groups for sidebar Env menu
        """
        user = AccountMgr().getRequestSessionUser(request)
        remoteController = request.data.get('remoteController', None)
        mainControllerIp, remoteControllerIp, ipPort = getMainAndRemoteControllerIp(request, remoteController)
        status = 'success'
        statusCode = HtmlStatusCodes.success
        errorMsg = None
        htmlEnvGroups = ''
        
        if remoteControllerIp and remoteControllerIp != mainControllerIp:
            params = {}
            restApi = '/api/v1/env/envGroups'
            response, errorMsg = executeRestApiOnRemoteController('post', remoteControllerIp, ipPort, restApi, params, 
                                                                  user, webPage=Vars.webpage, action='EnvGroups')
            if errorMsg:
                status = 'failed'
                statusCode = HtmlStatusCodes.error 
            else:
                htmlEnvGroups = response.json()['envGroups']
                       
        else:          
            try:
                # Env groups
                envPath = f'{GlobalVars.keystackTestRootPath}/Envs'
                envGroups = []
                for root,dirs,files in os.walk(envPath):
                    envGroup = root.split(GlobalVars.keystackTestRootPath)[1]
                    envGroups.append(envGroup[1:])

                htmlEnvGroups += '<a href="/setups/envLoadBalancer" class="collapse-item pl-0 pt-3 pb-3 textBlack fontSize12px">Load Balance Group Mgmt</a>'

                htmlEnvGroups += '<p class="pl-2 pt-2 textBlack fontSize12px">Select Env Group:</p><br>'
                for group in envGroups:
                    htmlEnvGroups += f'<a class="collapse-item pl-3 fontSize12px" href="/setups?group={group}"><i class="fa-regular fa-folder pr-3"></i>{group}</a>'
                    
            except Exception as errMsg:
                errorMsg = str(errMsg)
                status = 'failed'
                statusCode = HtmlStatusCodes.error
                
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='GetEnvGroups', msgType='Error',
                                          msg=errorMsg, forDetailLogs=traceback.format_exc(None, errMsg))            
        
        return Response(data={'envGroups':htmlEnvGroups, 'status':status, 'error':errorMsg}, status=statusCode)   
    
    
class GetEnvGroups(APIView):
    @swagger_auto_schema(tags=['/api/v1/env/groups'], operation_description="Get a list of Env Groups",
                         manual_parameters=[])
    @verifyUserRole()
    def get(self, request):
        """
        Description: 
            Return a list of all the env groups
        
        No parameters required

        GET /api/v1/env/groups
        
        Example:
            curl -H "API-Key: iNP29xnXdlnsfOyausD_EQ" -X GET http://192.168.28.7:8000/api/v1/env/groups
            
        Return:
            A list of environments
        """
        statusCode = HtmlStatusCodes.success
        status = 'success'
        envGroups = []
        errorMsg = None
        user = AccountMgr().getRequestSessionUser(request)
        remoteController = request.data.get('remoteController', None)
        mainControllerIp, remoteControllerIp, ipPort = getMainAndRemoteControllerIp(request, remoteController)

        if remoteControllerIp and remoteControllerIp != mainControllerIp:
            params = {}
            restApi = '/api/v1/env/groups'
            response, errorMsg = executeRestApiOnRemoteController('get', remoteControllerIp, ipPort, restApi, params, 
                                                                  user, webPage=Vars.webpage, action='GetEnvGroups')
            if errorMsg:
                status = 'failed'
                statusCode = HtmlStatusCodes.error 
            else:
                envGroups = response.json()['envGroups']
                       
        else:
            try:
                envPath = GlobalVars.envPath
                for root,dirs,files in os.walk(envPath):
                    # /opt/KeystackTests/Envs/LoadCore
                    regexMatch = search(f'.+(/Envs.+)$', root)
                    if regexMatch:
                        # /opt/KeystackTests/Envs
                        # /opt/KeystackTests/Envs/qa
                        envGroups.append(regexMatch.group(1))
        
            except Exception as errMsg:
                errorMsg = str(errMsg)
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='getGroupEnvs', msgType='Error',
                                        msg=errorMsg, forDetailLogs='')
                return Response(data={'status': 'failed', 'errorMsg': errorMsg}, status=HtmlStatusCodes.error)
        
        return Response(data={'envGroups': envGroups, 'status': status, 'errorMsg': errorMsg}, status=statusCode)
    

class EnvGroupsTableForDelete(APIView):
    """
    Internal usage only: Get Env groups for delete env group table selection
    """
    @verifyUserRole()
    def post(self, request):
        """
        Create a table for selecting Env groups to delete
        """
        user = AccountMgr().getRequestSessionUser(request)
        remoteController = request.data.get('remoteController', None)
        mainControllerIp, remoteControllerIp, ipPort = getMainAndRemoteControllerIp(request, remoteController)
        status = 'success'
        statusCode = HtmlStatusCodes.success
        errorMsg = None
        html = ''

        if remoteControllerIp and remoteControllerIp != mainControllerIp:
            params = {}
            restApi = '/api/v1/env/envGroupsTableForDelete'
            response, errorMsg = executeRestApiOnRemoteController('post', remoteControllerIp, ipPort, restApi, params, 
                                                                  user, webPage=Vars.webpage, action='EnvGroupsTableForDelete')
            if errorMsg:
                status = 'failed'
                statusCode = HtmlStatusCodes.error
            else:
                html = response.json()['envGroupsHtml'] 
                   
        else:  
            try:
                # Env groups
                execRestApiObj = ExecRestApi(ip=Vars.keystackUIIpAddress, port=Vars.keystackIpPort, https=False)
                response = execRestApiObj.get(restApi='/api/v1/env/groups', params={'webhook':True}, silentMode=False)
                
                if response.status_code == 200:
                    html +=   '<center><table class="tableFixHead2 table-bordered" style="width:90%">'    
                    html +=        '<thead>'
                    html +=            '<tr>'
                    html +=                 '<th><input type="checkbox" name="deleteAllEnvGroups" onclick="disableEnvGroupCheckboxes(this)" \></th>'
                    html +=                 '<th>EnvGroup</th>'
                    html +=            '</tr>'
                    html +=         '</thead>'
                    html +=         '<tbody>'
                    
                    for envGroup in response.json()['envGroups']:
                        envGroupName = envGroup.split('/Envs/')[-1]
                        html += '<tr>'
                        html += f'<td><input type="checkbox" name="deleteEnvGroups" value="{GlobalVars.keystackTestRootPath}/{envGroup}"></td>'
                        html += f'<td class="textAlignLeft">{envGroupName}</td>'
                        html += '</tr>'
                        
                    html +=  '</tbody>'    
                    html +=  '</table></center>'
                else:
                    raise Exception(response.json()['errorMsg'])
                
            except Exception as errMsg:
                errorMsg = str(errMsg)
                status = 'failed'
                statusCode = HtmlStatusCodes.error
                
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='EnvGroupsTableForDelete', msgType='Error',
                                          msg=errorMsg, forDetailLogs=traceback.format_exc(None, errMsg))            
            
        return Response(data={'envGroupsHtml':html, 'status':status, 'error':errorMsg}, status=statusCode)   
    

class GetWaitList(APIView):
    @verifyUserRole()
    def post(self, request):
        """ 
        "waitList": [{"module": "LoadCore",
                      "sessionId": "11-01-2022-04:21:00:339301_rocky_200Loops",
                      "user": "rocky"
                     },
                     {"module": "LoadCore",
                      "sessionId": "11-01-2022-04:23:05:749724_rocky_1test",
                      "user": "rocky"}]
        """
        user = AccountMgr().getRequestSessionUser(request)
        envNamespace = request.data.get('env', None)
        remoteController = request.data.get('remoteController', None)
        mainControllerIp, remoteControllerIp, ipPort = getMainAndRemoteControllerIp(request, remoteController)
        status = 'success'
        statusCode = HtmlStatusCodes.success
        errorMsg = None
        html = ''
        
        if remoteControllerIp and remoteControllerIp != mainControllerIp:
            params = {"env": envNamespace}
            restApi = '/api/v1/env/envWaitList'
            response, errorMsg = executeRestApiOnRemoteController('post', remoteControllerIp, ipPort, restApi, params, 
                                                                  user, webPage=Vars.webpage, action='GetWaitList')
            if errorMsg:
                status = 'failed'
                statusCode = HtmlStatusCodes.error
            else:
                html = response.json()['tableData'] 
                   
        else:
            if '-' in envNamespace:
                env = envNamespace.replace('-', '/')
            else:
                env = envNamespace

            try:
                envMgmtObj = ManageEnv(env)

                # waitList: [{'module': 'LoadCore', 'sessionId': '11-01-2022-04:21:00:339301_rocky_200Loops', 'user': 'rocky'}, {'module': 'LoadCore', 'sessionId': '11-01-2022-04:23:05:749724_rocky_1test', 'user': 'rocky'}]
                waitList = envMgmtObj.getWaitList()

                html = '<table id="envWaitListTable" class="mt-2 table table-sm table-bordered table-fixed tableFixHead tableMessages">' 
                html += '<thead>'
                html += '<tr>'
                html += '<th scope="col">Remove</th>'
                html += '<th scope="col" style="text-align:left">User</th>'
                html += '<th scope="col" style="text-align:left">SessionId</th>'
                html += '<th scope="col" style="text-align:left">Stage</th>'
                html += '<th scope="col" style="text-align:left">Task / Module</th>'
                html += '</tr>'
                html += '</thead>'
                html += '<tbody>'
                
                for eachWait in waitList:
                    user =      eachWait['user']
                    sessionId = eachWait['sessionId']
                    stage =     eachWait['stage']
                    module =    eachWait['module']
                
                    html += '<tr>'
                    html += f'<td><input type="checkbox" name="envWaitListCheckboxes" env="{env}" user="{user}" sessionId="{sessionId}" stage="{stage}" module="{module}"/></td>'
                    html += f'<td style="text-align:left">{user}</td>'
                    html += f'<td style="text-align:left">{sessionId}</td>'
                    html += f'<td style="text-align:left">{stage}</td>'
                    html += f'<td style="text-align:left">{module}</td>'
                    html += f'</tr>'
                    
                html += '</tbody>'       
                html += '</table>'
                
            except Exception as errMsg:
                status = 'failed'
                errorMsg = errMsg
                statusCode = HtmlStatusCodes.error
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='GetEnvWaitList',
                                        msgType='Error', msg=errorMsg,
                                        forDetailLogs=f'GetEnvWaitList: {traceback.format_exc(None, errMsg)}') 
            
        return Response(data={'tableData': html, 'status': status, 'errorMsg': errorMsg}, status=statusCode)
            
                    
class IsEnvAvailableRest(APIView):
    env = openapi.Parameter(name='env', description="The name of the envGroup/env",
                            required=True, in_=openapi.IN_QUERY, type=openapi.TYPE_STRING)        
    @swagger_auto_schema(tags=['/api/v1/env/isEnvAvailable'], operation_description="Verify if the env is available",
                         manual_parameters=[env])
    @verifyUserRole()
    def post(self, request):
        """
        Description: 
            Verify if the env is available

        POST /api/v1/envs/isEnvAvailable
        
        Example:
            curl -H "API-Key: iNP29xnXdlnsfOyausD_EQ" -X GET http://192.168.28.7:8000/api/v1/env/isEnvAvailable
            
        Return:
            A list of environments
        """
        statusCode = HtmlStatusCodes.success
        status = 'success'
        errorMsg = None
        user = AccountMgr().getRequestSessionUser(request)
        remoteController = request.data.get('remoteController', None)
        mainControllerIp, remoteControllerIp, ipPort = getMainAndRemoteControllerIp(request, remoteController)
        isAvailable = False
        
        # http://ip:port/api/v1/env/activeUsers&env=env
        if request.GET:
            # Rest APIs with inline params come in here
            try:
                env = request.GET.get('env')
            except Exception as errMsg:
                errorMsg = str(errMsg)
                status = 'failed'
                statusCode = HtmlStatusCodes.error
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='IsEnvAvailableRest', msgType='Error',
                                          msg=errorMsg, forDetailLogs=traceback.format_exc(None, errMsg))
                return Response(data={'status': status, 'errorMsg': errorMsg}, status=statusCode)
            
        # JSON format
        if request.data:
            # <QueryDict: {'env': 'loadcoreSample', 'sessionId': '02-04-2023-08:53:15:021768_7277', 'overallSummaryFile': '/opt/KeystackTests/Results/GROUP=Default/PLAYBOOK=pythonSample/02-04-2023-08:53:15:021768_7277/overallSummary.json', 'user': 'hgee', 'stage': 'Teardown', 'module': 'CustomPythonScripts', 'utilization': False, 'webhook': True}
            try:
                env = request.data['env']
            except Exception as errMsg:
                errorMsg = str(errMsg)
                status = 'failed'
                statusCode = HtmlStatusCodes.error
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='IsEnvAvailableRest', msgType='Error',
                                          msg=errorMsg, forDetailLogs=traceback.format_exc(None, errMsg))
                return Response(data={'status': status, 'errorMsg': errorMsg}, status=statusCode)

        if remoteControllerIp and remoteControllerIp != mainControllerIp:
            params = {"env": env}
            restApi = '/api/v1/env/isEnvAvailable'
            response, errorMsg = executeRestApiOnRemoteController('post', remoteControllerIp, ipPort, restApi, params, 
                                                                  user, webPage=Vars.webpage, action='IsEnvAvailableRest')
            if errorMsg:
                status = 'failed'
                statusCode = HtmlStatusCodes.error 
            else:
                isAvailable = response.json()['isAvailable']       
        else:                    
            try:    
                # env: Samples/pythonSample 
                envObj = EnvMgmt.ManageEnv(env=env)                     
                isAvailable = envObj.isEnvAvailable()
                del envObj

            except Exception as errMsg:
                errorMsg = str(errMsg)
                status = 'failed'
                statusCode = HtmlStatusCodes.error
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='IsEnvAvailableRest', msgType='Error',
                                          msg=errorMsg, forDetailLogs=traceback.format_exc(None, errMsg))

        return Response(data={'isAvailable': isAvailable, 'status': status, 'errorMsg': errorMsg}, status=statusCode)
    
     
class GetActiveUsers(APIView):
    # @swagger_auto_schema(tags=['/api/v1/env/activelist'], operation_description="Get a list of actively reserved Envs",
    #                      manual_parameters=[])
    @verifyUserRole()
    def get(self, request):
        """
        Description: 
            Return a list of actively reserved Envs
        
        No parameters required

        GET /api/v1/envs/activeUsers
        
        Example:
            curl -H "API-Key: iNP29xnXdlnsfOyausD_EQ" -X GET http://192.168.28.7:8000/api/v1/env/activeUsers
            
        Return:
            A list of environments
        """
        statusCode = HtmlStatusCodes.success
        status = 'success'
        error = None
        user = AccountMgr().getRequestSessionUser(request)
        remoteController = request.data.get('remoteController', None)
        mainControllerIp, remoteControllerIp, ipPort = getMainAndRemoteControllerIp(request, remoteController)
        activeUsers = []
        
        # http://ip:port/api/v1/env/activeUsers&env=env
        if request.GET:
            # Rest APIs with inline params come in here
            try:
                env = request.GET.get('env')
            except Exception as errMsg:
                errorMsg = str(errMsg)
                status = 'failed'
                statusCode = HtmlStatusCodes.error
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='GetActiveUsers', msgType='Error',
                                          msg=errorMsg, forDetailLogs=traceback.format_exc(None, errMsg))
                return Response(data={'status': status, 'errorMsg': errorMsg}, status=statusCode)
             
        # JSON format
        if request.data:
            # <QueryDict: {'env': 'loadcoreSample', 'sessionId': '02-04-2023-08:53:15:021768_7277', 'overallSummaryFile': '/opt/KeystackTests/Results/GROUP=Default/PLAYBOOK=pythonSample/02-04-2023-08:53:15:021768_7277/overallSummary.json', 'user': 'hgee', 'stage': 'Teardown', 'module': 'CustomPythonScripts', 'utilization': False, 'webhook': True}
            try:
                env = request.data['env']
            except Exception as errMsg:
                errorMsg = f'getActiveUsers: Unexpected param: {request.data}'
                status = 'failed'
                statusCode = HtmlStatusCodes.error
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='GetActiveUsers', msgType='Error',
                                          msg=errorMsg, forDetailLogs=traceback.format_exc(None, errMsg))
                return Response(data={'status': status, 'errorMsg': errorMsg}, status=statusCode)

        if remoteControllerIp and remoteControllerIp != mainControllerIp:
            params = {"env": env}
            restApi = '/api/v1/env/activeUsers'
            response, errorMsg = executeRestApiOnRemoteController('get', remoteControllerIp, ipPort, restApi, params, 
                                                                  user, webPage=Vars.webpage, action='GetActiveUsers')
            if errorMsg:
                status = 'failed'
                statusCode = HtmlStatusCodes.error
            else:
                activeUsers = response.json()['activeUsers'] 
                   
        else:                                    
            try:    
                # env: Samples/pythonSample 
                envObj = EnvMgmt.ManageEnv(env=env)                     
                activeUsers = envObj.getActiveUsers()
                del envObj

            except Exception as errMsg:
                errorMsg = str(errMsg)
                status = 'failed'
                statusCode = HtmlStatusCodes.error
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='GetActiveUsers', msgType='Error',
                                          msg=errorMsg, forDetailLogs=traceback.format_exc(None, errMsg))
        
        return Response(data={'activeUsers': activeUsers, 'status': status, 'errorMsg': errorMsg}, status=statusCode)

    
class ReserveEnvUI(APIView):
    swagger_schema = None
    
    @verifyUserRole()
    def post(self, request):
        """
        Description: 
            Reserve an Env.
            Called by keystack.py to automatically reserve an env.

        POST /api/v1/env/reserve
        
        Parameters:
            sessionId: The keystack session ID
            overallSummaryFile: keystack.py overll summary detail json data
                        /opt/KeystackTests/Results/GROUP=Default/PLAYBOOK=pythonSample/02-04-2023-08:53:15:021768_7277/overallSummary.json
            env: The env to reserve. Example: pythonSample
            user: user from keystack
            stage: stage
            module: module
            utilization: <bool>: For keystack.py.lockAndWaitForEnv().  This function calls reserveEnv() and amIRunning().
                         Both functions increment env utilization. We want to avoid hitting it twice.
                         So exclude hitting it here in reserveEnv and let amIRunning hit it.
        
        Usage:
            envObj = EnvMgmt.ManageEnv(env=self.moduleProperties['env'])                          
            envMgmtObj.reserveEnv(sessionId=sessionId, overallSummaryFile=overallSummaryFile, 
                                  user=user, stage=stage, module=module, utilization=False)
                                  
        Example:
            curl -X POST http://192.168.28.7:8000/api/v1/env/reserve
            
        Return:
            status and error
        """
        user = AccountMgr().getRequestSessionUser(request)
        remoteController = request.data.get('remoteController', None)
        mainControllerIp, remoteControllerIp, ipPort = getMainAndRemoteControllerIp(request, remoteController)
        statusCode = HtmlStatusCodes.success
        status = 'success'
        errorMsg = None
        
        if request.GET:
            # Rest APIs with inline params come in here
            try:
                sessionId = request.GET.get('sessionId')
                overallSummaryFile = request.GET.get('overallSummaryFile')
                env = request.GET.get('env')
                userReserving = request.GET.get('user')
                stage = request.GET.get('stage')
                module = request.GET.get('module')
                utilization = request.GET.get('utilization')
                
            except Exception as errMsg:
                errorMsg = str(errMsg)
                status = 'failed'
                statusCode = HtmlStatusCodes.error
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='reserveEnvUI', msgType='Error',
                                          msg=errorMsg, forDetailLogs=traceback.format_exc(None, errMsg))
                return Response(data={'status': status, 'errorMsg': errorMsg}, status=statusCode)
            
        # JSON format
        if request.data:
            # <QueryDict: {'env': 'loadcoreSample', 'sessionId': '02-04-2023-08:53:15:021768_7277', 'overallSummaryFile': '/opt/KeystackTests/Results/GROUP=Default/PLAYBOOK=pythonSample/02-04-2023-08:53:15:021768_7277/overallSummary.json', 'user': 'hgee', 'stage': 'Teardown', 'module': 'CustomPythonScripts', 'utilization': False, 'webhook': True}
            try:
                sessionId = request.data['sessionId']
                overallSummaryFile = request.data['overallSummaryFile']
                env = request.data['env']
                userReserving = request.data['user']
                stage = request.data['stage']
                module = request.data['module']
                utilization = request.data['utilization']
                
            except Exception as errMsg:
                errorMsg = str(errMsg)
                status = 'failed'
                statusCode = HtmlStatusCodes.error
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='reserveEnvUI', msgType='Error',
                                          msg=errorMsg, forDetailLogs=traceback.format_exc(None, errMsg))
                return Response(data={'status': status, 'errorMsg': errorMsg}, status=statusCode)

        if remoteControllerIp and remoteControllerIp != mainControllerIp:
            params = {"sessionId": sessionId, "overallSummaryFile": overallSummaryFile, "env": env, "user": userReserving,
                      "stage": stage, "module": module, "utilization": utilization}
            restApi = '/api/v1/env/reserve'
            response, errorMsg = executeRestApiOnRemoteController('post', remoteControllerIp, ipPort, restApi, params, 
                                                                  user, webPage=Vars.webpage, action='ReserveEnvUI')
            if errorMsg:
                status = 'failed'
                statusCode = HtmlStatusCodes.error 
                   
        else:            
            try:                       
                # env: Samples/pythonSample 
                envObj = EnvMgmt.ManageEnv(env=env)                     
                result = envObj.reserveEnv(sessionId=sessionId, overallSummaryFile=overallSummaryFile, 
                                           user=user, stage=stage, module=module, utilization=utilization)
                if result[0] != 'success':
                    SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='ReserveEnv', msgType='Failed',
                                              msg=result[1], forDetailLogs='')
                del envObj

                if result[0] == 'failed':
                    status = 'failed'
                    error = result[1]
                    statusCode = HtmlStatusCodes.error
                    SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='reserveEnvUI', msgType='Failed',
                                              msg=f'sessionId:{sessionId} Env:{env}  user:{user} stage:{stage} module:{module}<br>error:{error}',
                                              forDetailLogs='')
                else:    
                    SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='reserveEnvUI', msgType='Info',
                                              msg=f'sessionId:{sessionId}, stage:{stage}, module:{module}, env:{env}', forDetailLogs='')
                
            except Exception as errMsg:
                errorMsg = str(errMsg)
                status = 'failed'
                statusCode = HtmlStatusCodes.error
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='reserveEnvUI', msgType='Error',
                                          msg=f'sessionId:{sessionId}, stage:{stage}, module:{module}, env:{env}<br>error: {errorMsg}', 
                                          forDetailLogs=traceback.format_exc(None, errMsg))
                               
        return Response(data={'status': status, 'errorMsg': errorMsg}, status=statusCode)


class DeleteEnvGroups(APIView):
    selectAll         = openapi.Parameter(name='selectAll', description="Delete all env groups",
                                          required=False, in_=openapi.IN_QUERY, type=openapi.TYPE_BOOLEAN)
    selectedEnvGroups = openapi.Parameter(name='selectedEnvGroups', description="A list of env groups to delete in full paths",
                                          required=False, in_=openapi.IN_QUERY, type=openapi.TYPE_STRING)           
    @swagger_auto_schema(tags=['/api/v1/env/deleteEnvGroups'], operation_description="Verify if the env is available",
                         manual_parameters=[selectAll, selectedEnvGroups])
    @verifyUserRole(webPage=Vars.webpage, action='DeleteEnvGroups', exclude='engineer')
    def post(self, request):
        """
        Description: 
            Delete Env Groups

        POST /api/v1/env/deleteEnvGroups
        
        Parameters:
            selectAll: True|False.  Delete all env groups.
            selectedEnvGroups: A list of env groups in full paths.
                                  
        Example:
            curl -X POST http://192.168.28.7:8000/api/v1/env/deleteEnvGroups
            
        Return:
            status and error
        """
        remoteController = request.data.get('remoteController', None)
        mainControllerIp, remoteControllerIp, ipPort = getMainAndRemoteControllerIp(request, remoteController)
        user = AccountMgr().getRequestSessionUser(request)
        statusCode = HtmlStatusCodes.success
        status = 'success'
        errorMsg = None
        
        if request.GET:
            # Rest APIs with inline params come in here
            try:
                selectAll = request.GET.get('selectAll')
                selectedEnvGroups = request.GET.get('selectedEnvGroups')
                
            except Exception as errMsg:
                errorMsg = str(errMsg)
                status = 'failed'
                statusCode = HtmlStatusCodes.error
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='deleteEnvGroups', msgType='Error',
                                          msg=errorMsg, forDetailLogs=traceback.format_exc(None, errMsg))
                return Response(data={'status': status, 'errorMsg': errorMsg}, status=statusCode)
            
        # JSON format
        if request.data:
            # <QueryDict: {'env': 'loadcoreSample', 'sessionId': '02-04-2023-08:53:15:021768_7277', 'overallSummaryFile': '/opt/KeystackTests/Results/GROUP=Default/PLAYBOOK=pythonSample/02-04-2023-08:53:15:021768_7277/overallSummary.json', 'user': 'hgee', 'stage': 'Teardown', 'module': 'CustomPythonScripts', 'utilization': False, 'webhook': True}
            try:
                selectAll = request.data['selectAll']
                selectedEnvGroups = request.data['selectedEnvGroups']
                
            except Exception as errMsg:
                errorMsg = str(errMsg)
                status = 'failed'
                statusCode = HtmlStatusCodes.error
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='deleteEnvGroups', msgType='Error',
                                          msg=errorMsg, forDetailLogs=traceback.format_exc(None, errMsg))
                return Response(data={'status': status, 'errorMsg': errorMsg}, status=statusCode)

        if remoteControllerIp and remoteControllerIp != mainControllerIp:
            params = {"selectAll": selectAll, "selectedEnvGroups": selectedEnvGroups}
            restApi = '/api/v1/env/deleteEnvGroups'
            response, errorMsg = executeRestApiOnRemoteController('post', remoteControllerIp, ipPort, restApi, params, 
                                                                  user, webPage=Vars.webpage, action='DeleteEnvGroups')
            if errorMsg:
                status = 'failed'
                statusCode = HtmlStatusCodes.error 
                   
        else:            
            try:
                if selectAll:
                    envPath = f'{GlobalVars.keystackTestRootPath}/Envs'
                    for root,dirs,files in os.walk(envPath):
                        # /opt/KeystackTests/Envs/LoadCore
                        regexMatch = search(f'.+(/Envs.+)$', root)
                        if regexMatch:
                            # /opt/KeystackTests/Envs
                            # /opt/KeystackTests/Envs/qa
                            rmtree(regexMatch.group(1))
                
                if selectedEnvGroups:
                    for envGroup in selectedEnvGroups:
                        rmtree(envGroup)
                                
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='deleteEnvGroups', msgType='Info',
                                            msg=f'selectAll:{selectAll}, envs:{selectedEnvGroups}', forDetailLogs='')
                
            except Exception as errMsg:
                errorMsg = str(errMsg)
                status = 'failed'
                statusCode = HtmlStatusCodes.error
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='deleteEnvGroups', msgType='Error',
                                        msg=f'selectAll:{selectAll}, envs:{selectedEnvGroups}<br>error: {errorMsg}', 
                                        forDetailLogs=traceback.format_exc(None, errMsg))
                               
        return Response(data={'status': status, 'errorMsg': errorMsg}, status=statusCode)

    
class AmINext(APIView):
    swagger_schema = None
        
    @verifyUserRole()
    def post(self, request):
        """
        Description: 
            Check to see if the module/env is running after reserving the env.
            It could be in the waitlist.

        POST /api/v1/env/amINext
        
        Parameters:
            sessionId: The keystack session ID
            env: The env to reserve. Example: pythonSample
            user: user from keystack
            stage: stage
            module: module
            webhook: <optional>
        
        Usage:
            envObj = EnvMgmt.ManageEnv(env=self.moduleProperties['env'])
            envMgmtObj.amIRunning(user, sessionId, stage, module)                          
                                  
        Example:
            curl -X POST http://192.168.28.7:8000/api/v1/env/amINext
            
        Return:
            status and error
        """
        user = AccountMgr().getRequestSessionUser(request)
        remoteController = request.data.get('remoteController', None)
        mainControllerIp, remoteControllerIp, ipPort = getMainAndRemoteControllerIp(request, remoteController)
        statusCode = HtmlStatusCodes.success
        status = 'success'
        errorMsg = None

        if request.GET:
            # Rest APIs with inline params come in here
            try:
                sessionId = request.GET.get('sessionId')
                env = request.GET.get('env')
                userReserving = request.GET.get('user')
                stage = request.GET.get('stage')
                module = request.GET.get('module')
            except Exception as errMsg:
                errorMsg = str(errMsg)
                status = 'failed'
                statusCode = HtmlStatusCodes.error
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='AmINext', msgType='Error',
                                          msg=errorMsg, forDetailLogs=traceback.format_exc(None, errMsg))
                return Response(data={'status': status, 'errorMsg': errorMsg}, status=statusCode)
            
        # JSON format
        if request.data:
            # <QueryDict: {'playbook': pythonSample}
            try:
                sessionId = request.data['sessionId']
                env = request.data['env']
                userReserving = request.data['user']
                stage = request.data['stage']
                module = request.data['module']
            except Exception as errMsg:
                errorMsg = str(errMsg)
                status = 'failed'
                statusCode = HtmlStatusCodes.error
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='AmINext', msgType='Error',
                                          msg=errorMsg, forDetailLogs=traceback.format_exc(None, errMsg))
                return Response(data={'status': status, 'errorMsg': errorMsg}, status=statusCode)

        if remoteControllerIp and remoteControllerIp != mainControllerIp:
            params = {"sessionId": sessionId, "user": userReserving, "env": env, "stage": stage, "module": module}
            restApi = '/api/v1/env/amINext'
            response, errorMsg = executeRestApiOnRemoteController('post', remoteControllerIp, ipPort, restApi, params, 
                                                                  user, webPage=Vars.webpage, action='AmINext')
            if errorMsg:
                status = 'failed'
                statusCode = HtmlStatusCodes.error 
                   
        else:                    
            try:            
                envObj = EnvMgmt.ManageEnv(env=env)                          
                result = envObj.amIRunning(user, sessionId, stage, module) 
                del envObj

                if result not in [True, False] and result[0] == 'failed':
                    SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='AmINext', msgType='Error',
                                            msg=result[1], forDetailLogs=result[2])
                    
            except Exception as errMsg:
                errorMsg = str(errMsg)
                status = 'failed'
                statusCode = HtmlStatusCodes.error
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='AmINext', msgType='Error',
                                            msg=errorMsg, forDetailLogs=traceback.format_exc(None, errMsg))
                             
        return Response(data={'status': status, 'errorMsg': errorMsg, 'result':result}, status=statusCode)


class Reset(APIView):
    swagger_schema = None
        
    @verifyUserRole(webPage=Vars.webpage, action='Reset', exclude='engineer')
    def post(self, request):
        """
        Description: 
            Remove the user/env from the active env list

        POST /api/v1/env/reset
        
        Parameters:
            env: The env to reset
            webhook: <optional>
        
        Usage:
            envObj = EnvMgmt.ManageEnv(env=self.moduleProperties['env'])
            envObj.reset()                         
                                  
        Example:
            curl -X POST http://192.168.28.7:8000/api/v1/env/reset
            
        Return:
            status and error
        """
        user = AccountMgr().getRequestSessionUser(request)
        remoteController = request.data.get('remoteController', None)
        mainControllerIp, remoteControllerIp, ipPort = getMainAndRemoteControllerIp(request, remoteController)
        statusCode = HtmlStatusCodes.success
        status = 'success'
        errorMsg = None

        # http://ip:port/api/v1/envMgmt/reserveEnv?sessionId=sessionId&env=env
        if request.GET:
            # Rest APIs with inline params come in here
            try:
                env = request.GET.get('env')
            except Exception as errMsg:
                errorMsg = str(errMsg)
                status = 'failed'
                statusCode = HtmlStatusCodes.error
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='ResetEnv', msgType='Error',
                                          msg=errorMsg, forDetailLogs=traceback.format_exc(None, errMsg))
                return Response(data={'status': status, 'errorMsg': errorMsg}, status=statusCode)
             
        # JSON format
        if request.data:
            # <QueryDict: {'playbook': pythonSample}
            try:
                env = request.data['env']
            except Exception as errMsg:
                errorMsg = str(errMsg)
                status = 'failed'
                statusCode = HtmlStatusCodes.error
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='ResetEnv', msgType='Error',
                                          msg=errorMsg, forDetailLogs=traceback.format_exc(None, errMsg))
                return Response(data={'status': status, 'errorMsg': errorMsg}, status=statusCode)
 
        if remoteControllerIp and remoteControllerIp != mainControllerIp:
            params = {"env": env}
            restApi = '/api/v1/env/reset'
            response, errorMsg = executeRestApiOnRemoteController('post', remoteControllerIp, ipPort, restApi, params, 
                                                                  user, webPage=Vars.webpage, action='ResetEnv')
            if errorMsg:
                status = 'failed'
                statusCode = HtmlStatusCodes.error 
                   
        else:                    
            try:    
                envObj = EnvMgmt.ManageEnv(env=env)
                result = envObj.resetEnv()
                del envObj
                if result != True:
                    status = 'failed'
                    statusCode = HtmlStatusCodes.error
                    errorMsg = "DB failed to perform an env reset"
                    SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='resetEnv', msgType='Failed',
                                            msg=f'Env:{env}<br>error: {errorMsg}', forDetailLogs='')
                else:
                    SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='resetEnv', msgType='Info',
                                            msg=f'Env:{env}', forDetailLogs='')
                    
            except Exception as errMsg:
                errorMsg = str(errMsg)
                status = 'failed'
                statusCode = HtmlStatusCodes.error
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='resetEnv', msgType='Error',
                                        msg=f'Env:{env}<br>error: {errorMsg}', forDetailLogs=traceback.format_exc(None, errMsg))
                               
        return Response(data={'status': status, 'errorMsg': errorMsg}, status=statusCode)

'''    
class ReleaseEnvOnFailureRest(APIView):
    swagger_schema = None
        
    @verifyUserRole()
    def post(self, request):
        """
        Description: 
            Release the env that is on hold for a failure 

        POST /api/v1/env/releaseEnvOnFailure
        
        Parameters:
            env: The env to reset
            webhook: <optional>
        
        Usage:
            envObj = EnvMgmt.ManageEnv(env=self.moduleProperties['env'])
            envObj.reset()                         
                                  
        Example:
            curl -X POST http://192.168.28.7:8000/api/v1/env/releaseEnvOnFailure
            
        Return:
            status and error
        """
        user = AccountMgr().getRequestSessionUser(request)
        remoteController = request.data.get('remoteController', None)
        mainControllerIp, remoteControllerIp, ipPort = getMainAndRemoteControllerIp(request, remoteController)
        statusCode = HtmlStatusCodes.success
        status = 'success'
        errorMsg = None

        if request.GET:
            # Rest APIs with inline params come in here
            try:
                sessionId = request.GET.get('sessionId')
                userReleasing = request.GET.get('user')
                resultTimestampPath = request.GET.get('resultTimestampPath')
                env = request.GET.get('env')
                stage = request.GET.get('stage')
                module = request.GET.get('module')

            except Exception as errMsg:
                errorMsg = str(errMsg)
                status = 'failed'
                statusCode = HtmlStatusCodes.error
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='ReleaseEnvOnFailureRest', msgType='Error',
                                          msg=errorMsg, forDetailLogs=traceback.format_exc(None, errMsg))
                return Response(data={'status': status, 'errorMsg': errorMsg}, status=statusCode)
 
        # JSON format
        if request.data:
            # <QueryDict: {'playbook': pythonSample}
            try:
                sessionId = request.data['sessionId']
                userReleasing = request.data['user']
                resultTimestampPath = request.data['resultTimestampPath']
                env = request.data['env']
                stage = request.data['stage']
                module = request.data['module']

            except Exception as errMsg:
                errorMsg = str(errMsg)
                status = 'failed'
                statusCode = HtmlStatusCodes.error
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='ReleaseEnvOnFailureRest', msgType='Error',
                                          msg=errorMsg, forDetailLogs=traceback.format_exc(None, errMsg))
                return Response(data={'status': status, 'errorMsg': errorMsg}, status=statusCode)

        if remoteControllerIp and remoteControllerIp != mainControllerIp:
            params = {"sessionId": sessionId, "user": userReleasing, "resultTimestampPath": resultTimestampPath,
                      "env": env, "stage": stage, "module": module}
            restApi = '/api/v1/env/releaseEnvOnFailureRest'
            response, errorMsg = executeRestApiOnRemoteController('post', remoteControllerIp, ipPort, restApi, params, 
                                                                  user, webPage=Vars.webpage, action='ReleaseEnvOnFailureRest')
            if errorMsg:
                status = 'failed'
                statusCode = HtmlStatusCodes.error 
                   
        else:        
            envMgmtDataFile = f'{resultTimestampPath}/.Data/EnvMgmt/STAGE={stage}_MODULE={module}_ENV={env}.json'
            if os.path.exists(envMgmtDataFile) == False:
                return Response(data={'status': 'failed', 'errorMsg': f'No such file: {envMgmtDataFile}'}, status=HtmlStatusCodes.error)
    
            try:    
                session = {'sessionId':sessionId, 'stage':stage, 'module':module, 'user':user}           
                envMgmtData = readJson(envMgmtDataFile)
                envMgmtData['envIsReleased'] = True
                writeToJson(envMgmtDataFile, envMgmtData)
                
                envMgmtObj = ManageEnv(env)
                result = envMgmtObj.removeFromActiveUsersList([session])
                del envMgmtObj
                
                if result != 'success':
                    SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='ReleaseEnvOnFailureRest', msgType='Error',
                                              msg=f'Env:{env} user:{user} stage:{stage} module:{module}<br>error: {result}', 
                                              forDetailLogs='')
                else:
                    SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='ReleaseEnvOnFailureRest', msgType='Info',
                                              msg=f'Env:{env} user:{user} stage:{stage} module:{module}', 
                                              forDetailLogs='')  
            except Exception as errMsg:
                errorMsg = str(errMsg)
                status = 'failed'
                statusCode = HtmlStatusCodes.error
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='ReleaseEnvOnFailureRest', msgType='Error',
                                          msg=f'Env:{env} user:{user} stage:{stage} module:{module}<br>error: {errorMsg}', 
                                          forDetailLogs=traceback.format_exc(None, errMsg))
                               
        return Response(data={'status': status, 'errorMsg': errorMsg}, status=statusCode)
'''    
            
class RemoveFromActiveUsersListUI(APIView):
    swagger_schema = None
 
    @verifyUserRole()
    def post(self, request):
        """
        Description: 
            Called by keystack.py.  Remove the user/env from the active env list

        POST /api/v1/env/removeFromActiveUsersList
        
        Parameters:
            sessionId: The keystack session ID
            user: user from keystack
            stage: stage
            module: module
            webhook: <optional>
        
        Usage:
            envObj = EnvMgmt.ManageEnv(env=self.moduleProperties['env'])
            envObj.removeFromActiveUsersList([{'user':self.user, 'sessionId':self.timestampFolderName, 
                                               'stage':self.stage, 'module':self.module}])                         
                                  
        Example:
            curl -X POST http://192.168.28.7:8000/api/v1/env/removeFromActiveUsersList
            
        Return:
            status and error
        """
        user = AccountMgr().getRequestSessionUser(request)
        remoteController = request.data.get('remoteController', None)
        mainControllerIp, remoteControllerIp, ipPort = getMainAndRemoteControllerIp(request, remoteController)
        statusCode = HtmlStatusCodes.success
        status = 'success'
        errorMsg = None
        
        # http://ip:port/api/v1/envMgmt/reserveEnv?sessionId=sessionId&env=env
        if request.GET:
            # Rest APIs with inline params come in here
            try:
                sessionId = request.GET.get('sessionId')
                env = request.GET.get('env')
                removeUser = request.GET.get('user')
                stage = request.GET.get('stage')
                module = request.GET.get('module')
            except Exception as errMsg:
                errorMsg = str(errMsg)
                status = 'failed'
                statusCode = HtmlStatusCodes.error
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='RemoveFromActiveUsersListUI', msgType='Error',
                                          msg=errorMsg, forDetailLogs=traceback.format_exc(None, errMsg))
                return Response(data={'status': status, 'errorMsg': errorMsg}, status=statusCode)
            
        # JSON format
        if request.data:
            # <QueryDict: {'playbook': pythonSample}
            try:
                sessionId = request.data['sessionId']
                env = request.data['env']
                removeUser = request.data['user']
                stage = request.data['stage']
                module = request.data['module']
            except Exception as errMsg:
                errorMsg = str(errMsg)
                status = 'failed'
                statusCode = HtmlStatusCodes.error
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='RemoveFromActiveUsersListUI', msgType='Error',
                                          msg=errorMsg, forDetailLogs=traceback.format_exc(None, errMsg))
                return Response(data={'status': status, 'errorMsg': errorMsg}, status=statusCode)

        if remoteControllerIp and remoteControllerIp != mainControllerIp:
            params = {"sessionId": sessionId, "env": env, "user": removeUser, "stage": stage, "module": module}
            restApi = '/api/v1/env/removeFromActiveUsersListUI'
            response, errorMsg = executeRestApiOnRemoteController('post', remoteControllerIp, ipPort, restApi, params, 
                                                                  user, webPage=Vars.webpage, action='RemoveFromActiveUsersListUI')
            if errorMsg:
                status = 'failed'
                statusCode = HtmlStatusCodes.error 
                   
        else:            
            try:    
                envObj = EnvMgmt.ManageEnv(env=env)
                result = envObj.removeFromActiveUsersList([{'user':removeUser, 'sessionId':sessionId, 'stage':stage, 'module':module}])
                del envObj
                
                if result == False:
                    error = result
                    status = 'failed'
                    statusCode = HtmlStatusCodes.error
                    SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='RemoveFromActiveUsersListUI', msgType='Failed',
                                            msg=f'Env:{env}  user:{user} stage:{stage} module:{module}<br>error:{error}', forDetailLogs='')
                else:
                    SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='RemoveFromActiveUsersListUI', msgType='Info',
                                            msg=f'Env:{env}  user:{user} stage:{stage} module:{module}', forDetailLogs='')
                                
            except Exception as errMsg:
                errorMsg = str(errMsg)
                status = 'failed'
                statusCode = HtmlStatusCodes.error
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='RemoveFromActiveUsersListUI', msgType='Failed',
                                        msg=f'Env:{env}  user:{user} stage:{stage} module:{module}<br>error:{errorMsg}',
                                        forDetailLogs=traceback.format_exc(None, errMsg))
                               
        return Response(data={'status': status, 'errorMsg': errorMsg}, status=statusCode)


'''
class RemoveFromWaitList(APIView):
    swagger_schema = None
    
    @verifyUserRole()
    def post(self, request):
        """
        Description: 
            Remove the user/env from the active env list

        POST /api/v1/env/removeFromWaitList
        
        Parameters:
            sessionId: The keystack session ID
            user: user from keystack
            stage: stage
            module: module
            webhook: <optional>
        
        Usage:
            envObj = EnvMgmt.ManageEnv(env=self.moduleProperties['env'])
            envObj.removeFromWaitList([{'user':self.user, 'sessionId':self.timestampFolderName, 
                                               'stage':self.stage, 'module':self.module}])                         
                                  
        Example:
            curl -X POST http://192.168.28.7:8000/api/v1/env/removeFromWaitList
            
        Return:
            status and error
        """
        user = AccountMgr().getRequestSessionUser(request)
        remoteController = request.data.get('remoteController', None)
        mainControllerIp, remoteControllerIp, ipPort = getMainAndRemoteControllerIp(request, remoteController)
        statusCode = HtmlStatusCodes.success
        status = 'success'
        errorMsg = None
        
        # http://ip:port/api/v1/env/removeFromWaitList?sessionId=sessionId&env=env
        if request.GET:
            # Rest APIs with inline params come in here
            try:
                sessionId = request.GET.get('sessionId')
                env = request.GET.get('env')
                user = request.GET.get('user')
                stage = request.GET.get('stage')
                module = request.GET.get('module')
            except Exception as errMsg:
                errorMsg = str(errMsg)
                status = 'failed'
                statusCode = HtmlStatusCodes.error
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='RemoveFromWaitList', msgType='Error',
                                          msg=errorMsg, forDetailLogs=traceback.format_exc(None, errMsg))
                return Response(data={'status': status, 'errorMsg': errorMsg}, status=statusCode)
         
        # JSON format
        if request.data:
            # <QueryDict: {'playbook': pythonSample}
            try:
                sessionId = request.data['sessionId']
                env = request.data['env']
                user = request.data['user']
                stage = request.data['stage']
                module = request.data['module']
            except Exception as errMsg:
                errorMsg = str(errMsg)
                status = 'failed'
                statusCode = HtmlStatusCodes.error
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='RemoveFromWaitList', msgType='Error',
                                          msg=errorMsg, forDetailLogs=traceback.format_exc(None, errMsg))
                return Response(data={'status': status, 'errorMsg': errorMsg}, status=statusCode)

        if remoteControllerIp and remoteControllerIp != mainControllerIp:
            params = {"sessionId": sessionId, "env": env, "user": user, "stage": stage, "module": module}
            restApi = '/api/v1/env/removeFromWaitList'
            response, errorMsg = executeRestApiOnRemoteController('post', remoteControllerIp, ipPort, restApi, params, 
                                                                  user, webPage=Vars.webpage, action='RemoveFromWaitList')
            if errorMsg:
                status = 'failed'
                statusCode = HtmlStatusCodes.error 
                   
        else:        
            try:    
                envObj = EnvMgmt.ManageEnv(env=env)
                # sessionId, user=None, stage=None, module=None
                result = envObj.removeFromWaitList(user=user, sessionId=sessionId, stage=stage, module=module)
                del envObj
                
                if result == False:
                    errorMsg = result
                    status = 'failed'
                    statusCode = HtmlStatusCodes.error
                    SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='RemoveEnvFromWaitList', msgType='Failed',
                                            msg=f'Env:{env}  user:{user} stage:{stage} module:{module}<br>error:{errorMsg}', forDetailLogs='')
                else:
                    SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='RemoveEnvFromWaitList', msgType='Info',
                                            msg=f'Env:{env}  user:{user} stage:{stage} module:{module}', forDetailLogs='')
                                
            except Exception as errMsg:
                errorMsg = str(errMsg)
                status = 'failed'
                statusCode = HtmlStatusCodes.error
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='RemoveEnvFromWaitList', msgType='Failed',
                                        msg=f'Env:{env}  user:{user} stage:{stage} module:{module}<br>error:{errorMsg}',
                                        forDetailLogs=traceback.format_exc(None, errMsg))
                               
        return Response(data={'status': status, 'errorMsg': errorMsg}, status=statusCode)
'''
                

class RemoveEnvFromWaitList(APIView):
    @verifyUserRole()
    def post(self, request):
        """ 
        "waitList": [{"module": "LoadCore",
                      "sessionId": "11-01-2022-04:21:00:339301_rocky_200Loops",
                      "stage": "LoadCoreTest",
                      "user": "rocky"
                     },
                     {"module": "LoadCore",
                      "sessionId": "11-01-2022-04:23:05:749724_rocky_1test",
                      "stage": "Test",
                      "user": "bullwinkle"}]
        """
        remoteController = request.data.get('remoteController', None)
        mainControllerIp, remoteControllerIp, ipPort = getMainAndRemoteControllerIp(request, remoteController)
        user = AccountMgr().getRequestSessionUser(request)
        removeList = request.data.get('removeList', None)
        envNamespace = request.data.get('env', None)
        errorMsg = None
        status = 'success'
        statusCode = HtmlStatusCodes.success

        if remoteControllerIp and remoteControllerIp != mainControllerIp:
            params = {"removeList": removeList, "env": envNamespace}
            restApi = '/api/v1/env/removeEnvFromWaitList'
            response, errorMsg = executeRestApiOnRemoteController('post', remoteControllerIp, ipPort, restApi, params, 
                                                                  user, webPage=Vars.webpage, action='RemoveEnvFromWaitList')
            if errorMsg:
                status = 'failed'
                statusCode = HtmlStatusCodes.error 
                   
        else:        
            if '-' in envNamespace:
                env = envNamespace.replace('-', '/')
            else:
                env = envNamespace

            try:            
                envMgmtObj = ManageEnv(env)
    
                for waiting in removeList:
                    # {'env': 'loadcoreSample', 'sessionId': '11-06-2022-07:11:12:859325', 'stage': None, 'module': None}
                    envMgmtObj.removeFromWaitList(sessionId=waiting['sessionId'], user=waiting['user'], 
                                                stage=waiting['stage'], module=waiting['module'])
                                                                                    
                    SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='RemoveEnvFromWaitList', msgType='Info',
                                              msg=f'SessionId:{waiting["sessionId"]} User:{waiting["user"]} Stage:{waiting["stage"]}  Module:{waiting["module"]}', forDetailLogs=f'')
                    
            except Exception as errMsg:
                status = 'failed'
                errorMsg = errMsg
                statusCode = HtmlStatusCodes.error
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='RemoveEnvFromWaitList', msgType='Error',
                                        msg=errorMsg, forDetailLogs=traceback.format_exc(None, errMsg))
            
        return Response(data={'status': status, 'errorMsg': errorMsg}, status=statusCode)
 

class GetActiveUsersList(APIView):
    @verifyUserRole()
    def post(self, request):
        """ 
        "waitList": [{"module": "LoadCore",
                      "sessionId": "11-01-2022-04:21:00:339301_rocky_200Loops",
                      "user": "rocky"
                     },
                     {"module": "LoadCore",
                      "sessionId": "11-01-2022-04:23:05:749724_rocky_1test",
                      "user": "rocky"}]
        """
        remoteController = request.data.get('remoteController', None)
        mainControllerIp, remoteControllerIp, ipPort = getMainAndRemoteControllerIp(request, remoteController)
        user = AccountMgr().getRequestSessionUser(request)
        envNamespace = request.data.get('env', None)
        status = 'success'
        statusCode = HtmlStatusCodes.success
        errorMsg = None

        if remoteControllerIp and remoteControllerIp != mainControllerIp:
            params = {"env": envNamespace}
            restApi = '/api/v1/env/getActiveUsersList'
            response, errorMsg = executeRestApiOnRemoteController('post', remoteControllerIp, ipPort, restApi, params, 
                                                                  user, webPage=Vars.webpage, action='GetActiveUsersList')
            if errorMsg:
                status = 'failed'
                statusCode = HtmlStatusCodes.error 
            else:
                html = response.json()['tableData'] 
                      
        else:
            if '-' in envNamespace:
                env = envNamespace.replace('-', '/')
            else:
                env = envNamespace
                
            try:
                envMgmtObj = ManageEnv(env)
                envMgmtObj.setenv = env
                            
                html = '<table id="envActiveUsersTable" class="mt-2 table table-sm table-bordered table-fixed tableFixHead tableMessages">' 
                html += '<thead>'
                html += '<tr>'
                html += '<th scope="col" style="text-align:left">Release</th>'
                html += '<th scope="col" style="text-align:left">User</th>'
                html += '<th scope="col" style="text-align:left">SessionId</th>'
                html += '<th scope="col" style="text-align:left">Stage</th>'
                html += '<th scope="col" style="text-align:left">Task / Module</th>'
                html += '</tr>'
                html += '</thead>'
                html += '<tbody>'
                            
                # "inUsedBy": {'available': False, 'activeUsers': {'sessionId': '11-04-2022-10:26:25:988063', 'user': 'Hubert Gee', 'stage': None, 'module': None}, 'waitList': [{'sessionId': '11-05-2022-09:37:23:403861', 'user': 'Hubert Gee', 'stage': None, 'module': None}, {'sessionId': '11-05-2022-10:13:25:068764', 'user': 'Hubert Gee', 'stage': None, 'module': None}, {'sessionId': '11-05-2022-10:25:48:431241', 'user': 'Hubert Gee', 'stage': None, 'module': None}], 'isAvailable': False}

                for inUsedBy in envMgmtObj.getActiveUsers():
                    user = inUsedBy.get('user')
                    sessionId = inUsedBy.get('sessionId')
                    overallSummaryFile= inUsedBy.get('overallSummaryFile')
                    stage = inUsedBy.get('stage', None)
                    module = inUsedBy.get('module', None)
    
                    html += '<tr>'
                    html += f'<td><input type="checkbox" name="envActiveUsersCheckboxes" env="{env}" sessionId="{sessionId}" overallSummaryFile="{overallSummaryFile}" stage="{stage}" module="{module}" /></td>'
                    html += f'<td style="text-align:left">{user}</td>'
                    html += f'<td style="text-align:left">{sessionId}</td>'
                    html += f'<td style="text-align:left">{stage}</td>'
                    html += f'<td style="text-align:left">{module}</td>'
                    html += f'</tr>'

                html += '</tbody>'
                html += '</table>' 
                            
            except Exception as errMsg:
                status = 'failed'
                errorMsg = str(errMsg)
                statusCode = HtmlStatusCodes.error
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='GetEnvActiveUsers', msgType='Error',
                                        msg=errorMsg, forDetailLogs=traceback.format_exc(None, errMsg))
            
        return Response(data={'tableData': html, 'status': status, 'errorMsg': errorMsg}, status=statusCode)
 

class RemoveFromActiveUsersList(APIView):
    @verifyUserRole()
    def post(self, request):
        """ 
        Remove users or sessionId from using the env
        """
        remoteController = request.data.get('remoteController', None)
        mainControllerIp, remoteControllerIp, ipPort = getMainAndRemoteControllerIp(request, remoteController)
        user = AccountMgr().getRequestSessionUser(request)
        removeList = request.data.get('removeList', None)
        envNamespace = request.data.get('env', None)
        errorMsg = None
        status = 'success'
        statusCode = HtmlStatusCodes.success

        if remoteControllerIp and remoteControllerIp != mainControllerIp:
            params = {"removeList": removeList, 'env': envNamespace}
            restApi = '/api/v1/env/removeEnvFromActiveUsersList'
            response, errorMsg = executeRestApiOnRemoteController('post', remoteControllerIp, ipPort, restApi, params, 
                                                                  user, webPage=Vars.webpage, action='RemoveFromActiveUsersList')
            if errorMsg:
                status = 'failed'
                statusCode = HtmlStatusCodes.error 
                   
        else:   
            if '-' in envNamespace:
                env = envNamespace.replace('-', '/')
            else:
                env = envNamespace

            try:
                envMgmtObj = ManageEnv(env)
                excludeRemovingActiveUsers = []

                if '/' in env:
                    env = env.replace('/', '-')

                # Check if the env session is currently runing. Can't just release the env when it's testing.
                # But allow to release the env if it's manually reserved   
                # removeList: 
                #     [{'env': 'pythonSample', 'sessionId': '04-25-2023-18:13:51:640030', 'overallSummaryFile': 'None', 'stage': 'None', 'module': 'None'}]        
                for index,activeUser in enumerate(removeList): 
                    # overallSummaryFile exists only if it is a test. It doesn't exists for 
                    # manual users reserving the env. 
                    overallSummaryFile = activeUser['overallSummaryFile']                      
                    if activeUser['overallSummaryFile']:
                        if os.path.exists(overallSummaryFile):
                            overallSummaryData = readJson(overallSummaryFile)
                            resultPath = '/'.join(overallSummaryFile.split('/')[:-1])
                            envMgmtFile = f'/{resultPath}/.Data/EnvMgmt/STAGE={activeUser["stage"]}_MODULE={activeUser["module"]}_ENV={env}.json'
                            
                            if overallSummaryData['status'] == 'Running':
                                excludeRemovingActiveUsers.append(index)
                                status = 'failed'
                                errorMsg = f'Cannot remove an active session from a actively running session: {activeUser["sessionId"]}'
                                statusCode = HtmlStatusCodes.error
                                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='RemoveActiveUserFromEnv', 
                                                            msgType='Failed', msg=errorMsg, forDetailLogs='')
                                Response({'status': status, 'errorMsg': errorMsg}, status=statusCode)
                                
                            elif overallSummaryData['holdEnvsIfFailed']:
                                envMgmtData = readJson(envMgmtFile)
                                if envMgmtData['result'] == 'Failed' and envMgmtData['envIsReleased'] == False:
                                    excludeRemovingActiveUsers.append(index)
                                    status = 'failed'
                                    errorMsg = f'The Env:{env} is on hold for test failure debugging. It must be released in the pipeline page on pipelineId: {activeUser["sessionId"]}'
                                    statusCode = HtmlStatusCodes.error
                                    SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='RemoveActiveUserFromEnv', msgType='Failed', msg=errorMsg, forDetailLogs='')
                                    Response({'status': status, 'errorMsg': errorMsg}, status=statusCode)
                                    
                if len(excludeRemovingActiveUsers) > 0:
                    for index in excludeRemovingActiveUsers:
                        removeList.pop(index)
                            
                envMgmtObj.removeFromActiveUsersList(removeList)
                
                for env in removeList:
                    SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='RemoveUsersFromEnvActiveList', 
                                            msgType='Info',
                                            msg=f'SessionId:{env["sessionId"]} stage:{env["stage"]} module:{env["module"]}', forDetailLogs='')
                    
            except Exception as errMsg:
                status = 'failed'
                errorMsg = str(errMsg)
                statusCode = HtmlStatusCodes.error
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='RemoveActiveUsersFromEnv', msgType='Error',
                                        msg=errorMsg, forDetailLogs=f'RemoveUsersFromEnvActiveList: {traceback.format_exc(None, errMsg)}')
            
        return Response(data={'status': status, 'errorMsg': errorMsg}, status=statusCode)
        
        
class ReserveEnv(APIView):
    @verifyUserRole()
    def post(self, request):
        """ 
        User clicked the reserve button on the UI
        Go on the env wait-list.
        The reserve button has no stage and module
        """
        remoteController = request.data.get('remoteController', None)
        mainControllerIp, remoteControllerIp, ipPort = getMainAndRemoteControllerIp(request, remoteController)
        user = AccountMgr().getRequestSessionUser(request)
        envNamespace = request.data.get('env', None)
        sessionId = getTimestamp()
        status = 'success'
        statusCode = HtmlStatusCodes.success
        errorMsg = None

        if remoteControllerIp and remoteControllerIp != mainControllerIp:
            params = {"env": envNamespace}
            restApi = '/api/v1/env/reserveEnv'
            response, errorMsg = executeRestApiOnRemoteController('post', remoteControllerIp, ipPort, restApi, params, 
                                                                  user, webPage=Vars.webpage, action='ReserveEnv')
            if errorMsg:
                status = 'failed'
                statusCode = HtmlStatusCodes.error 
                   
        else:
            if '-' in envNamespace:
                env = envNamespace.replace('-', '/')
            else:
                env = envNamespace

            try:
                envMgmtObj = ManageEnv(env)
                if envMgmtObj.isUserInActiveUsersList(user):
                    status = 'failed'
                    errorMsg = f'The user is already actively using the env: {user}'
                    statusCode = HtmlStatusCodes.notAllowed
                    SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='ReserveEnv', msgType='Failed',
                                            msg=errorMsg, forDetailLogs='')
                    return Response({'status': status, 'errorMsg': errorMsg}, status=statusCode)
                
                if envMgmtObj.isUserInWaitList(user):
                    status = 'failed'
                    errorMsg = f'the user is already in the wait list: {user}'
                    statusCode = HtmlStatusCodes.notAllowed
                    SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='ReserveEnv', msgType='Failed',
                                              msg=errorMsg, forDetailLogs='')
                    return Response({'status': status, 'errorMsg': errorMsg}, status=statusCode)
             
                result = envMgmtObj.reserveEnv(sessionId=sessionId, user=user)
                if result[0] == 'success':
                    SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='ReserveEnv', msgType='Info',
                                              msg=result[1], forDetailLogs='')
                                    
                else:
                    status = 'failed'
                    errorMsg = result[1]
                    statusCode = HtmlStatusCodes.error
                    SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='ReserveEnv', msgType='Failed',
                                              msg=errorMsg, forDetailLogs='')
                                        
            except Exception as errMsg:
                status = 'failed'
                errorMsg = errMsg
                statusCode = HtmlStatusCodes.notAllowed
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='ReserveEnv', msgType='Error',
                                          msg=errorMsg, forDetailLogs=traceback.format_exc(None, errMsg))
            
        return Response(data={'status': status, 'errorMsg': errorMsg}, status=statusCode)
    

class ReleaseEnv(APIView):
    @verifyUserRole()
    def post(self, request):
        """ 
        Release button to release the current occupying session/user from the env in InUsedBy.
        """
        remoteController = request.data.get('remoteController', None)
        mainControllerIp, remoteControllerIp, ipPort = getMainAndRemoteControllerIp(request, remoteController)
        user = AccountMgr().getRequestSessionUser(request)
        env = request.data.get('env', None)
        status = 'success'
        statusCode = HtmlStatusCodes.success
        errorMsg = None
            
        if remoteControllerIp and remoteControllerIp != mainControllerIp:
            params = {"env": env}
            restApi = '/api/v1/results/archive'
            response, errorMsg = executeRestApiOnRemoteController('post', remoteControllerIp, ipPort, restApi, params, 
                                                                  user, webPage=Vars.webpage, action='ReleaseEnv')
            if errorMsg:
                status = 'failed'
                statusCode = HtmlStatusCodes.error 
                   
        else:
            if '/' in env:
                envNamespace = env.replace('/', '-')
            else:
                envNamespace = env
            
            try:
                envMgmtObj = ManageEnv()
                # [{'sessionId': '11-08-2022-15:10:36:026486_1231', 'overallSummaryFile': '/opt/KeystackTests/Results/GROUP=Default/PLAYBOOK=pythonSample/11-08-2022-15:10:36:026486_1231/overallSummary.json', 'user': 'hgee', 'stage': 'Test', 'module': 'CustomPythonScripts'}]
                envMgmtObj.setenv = env
                details = envMgmtObj.getEnvDetails()
                
                if len(details['activeUsers']) > 0:
                    # topActiveUser: {'sessionId': '11-16-2022-14:05:18:399384_hubogee', 'overallSummaryFile': '/opt/KeystackTests/Results/GROUP=Default/PLAYBOOK=pythonSample/11-16-2022-14:05:18:399384_hubogee/overallSummary.json', 'user': 'hgee', 'stage': 'DynamicVariableSample', 'module': 'CustomPythonScripts'}
                    
                    topActiveUser = details['activeUsers'][0]
                    # Check if the env session is currently runing. Can't just release the env when it's testing.
                    # But allow to release the env if it's manually reserved 
                    # If overallSummaryFile exists, this means the session is an automated test. Not manual user.           
                    if topActiveUser['overallSummaryFile']:
                        overallSummaryFile = topActiveUser['overallSummaryFile']
                        if os.path.exists(overallSummaryFile):
                            overallSummaryData = readJson(overallSummaryFile)
                            resultPath = '/'.join(overallSummaryFile.split('/')[:-1])
                            envMgmtFile = f'/{resultPath}/.Data/EnvMgmt/STAGE={topActiveUser["stage"]}_MODULE={topActiveUser["module"]}_ENV={envNamespace}.json'
                            
                            if overallSummaryData['status'] == 'Running':
                                status = 'failed'
                                errorMsg = f'The Env:{env} is still being used by a running session: {topActiveUser["sessionId"]}'
                                statusCode = HtmlStatusCodes.error
                                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='ReleaseEnv', msgType='Error',
                                                          msg=errorMsg, forDetailLogs='')
                                return Response({'status': status, 'errorMsg': errorMsg}, status=statusCode)
                            else:
                                # Completed or Aborted
                                if overallSummaryData['holdEnvsIfFailed']:
                                    envMgmtData = readJson(envMgmtFile)
                                    if envMgmtData['result'] == 'Failed' and envMgmtData['envIsReleased'] == False:
                                        status = 'failed'
                                        errorMsg = f'The Env:{env} is on hold for test failure debugging. It must be released in the pipeline page on sessionId: {topActiveUser["sessionId"]}'
                                        statusCode = HtmlStatusCodes.error
                                        SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='ReleaseEnv', msgType='Error', msg=errorMsg, forDetailLogs='')
                                        return Response({'status': status, 'errorMsg': errorMsg}, status=statusCode)
                            
                    envMgmtObj.releaseEnv()
                    SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='ReleaseEnv', msgType='Info',
                                              msg=f'Env: {env}', forDetailLogs='') 

            except Exception as errMsg:
                status = 'failed'
                errorMsg = str(errMsg)
                statusCode = HtmlStatusCodes.error
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='ReleaseEnv', msgType='Error',
                                          msg=errorMsg, forDetailLogs=f'ReleaseEnv: {traceback.format_exc(None, errMsg)}')
            
        return Response(data={'status': status, 'errorMsg': errorMsg}, status=statusCode)


class ReleaseEnvOnFailure(APIView):
    """ 
    sessionMgmt release-env button for each stage/module/env failure.
    If test failed, envs are on hold for debugging. A Release Envs button is created and blinking.
    """
    @verifyUserRole()
    def post(self,request):
        remoteController = request.data.get('remoteController', None)
        mainControllerIp, remoteControllerIp, ipPort = getMainAndRemoteControllerIp(request, remoteController)
        user = AccountMgr().getRequestSessionUser(request)
        statusCode = HtmlStatusCodes.success
        errorMsg = None
        status = 'success'
            
        sessionId     = request.data.get('sessionId', None)
        sessionUser   = request.data.get('user', None)
        stage         = request.data.get('stage', None)
        module        = request.data.get('module', None)
        env           = request.data.get('env', None)
        resultTimestampPath = request.data.get('resultTimestampPath', None)

        if remoteControllerIp and remoteControllerIp != mainControllerIp:
            params = {"user": sessionUser, 'sessionId': sessionId, 'stage': stage,
                      'module': module, 'env': env, 'resultTimestampPath': resultTimestampPath}
            restApi = '/api/v1/env/releaseEnvOnFailure'
            response, errorMsg = executeRestApiOnRemoteController('post', remoteControllerIp, ipPort, restApi, params, 
                                                                  user, webPage=Vars.webpage, action='ReleaseEnvOnFailure')
            if errorMsg:
                status = 'failed'
                statusCode = HtmlStatusCodes.error 
                   
        else:
            if '/' in env:
                env = env.replace('/', '-')
                
            envMgmtDataFile = f'{resultTimestampPath}/.Data/EnvMgmt/STAGE={stage}_MODULE={module}_ENV={env}.json'

            if '-' in env:
                env = env.replace('-', '/')
            
            try:
                envMgmtData = readJson(envMgmtDataFile)
                envMgmtObj = ManageEnv(env)
                session = {'sessionId':sessionId, 'stage':stage, 'module':module, 'user':sessionUser}
                envMgmtObj.removeFromActiveUsersList([session])
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='ReleaseEnvOnFailed', msgType='Info',
                                        msg=f'{session}', forDetailLogs='')

                envMgmtData['envIsReleased'] = True
                writeToJson(envMgmtDataFile, envMgmtData)
                    
            except Exception as errMsg:
                statusCode = HtmlStatusCodes.error
                error = str(errMsg)
                status = 'failed'
                statusCode = HtmlStatusCodes.error
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='ReleaseEnvOnFailed', msgType='Error',
                                         msg=errMsg, forDetailLogs=f'error: {traceback.format_exc(None, errMsg)}')
          
        return Response(data={'status': status, 'errorMsg': errorMsg}, status=statusCode)


class ResetEnv(APIView):
    """ 
    If the DB is unrepairable, reset it as last resort. 
    """
    @verifyUserRole()
    def post(self, request):
        remoteController = request.data.get('remoteController', None)
        mainControllerIp, remoteControllerIp, ipPort = getMainAndRemoteControllerIp(request, remoteController)
        user = AccountMgr().getRequestSessionUser(request)
        env = request.data.get('env', None)
        status = 'success'
        statusCode = HtmlStatusCodes.success
        errorMsg = None

        if remoteControllerIp and remoteControllerIp != mainControllerIp:
            params = {'env': env}
            restApi = '/api/v1/env/resetEnv'
            response, errorMsg = executeRestApiOnRemoteController('post', remoteControllerIp, ipPort, restApi, params, 
                                                                  user, webPage=Vars.webpage, action='ResetEnv')
            if errorMsg:
                status = 'failed'
                statusCode = HtmlStatusCodes.error 
                   
        else:        
            try:
                envMgmtObj = ManageEnv(env)
                envMgmtObj.resetEnv()
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='ResetEnv', msgType='Info',
                                          msg=f'Env: {env}', forDetailLogs='')
                            
            except Exception as errMsg:
                status = 'failed'
                errorMsg = errMsg
                statusCode = HtmlStatusCodes.error
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='ResetEnv', msgType='Error',
                                          msg=errorMsg, forDetailLogs=f'ResetEnv: {traceback.format_exc(None, errMsg)}')
            
        return Response(data={'status': status, 'errorMsg': errorMsg}, status=statusCode)

