import os, sys, subprocess, json, traceback
from re import search
from glob import glob
from time import sleep

from commonLib import createTestResultTimestampFolder, groupExists, validatePlaybook
from keystackUtilities import convertStringToDict, getDeepDictKeys, readFile, readYaml, writeToJson, convertStrToBoolean, mkdir2, writeToFile
from systemLogging import SystemLogsAssistant
from topbar.settings.accountMgmt.verifyLogin import verifyUserRole
from topbar.settings.accountMgmt.accountMgr import AccountMgr
from topbar.settings.accountMgmt.verifyLogin import authenticateLogin
from topbar.docs.restApi.controllers import getMainAndRemoteControllerIp, executeRestApiOnRemoteController
from execRestApi import ExecRestApi
from globalVars import GlobalVars, HtmlStatusCodes
from db import DB

from django.views import View
from django.http import JsonResponse
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
    webpage = 'playbooks'

       
class GetPlaybookDetails(APIView):
    playbook = openapi.Parameter(name='playbook', description="Name of the Playbook", example="qaPlaybook",
                                 required=True, in_=openapi.IN_QUERY, type=openapi.TYPE_STRING) 
    @swagger_auto_schema(tags=['/api/v1/playbook/details'], manual_parameters=[playbook], 
                         operation_description="Get playbook details")
    @verifyUserRole()
    def get(self, request, data=None):
        """
        Description:
            Get details of a playbook
        
        GET /api/vi/playbook/details
        
        ---
        Examples:
            curl -H "API-Key: iNP29xnXdlnsfOyausD_EQ" -X GET http://192.168.28.7:8000/api/v1/playbook/details?playbook=pythonSample
            
            curl -H "API-Key: iNP29xnXdlnsfOyausD_EQ" -d "playbook=pythonSample" -H "Content-Type: application/x-www-form-urlencoded" -X GET http://192.168.28.7:8000/api/v1/playbook/details 
            
            curl -H "API-Key: iNP29xnXdlnsfOyausD_EQ" -d '{"playbook": "pythonSample"}' -H "Content-Type: application/json" -X GET http://192.168.28.7:8000/api/v1/playbook/details
            
            session = requests.Session()
            response = session.request('Get', 'http://localhost:8000/api/v1/playbook/details')
            return Response({'playbooks': response.json()['playbooks']})
        """
        status = HtmlStatusCodes.success
        playbookDetails = None
        playbookName = None
        errorMsg = None
        user = AccountMgr().getRequestSessionUser(request)
        remoteController = request.data.get('remoteController', None)
        mainControllerIp, remoteControllerIp, ipPort = getMainAndRemoteControllerIp(request, remoteController)

        # http://ip:port/api/v1/playbook/details?playbook=myCoolPlaybook
        if request.GET:
            try:
                playbookName = request.GET.get('playbook')
            except Exception as error:
                errorMsg = f'Expecting key playbook, but got: {request.GET}'
                return Response(data={'playbookDetails': playbookDetails, 'status': 'failed', 
                                      'errorMsg': errorMsg}, status=HtmlStatusCodes.error)
            
        # JSON format
        if request.data:
            # <QueryDict: {'playbook': pythonSample}
            try:
                playbookName = request.data['playbook']
            except Exception as errMsg:
                errorMsg = f'Expecting key playbook, but got: {request.data}'
                return Response(data={'playbookDetails': playbookDetails, 'status': 'failed', 
                                      'errorMsg': errorMsg}, status=HtmlStatusCodes.error)

        if remoteControllerIp and remoteControllerIp != mainControllerIp:
            params = {"playbook": playbookName}
            restApi = '/api/v1/playbook/details'
            response, errorMsg = executeRestApiOnRemoteController('get', remoteControllerIp, ipPort, restApi, params, 
                                                                  user, webPage=Vars.webpage, action='GetPlaybookDetails')
            if errorMsg:
                status = 'failed'
                statusCode = HtmlStatusCodes.error 
            else:
                playbookDetails = response.json()['playbookDetails']
                      
        else:
            try:
                if '.yml' not in playbookName:
                    playbookName = f'{playbookName}.yml'
                
                playbookPath = f'{GlobalVars.playbooks}/{playbookName}'
                playbookDetails = readYaml(playbookPath)
        
            except Exception as errMsg:
                errorMsg = str(errMsg)
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='GetPlaybookDetails', 
                                          msgType='Error', msg=errorMsg, forDetailLogs=traceback.format_exc(None, errMsg))
                return Response(data={'playbookDetails': playbookDetails, 'status': 'failed', 
                                      'errorMsg': errorMsg}, status=HtmlStatusCodes.error)
            
        return Response(data={'playbookDetails': playbookDetails, 'errorMsg': errorMsg, 'status': 'success'}, status=status)


