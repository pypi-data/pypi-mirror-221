import os, sys, json, traceback
from glob import glob
from re import search

from systemLogging import SystemLogsAssistant
from topbar.settings.accountMgmt.verifyLogin import verifyUserRole
from topbar.settings.accountMgmt.accountMgr import AccountMgr
from topbar.docs.restApi.controllers import getMainAndRemoteControllerIp, executeRestApiOnRemoteController
from globalVars import HtmlStatusCodes
from sidebar.sessionMgmt.views import SessionMgmt
from keystackUtilities import readYaml, readFile, writeToFile, execSubprocessInShellMode
from globalVars import GlobalVars, HtmlStatusCodes

from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

class Vars:
    webpage = 'globals'
       

class GetSystemSettings(APIView):
    @verifyUserRole(webPage=Vars.webpage, action='view', adminOnly=True)
    def post(self, request):
        remoteController = request.data.get('remoteController', None)
        mainControllerIp, remoteControllerIp, ipPort = getMainAndRemoteControllerIp(request, remoteController)
        user = AccountMgr().getRequestSessionUser(request)
        statusCode = HtmlStatusCodes.success
        status = 'success'
        errorMsg = None
        settingsData = ''

        if remoteControllerIp and remoteControllerIp != mainControllerIp:
            params = {}
            restApi = '/api/v1/system/getSystemSettings'
            response, errorMsg = executeRestApiOnRemoteController('post', remoteControllerIp, ipPort, restApi, params, 
                                                                  user, webPage=Vars.webpage, action='GetSystemSettings')
            if errorMsg:
                status = 'failed'
                statusCode = HtmlStatusCodes.error
            else:
                settingsData = response.json()['settings']

        else:        
            try:
                settingsFile = f'{GlobalVars.keystackSystemPath}/keystackSystemSettings.env'
                settingsData = readFile(settingsFile)
            except Exception as errMsg:
                errorMsg = str(errMsg)
                status = 'failed'
                statusCode = HtmlStatusCodes.error
        
        return Response({'settings': settingsData, 'status': status, 'errorMsg': errorMsg}, status=statusCode)
    

class ModifySystemSettings(APIView):
    @verifyUserRole(webPage=Vars.webpage, action='modify', adminOnly=True)
    def post(self, request):
        remoteController = request.data.get('remoteController', None)
        mainControllerIp, remoteControllerIp, ipPort = getMainAndRemoteControllerIp(request, remoteController)
        user = AccountMgr().getRequestSessionUser(request)
        textarea = request.data.get('textarea', None)
        
        # import json
        # body = json.loads(request.body.decode('UTF-8'))
        # textarea = body['textarea']
        #user = request.session['user']
        statusCode = HtmlStatusCodes.success
        status = 'success'
        errorMsg = None

        if remoteControllerIp and remoteControllerIp != mainControllerIp:
            params = {'textarea': textarea}
            restApi = '/api/v1/system/modifySystemSettings'
            response, errorMsg = executeRestApiOnRemoteController('post', remoteControllerIp, ipPort, restApi, params, 
                                                                  user, webPage=Vars.webpage, action='ModifySystemSettings')
            if errorMsg:
                status = 'failed'
                statusCode = HtmlStatusCodes.error

        else:        
            try:
                settingsFile = f'{GlobalVars.keystackSystemPath}/keystackSystemSettings.env'
                writeToFile(settingsFile, textarea, mode='w')

                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='modify', msgType='Success',
                                        msg='', forDetailLogs='')              
            except Exception as errMsg:
                errorMsg = str(errMsg)
                status = 'failed'
                statusCode = HtmlStatusCodes.error
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='modify', msgType='Error',
                                        msg=f'Settings: {errMsg}', 
                                        forDetailLogs=traceback.format_exc(None, errMsg))  
        
        return Response({'status': status, 'errorMsg': errorMsg}, status=statusCode)
     
