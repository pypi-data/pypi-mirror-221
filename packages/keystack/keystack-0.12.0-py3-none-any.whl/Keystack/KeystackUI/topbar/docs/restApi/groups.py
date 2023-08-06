import os, sys, json, traceback, secrets

from rest_framework.views import APIView
from rest_framework.response import Response

from keystackUtilities import readYaml, writeToYamlFile
from globalVars import GlobalVars, HtmlStatusCodes
from db import DB
from systemLogging import SystemLogsAssistant
from topbar.settings.accountMgmt.verifyLogin import  verifyUserRole
from topbar.settings.accountMgmt.accountMgr import AccountMgr
from topbar.docs.restApi.controllers import getMainAndRemoteControllerIp, executeRestApiOnRemoteController

groupsDB = GlobalVars.testGroupsFile

class Vars:
    webpage = 'groups'
    

class CreateGroup(APIView):
    @verifyUserRole(webPage=Vars.webpage, action='create', exclude=['engineer']) 
    def post(self, request):
        """ 
        Create a new group
        """
        remoteController = request.data.get('remoteController', None)
        mainControllerIp, remoteControllerIp, ipPort = getMainAndRemoteControllerIp(request, remoteController)
        user = AccountMgr().getRequestSessionUser(request)
        group = request.data.get('group', None)
        statusCode = HtmlStatusCodes.success
        status = 'success'
        errorMsg = None

        if remoteControllerIp and remoteControllerIp != mainControllerIp:
            params = {'group': group}
            restApi = '/api/v1/createGroup'
            response, errorMsg = executeRestApiOnRemoteController('post', remoteControllerIp, ipPort, restApi, params, 
                                                                  user, webPage=Vars.webpage, action='CreateGroup')
            if errorMsg:
                status = 'failed'
                statusCode = HtmlStatusCodes.error
        else:        
            try:
                if os.path.exists(groupsDB) == False:
                    groupsData = {'Default': {'allow': ['*']}}
                else:
                    groupsData = readYaml(groupsDB)
                    
                groupsData.update({group: {'allow': ["*"]}})
                writeToYamlFile(groupsData, groupsDB, retry=5)
                
                if group == '':
                    status = 'failed'
                    statusCode = HtmlStatusCodes.error
                    errorMsg = "A group name cannot be blank"
                    SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='CreateTestGroup', msgType='Error',
                                              msg=f'Failed: A group name cannot be blank', forDetailLogs='')
                    return Response({'status': status, 'error': errorMsg}, status=statusCode)
                    
            except Exception as errMsg:
                errorMsg = str(errMsg)
                status = 'failed'
                statusCode = HtmlStatusCodes.error
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='CreateTestGroup', msgType='Error',
                                          msg=errorMsg, forDetailLogs=traceback.format_exc(None, errMsg))
            
        return Response({'status': status, 'errorMsg': errorMsg}, status=statusCode)
    

class DeleteGroups(APIView):
    @verifyUserRole(webPage=Vars.webpage, action='deleteGroup', adminOnly=True) 
    def delete(self, request):
        remoteController = request.data.get('remoteController', None)
        mainControllerIp, remoteControllerIp, ipPort = getMainAndRemoteControllerIp(request, remoteController)
        user = AccountMgr().getRequestSessionUser(request)
        groups = request.data.get('groups', None)
        statusCode = HtmlStatusCodes.success
        status = 'success'
        errorMsg = None

        if remoteControllerIp and remoteControllerIp != mainControllerIp:
            params = {'groups': groups}
            restApi = '/api/v1/deleteGroups'
            response, errorMsg = executeRestApiOnRemoteController('delete', remoteControllerIp, ipPort, restApi, params, 
                                                                  user, webPage=Vars.webpage, action='DeleteGroups')
            if errorMsg:
                status = 'failed'
                statusCode = HtmlStatusCodes.error
        else:        
            try:
                groupsData = readYaml(groupsDB)
                for group in groups:
                    if group == 'Default':
                        status = 'failed'
                        errorMsg = "Cannot delete the default group"
                        SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='DeleteTestGroup', msgType='Error',
                                                msg=f'Cannot delete the default group', forDetailLogs='')
                        break
                    
                    if group in groupsData:
                        groupsData.pop(group, None)
                    
                        SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='DeleteTestGroup', msgType='Info',
                                                msg=group, forDetailLogs='')
                        
                writeToYamlFile(groupsData, groupsDB, retry=5)
                
            except Exception as errMsg:
                errorMsg = str(errMsg)
                status = 'failed'
                statusCode = HtmlStatusCodes.error
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='DeleteTestGroup', msgType='Error',
                                        msg=errorMsg, forDetailLogs=traceback.format_exc(None, errMsg))
            
        return Response({'status': status, 'errorMsg': errorMsg}, status=statusCode)
    
    
class GetGroups(APIView):
    """ 
    The Groups webpage
    """
    @verifyUserRole()
    def post(self,request):
        remoteController = request.data.get('remoteController', None)
        mainControllerIp, remoteControllerIp, ipPort = getMainAndRemoteControllerIp(request, remoteController)
        user = AccountMgr().getRequestSessionUser(request)
        errorMsg = None
        status = 'success'
        tableData = ''
        statusCode = HtmlStatusCodes.success

        if remoteControllerIp and remoteControllerIp != mainControllerIp:
            params = {}
            restApi = '/api/v1/getGroups'
            response, errorMsg = executeRestApiOnRemoteController('post', remoteControllerIp, ipPort, restApi, params, 
                                                                  user, webPage=Vars.webpage, action='SidebarTestResults')
            if errorMsg:
                status = 'failed'
                statusCode = HtmlStatusCodes.error
            else:
                tableData = response.json()['tableData']
        else:        
            try:
                if os.path.exists(groupsDB):
                    groupsData = readYaml(groupsDB)
                    tableData = ''
                    for group in groupsData.keys():
                        tableData += '<tr>'
                        tableData += f'<td><input type="checkbox" name="groupsCheckboxes" group="{group}"/></td>'
                        tableData += f'<td style="text-align:left">{group}</td>'
                        tableData += '</tr>'
        
                    SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='GetTestGroup', msgType='Info',
                                            msg=f'getGroups()', forDetailLogs='')
                                    
            except Exception as errMsg:
                statusCode = HtmlStatusCodes.error
                errorMsg = str(errMsg)
                status = 'failed'
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='GetTestGroups', msgType='Error',
                                        msg=errorMsg, forDetailLogs=f'getGroups() -> {traceback.format_exc(None, errMsg)}')
         
        return Response(data={'tableData': tableData, 'status': status, 'errorMsg': errorMsg}, status=statusCode)    