class RunPlaybook(APIView):
    #serializers = RunPlaybookSerializer
    # Parameter([('name', 'playbook'), ('in', 'query'), ('type', 'string')]) 
    # Parameter([('name', 'sessionId'), ('in', 'query'), ('type', 'string')])
    playbook        = openapi.Parameter(name='playbook',
                                        description="Name of the Playbook to execute", example="pythonSample",
                                        required=False, in_=openapi.IN_QUERY, type=openapi.TYPE_STRING)  
    sessionId       = openapi.Parameter(name='sessionId',
                                        description="Give a name for the test to help locate the result", 
                                        in_=openapi.IN_QUERY, type=openapi.TYPE_STRING)
    group           = openapi.Parameter(name='group',
                                        description="The group to put the results under. Defaults to 'Default' group", 
                                        in_=openapi.IN_QUERY, type=openapi.TYPE_STRING)                               
    playbookConfigs = openapi.Parameter(name='playbookConfigs',
                                        description="Playbook JSON configs", in_=openapi.IN_QUERY, 
                                        type=openapi.TYPE_STRING,
                                        example='Modify anything in the Playbook using JSON format (Modifications are done in memory. Not in actual files). Note: Modules are in a list.  This means you must include all module parameters/values that the playbook has even if you are modifying just one parameter.  Example: Let say we want to modify the env, we must include the playlist also. This is the nature of modifying json list.  {"stages": {"Test": {"Modules": [{"/Modules/CustomPythonScripts": {"env": "rack2", "playlist": ["/opt/KeystackTests/Modules/CustomPythonScripts/Testcases"]}}] }}}}')
    testcaseConfigs = openapi.Parameter(name='testcaseConfigs',
                                       description="Modify a Playbook playlist testcase yml files (Modifications are done in memory. Not in actual files)", 
                                       in_=openapi.IN_QUERY, type=openapi.TYPE_STRING,
                                       example="A list of testcase yml files associating with modifications in json format: [{'/Modules/IxNetwork/Testcases/bgp.yml': {'script': 'script1.py'}}, {}, ...]")
           
    envConfigs      = openapi.Parameter(name='envConfigs', description="Modify the playbook's env params (in memory)", 
                                       in_=openapi.IN_QUERY, type=openapi.TYPE_STRING,
                                       example="A list of json env settings. Example: [{'stage': 'Test', 'module': 'LoadCore', 'params':   {'mwIp': '10.1.2.3'}, {'stage': 'teardown', 'module': 'cleanup', 'params': {'serverIp': '1.1.1.1'}, {}} ...}]")
    jira            = openapi.Parameter(name='jira', description="Open/Update Jira Issue", in_=openapi.IN_QUERY, 
                                        type=openapi.TYPE_BOOLEAN)
    awsS3           = openapi.Parameter(name='awsS3', description="Push results to AWS S3", in_=openapi.IN_QUERY, 
                                        type=openapi.TYPE_BOOLEAN)
    emailResults    = openapi.Parameter(name='emailResults', description="Email results", in_=openapi.IN_QUERY, 
                                        type=openapi.TYPE_BOOLEAN)
    trackResults    = openapi.Parameter(name='trackResults', 
                                        description="Track and monitor results in a CSV file for graphing", 
                                        in_=openapi.IN_QUERY, type=openapi.TYPE_BOOLEAN)   
    holdEnvsIfFailed = openapi.Parameter(name='holdEnvsIfFailed', description="Keep the env reserved for debugging if test failed", in_=openapi.IN_QUERY, 
                                        type=openapi.TYPE_BOOLEAN)
    debug           = openapi.Parameter(name='debug', description="Debug/Dev mode", 
                                        in_=openapi.IN_QUERY, type=openapi.TYPE_BOOLEAN)
    emailResults    = openapi.Parameter(name='emailResults', description="Email results", 
                                        in_=openapi.IN_QUERY, type=openapi.TYPE_BOOLEAN)        
    @swagger_auto_schema(tags=['/api/v1/playbook/run'], manual_parameters=[playbook, sessionId, group,
                         playbookConfigs, testcaseConfigs, envConfigs, jira, awsS3, emailResults, trackResults, debug])
    @verifyUserRole()
    def post(self, request, data=None):
        """
        Run a playbook. Minimum param requirement: playbook=[playbooName]
         
        If you want to create a playbook from scratch, leave the playbook param blank and put the
        playbook json string in the param playbookConfigs. 
        
        POST: /api/v1/playbook/run
        
        parameters:
            playbook:         Optional: Playbook name to run
            sessionId:        Optional
            group:            Optiona: The name of the group to put the results. Defauls to Default group.
            playbookConfigs:  Optional <JSON object>: To modify a playbook.
            emailResults:     Optional: True|False.  Example: inline=emailResults=true  json={"emailResults": "true"}
            debug:            Optional: True|False.  Example: inline=debug=true  json={"debug": "true"}
            awsS3:            Optional: True|False.  Example: inline=awsS3=true  json={"awsS3": "true"}
            jira:             Optional: True|False.  Example: inline=jira=true   json={"jira": "true"}
            trackResults:     Optional  True|False.  Example: inline=trackResults=true  json={"trackResults": "true"}
            holdEnvsIfFailed: Optional  True|False.  Example: inline=holdEnvsIfFailed=true  json={"holdEnvsIfFailed": "true"}
            testcaseConfigs:  Optional: [{testcase: jsonDetailsOfTheTestcaseToModify}].
            removeJobAfterRunning Optional: True|False: For jobScheduling. Remove the scheduled job after running the job.
            scheduledJob      Optional: <JSON object>: cron job properties.
            
            # You could modify the env file or state an env file to use for the stage/module
            # To modify an env file, use 'configs'.
            # To state a different env file, use 'envFile'.
            envConfigs:      Optional: [{env: jsonDetailsOfTheEnvToModify}].
            
                             Example 1: [{'stage': 'Test', 'module': 'LoadCore', 'configs': {'mwIp': '10.1.2.3'}, 
                                         {'stage': 'teardown', 'module': 'cleanup', configs: {'serverIp': '1.1.1.1'}, {}} ...}]
                                                 
                             Example 2: [{'stage': 'Test', 'module': 'LoadCore', 'envFile': 'sanityTest.yml', 
                                         {'stage': 'teardown', 'module': 'cleanup', configs: {'serverIp': '1.1.1.1'}, {}} ...}]
                                                 
            createDynamicPlaybook Optional: <Json object> Create a playbook from blank.
        
        Examples:
            # Inline parameters must wrap rest api in quotes
            curl -H "API-Key: iNP29xnXdlnsfOyausD_EQ" -X POST 'http://192.168.28.7:8000/api/v1/playbook/run?playbook=pythonSample&sessionId=awesomeTest2&awsS3=true&pauseOnError=false'
            
            curl --insecure -L -X POST 'https://192.168.28.17/api/v1/playbook/run?playbook=pythonSample&sessionId=awesomeTest'
        
            # works
            curl -d "playbook=pythonSample&sessionId=awesomeTest" -H "API-Key: iNP29xnXdlnsfOyausD_EQ" -H "Content-Type: application/x-www-form-urlencoded" -X POST http://192.168.28.7:8000/api/v1/playbook/run 
            
            
            curl -d "sessionId=hello&playbook=/opt/KeystackTests/Playbooks/pythonSample.yml&awsS3=True&jira=False&pauseOnError=False&debug=False&group=QA" -H "Content-Type: application/x-www-form-urlencoded" -X POST http://192.168.28.7:8000/api/v1/playbook/run
            
            curl -d '{"playbook": "pythonSample", "sessionId": "awesomeTest", "awsS3": "true"}' -H "Content-Type: application/json" -X POST http://192.168.28.7:8000/api/v1/playbook/run 
        
            # playbookConfigs
            curl -H "API-Key: VZleFqgtRtfwvHwlSujOXA" -d '{"playbook": "pythonSample", "sessionId": "awesomeTest", "awsS3": true, "playbookConfigs": {"stages": {"Test": {"Modules": [{"/Modules/CustomPythonScripts": {"env": "hubert", "playlist": ["/opt/KeystackTests/Modules/CustomPythonScripts/Testcases"]}}] }}}}' -H "Content-Type: application/json"  -X POST http://192.168.28.7:8000/api/v1/playbook/run

            # Not work: Curly braces are unsafe. You must use urlencode or -d.
            #    Or include -g|--globoff
            # This  option  switches  off  the "URL globbing parser". When you set this option, you can
            # specify URLs that contain the letters {}[] without having them being interpreted by  curl
            # itself.  Note  that  these  letters  are not normal legal URL contents but they should be
            # encoded according to the URI standard.
            curl -X POST 'http://192.168.28.17:8000/api/v1/playbook/run?playbook=pythonSample&sessionId=awesomeTest2&playbookConfigs={"stages": {"Test": {"/Modules/CustomPythonScripts": {"enable": false}}}}'
                        
            curl -d '{"playbook": "pythonSample", "sessionId": "awesomeTest", "playbookConfigs": {"globalSettings": {"loginCredentialKey": "regressionTest"}, "stages": {"Test": {"/Modules/CustomPythonScripts": {"enable": false}}}}}' -H "Content-Type: application/json" -X POST http://192.168.28.7:8000/api/v1/playbook/run
            
            # Modify the playlist TESTCASES (Not the playbook itself)
            curl -d '{"playbook": "pythonSample", "sessionId": "awesomeTest", "playlistMods": [{"/Modules/CustomPythonScripts/Testcases/bgp.yml": {"script": "ospf.py"}}]}' -H "Content-Type: application/json" -X POST http://192.168.28.7:8000/api/v1/playbook/run
            
            # Modify playbook module's ENV configs (Not the playbook itself)
            curl -H "API-Key: iNP29xnXdlnsfOyausD_EQ" -d '{"playbook": "pythonSample", "sessionId": "awesomeTest", "envConfigs": [{"stage": "Test", "module": "CustomPythonScripts",  "params": {"login": false}}]}' -H "Content-Type: application/json" -X POST http://192.168.28.7:8000/api/v1/playbook/run

            # Create a dynamic playbook

        Use form-data. Don't use RAW because it requires csrf token. A hassle to insert it.
        Must do a GET to get it and then insert it as a RAW with Content-Type: application/JSON
        
        If the URL contains the data such as the following, then use request.GET.get('<parameter_name>')
           http://ip:port/api/v1/runPlaybook?playbook=myCoolPlaybook&sessionId=myCoolTestSession
           
        If you pass in the data as raw format, then use request.data
        
        Returns:
           - The sessionId
           - The result path
        """
        sessionIdPath = None
        resultTimestampFolderName = None 
        self.Group = 'Default'
        
        # action: runPlaybook or runPipeline
        action = 'runPlaybook'
        self.playbookName = 'Dynamically-Created'
        self.awsLoginFile = None
        self.awsAccessKey = None
        self.awsSecretKey = None
        self.awsRegion = None
        self.s3BucketPath = None
        errorMsg = None
        user = AccountMgr().getRequestSessionUser(request)
        errorMsg = None 
        status = 'success'
        statusCode = HtmlStatusCodes.success
        
        try:
            # http://ip:port/api/v1/playbook/run?playbook=myPlaybook&sessionId=mySessionId
            if request.GET:
                self.remoteController      = request.GET.get('remoteController', None)
                self.scheduledJob          = convertStrToBoolean(request.GET.get('scheduledJob', False))
                self.removeJobAfterRunning = convertStrToBoolean(request.GET.get('removeJobAfterRunning', False))
                self.pipeline              = request.GET.get('pipeline', None)
                self.sessionId             = request.GET.get('sessionId', None)
                self.group                 = request.GET.get('group', 'Default')
                # <QueryDict: {'playbook': ['pythonSample'], 'sessionId': ['awesomeTest2'], 'awsS3': ['']}>
                self.playbook              = request.GET.get('playbook', None)
  
                self.envConfigs            = request.GET.get('envConfigs', None)
                if self.envConfigs:
                    self.envConfigs        = json.loads(self.envConfigs)                
                
                self.playlistMods          = request.GET.get('playlistMods', None)
                if self.playlistMods:
                    self.playlistMods      = json.loads(self.playlistMods)
                    
                self.playbookConfigs       = request.GET.get('playbookConfigs', None)
                if self.playbookConfigs is not None:
                    self.playbookConfigs   = json.loads(self.playbookConfigs)
    
                self.awsS3                 = convertStrToBoolean(request.GET.get('awsS3', False))
                # awsLoginFile=<playbook>.globalSettings.awsLogin.<value>
                self.loginCredentialKey    = request.GET.get('loginCredentialKey', None)
                self.jira                  = convertStrToBoolean(request.GET.get('jira', False))
                self.trackResults          = convertStrToBoolean(request.GET.get('trackResults', False))
                self.env                   = request.GET.get('env', None)
                self.debug                 = convertStrToBoolean(request.GET.get('debug', False))          
                self.emailResults          = convertStrToBoolean(request.GET.get('emailResults', False))
                self.pauseOnError          = convertStrToBoolean(request.GET.get('pauseOnError', False))
                self.holdEnvsIfFailed      = convertStrToBoolean(request.GET.get('holdEnvsIfFailed', False))
                self.abortTestOnFailure    = convertStrToBoolean(request.GET.get('abortTestOnFailure', False))
                self.includeLoopTestPassedResults  = convertStrToBoolean(request.GET.get('includeLoopTestPassedResults', False))
                
        except Exception as errMsg:
            errorMsg = str(errMsg)
            print('\nrunPlaybook error: request.GET error:', errMsg)
            SystemLogsAssistant().log(user=user, webPage='pipelines', action=action, msgType='Error',
                                        msg=errorMsg, forDetailLogs=traceback.format_exc(None, errMsg)) 
            return Response(data={'status': 'failed', 'errorMsg': errorMsg, 'sessionIdPath': None, 
                                  'sessionId': None, 'testGroup':self.group}, status=HtmlStatusCodes.error)

        # Calls from sessionMgmt template comes here
        # curl -d {} and keystackUI
        if request.data:
            # Rest API json data 
            # {'playbook': '/opt/KeystackTests/Playbooks/pythonSample.yml', 'debug': True, 'emailResults': True, 'awsS3': True, 'jira': True, 'pauseOnError': True}
            
            # RUN DATA: <QueryDict: {'sessionId': [''], 'playbook': ['pythonSample'], 'awsS3': ['False'], 'jira': ['False'], 'pauseOnError': ['False'], 'debug': ['False'], 'group': ['Default'], 'holdEnvsIfFailed': ['False'], 'abortTestOnFailure': ['False'], 'includeLoopTestPassedResults': ['False'], 'scheduledJob': ['minute=* hour=* dayOfMonth=* month=* dayOfWeek=*'], 'webhook': ['true']}
            try:
                self.remoteController              = request.data.get('remoteController', None)
                self.scheduledJob                  = request.data.get('scheduledJob', None)
                self.removeJobAfterRunning = convertStrToBoolean(request.data.get('removeJobAfterRunning', False))
                self.pipeline                      = request.data.get('pipeline', None)
                self.sessionId                     = request.data.get('sessionId', None)
                self.group                         = request.data.get('group', 'Default')
                self.playbook                      = request.data.get('playbook', None)
                self.playlistMods                  = request.data.get('playlistMods', None)
                self.playbookConfigs               = request.data.get('playbookConfigs', None)
                self.envConfigs                    = request.data.get('envConfigs', None)
                self.awsS3                         = convertStrToBoolean(request.data.get('awsS3', False))
                self.loginCredentialKey            = request.data.get('loginCredentialKey', None)
                self.jira                          = convertStrToBoolean(request.data.get('jira', False))
                self.trackResults                  = convertStrToBoolean(request.data.get('trackResults', False))
                self.env                           = request.data.get('env', None)
                self.debug                         = convertStrToBoolean(request.data.get('debug', False))
                self.emailResults                  = convertStrToBoolean(request.data.get('emailResults', False))
                self.pauseOnError                  = convertStrToBoolean(request.data.get('pauseOnError', False))
                self.holdEnvsIfFailed              = convertStrToBoolean(request.data.get('holdEnvsIfFailed', False))
                self.abortTestOnFailure            = convertStrToBoolean(request.data.get('abortTestOnFailure', False))
                self.includeLoopTestPassedResults  = convertStrToBoolean(request.data.get('includeLoopTestPassedResults', False))
                
            except Exception as errMsg:
                errorMsg = str(errMsg)
                print('\nrunPlaybook error: request.data error:', errMsg)
                SystemLogsAssistant().log(user=user, webPage='pipelines', action=action, msgType='Error',
                                          msg=errorMsg, forDetailLogs=traceback.format_exc(None, errMsg)) 
                return Response(data={'status': 'failed', 'errorMsg': errorMsg, 'sessionIdPath': None, 
                                      'sessionId': None, 'testGroup':self.group}, status=HtmlStatusCodes.error)
                
        mainControllerIp, remoteControllerIp, ipPort = getMainAndRemoteControllerIp(request, self.remoteController)

        if remoteControllerIp and remoteControllerIp != mainControllerIp:
            params = {'scheduledJob': self.scheduledJob, 'removeJobAfterRunning':self.removeJobAfterRunning,
                      'pipeline': self.pipeline, 'sessionId': self.sessionId, 'group': self.group, 'playbook': self.playbook,
                      'playlistMods': self.playlistMods, 'playbookConfigs': self.playbookConfigs, 'envConfigs': self.envConfigs,
                      'awsS3': self.awsS3, 'loginCredentialKey': self.loginCredentialKey, 'jira': self.jira, 'trackResults': self.trackResults,
                      'env': self.env, 'debug': self.debug, 'emailResults': self.emailResults, 'pauseOnError': self.pauseOnError,
                      'holdEnvsIfFailed': self.holdEnvsIfFailed, 'abortTestOnFailure': self.abortTestOnFailure, 
                      'includeLoopTestPassedResults': self.includeLoopTestPassedResults}
            
            restApi = '/api/v1/playbook/run'
            response, errorMsg = executeRestApiOnRemoteController('post', remoteControllerIp, ipPort, restApi, params, 
                                                                  user, webPage=Vars.webpage, action='RunPlaybook')
            if errorMsg:
                status = 'failed'
                statusCode = HtmlStatusCodes.error

            else:
                resultTimestampFolder      = response.json()['sessionIdPath']
                resultTimestampFolderName  = response.json()['sessionId']
                self.group                 = response.json()['testGroup']

        else:
            if self.pipeline:
                # /opt/KeystackTests/Pipelines/samples-pythonSample.yml
                pipelineArgs = readYaml(self.pipeline)
                      
                # pipeline:samples-pythonSample
                # playbook:Samples/pythonSample
                for key,value in pipelineArgs.items():
                    if key == 'pipelineName':
                        continue
                    
                    if value:
                        setattr(self, key, value)

                action = 'runPipeline'
            
            if self.playbook is None:
                pipelineName = self.pipeline.split('/')[-1].split('.')[0]
                SystemLogsAssistant().log(user=user, webPage='pipelines', action=action, msgType='Error',
                                          msg=f'Pipeline has no playbook defined: {pipelineName}', forDetailLogs='')            
                return Response(data={'status': 'failed', 
                                      'errorMsg': f'Pipeline has no playbook defined: {pipelineName}'}, status=HtmlStatusCodes.error)
                                                
            if self.playbook is None and self.playbookConfigs is None:            
                return Response(data={'status': 'failed', 
                                      'errorMsg': 'Must include a playbook name and/or playbookConfigs to modify the playbook or create from blank'}, status=HtmlStatusCodes.error)

            if self.sessionId and len(self.sessionId.split(' ')) > 1:
                return Response(data={'status': 'failed', 
                                      'errorMsg': f'The parameter sessionId cannot have spaces: {self.sessionId}'}, status=HtmlStatusCodes.error)

            if self.playbook:
                # In case user state the full Playbook path and/or included the .yml extension
                matchedParse = search('^(/)?(.*)', self.playbook)
                if matchedParse:
                    self.playbookName = matchedParse.group(2)
                else:
                    self.playbookName = self.playbook
                    
                if '/' in self.playbookName:
                    self.playbookName = self.playbookName.replace('/', '-')
                
                match = search(f'({GlobalVars.playbooks}/)?(.*)(\.yml)?', self.playbook)
                playbook = match.group(2)
                self.playbookPath = f'{GlobalVars.playbooks}/{playbook}'
                if '.yml' not in self.playbookPath:
                    self.playbookPath = f'{self.playbookPath}.yml'
            
                try:
                    # Verify for ymal syntax error
                    readYaml(self.playbookPath)
                except Exception as errMsg:
                    errorMsg = f'The playbook yml file has syntax errors: {self.playbookPath}. ErrorMsg: {str(errMsg)}'
                    SystemLogsAssistant().log(user=user, webPage='pipelines', action=action, msgType='Error',
                                              msg=errorMsg, forDetailLogs=traceback.format_exc(None, errMsg))  
                             
                    return Response(data={'status': 'failed', 
                                        'errorMsg': errorMsg}, status=HtmlStatusCodes.error)
                    
            if self.sessionId is None or self.sessionId == '':
                import random
                self.sessionId = str(random.sample(range(1,10000), 1)[0])
            
            # Commenting this out for now until groups is used correctly
            if self.group != "Default" and groupExists(self.group) is None:
                if 'user 'in request.session:
                    SystemLogsAssistant().log(user=user, webPage='pipelines', action=action, msgType='Error',
                                              msg=f'runPlaybook: No group name: {self.group}', forDetailLogs='')
                                        
                return Response(data={'status': 'failed',
                                      'errorMsg': f'The group {self.group} does not exists. Please create the group first.'},
                                status=HtmlStatusCodes.error)

            # For validatePlaybook
            if self.awsS3 or self.jira:
                checkLoginCredentials = True
            else:
                checkLoginCredentials = False
                
            # If users want to modify something prior to testing.
            # Initialize the keys.
            reconfigData = {'KeystackSystemEnv': {}, 'env': [], 'playbook': {}, 'testcases': [], "createDynamicPlaybook": False}

            if self.playbookConfigs:
                # jsonStrObj = json.dumps(playbookConfigs)
                # reconfigs = json.loads(jsonStrObj)
                reconfigData['playbook'].update(self.playbookConfigs)
                playbookObj = readYaml(self.playbookPath)    
                playbookObj.update(self.playbookConfigs)
                
                result,problems = validatePlaybook(self.playbookName, playbookObj, checkLoginCredentials=checkLoginCredentials)
            
                if result == False:
                    errorMsg = problems
                    print('\nrunPlaybook: validatePlaybook error:', errorMsg)
                    SystemLogsAssistant().log(user=user, webPage='pipelines', action=action, 
                                            msgType='Error', msg=errorMsg, forDetailLogs='')
                    
                    return Response(data={'status': 'failed', 'errorMsg': errorMsg, 'sessionIdPath':None, 'sessionId': None}, 
                                    status=HtmlStatusCodes.error)
                            
            # Create a playbook from blank
            if self.playbook is None and self.playbookConfigs:
                reconfigData['createDynamicPlaybook'] = True
                if self.awsS3:
                    try:
                        'loginCredentialKey' in self.playbookConfigs['globalSettings']
                    except:
                        return Response(data={'status': 'failed',
                                              'errorMsg': 'awsS3 param was set to True, but missing playbook globalSettings.loginCredentialKey setting'}, 
                                              status=HtmlStatusCodes.error)                          
            # Modify playbook
            if self.playbook and self.playbookConfigs:
                reconfigData['createDynamicPlaybook'] = False
                                    
            if self.playlistMods:
                reconfigData['testcases'] = self.playlistMods

            if self.envConfigs:
                reconfigData['env'] = self.envConfigs
                
            # /opt/KeystackTests/Results/PLAYBOOK=pythonSample/09-21-2022-08:53:04:330610_awesomeTest
            resultTimestampFolder = createTestResultTimestampFolder(group=self.group, playbookName=self.playbookName, 
                                                                    sessionId=self.sessionId, debugMode=self.debug)
    
            resultTimestampFolderName = resultTimestampFolder.split('/')[-1]
            sessionTempFile = f'{GlobalVars.restApiModsPath}/{resultTimestampFolderName}'      
            writeToJson(sessionTempFile, reconfigData, mode='w', sortKeys=False, indent=4)
                
            if self.playbook and self.playbookConfigs is None:
                if os.path.exists(self.playbookPath) == False:  
                    return Response(data={'status': 'failed', 'errorMsg': f'Playbook does not exists: {self.playbookPath}'},
                                    status=HtmlStatusCodes.error)
                else:
                    playbookObj = readYaml(self.playbookPath)
                    result,problems = validatePlaybook(self.playbookName, playbookObj, checkLoginCredentials=checkLoginCredentials)
                    if result == False:
                        errorMsg = problems
                        SystemLogsAssistant().log(user=user, webPage='pipelines', action=action, 
                                                msgType='Error', msg=errorMsg, forDetailLogs='')
                        return Response(data={'status': 'failed', 'errorMsg': errorMsg, 
                                              'sessionIdPath':None, 'sessionId': None}, status=HtmlStatusCodes.error)

            try:
                # request.session['mainControllerIp'] was set at login.
                # But if this runPlaybook was called by rest api or ExecRestApi, the
                # request doesn't have session['mainControllerIp']
                # If this was called by rest api, it uses http://ipAddress. It will
                # run on the local controller of the ipAddress. Also, it will include
                # parameter webhook as a way to bypass verifyApiKey
                if remoteControllerIp and remoteControllerIp != mainControllerIp:
                    runOnLocalController = False
                            
                if remoteControllerIp is None or remoteControllerIp == mainControllerIp:
                    runOnLocalController = True
                    
            except:
                runOnLocalController = True
            
            if runOnLocalController == False:
                params = {'remoteController': self.remoteController, 'sessionId': self.sessionId, 'playbook': self.playbookPath,
                          'resultsFolder': resultTimestampFolder, 'group': self.group, 'awsS3': self.awsS3, 'jira': self.jira,
                          'trackResults': self.trackResults, 'debug': self.debug, 'emailResults': self.emailResults,
                          'pauseOnError': self.pauseOnError, 'holdEnvsIfFailed': self.holdEnvsIfFailed, 
                          'includeLoopTestPassedResults': self.includeLoopTestPassedResults, 'abortTestOnFailure': self.abortTestOnFailure}
                
                # Run Keystack on remote controller -> https://<controllerIp:ipPort>    
                return self.execRestApi(user, remoteControllerIp, ipPort, params)
            
            #if self.controller is None or self.controller == request.session['mainControllerIp']:
            if runOnLocalController:
                # Run Keystack on local controller  
                command = f'keystack -playbook {self.playbookPath} -isFromKeystackUI -resultsFolder {resultTimestampFolder} -group {self.group} '
                #command = f'python3.10 /opt/Keystack/keystack.py -playbook {self.playbookPath} -isFromKeystackUI -group {self.group} -resultsFolder {resultTimestampFolder} '
                
                if self.sessionId:
                    command += f' -sessionId {self.sessionId}'
                if self.awsS3:
                    command +=  ' -awsS3'
                if self.jira:
                    command += ' -jira'
                if self.trackResults:
                    command += ' -trackResults'
                if self.debug:
                    command += ' -debug'
                if self.emailResults:
                    command += ' -emailResults'
                if self.pauseOnError:
                    command += ' -pauseOnError'
                if self.holdEnvsIfFailed:
                    command += ' -holdEnvsIfFailed'
                if self.abortTestOnFailure:
                    command += ' -abortTestOnFailure' 
                if self.includeLoopTestPassedResults:
                    command += ' -includeLoopTestPassedResults'
                                                            
                command += ' > /dev/null 2>&1 &'
                
                try:
                    print(f'\nrunPlaybook: {command}')
                    result = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
                    result, err = result.communicate()

                    if err:
                        errMsg = err.decode("utf-8")
                        errMsg = errMsg.replace('\n', '')
                        errorMsg = errMsg
                        return Response(data={'status': 'failed', 'errorMsg': errorMsg}, status=HtmlStatusCodes.error)

                    didTestRunSuccessfully = False
                    timeout = 10
                    for counter in range(0,timeout):
                        # If the test had executed successfully, an overallSummary.json file is created
                        overallSummary = f"{resultTimestampFolder}/overallSummary.json"
                        if os.path.exists(overallSummary) == False:
                            print(f'Waiting for the session overallSummary.json creation: {counter}/{timeout}')
                            sleep(1)
                        else:
                            didTestRunSuccessfully = True
                            break

                    if didTestRunSuccessfully:    
                        statusCode = HtmlStatusCodes.success
                    else:
                        statusCode= HtmlStatusCodes.error        
                        errorMsg = 'Test failed to run'

                    SystemLogsAssistant().log(user=user, webPage='pipelines', action=action, msgType='Success', msg=command, forDetailLogs='')
                                
                except Exception as errMsg:
                    statusCode = HtmlStatusCodes.error
                    errorMsg = f'Test failed to run: {errMsg}'
                    SystemLogsAssistant().log(user=user, webPage='pipelines', action=action, msgType='Error',
                                              msg=f'user:{user}<br>command:{command}<br>error: {errorMsg}',
                                              forDetailLogs=traceback.format_exc(None, errMsg))
                finally:
                    if self.removeJobAfterRunning:
                        from topbar.docs.restApi.pipelineViews import JobSchedulerAssistant
                        
                        # playbook=pythonSample minute=* hour=* day=* month=* dayOfWeek=*
                        removeJobDict = {}
                        for param in self.scheduledJob.split(' '):
                            key   = param.split('=')[0]
                            value = param.split('=')[1]
                            removeJobDict[key] = value

                        JobSchedulerAssistant().removeCronJobs([removeJobDict], user)   
                
        #serializer = RunPlaybookSerializer(data=request.data)
        #return Response(serializer.data, data={'message': message}, status=statusCode)
        return Response(data={'status': 'success', 'errorMsg': None, 'sessionIdPath': resultTimestampFolder, 
                              'sessionId': resultTimestampFolderName, 'testGroup':self.group}, status=statusCode)

    def execRestApi(self, user, controllerIp, ipPort, params):
        """ 
        Execute runPlaybook rest api on the remote controller
        """
        # Get the Access-Key from the remote_<controller_ip>.yml file
        controllerRegistryPath = f'{GlobalVars.controllerRegistryPath}'
        controllerRegistryFile = f'{controllerRegistryPath}/remote_{controllerIp}.yml'
    
        if os.path.exists(controllerRegistryFile):
            data = readYaml(controllerRegistryFile) 
                               
            restObj = ExecRestApi(ip=controllerIp, port=ipPort, https=data['https'],
                                  headers={"Content-Type": "application/json", "Access-Key": data['accessKey']})
 
            response = restObj.post('/api/v1/playbook/run', params=params, silentMode=True,
                                           user=user, webPage=Vars.webpage, action='getAvailableApps')
            del restObj 
            
            if str(response.status_code).startswith('2') == False:
                #  {"sessions": {}, "status": "failed", "errorMsg": "GET Exception error 2/2 retries: HTTPSConnectionPool(host='192.168.28.17', port=88028): Max retries exceeded with url: /api/v1/sessions?view=current&group=Default (Caused by SSLError(SSLError(1, '[SSL: WRONG_VERSION_NUMBER] wrong version number (_ssl.c:997)')))"}
                error = json.loads(response.content.decode('utf-8'))
                errorMsg = error['errorMsg']
                
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='runPlaybook', msgType='Error',
                                        msg=errorMsg, forDetailLogs='')

                return JsonResponse({'status': 'failed', 'errorMsg': errorMsg, 'tableData': ''}, status=HtmlStatusCodes.error)
            else:
                return JsonResponse({'status': 'success', 'errorMsg': None}, status=HtmlStatusCodes.success)            