class GetSystemPaths(APIView):
    @swagger_auto_schema(tags=['/api/v1/system/paths'], operation_description="Get paths from /etc/keystack",
                         manual_parameters=[],)
    @verifyUserRole()
    def get(self, request):
        """
        Description: 
            Return a list of all the system paths from /etc/keystack.yml
        
        No parameters required

        GET /api/v1/system/paths
        
        Example:
            curl -H "API-Key: iNP29xnXdlnsfOyausD_EQ" -X GET http://192.168.28.7:8000/api/v1/system/paths
            
        Return:
            A list of environments
        """
        remoteController = request.data.get('remoteController', None)
        mainControllerIp, remoteControllerIp, ipPort = getMainAndRemoteControllerIp(request, remoteController)
        user = AccountMgr().getRequestSessionUser(request)
        statusCode = HtmlStatusCodes.success
        status = 'success'
        errorMsg = None
        systemPaths = ''
        
        # TODO: Need to set controller in central location in order to use rest apis

        if remoteControllerIp and remoteControllerIp != mainControllerIp:
            params = {}
            restApi = '/api/v1/system/paths'
            response, errorMsg = executeRestApiOnRemoteController('get', remoteControllerIp, ipPort, restApi, params, 
                                                                  user, webPage=Vars.webpage, action='GetSystemPaths')
            if errorMsg:
                status = 'failed'
                statusCode = HtmlStatusCodes.error
            else:
                systemPaths = response.json()['systemPaths']
                
        else:        
            try:
                if os.path.exists('/etc/keystack.yml'):
                    systemPaths = readYaml('/etc/keystack.yml')
                else:
                    systemPaths = None
                    errorMsg = 'Not found: /etc/keystack.yml'
                    status = 'failed'
                    statusCode = HtmlStatusCodes.error
                                    
            except Exception as errMsg:
                errorMsg = str(errMsg)
                status = 'failed'
                statusCode = HtmlStatusCodes.error
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='getSystemPaths', msgType='Error',
                                          msg=errorMsg, forDetailLogs='')
        
        return Response(data={'systemPaths':systemPaths, 'status': status, 'errorMsg': errorMsg}, status=statusCode)


class GetServerTime(APIView):
    @verifyUserRole()
    def post(self, request):
        """ 
                timedatectl:
                
                    Local time: Tue 2023-03-21 13:44:35 PDT
                Universal time: Tue 2023-03-21 20:44:35 UTC
                        RTC time: Tue 2023-03-21 20:44:35
                        Time zone: America/Los_Angeles (PDT, -0700)
        System clock synchronized: yes
                    NTP service: active
                RTC in local TZ: no

        """
        remoteController = request.data.get('remoteController', None)
        mainControllerIp, remoteControllerIp, ipPort = getMainAndRemoteControllerIp(request, remoteController)
        user = AccountMgr().getRequestSessionUser(request)
        statusCode = HtmlStatusCodes.success
        status = 'success'
        errorMsg = None
        serverTime = ''
    
        if remoteControllerIp and remoteControllerIp != mainControllerIp:
            params = {}
            restApi = '/api/v1/system/serverTime'
            response, errorMsg = executeRestApiOnRemoteController('post', remoteControllerIp, ipPort, restApi, params, 
                                                                  user, webPage=Vars.webpage, action='GetServerTime')
            if errorMsg:
                status = 'failed'
                statusCode = HtmlStatusCodes.error
            else:
                serverTime = response.json()['serverTime']
                
        else:
            try:
                # Use zdump /etc/localtime to get the local time. This will work for both
                # Linux mode and docker mode.  Docker will use UTC. Linux mode will use the local host time. 
                
                # (True, '/etc/localtime  Fri Mar 24 12:01:21 2023 PDT')
                localHostTime = execSubprocessInShellMode('zdump /etc/localtime', showStdout=False)[1]
                match = search('/etc/localtime +([a-zA-Z]+) +([a-zA-Z]+) +([0-9]+) +([0-9]+:[0-9]+:.*) +([^ ]+) (.*)', localHostTime)
                serverTime = f'{match.group(1)} {match.group(2)} {match.group(3)} {match.group(5)} {match.group(4)} {match.group(6)}'
                
                # UTC: serverTime: (True, 'Thu Mar 16 01:39:55 UTC 2023')
                # serverTimeLinux = keystackUtilities.execSubprocessInShellMode('date', showStdout=True)[1]
                # match = search('([a-zA-Z]+) +([a-zA-Z]+) +([0-9]+) +([0-9]+:[0-9]+:.*) +([^ ]+) (.*)', serverTimeLinux)
                # serverTime = f'{match.group(1)} {match.group(2)} {match.group(3)} {match.group(6)} {match.group(4)} {match.group(5)}'
                
                # timedatectl: (This doesn't work in docker ubuntu)
                # Local time: Tue 2023-03-21 13:47:04 PDT
                #serverTimeLinux = keystackUtilities.execSubprocessInShellMode('timedatectl', showStdout=False)[1]
                #regexp = search('.*Local time:\s+([a-zA-Z]+.*)\n', serverTimeLinux)
                #serverTime = regexp.group(1)
                
            except Exception as errMsg:
                errorMsg = str(errMsg)
                status = 'failed'
                statusCoe = HtmlStatusCodes.error 
            
        return Response({'status':status, 'errorMsg': errorMsg, 'serverTime': serverTime}, status=statusCode)
    
