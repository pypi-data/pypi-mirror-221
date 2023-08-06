import json
from dotenv import load_dotenv

from rest_framework.views import APIView
from rest_framework.response import Response

from systemLogging import SystemLogsAssistant
from topbar.settings.accountMgmt.verifyLogin import verifyUserRole
from topbar.settings.accountMgmt.accountMgr import AccountMgr
from topbar.docs.restApi.controllers import getMainAndRemoteControllerIp, executeRestApiOnRemoteController
from globalVars import GlobalVars, HtmlStatusCodes

class Vars:
    webpage = 'debug'
    
load_dotenv(GlobalVars.keystackSystemSettingsFile)
            
class GetLogMessages(APIView):
    @verifyUserRole()
    def post(self, request):
        """ 
        User selects the log webPage 
        """
        remoteController = request.data.get('remoteController', None)
        mainControllerIp, remoteControllerIp, ipPort = getMainAndRemoteControllerIp(request, remoteController)
        user = AccountMgr().getRequestSessionUser(request)
        webPage = request.data.get('webPage', None)
        errorMsg = None
        status = 'success'
        statusCode = HtmlStatusCodes.success
        html = ''
        
        if remoteControllerIp and remoteControllerIp != mainControllerIp:
            params = {'webPage': webPage}
            restApi = '/api/v1/system/getLogMessages'
            response, errorMsg = executeRestApiOnRemoteController('post', remoteControllerIp, ipPort, restApi, params, 
                                                                  user, webPage=Vars.webpage, action='GetLogMessages')
            if errorMsg:
                status = 'failed'
                statusCode = HtmlStatusCodes.error
            else:
                html = response.json()['logs']
        else:        
            try:
                html = SystemLogsAssistant().getLogMessages(webPage=webPage)
                statusCode = HtmlStatusCodes.success
                
            except Exception as errMsg:
                errorMsg = str(errMsg)
                status = 'failed'
                statusCode = HtmlStatusCodes.error
            
        return Response({'logs': html}, status=statusCode)
    

class DeleteLogs(APIView):
    @verifyUserRole(webPage=Vars.webpage, action='deleteLogs', exclude=['engineer'])
    def post(self, request):
        remoteController = request.data.get('remoteController', None)
        mainControllerIp, remoteControllerIp, ipPort = getMainAndRemoteControllerIp(request, remoteController)
        user = AccountMgr().getRequestSessionUser(request)
        logPage = request.data.get('webPage', None)
        statusCode = HtmlStatusCodes.success
        status = 'success'
        errorMsg = None

        if remoteControllerIp and remoteControllerIp != mainControllerIp:
            params = {'webPage': logPage}
            restApi = '/api/v1/system/deleteLogs'
            response, errorMsg = executeRestApiOnRemoteController('post', remoteControllerIp, ipPort, restApi, params, 
                                                                  user, webPage=Vars.webpage, action='DeleteLogs')
            if errorMsg:
                status = 'failed'
                statusCode = HtmlStatusCodes.error
        else:        
            try:
                SystemLogsAssistant().delete(logPage)
                
            except Exception as errMsg:
                status = 'failed'
                errorMsg = str(errMsg)
                statusCode = HtmlStatusCodes.error
        
        return Response({'status':status, 'errorMsg':errorMsg}, status=statusCode)
    