class GetPlaybookEnvDetails(APIView):
    playbook = openapi.Parameter(name='playbook', description="Name of the Playbook",
                                 required=True, in_=openapi.IN_QUERY, type=openapi.TYPE_STRING)
    stage    = openapi.Parameter(name='stage', description="The stage name",
                                 required=True, in_=openapi.IN_QUERY, type=openapi.TYPE_STRING)
    module   = openapi.Parameter(name='module', description="The module name",
                                 required=True, in_=openapi.IN_QUERY, type=openapi.TYPE_STRING)   
    @swagger_auto_schema(tags=['/api/v1/playbook/env/details'], operation_description="Get detail configs of an Env",
                         manual_parameters=[playbook, stage, module])
    @verifyUserRole()
    def get(self, request):
        """
        Description:
            Return an Env parameters/values of a Playbook.Stage.Module
        
        GET /api/v1/playbook/env/details?playbook=[playbookName]&stage=[stageName]&module=[module]
        
        Replace [playbookName] [stageName] [module]
        
        Parameter:
            playbook:  The playbook name
            stage:     The stage name
            module:    The stage module name

        Examples:
            curl -H "API-Key: iNP29xnXdlnsfOyausD_EQ" -X GET 'http://192.168.28.7:8000/api/v1/playbook/env/details?playbook=loadcoreSample&stage=LoadCoreTest&module=/Modules/LoadCore'
            
            curl -d "playbook=loadcoreSample&stage=LoadCoreTest&module=/Modules/LoadCore" -H "Content-Type: application/x-www-form-urlencoded" -X GET http://192.168.28.7:8000/api/v1/playbook/env/details 
            
            curl -d '{"playbook": "loadcoreSample", "stage": "LoadCoreTest", "module": "/Modules/LoadCore"}' -H "Content-Type: application/json" -X GET http://192.168.28.7:8000/api/v1/playbook/env/details
        """
        playbook = None
        stage = None
        module = None
        envFile = None
        envParams = {}
        errorMsg = None
        statusCode = HtmlStatusCodes.success
        status = 'success'
        user = AccountMgr().getRequestSessionUser(request)
        remoteController = request.data.get('remoteController', None)
        mainControllerIp, remoteControllerIp, ipPort = getMainAndRemoteControllerIp(request, remoteController)
        playbook = ''
        listOfModuleEnvParams = [] 
                
        # /api/v1/playbook/env/details?playbook=<playbook_name>&envXPath=<stageName>.<module>
        if request.GET:
            try:
                playbook = request.GET.get('playbook')
                stage = request.GET.get('stage')
                module = request.GET.get('module')
            except Exception as error:
                errorMsg = f'Expecting parameters playbook, stage, module, but got: {request.GET}'
                return Response(data={'error': errorMsg, 'status': 'failed'}, status=HtmlStatusCodes.error)
            
        # JSON format
        if request.data:
            # <QueryDict: {'sessionId': <session_name>}
            try:
                playbook = request.data['playbook']
                stage = request.data['stage']
                module = request.data['module']
            except Exception as errMsg:
                errorMsg = f'Expecting parameters playbook, stage, module, but got: {request.data}'
                return Response(data={'errorMsg': errorMsg, 'status': 'failed'}, status=HtmlStatusCodes.error)

        if remoteControllerIp and remoteControllerIp != mainControllerIp:
            params = {"playbook": playbook, "stage": stage, "module": module}
            restApi = '/api/v1/playbook/env/details'
            response, errorMsg = executeRestApiOnRemoteController('get', remoteControllerIp, ipPort, restApi, params, 
                                                                  user, webPage=Vars.webpage, action='GetPlaybookEnvDetails')
            if errorMsg:
                status = 'failed'
                statusCode = HtmlStatusCodes.error 
            else:
                # 'playbook': playbook, 'envList': listOfModuleEnvParams,
                playbook = response.json()['playbook']
                listOfModuleEnvParams  = response.json()['envList'] 
    
        else:        
            for param in [playbook, stage, module]:
                if param is None:
                    return Response(data={'status': 'failed', 'errorMsg': f'Must include param {param}'}, status=HtmlStatusCodes.error)
                            
            if '.yml' not in playbook:
                playbook = f'{playbook}.yml'

            # In case the user included the /Module path.  Get just the module name.
            if 'Modules/' not in module:
                module = f'Modules/{module}'
            if module.startswith('/') == False:
                module = f'/{module}'
                            
            playbookFullPath = f'{GlobalVars.playbooks}/{playbook}'
            if os.path.exists(playbookFullPath) == False:
                return Response(data={'status': 'failed', 'errorMsg': f'No playbook found: {playbookFullPath}'}, status=HtmlStatusCodes.error)

            playbookData = readYaml(playbookFullPath)
            listOfModuleEnvParams = []
            for eachModule in playbookData['stages'][stage]['modules']:
                # {'/Modules/LoadCore': {'env': 'loadcoreSample', 'playlist': ['/Modules/LoadCore/Testcases/fullcoreBase.yml'], 'innerLoop': {'allTestcases': 1}, 'rebootAgentsBeforeEachTest': False, 'deleteTestLogsAndResultsOnLoadCore': True, 'waitTimeBetweenTests': 0, 'deleteSession': True, 'deleteSessionOnFailure': True, 'abortOnFailure': False, 'getPdfResultsFile': True, 'getCsvResultsFile': True, 'getCapturesAndLogs': True}}
                
                if module in list(eachModule.keys()):
                    actualModuleSpellingInPlaybook = list(eachModule.keys())[0]
                    
                    if 'env' in list(eachModule[module].keys()):
                        env = eachModule[actualModuleSpellingInPlaybook]['env']
                        if env == 'None':
                            env = None
                            
                        if env:
                            if '.yml' not in env:
                                env = f'{env}.yml'
                            
                            envFile = f'{GlobalVars.envPath}/{env}'
                            
                            if os.path.exists(envFile) == False:
                                status = 'failed'
                                errorMsg = f'The env "{env}" in playbook:{playbook} stage:{stage} module:{module} does not exists in the Env inventory.'
                                return Response(data={'playbook': playbook, 'data': {}, 'errorMsg': errorMsg, 'status': status}, status=HtmlStatusCodes.error)
                            
                            try:
                                envParams = readYaml(envFile)
                                listOfModuleEnvParams.append({'env': env, 'data': envParams})
                                
                            except Exception as errMsg:
                                statusCode = HtmlStatusCodes.error
                                status = 'failed'
                                errorMsg = str(errMsg)
                
        return Response(data={'playbook': playbook, 'envList': listOfModuleEnvParams, 'errorMsg': errorMsg, 'status': status}, status=statusCode)


