import os, sys, subprocess, json
from glob import glob
from time import sleep

# /Keystack/KeystackUI/sidebar/sessionMgmt
currentDir = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, currentDir.replace('/KeystackUI/restApi', ''))

from keystackUtilities import convertStringToDict, getDeepDictKeys, readJson, readYaml, writeToJson, convertStrToBoolean
from systemLogging import SystemLogsAssistant
from topbar.settings.accountMgmt.verifyLogin import verifyUserRole
from topbar.settings.accountMgmt.accountMgr import AccountMgr
from topbar.docs.restApi.controllers import getMainAndRemoteControllerIp, executeRestApiOnRemoteController
from globalVars import GlobalVars, HtmlStatusCodes

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
    webpage = 'modules'
       

class GetTestcaseDetails(APIView):
    testcasePath = openapi.Parameter(name='testcasePath', description="The testcase path beginning with /Modules",
                                     required=True, in_=openapi.IN_QUERY, type=openapi.TYPE_STRING)  
    
    @swagger_auto_schema(tags=['/api/v1/testcase/details'], operation_description="Get a testcase details from a playbook playlist",
                         manual_parameters=[testcasePath])
    @verifyUserRole() 
    def get(self, request):
        """
        Description:
           Get testcase details
        
        GET /api/v1/testcase/details?testcasePath=<testcasePath>
        
        Replace <testcasePath>
        
        Parameter:
            testcasePath: The testcase path beginning with /Modules/<moduleName>/
        
        Examples:
            curl -H "API-Key: iNP29xnXdlnsfOyausD_EQ" -X GET 'http://192.168.28.7:8000/api/v1/testcase/details?testcasePath=/Modules/LoadCore/Testcases/fullcoreBase.yml'
            
            curl -d "testcasePath=/Modules/LoadCore/Testcases/fullcoreBase.yml" -H "Content-Type: application/x-www-form-urlencoded" -X GET http://192.168.28.7:8000/api/v1/testcase/details
            
            curl -d '{"testcasePath": "/Modules/LoadCore/Testcases/fullcoreBase.yml"}' -H "Content-Type: application/json" -X GET http://192.168.28.7:8000/api/v1/testcase/details
                        
        Return:
            testcase details
        """
        remoteController = request.data.get('remoteController', None)
        mainControllerIp, remoteControllerIp, ipPort = getMainAndRemoteControllerIp(request, remoteController)
        user = AccountMgr().getRequestSessionUser(request)
        statusCode = HtmlStatusCodes.success
        testcaseData = {}
        testcasePath = None # User input
        errorMsg = None
        status = 'success'

        # /api/v1/playbook/testcase?testcasePath=/Modules/LoadCore/Testcases/fullcoreBase.yml
        if request.GET:
            try:
                testcasePath= request.GET.get('testcasePath')
            except Exception as error:
                errorMsg = f'Expecting parameter testcasePath, but got: {request.GET}'
                statusCode = HtmlStatusCodes.error
                return Response(data={'errorMsg': errorMsg, 'status': 'failed'}, status=statusCode)
            
        # JSON format
        if request.data:
            # <QueryDict: {'testcasePath': </Modules/LoadCore>}
            try:
                testcasePath = request.data['testcasePath']
            except Exception as errMsg:
                errorMsg = f'Expecting parameter testcasePath, but got: {request.data}'
                statusCode = HtmlStatusCodes.error
                return Response(data={'errorMsg': errorMsg, 'status': 'failed'}, status=statusCode)

        if remoteControllerIp and remoteControllerIp != mainControllerIp:
            params = {'testcasePath':testcasePath}
            restApi = '/api/v1/results/nestedFolderFiles'
            response, errorMsg = executeRestApiOnRemoteController('gett', remoteControllerIp, ipPort, restApi, params, 
                                                                  user, webPage=Vars.webpage, action='GetTestcaseDetails')
            if errorMsg:
                return Response({'status': 'failed', 'errorMsg': errorMsg}, status=HtmlStatusCodes.error)
            else:
                testcasePath = response.json()['testcase']
                testcaseData = response.json()['data']
  
        else: 
            if testcasePath is None:
                return Response(data={'errorMsg': f'Must include the parameter testcasePath', 'status': 'failed'}, status=HtmlStatusCodes.error)
                    
            if '.yml' not in testcasePath:
                testcasePath = f'{testcasePath}.yml'
            
            testcasePath = testcasePath.split(f'{GlobalVars.keystackTestRootPath}')[-1]  
        
            testcaseFullPath = f'{GlobalVars.keystackTestRootPath}/{testcasePath}'
            if os.path.exists(testcaseFullPath) == False:
                errorMsg = f'Testcase path not found: {testcaseFullPath}'
                return Response(data={'errorMsg': errorMsg, 'status': 'failed'}, status=HtmlStatusCodes.error)

            try:
                testcaseData = readYaml(testcaseFullPath)
            except Exception as errMsg:
                errorMsg = str(errMsg)
                status = 'failed'
                statusCode = HtmlStatusCodes.error

        return Response(data={'testcase': testcasePath, 'data': testcaseData, 
                              'status': status, 'errorMsg': errorMsg}, status=statusCode)
 