class Ping(APIView):
    swagger_schema = None
    
    def post(self, request):
        """
        Description: 
            Internal use only.  Check if KeystackUI is alive.
            If it gets here, then return a 200 status code for success
        
        No parameters required

        POST /api/system/ping
        
        Example:
            curl -X POST http://192.168.28.7:8000/api/system/ping
            
        Return:
            A list of environments
        """
        user = AccountMgr().getRequestSessionUser(request)
        statusCode = HtmlStatusCodes.success
        status = 'success'
        errorMsg = None
        return Response(data={'status': status, 'errorMsg': errorMsg}, status=statusCode)


class GetInstantMessages(APIView):
    @verifyUserRole()
    def post(self, request):
        """
        Get today's instant messages from systemLogging.py.SystemLogAssistant()
        """
        remoteController = request.data.get('remoteController', None)
        mainControllerIp, remoteControllerIp, ipPort = getMainAndRemoteControllerIp(request, remoteController)
        user = AccountMgr().getRequestSessionUser(request)
        errorMsg = None
        status = 'success'
        statusCode = HtmlStatusCodes.success
        webPage = request.data.get('webPage', None)
        html = ''

        if remoteControllerIp and remoteControllerIp != mainControllerIp:
            params = {'webPage': webPage}
            restApi = '/api/v1/system/getInstantMessages'
            response, errorMsg = executeRestApiOnRemoteController('post', remoteControllerIp, ipPort, restApi, params, 
                                                                  user, webPage=Vars.webpage, action='GetInstantMessages')
            if errorMsg:
                status = 'failed'
                statusCode = HtmlStatusCodes.error
            else:
                html = response.json()['instantMessages']
                
        else:        
            try:
                # The template informs which message topic to get messages from
                html = SystemLogsAssistant().getInstantMessages(webPage)
                
            except Exception as errMsg:
                errorMsg = str(errMsg)
                statusCode = HtmlStatusCodes.error
                status = 'failed'
                SystemLogsAssistant().log(user=request.session['user'], webPage=webPage,
                                        action='GetInstantMessages', msgType='Error', 
                                        msg=errorMsg, forDetailLogs=traceback.format_exc(None, errMsg))
            
        return Response(data={'instantMessages': html}, content_type='application/json', status=statusCode)
    
class WebsocketDemo(View):
    def get(self, request):
        return render(request, 'realtimeLogs.html') 