class GetPlaybookPlaylist(APIView):
    playbook  = openapi.Parameter(name='playbook', description="The Playbook name",
                                  required=True, in_=openapi.IN_QUERY, type=openapi.TYPE_STRING)  
    stage     = openapi.Parameter(name='stage', description="The Playbook Stage",
                                  required=True, in_=openapi.IN_QUERY, type=openapi.TYPE_STRING)  
    module    = openapi.Parameter(name='module', description="The Playbook Stage Module name in which the testcases are located",
                                  required=True, in_=openapi.IN_QUERY, type=openapi.TYPE_STRING)      
    @swagger_auto_schema(tags=['/api/v1/playbook/playlist'], operation_description="Get the playlist of a Playbook Stage/Module",
                         manual_parameters=[playbook, stage, module])
    @verifyUserRole() 
    def get(self, request):
        """
        Description:
           Get playbook playlist
        
        GET /api/v1/playbook/playlist?playbook=<playbook>&stage=<stage>&module=<module>
        
        Parameter:
            playbook: The name of the playbook (without the .yml extension)
            stage:  The stage where the playlist is located
            module: Just the module's name.  The playbook/stage/module where the playlist is located
        
        Examples:
            curl -H "API-Key: iNP29xnXdlnsfOyausD_EQ" -X GET 'http://192.168.28.7:8000/api/v1/playbook/playlist?playbook=loadcoreSample&stage=LoadCoreTest&module=LoadCore'
            
            curl -H "API-Key: iNP29xnXdlnsfOyausD_EQ" -d "playbook=loadcoreSample&stage=LoadCoreTest&module=LoadCore" -H "Content-Type: application/x-www-form-urlencoded" -X GET http://192.168.28.7:8000/api/v1/playbook/playlist 
            
            curl -H "API-Key: iNP29xnXdlnsfOyausD_EQ" -d '{"playbook": "loadcoreSample", "stage": "LoadCoreTest", "module": "LoadCore"}' -H "Content-Type: application/json" -X GET http://192.168.28.7:8000/api/v1/playbook/playlist
                        
        Return:
            the Playbook/Stage/Module playlist
        """     
        statusCode = HtmlStatusCodes.success
        modulePlaylist = []
        errorMsg = None
        user = AccountMgr().getRequestSessionUser(request)
        remoteController = request.data.get('remoteController', None)
        mainControllerIp, remoteControllerIp, ipPort = getMainAndRemoteControllerIp(request, remoteController)
        
        if request.GET:
            try:
                playbook = request.GET.get('playbook')
                stage = request.GET.get('stage')
                module = request.GET.get('module')
            except Exception as error:
                errorMsg = f'Expecting parameters apiKey, playbook, stage and module, but got: {request.GET}'
                return Response(data={'errorMsg': errorMsg, 'status': 'failed'}, status=HtmlStatusCodes.error)
            
        # JSON format
        if request.data:
            # <QueryDict: {'testcasePath': </Modules/LoadCore>}
            try:
                playbook  = request.data['playbook']
                stage  = request.data['stage']
                module = request.data['module']
            except Exception as errMsg:
                errorMsg = f'Expecting parameters apiKey, playbook, stage and module, but got: {request.data}'
                return Response(data={'errorMsg': errorMsg, 'status': 'failed'}, status=HtmlStatusCodes.error)

        if remoteControllerIp and remoteControllerIp != mainControllerIp:
            params = {"playbook": playbook, "stage": stage, "module": module}
            restApi = '/api/v1/playbook/playlist'
            response, errorMsg = executeRestApiOnRemoteController('get', remoteControllerIp, ipPort, restApi, params, 
                                                                  user, webPage=Vars.webpage, action='GetPlaybookPlaylist')
            if errorMsg:
                status = 'failed'
                statusCode = HtmlStatusCodes.error 
            else:
                modulePlaylist = response.json()['playlist'] 
                      
        else:            
            # In case the user included the /Module path.  Get just the module name.
            if 'Modules/' not in module:
                module = f'Modules/{module}'
            if module.startswith('/') == False:
                module = f'/{module}'
            
            if '.yml' not in playbook:
                playbook = f'{playbook}.yml'

            playbookPath = f'{GlobalVars.playbooks}/{playbook}'
            if os.path.exists(playbookPath) == False:
                errorMsg = f'No such playbook exists: {playbookPath}'
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage , action='getPlaybookPlaylist', 
                                        msgType='Error', msg='')
                return Response(data={'errorMsg': errorMsg, 'status': 'failed'}, status=HtmlStatusCodes.error)

            try:
                playbookData = readYaml(playbookPath)
                stageAndModuleExists = False
                
                if stage not in playbookData['stages'].keys():
                    errorMsg = f"No such stage in playbook: {stage}"
                    SystemLogsAssistant().log(user=user, webPage=Vars.webpage , action='getPlaybookPlaylist', 
                                            msgType='Error', msg=errorMsg)
                    return Response(data={'errorMsg': errorMsg, 'status': 'failed'}, status=HtmlStatusCodes.error)

                # Each Stage could have multiple same modules with different env
                for eachModule in playbookData['stages'][stage]['modules']:                      
                    if module in list(eachModule.keys()):
                        stageAndModuleExists = True
                        actualModuleSpellingInPlaybook = list(eachModule.keys())[0]
                        env = eachModule[actualModuleSpellingInPlaybook].get('env', None)
                            
                        if 'playlist' in list(eachModule[module].keys()):
                            playlist = eachModule[actualModuleSpellingInPlaybook]['playlist']
                            modulePlaylist.append({'module': module, 'env': env, 'playlist': playlist})
                        else:
                            errorMsg = f"No playlist defined in playbook:{playbook} stage:{stage}: {module}"
                            SystemLogsAssistant().log(user=user, webPage=Vars.webpage , action='getPlaybookPlaylist', 
                                                    msgType='Error', msg=errorMsg)
                            return Response(data={'errorMsg': errorMsg, 'status': 'failed'}, status=HtmlStatusCodes.error)                          

                if stageAndModuleExists == False:
                    errorMsg = f"No such stage:module in playbook:{playbook} stage:{stage}: module:{module}"
                    SystemLogsAssistant().log(user=user, webPage=Vars.webpage , action='getPlaybookPlaylist', 
                                                msgType='Error', msg=errorMsg)
                    return Response(data={'errorMsg': errorMsg, 'status': 'failed'}, status=HtmlStatusCodes.error)    
                                        
            except Exception as errMsg:
                errorMsg = errMsg
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage , action='getPlaybookPlaylist', 
                                        msgType='Error', msg=traceback.format_exc(None, errMsg))
                return Response(data={'errorMsg': errorMsg, 'status': 'failed'}, status=HtmlStatusCodes.error)

        return Response(data={'playlist': modulePlaylist, 'status': 'success', 'errorMsg': errorMsg}, status=statusCode)


class GetPlaybooks(APIView):
    playbookGroup  = openapi.Parameter(name='playbookGroup', description="The playbook group",
                                       required=True, in_=openapi.IN_QUERY, type=openapi.TYPE_STRING)  
  
    @swagger_auto_schema(tags=['/api/v1/playbook'], operation_description="Get playbooks from playbook group",
                         manual_parameters=[playbookGroup])
    @verifyUserRole()
    def post(self, request, data=None):
        """
        Description:
           Get playbooks table data from a playbook group for the playbook page
        
        POST /api/v1/playbook?playbookGroup=<playbookGroup>
        
        Parameter:
            playbookGroup: The name of the playbook group
        
        Examples:
            curl -H "API-Key: iNP29xnXdlnsfOyausD_EQ" -X POST 'http://192.168.28.7:8000/api/v1/playbook?playbookGroup=<group>
            
            curl -H "API-Key: iNP29xnXdlnsfOyausD_EQ" -d "playbookGroup=loadcoreSample" -H "Content-Type: application/x-www-form-urlencoded" -X POST http://192.168.28.7:8000/api/v1/playbook
            
            curl -H "API-Key: iNP29xnXdlnsfOyausD_EQ" -d '{"playbookGroup": "loadcoreSample"}' -H "Content-Type: application/json" -X POST http://192.168.28.7:8000/api/v1/playbook
                        
        Return:
            None
        """     
        statusCode = HtmlStatusCodes.success
        status = 'success'
        errorMsg = None
        user = AccountMgr().getRequestSessionUser(request)
        remoteController = request.data.get('remoteController', None)
        mainControllerIp, remoteControllerIp, ipPort = getMainAndRemoteControllerIp(request, remoteController)
        tableData: str = ''
        
        if request.GET:
            try:
                playbookGroup = request.GET.get('playbookGroup')
            except Exception as error:
                errorMsg = f'Expecting parameters apiKey, playbook, stage and module, but got: {request.GET}'
                return Response(data={'errorMsg': errorMsg, 'status': 'failed'}, status=HtmlStatusCodes.error)
            
        # JSON format
        if request.data:
            # <QueryDict: {'testcasePath': </Modules/LoadCore>}
            try:
                # ['/opt/KeystackTests/Playbooks/qa/qa1.yml']
                playbookGroup  = request.data['playbookGroup']
            except Exception as errMsg:
                errorMsg = f'Expecting parameters apiKey, playbook, stage and module, but got: {request.data}'
                return Response(data={'errorMsg': errorMsg, 'status': 'failed'}, status=HtmlStatusCodes.error)

        """
        Construct each table <tr> with multiple modules in the <td>
        
        <tr>
            <td>1</td>
            <td>nightly test</td>
            <td>LoadCore<br>AirMosaic</td>
            <td>env.yml<br>rack1.yml</td>
            <td>
                <div class="dropdown">
                    <div class="dropdown-toggle" type="text" data-toggle="dropdown" id="drop1">
                        View Playlist
                        <ul class="dropdown-menu mt-0" aria-labelledby="drop1">
                            <li class="dropdown-item">/Testcases/01_testcase.yml</li>
                            <li class="dropdown-item">/Testcases/02_testcase.yml</li>
                            <li class="dropdown-item">/Testcases/03_testcase.yml</li>
                        </ul>
                    </div>
                </div>
                <div class="dropdown">
                    <div class="dropdown-toggle" type="text" data-toggle="dropdown" id="drop2">
                        View Playlist
                        <ul class="dropdown-menu mt-0" aria-labelledby="drop2">
                            <li class="dropdown-item">/Testcases/01_20UE_NGRAN.yml</li>
                            <li class="dropdown-item">/Testcases/02_80UE_NGRAN.yml</li>
                            <li class="dropdown-item">/Testcases/03_80UE_NGRAN.yml</li>
                        </ul>   
                    </div>
                </div>                    
            </td>
            <td>Yes</td>
            <td>No</td>
        </tr>
        """

        if remoteControllerIp and remoteControllerIp != mainControllerIp:
            params = {"playbookGroup": playbookGroup}
            restApi = '/api/v1/playbook/get'
            response, errorMsg = executeRestApiOnRemoteController('post', remoteControllerIp, ipPort, restApi, params, 
                                                                  user, webPage=Vars.webpage, action='GetPlaybooks')
            if errorMsg:
                status = 'failed'
                statusCode = HtmlStatusCodes.error 
            else:
                tableData = response.json()['tableData']
                       
        else:
            try:
                playbookPath = GlobalVars.playbooks

                for rootPath,dirs,files in os.walk(playbookPath):      
                    if bool(search(f'^{GlobalVars.keystackTestRootPath}/{playbookGroup}$', rootPath)) and files:
                        # Just file names. Not path included.
                        for playbookYmlFile in files:
                            if playbookYmlFile.endswith('.yml'):
                                playbookName = playbookYmlFile.split('.')[0]
                                filename = playbookYmlFile.split('/')[-1]
                                
                                match = search(f'.*Playbooks/(.*)', rootPath)
                                if match:
                                    playbookSubFolders = match.group(1)
                                else:
                                    playbookSubFolders = ''

                                tableData += '<tr>'
                                # Delete
                                tableData += f'<td><input type="checkbox" name="playbookCheckboxes" value="{rootPath}/{playbookYmlFile}"/></td>'

                                tableData += f'<td><button class="btn btn-sm btn-outline-primary" value="{rootPath}/{playbookYmlFile}" onclick="getFileContents(this)" data-bs-toggle="modal" data-bs-target="#viewEditPlaybookModal">View / Edit</button></td>'
                                            
                                tableData += f'<td style="text-align:left">{playbookName}</td>'
                                tableData += '</tr>'
                    
            except Exception as errMsg:
                errorMsg= str(errMsg)
                status = 'failed'
                statusCode = HtmlStatusCodes.error
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage , action='GetPlaybooks', 
                                        msgType='Error', msg=errorMsg, forDetailLogs=traceback.format_exc(None, errMsg))

        return Response(data={'tableData': tableData, 'status': status, 'errorMsg': errorMsg}, status=statusCode)


class CreatePlaybook(APIView):
    playbook  = openapi.Parameter(name='playbook', description="The Playbook name",
                                  required=True, in_=openapi.IN_QUERY, type=openapi.TYPE_STRING)  
    playbookGroup  = openapi.Parameter(name='playbookGroup', description="The Playbook group",
                                       required=True, in_=openapi.IN_QUERY, type=openapi.TYPE_STRING)  
    jsonObject     = openapi.Parameter(name='jsonObject', description="Playbook contets",
                                       required=True, in_=openapi.IN_QUERY, type=openapi.TYPE_STRING)    
    @swagger_auto_schema(tags=['/api/v1/playbook/create'], operation_description="Create a playbook",
                         manual_parameters=[playbook, playbookGroup, jsonObject])

    @verifyUserRole(webPage=Vars.webpage, action='CreatePlaybook', exclude=['engineer'])
    def post(self, request, data=None):
        """
        Description:
           Create a new playbook
        
        POST /api/v1/playbook/create?playbook=<playbook>&playbookGroup=<playbookGroup>&jsonObject=<contents>
        
        Parameter:
            playbook: The name of the playbook (without the .yml extension)
        
        Examples:
            curl -H "API-Key: iNP29xnXdlnsfOyausD_EQ" -X POST 'http://192.168.28.7:8000/api/v1/playbook/create?playbook
            
            curl -H "API-Key: iNP29xnXdlnsfOyausD_EQ" -d "newPlaybook=loadcoreSample" -H "Content-Type: application/x-www-form-urlencoded" -X POST http://192.168.28.7:8000/api/v1/playbook/create
            
            curl -H "API-Key: iNP29xnXdlnsfOyausD_EQ" -d '{"newPlaybook": "loadcoreSample", "playbookGroup": "qa", "jsonObject": object}' -H "Content-Type: application/json" -X POST http://192.168.28.7:8000/api/v1/playbook/create

            curl -H "API-Key: uJNmx1WuSvruOgLUehMJlw" -d '{"newPlaybook": "loadcoreSample", "playbookGroup": "qa", "textArea": {"howdy": "doody"}}' -H "Content-Type: application/json" -X POST http://192.168.28.7:8000/api/v1/playbook/create                        
        Return:
            None
        """     
        statusCode = HtmlStatusCodes.success
        status = 'success'
        errorMsg = None
        user = AccountMgr().getRequestSessionUser(request)
        remoteController = request.data.get('remoteController', None)
        mainControllerIp, remoteControllerIp, ipPort = getMainAndRemoteControllerIp(request, remoteController)
        playbookExists = True
        
        if request.GET:
            try:
                playbook      = request.GET.get('newPlaybook')
                playbookGroup = request.GET.get('playbookGroup')
                textArea      = request.GET.get('textArea')
            except Exception as errMsg:
                errorMsg = f'Expecting parameters newPlaybook, playbookGroup, textArea, but got: {request.GET}'
                return Response(data={'errorMsg': errorMsg, 'status': 'failed'}, status=HtmlStatusCodes.error)
            
        # JSON format
        if request.data:
            # <QueryDict: {'testcasePath': </Modules/LoadCore>}
            try:
                # ['/opt/KeystackTests/Playbooks/qa/qa1.yml']
                #  {textArea: textArea, newPlaybook: newPlaybook, playbookGroup:playbookGroup})
                playbook      = request.data['newPlaybook']
                playbookGroup = request.data['playbookGroup']
                textArea      = request.data['textArea']
            except Exception as errMsg:
                errorMsg = f'Expecting parameters newPlaybook, playbookGroup, textArea, but got: {request.data}'
                return Response(data={'errorMsg': errorMsg, 'status': 'failed'}, status=HtmlStatusCodes.error)

        if remoteControllerIp and remoteControllerIp != mainControllerIp:
            params = {"newPlaybook": playbook, "playbookGroup": playbookGroup, "textArea": textArea}
            restApi = '/api/v1/playbook/create'
            response, errorMsg = executeRestApiOnRemoteController('post', remoteControllerIp, ipPort, restApi, params, 
                                                                  user, webPage=Vars.webpage, action='CreatePlaybook')
            if errorMsg:
                status = 'failed'
                statusCode = HtmlStatusCodes.error
                   
        else:        
            try:
                if '.yml' not in playbook:
                    playbook = f'{playbook}.yml'

                if playbookGroup:
                    if playbookGroup[0] == '/':
                        playbookGroup = f'/{playbookGroup[1:]}'
                    
                    playbookGroupPath = f'{GlobalVars.playbooks}/{playbookGroup}'
                    if os.path.exists(playbookGroupPath) == False:    
                        mkdir2(playbookGroupPath)
                    
                    fullPathFile = f'{GlobalVars.playbooks}/{playbookGroup}/{playbook}'
                    if os.path.exists(fullPathFile) == False:
                        playbookExists = False
                        writeToFile(fullPathFile, textArea, mode='w', printToStdout=False)
                        
                else:
                    playbookGroup = None
                    fullPathFile = f'{GlobalVars.playbooks}/{playbook}'  
                    if os.path.exists(fullPathFile) == False:
                        playbookExists = False  
                        writeToFile(fullPathFile, textArea, mode='w', printToStdout=False)
                    
                try:
                    # Verify for YAML synatx error
                    readYaml(fullPathFile)
                    SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='VerifyCreatePlaybook', 
                                              msgType='Info',
                                              msg=f'Playbook:{playbook} Group:{playbookGroup}', forDetailLogs='') 
                except Exception as errMsg:
                    statusCode = HtmlStatusCodes.error
                    status = 'failed'
                    errorMsg = f"Error: YAML syntax error."
                    SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='CreatePlaybook', 
                                              msgType='Error',
                                              msg=errorMsg, forDetailLogs='') 
                
            except Exception as errMsg:
                statusCode = HtmlStatusCodes.error
                status = "failed"
                errorMsg = str(errMsg)
                SystemLogsAssistant().log(user=user, webPage='playbooks', action='CreatePlaybook', msgType='Error',
                                          msg=errMsg, forDetailLogs=traceback.format_exc(None, errMsg))

            if playbookExists:
                status = 'failed'
                statusCode = HtmlStatusCodes.error
                errorMsg = f'Playbook already exists: {playbook}'
            
        return Response(data={'status': status, 'errorMsg': errorMsg}, status=statusCode)
    
    
class DeletePlaybooks(APIView):
    playbook  = openapi.Parameter(name='playbook', description="The Playbook name",
                                  required=True, in_=openapi.IN_QUERY, type=openapi.TYPE_STRING)  
  
    @swagger_auto_schema(tags=['/api/v1/playbook/delete'], operation_description="Delete a list of playbooks",
                         manual_parameters=[playbook])
    @verifyUserRole(webPage=Vars.webpage, action='DeletePlaybook', exclude=['engineer'])
    def post(self, request, data=None):
        """
        Description:
           Delete one or more playbooks
        
        POST /api/v1/playbook/delete?playbook=<playbook>
        
        Parameter:
            playbook: The name of the playbook (without the .yml extension)
        
        Examples:
            curl -H "API-Key: iNP29xnXdlnsfOyausD_EQ" -X Delete 'http://192.168.28.7:8000/api/v1/playbook/delete?playbook
            
            curl -H "API-Key: iNP29xnXdlnsfOyausD_EQ" -d "playbook=loadcoreSample&stage=LoadCoreTest&module=LoadCore" -H "Content-Type: application/x-www-form-urlencoded" -X DELETE http://192.168.28.7:8000/api/v1/playbook/delete
            
            curl -H "API-Key: iNP29xnXdlnsfOyausD_EQ" -d '{"playbook": "loadcoreSample"}' -H "Content-Type: application/json" -X POST http://192.168.28.7:8000/api/v1/playbook/delete
                        
        Return:
            None
        """     
        statusCode = HtmlStatusCodes.success
        status = 'success'
        errorMsg = None
        user = AccountMgr().getRequestSessionUser(request)
        remoteController = request.data.get('remoteController', None)
        mainControllerIp, remoteControllerIp, ipPort = getMainAndRemoteControllerIp(request, remoteController)
        
        if request.GET:
            try:
                playbooks = request.GET.get('deletePlaybooks')
            except Exception as error:
                errorMsg = f'Expecting parameters deletePlaybooks, but got: {request.GET}'
                return Response(data={'errorMsg': errorMsg, 'status': 'failed'}, status=HtmlStatusCodes.error)
            
        # JSON format
        if request.data:
            # <QueryDict: {'testcasePath': </Modules/LoadCore>}
            try:
                # ['/opt/KeystackTests/Playbooks/qa/qa1.yml']
                playbooks  = request.data['deletePlaybooks']
            except Exception as errMsg:
                errorMsg = f'Expecting parameters deletePlaybooks, but got: {request.data}'
                return Response(data={'errorMsg': errorMsg, 'status': 'failed'}, status=HtmlStatusCodes.error)

        if remoteControllerIp and remoteControllerIp != mainControllerIp:
            params = {"deletePlaybooks": playbooks}
            restApi = '/api/v1/playbook/delete'
            response, errorMsg = executeRestApiOnRemoteController('post', remoteControllerIp, ipPort, restApi, params, 
                                                                  user, webPage=Vars.webpage, action='DeletePlaybooks')
            if errorMsg:
                status = 'failed'
                statusCode = HtmlStatusCodes.error 
                   
        else:
            try:
                for playbook in playbooks:
                    os.remove(playbook)
                    SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='DeletePlaybooks', 
                                              msgType='Info', msg=playbooks)
            except Exception as errMsg:
                errorMsg= str(errMsg)
                status = 'failed'
                statusCode = HtmlStatusCodes.error
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage , action='DeletePlaybooks', 
                                        msgType='Error', msg=traceback.format_exc(None, errMsg))

        return Response(data={'status': status, 'errorMsg': errorMsg}, status=statusCode)

    
class IsExists(APIView):
    playbook  = openapi.Parameter(name='playbook', description="The playbook name",
                                  required=True, in_=openapi.IN_QUERY, type=openapi.TYPE_STRING)  
  
    @swagger_auto_schema(tags=['/api/v1/playbook/isExists'], operation_description="Verify if playbook exists",
                         manual_parameters=[playbook])
    @verifyUserRole() 
    def post(self, request, data=None):
        """
        Description:
           Is playbook exists
        
        POST /api/v1/playbook/isExists?playbook=<playbook>
        
        Parameter:
            playbook: Playbook name
        
        Examples:
            curl -H "API-Key: iNP29xnXdlnsfOyausD_EQ" -X POST 'http://192.168.28.7:8000/api/v1/playbook/isExists?playbook=<playbook>
            
            curl -H "API-Key: iNP29xnXdlnsfOyausD_EQ" -d "playbook=loadcoreSample&stage=LoadCoreTest&module=LoadCore" -H "Content-Type: application/x-www-form-urlencoded" -X POST http://192.168.28.7:8000/api/v1/playbook/isExists
            
            curl -H "API-Key: iNP29xnXdlnsfOyausD_EQ" -d '{"playbook": "loadcoreSample"}' -H "Content-Type: application/json" -X POST http://192.168.28.7:8000/api/v1/playbook/isExists
                        
        Return:
            None
        """     
        statusCode = HtmlStatusCodes.success
        status = 'success'
        error = None
        isExists = True
        user = AccountMgr().getRequestSessionUser(request)
        remoteController = request.data.get('remoteController', None)
        mainControllerIp, remoteControllerIp, ipPort = getMainAndRemoteControllerIp(request, remoteController)
        isExists = False
        
        if request.GET:
            try:
                playbook = request.GET.get('playbook')
            except Exception as error:
                errorMsg = f'Expecting parameters playbook, but got: {request.GET}'
                return Response(data={'errorMsg': errorMsg, 'status': 'failed'}, status=HtmlStatusCodes.error)
        
        # JSON format
        if request.data:
            # <QueryDict: {'testcasePath': </Modules/LoadCore>}
            try:
                # ['/opt/KeystackTests/Playbooks/qa/qa1.yml']
                playbook  = request.data['playbook']
            except Exception as errMsg:
                errorMsg = f'Expecting parameters playbook, but got: {request.data}'
                return Response(data={'errorMsg': errorMsg, 'status': 'failed'}, status=HtmlStatusCodes.error)

        if remoteControllerIp and remoteControllerIp != mainControllerIp:
            params = {"playbook": playbook}
            restApi = '/api/v1/playbook/isExists'
            response, errorMsg = executeRestApiOnRemoteController('post', remoteControllerIp, ipPort, restApi, params, 
                                                                  user, webPage=Vars.webpage, action='IsPlaybookExists')
            if errorMsg:
                status = 'failed'
                statusCode = HtmlStatusCodes.error
            else:
                isExists = response.json()['isExists'] 
                   
        else:            
            try:
                isExists = DB.name.isDocumentExists(collectionName=Vars.webpage, key='playbook', value=f'^{playbook}$', regex=True)        
                status = HtmlStatusCodes.success

            except Exception as errMsg:
                errorMsg = str(errMsg)
                status = 'failed'
                statusCode = HtmlStatusCodes.error
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage , action='isPlaybookExists', 
                                          msgType='Error', msg=errorMsg)

        return Response(data={'exists': isExists, 'status': status, 'errorMsg': errorMsg}, status=statusCode)
    

class PlaybookTemplate(APIView):
    swagger_schema = None
    
    @verifyUserRole() 
    def post(self, request, data=None):
        """
        Description:
           Get playbook template for creating new playbook
        
        POST /api/v1/playbook/template
        
        Parameter:
            None
        
        Examples:
            curl -H "API-Key: iNP29xnXdlnsfOyausD_EQ" -X POST 'http://192.168.28.7:8000/api/v1/playbook/template
            
            curl -H "API-Key: iNP29xnXdlnsfOyausD_EQ" -H "Content-Type: application/x-www-form-urlencoded" -X POST http://192.168.28.7:8000/api/v1/playbook/template
            
            curl -H "API-Key: iNP29xnXdlnsfOyausD_EQ" -H "Content-Type: application/json" -X POST http://192.168.28.7:8000/api/v1/playbook/template
                        
        Return:
            None
        """     
        statusCode = HtmlStatusCodes.success
        status = 'success'
        errorMsg = None
        user = AccountMgr().getRequestSessionUser(request)
        remoteController = request.data.get('remoteController', None)
        mainControllerIp, remoteControllerIp, ipPort = getMainAndRemoteControllerIp(request, remoteController)

        if remoteControllerIp and remoteControllerIp != mainControllerIp:
            params = {}
            restApi = '/api/v1/playbook/template'
            response, errorMsg = executeRestApiOnRemoteController('post', remoteControllerIp, ipPort, restApi, params, 
                                                                  user, webPage=Vars.webpage, action='PlaybookTemplate')
            if errorMsg:
                status = 'failed'
                statusCode = HtmlStatusCodes.error 
            else:
                playbookTemplate = response.json()['playbookTemplate']
                       
        else:                
            playbookTemplate = """# Playbook template
---
globalSettings:
    abortOnFailure: False
    abortStageFailure: True

stages:
    Test:
        enable: True
        modules:
        - /Modules/Demo:
            enable: True
            #env: None
            playlist:
                - /Modules/Demo/Samples/Bringups/bringupDut1.yml
        """

        return Response(data={'playbookTemplate': playbookTemplate, 'status': status, 'errorMsg': errorMsg}, status=statusCode)


class PlaybookGroups(APIView):
    swagger_schema = None
    
    @verifyUserRole() 
    def post(self, request, data=None):
        """
        Description:
           Get playbook groups
        
        POST /api/v1/playbook/groups
        
        Parameter:
            None
        
        Examples:
            curl -H "API-Key: iNP29xnXdlnsfOyausD_EQ" -X POST 'http://192.168.28.7:8000/api/v1/playbook/groups
            
            curl -H "API-Key: iNP29xnXdlnsfOyausD_EQ" -H "Content-Type: application/x-www-form-urlencoded" -X POST http://192.168.28.7:8000/api/v1/playbook/groups
            
            curl -H "API-Key: iNP29xnXdlnsfOyausD_EQ" -H "Content-Type: application/json" -X POST http://192.168.28.7:8000/api/v1/playbook/groups
                        
        Return:
            playbook groups in hmtl
        """     
        statusCode = HtmlStatusCodes.success
        status = 'success'
        errorMsg= None
        user = AccountMgr().getRequestSessionUser(request)
        remoteController = request.data.get('remoteController', None)
        mainControllerIp, remoteControllerIp, ipPort = getMainAndRemoteControllerIp(request, remoteController)
        htmlPlaybookGroups = ''

        if remoteControllerIp and remoteControllerIp != mainControllerIp:
            params = {}
            restApi = '/api/v1/playbook/groups'
            response, errorMsg = executeRestApiOnRemoteController('post', remoteControllerIp, ipPort, restApi, params, 
                                                                  user, webPage=Vars.webpage, action='PlaybookGroups')
            if errorMsg:
                status = 'failed'
                statusCode = HtmlStatusCodes.error 
            else:
                htmlPlaybookGroups = response.json()['playbookGroups']
                       
        else:        
            try:
                # Get Playbook groups
                playbookPath = f'{GlobalVars.keystackTestRootPath}/Playbooks'
                playbookGroups = []
                for root,dirs,files in os.walk(playbookPath):
                    playbookGroup = root.split(GlobalVars.keystackTestRootPath)[1]
                    playbookGroups.append(playbookGroup[1:])
                
                # Tell Playbook the group. Playbook renders html and JS will get all playbooks from the specified group
                htmlPlaybookGroups += '<p class="pl-2 pt-2 textBlack">Select Playbook Group</p><br>'
                for group in playbookGroups:
                    htmlPlaybookGroups += f'<a class="collapse-item pl-3" href="/playbooks?group={group}"><i class="fa-regular fa-folder pr-3"></i>{group}</a>'

            except Exception as errMsg:
                errorMsg = str(errMsg)
                status = 'failed'
                statusCode = HtmlStatusCodes.error
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage , action='getPlaybookGroups', 
                                        msgType='Error', msg=errorMsg)

        return Response(data={'playbookGroups':htmlPlaybookGroups, 'status': status, 'errorMsg': errorMsg}, status=statusCode)
    

class GetPlaybookNames(APIView):
    swagger_schema = None
    
    @verifyUserRole() 
    def post(self, request, data=None):
        """
        Description:
           For sessionMgmt page.
           Get playbook names dropdown that includes the group
           
            [('ixnetwork.yml', '/opt/KeystackTests/Playbooks/ixnetwork.yml'),
             ('/qa/qa1.yml', '/opt/KeystackTests/Playbooks/qa/qa1.yml')
            ]
        
        POST /api/v1/playbook/names
        
        Parameter:
            None
        
        Examples:
            curl -H "API-Key: iNP29xnXdlnsfOyausD_EQ" -X GET 'http://192.168.28.7:8000/api/v1/playbook/names
            
            curl -H "API-Key: iNP29xnXdlnsfOyausD_EQ" -H "Content-Type: application/x-www-form-urlencoded" -X GET http://192.168.28.7:8000/api/v1/playbook/names
            
            curl -H "API-Key: iNP29xnXdlnsfOyausD_EQ" -H "Content-Type: application/json" -X GET http://192.168.28.7:8000/api/v1/playbook/names
                        
        Return:
            playbook groups in hmtl
        """
        from baseLibs import getPlaybookNames

        user = AccountMgr().getRequestSessionUser(request)
        remoteController = request.data.get('remoteController', None)
        mainControllerIp, remoteControllerIp, ipPort = getMainAndRemoteControllerIp(request, remoteController)
        statusCode = HtmlStatusCodes.success
        status = 'success'
        errorMsg = None
        playbookNames = ''
        
        if remoteControllerIp and remoteControllerIp != mainControllerIp:
            params = {}
            restApi = '/api/v1/playbook/names'
            response, errorMsg = executeRestApiOnRemoteController('post', remoteControllerIp, ipPort, restApi, params, 
                                                                  user, webPage=Vars.webpage, action='GetPlaybookNames')
            if errorMsg:
                status = 'failed'
                statusCode = HtmlStatusCodes.error 
            else:
                playbookNames = response.json()['playbookNames']
                       
        else:   
            try:
                for playbookPath in getPlaybookNames():
                    # ('/qa/qa1.yml', '/opt/KeystackTests/Playbooks/qa/qa1.yml')
                    playbook = playbookPath[0].split('.')[0]
                    if playbook[0] == '/':
                        playbook = playbook[1:]

                    playbookNames += f'<li class="dropdown-item" id="{playbook}">{playbook}</li>'
                    
            except Exception as errMsg:
                errorMsg = str(errMsg)
                status = 'failed'
                statusCode = HtmlStatusCodes.error
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage , action='GetPlaybookNames', 
                                          msgType='Error', msg=errorMsg)

        return Response(data={'playbookNames':playbookNames, 'status': status, 'errorMsg': errorMsg}, status=statusCode)
    
    