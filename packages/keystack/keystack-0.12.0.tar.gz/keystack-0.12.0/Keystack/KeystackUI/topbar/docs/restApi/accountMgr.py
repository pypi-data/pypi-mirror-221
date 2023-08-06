import os, re, sys, json, traceback, secrets

from rest_framework.views import APIView
from rest_framework.response import Response

from db import DB
from systemLogging import SystemLogsAssistant
from topbar.settings.accountMgmt.verifyLogin import verifyUserRole
from topbar.settings.accountMgmt.accountMgr import AccountMgr

from topbar.docs.restApi.controllers import getMainAndRemoteControllerIp, executeRestApiOnRemoteController
from globalVars import GlobalVars, HtmlStatusCodes
  
class Vars:
    webpage = 'accountMgmt'
        
        
class AddUser(APIView):
    @verifyUserRole(webPage=Vars.webpage, action='AddUser', exclude=['engineer'])
    def post(self, request):
        #from topbar.settings.accountMgmt.views import AccountMgr
        
        #body      = json.loads(request.body.decode('UTF-8'))
        remoteController = request.data.get('remoteController', None)
        mainControllerIp, remoteControllerIp, ipPort = getMainAndRemoteControllerIp(request, remoteController)
        user = AccountMgr().getRequestSessionUser(request)
        fullName  = request.data.get('fullName', None).strip()
        loginName = request.data.get('loginName', None).strip()
        password  = request.data.get('password', None).strip()
        email     = request.data.get('email', None).strip()
        userRole  = request.data.get('userRole', None)
        failFlag  = False
        status = 'success'
        errorMsg = None
        statusCode = HtmlStatusCodes.success

        if remoteControllerIp and remoteControllerIp != mainControllerIp:
            params = {'fullName': fullName, 'loginName': loginName, 'password': password, 'email': email, 'userRole': userRole}
            restApi = '/api/v1/system/account/add'
            response, errorMsg = executeRestApiOnRemoteController('post', remoteControllerIp, ipPort, restApi, params, 
                                                                  user, webPage=Vars.webpage, action='AddUser')
            if errorMsg:
                status = 'failed'
                statusCode = HtmlStatusCodes.error

        else:
            try:            
                isFullNameExists = AccountMgr().isUserExists(key='fullName', value=fullName)  
                if isFullNameExists:
                    failFlag = True
                    SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='AddUser', msgType='Failed', msg=f'User already exists: {fullName}')
                    # Return conflict with the DB
                    statusCode = HtmlStatusCodes.conflict
                    return Response({}, status=statusCode)

                isLoginExists = AccountMgr().isUserExists(key='loginName', value=loginName)                    
                if isLoginExists:
                    failFlag = True
                    SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='AddUser', msgType='Failed', msg=f'User login name already exists: {loginName}')
                    # Return conflict with the DB
                    statusCode = HtmlStatusCodes.conflict
                    return Response({}, status=statusCode)
                    
                if failFlag == False:
                    # domains and userPreferences are placeholders
                    response = DB.name.insertOne(collectionName=Vars.webpage,
                                                data={'fullName': fullName, 'loginName': loginName, 'password': password,
                                                    'apiKey': secrets.token_urlsafe(16), 'email': email, 'userRole': userRole, 
                                                    'isLoggedIn': False, 'defaultDomain': None, 'domains': [], 'userPreferences': {}})
                    if response.acknowledged:
                        SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='AddUser', msgType='Success', msg=f'Added new user: {fullName}: {userRole}')
                        statusCode = HtmlStatusCodes.success
                    else:
                        SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='AddUser', msgType='Failed', msg=f'User [{fullName}] does not exists, but failed to add user in DB')
                        statusCode = HtmlStatusCodes.conflict

            except Exception as errMsg:
                errorMsg = str(errMsg)
                status = 'failed'
                # Return not acceptable
                statusCode = HtmlStatusCodes.error
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='AddUser', msgType='Error',
                                          msg=f'Add user error: {fullName}', 
                                          forDetailLogs=traceback.format_exc(None, errMsg))

        return Response({'status':status, 'errorMsg':errorMsg}, status=statusCode)


class DeleteUser(APIView):
    @verifyUserRole(webPage=Vars.webpage, action='DeleteUser', adminOnly=True)
    def post(self, request):        
        remoteController = request.data.get('remoteController', None)
        mainControllerIp, remoteControllerIp, ipPort = getMainAndRemoteControllerIp(request, remoteController)
        user = AccountMgr().getRequestSessionUser(request)
        fullName = request.data.get('fullName', None).strip()
        statusCode = HtmlStatusCodes.success
        status = 'success'
        errorMsg = None

        if remoteControllerIp and remoteControllerIp != mainControllerIp:
            params = {'fullName': fullName}
            restApi = '/api/v1/system/account/delete'
            response, errorMsg = executeRestApiOnRemoteController('post', remoteControllerIp, ipPort, restApi, params, 
                                                                  user, webPage=Vars.webpage, action='DeleteUser')
            if errorMsg:
                status = 'failed'
                statusCode = HtmlStatusCodes.error

        else:        
            try:    
                if fullName in ['root', 'Administrator']:
                    SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='DeleteUser', msgType='Error',
                                            msg=f'{fullName} cannot be deleted', 
                                            forDetailLogs='')
                elif fullName == user:
                    SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='DeleteUser', msgType='Error',
                                            msg=f'Cannot delete yourself: {fullName}', 
                                            forDetailLogs='')
                else:
                    AccountMgr().deleteUser(fullName=fullName) 
                    SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='DeleteUser', msgType='Success', msg=f'{fullName}')
                
            except Exception as errMsg:
                errorMsg = str(errMsg)
                status = 'failed'
                statusCode = HtmlStatusCodes.error
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='DeleteUser', msgType='Error',
                                        msg=f'accountMgmt().DeleteUser() Failed to delete user: {fullName}', 
                                        forDetailLogs=traceback.format_exc(None, errMsg))

        return Response({'status': status, 'errorMsg': errorMsg}, status=statusCode) 

    
class GetUserAccountTableData(APIView):
    @verifyUserRole(webPage=Vars.webpage, action='GetUserAccountTableData', exclude=['engineer'])
    def post(self, request):
        remoteController = request.data.get('remoteController', None)
        mainControllerIp, remoteControllerIp, ipPort = getMainAndRemoteControllerIp(request, remoteController)
        user = AccountMgr().getRequestSessionUser(request)
        statusCode = HtmlStatusCodes.success
        status = 'success'
        errorMsg = None  
        tableData = ''

        if remoteControllerIp and remoteControllerIp != mainControllerIp:
            params = {}
            restApi = '/api/v1/system/account/tableData'
            response, errorMsg = executeRestApiOnRemoteController('post', remoteControllerIp, ipPort, restApi, params, 
                                                                  user, webPage=Vars.webpage, action='GetUserAccountTableData')
            if errorMsg:
                status = 'failed'
                statusCode = HtmlStatusCodes.error
            else:
                tableData = response.json()['tableData']
                
        else:        
            try:
                userAccountData = DB.name.getDocuments(collectionName=Vars.webpage,
                                                    fields={},
                                                    includeFields={'_id': 0, 'fullName':1, 'loginName':1,
                                                                    'password':1, 'domains':1, 'email':1, 'userRole':1},
                                                    sortBy=[('fullName', 1)])
                
                tableData += '<tr>'
                # {'fullName': 'Hubert Gee', 'loginName': 'hgee', 'password': 'password', 'email': 'hgee@domain.com', 'userRole': 'admin', 'domains': []}
                for user in userAccountData:
                    if user['fullName'] == 'Administrator':
                        tableData += f'<td></td>'
                    else:
                        tableData += f'<td><a href="#" style="text-decoration:none" userFullName="{user["fullName"]}"onclick="deleteUser(this)">Delete</a></td>'
                    tableData += f'<td><a href="#" user="{user["fullName"]}" onclick="modifyUserForm(this)">{user["fullName"]}</a></td>'
                    tableData += f'<td>{user["loginName"]}</td>'
                    tableData += f'<td>{user["userRole"]}</td>'
                    tableData += f'<td style="text-align:left">{user["email"]}</td>'
                    tableData += f'<td><button class="btn btn-sm btn-outline-primary" type="button" user="{user["fullName"]}" onclick="getPassword(this)">Password</button></td>'
                    tableData += f'<td><button class="btn btn-sm btn-outline-primary" type="button" user="{user["fullName"]}" onclick="openApiKeyModal(this)" data-bs-toggle="modal" data-bs-target="#apiKeyModal">api-key</button></td>'
                    tableData += '</tr>'            

            except Exception as errMsg:
                errorMsg = str(errMsg)
                status = 'failed'
                statusCode = HtmlStatusCodes.error
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='Get', msgType='Error', 
                                          msg=f'GetUserAccountTableData() Error: {errMsg}', 
                                          forDetailLogs=traceback.format_exc(None, errMsg))

        return Response({'tableData': tableData, 'status':status, 'errorMsg':errorMsg}, status=statusCode)
            

class GetUserDetails(APIView):
    @verifyUserRole(webPage=Vars.webpage, action='GetUserDetails')
    def post(self, request):
        """
        Get user current details.  Used by modify user in accountMgmt template
        """
        #from topbar.settings.accountMgmt.views import AccountMgr
         
        remoteController = request.data.get('remoteController', None)
        mainControllerIp, remoteControllerIp, ipPort = getMainAndRemoteControllerIp(request, remoteController)
        user = AccountMgr().getRequestSessionUser(request)
        fullName = request.data.get('fullName', None).strip()
        statusCode = HtmlStatusCodes.success
        status = 'success'
        errorMsg = None

        if remoteControllerIp and remoteControllerIp != mainControllerIp:
            params = {'fullName': fullName}
            restApi = '/api/v1/system/account/getUserDetails'
            response, errorMsg = executeRestApiOnRemoteController('post', remoteControllerIp, ipPort, restApi, params, 
                                                                  user, webPage=Vars.webpage, action='GetUserDetails')
            if errorMsg:
                status = 'failed'
                statusCode = HtmlStatusCodes.error
            else:
                userDetails['loginName'] = response.json()['loginName']
                userDetails['email']     = response.json()['email']
                userDetails['password']  = response.json()['password']
                userDetails['userRole']  = response.json()['userRole']
                         
        else:        
            try:
                userDetails = AccountMgr().getUserDetails(key='fullName', value=fullName)
                    
            except Exception as errMsg:
                errorMsg = str(errMsg)
                status = 'failed'
                statusCode = HtmlStatusCodes.error
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='GetUserDetails', msgType='Error', 
                                        msg=errorMsg, forDetailLogs=traceback.format_exc(None, errMsg))

        return Response({'loginName': userDetails['loginName'], 'email': userDetails['email'],
                         'password': userDetails['password'], 'userRole': userDetails['userRole'], 
                         'status':status, 'errorMsg':errorMsg}, status=statusCode)


class ModifyUserAccount(APIView):
    @verifyUserRole(webPage=Vars.webpage, action='Modify', exclude=['engineer'])
    def post(self, request):
        """
        Modify user details
        """
        #from topbar.settings.accountMgmt.views import AccountMgr
        
        remoteController = request.data.get('remoteController', None)
        mainControllerIp, remoteControllerIp, ipPort = getMainAndRemoteControllerIp(request, remoteController)
        user = AccountMgr().getRequestSessionUser(request).strip()
        modifyFields = request.data.get('modifyFields', None)
        userFullName = request.data.get('userFullName', None).strip()
        statusCode = HtmlStatusCodes.success
        status = 'success'
        errorMsg = None

        if remoteControllerIp and remoteControllerIp != mainControllerIp:
            params = {'modifyFields': modifyFields, 'userFullName': userFullName}
            restApi = '/api/v1/system/account/modify'
            response, errorMsg = executeRestApiOnRemoteController('post', remoteControllerIp, ipPort, restApi, params, 
                                                                  user, webPage=Vars.webpage, action='ModifyUserAccount')
            if errorMsg:
                status = 'failed'
                statusCode = HtmlStatusCodes.error

        else:
            try:            
                result = AccountMgr().updateUser(userFullName, modifyFields)
                if result:
                    SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='ModifyAccount', msgType='Success', 
                                              msg=f'Modified user account: {userFullName}') 
                else:
                    SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='ModifyAccount', msgType='Failed', 
                                              msg=f'Modified user account: {userFullName}')
                    errorMsg = f"Failed to modify user: {userFullName}"
                    statusCode = HtmlStatusCodes.error
                    status = 'failed'
                                                                            
            except Exception as errMsg:
                errorMsg = str(errMsg)
                status = 'failed'
                statusCode = HtmlStatusCodes.error
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='ModifyAccount', msgType='Error', 
                                          msg=errorMsg, forDetailLogs=traceback.format_exc(None, errMsg))

        return Response({'status': status, 'errorMsg':errorMsg}, status=statusCode)    


class GetApiKey(APIView):
    @verifyUserRole()
    def post(self, request):
        """
        Get user API-Key
        """
        #from topbar.settings.accountMgmt.views import AccountMgr

        remoteController = request.data.get('remoteController', None)
        mainControllerIp, remoteControllerIp, ipPort = getMainAndRemoteControllerIp(request, remoteController)
        user = AccountMgr().getRequestSessionUser(request)
        userFullName = request.data.get('userFullName', None)
        statusCode = HtmlStatusCodes.success
        status = 'success'
        errorMsg = None                    
        apiKey = None

        if remoteControllerIp and remoteControllerIp != mainControllerIp:
            params = {'userFullName': userFullName}
            restApi = '/api/v1/system/account/getApiKey'
            response, errorMsg = executeRestApiOnRemoteController('post', remoteControllerIp, ipPort, restApi, params, 
                                                                  user, webPage=Vars.webpage, action='GetApiKey')
            if errorMsg:
                status = 'failed'
                statusCode = HtmlStatusCodes.error
            else:
                apiKey = response.json()['apiKey']
                
        else:
            try:
                if userFullName is None:
                    raise Exception('You must provide a user full name')
                            
                if userFullName == user:
                    apiKey = AccountMgr().getApiKey(fullName=userFullName)
                    SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='GetApiKey', msgType='Success', 
                                              msg=userFullName)  
                else:
                    apiKey = "You have no privilege to view other user API-Keys"
                    SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='GetApiKey', msgType='Failed', 
                                              msg=f'User {userFullName} does not have privilege to view other user API Keys')  
                                        
            except Exception as errMsg:
                errorMsg = str(errMsg)
                status = 'failed'
                statusCode = HtmlStatusCodes.error
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='GetApiKey', msgType='Error', 
                                          msg=errorMsg, forDetailLogs=traceback.format_exc(None, errMsg))

        return Response({'apiKey': apiKey, 'status':status, 'errorMsg':errorMsg}, status=statusCode)


class RegenerateApiKey(APIView):
    @verifyUserRole(webPage=Vars.webpage, action='RegenerateApiKey', exclude=['engineer'])
    def post(self, request):
        """
        Regenerate user API-Key
        """
        #from topbar.settings.accountMgmt.views import AccountMgr

        remoteController = request.data.get('remoteController', None)
        mainControllerIp, remoteControllerIp, ipPort = getMainAndRemoteControllerIp(request, remoteController)
        user = AccountMgr().getRequestSessionUser(request)
        userFullName = request.data.get('userFullName', None)
        statusCode = HtmlStatusCodes.success
        status = 'success'
        errorMsg = None       
        apiKey = None

        if remoteControllerIp and remoteControllerIp != mainControllerIp:
            params = {'userFullName': userFullName}
            restApi = '/api/v1/results/sidebarMenu'
            response, errorMsg = executeRestApiOnRemoteController('post', remoteControllerIp, ipPort, restApi, params, 
                                                                  user, webPage=Vars.webpage, action='RegenerateApiKey')
            if errorMsg:
                status = 'failed'
                statusCode = HtmlStatusCodes.error
            else:
                apiKey = response.json()['apiKey']
                
        else:
            try:
                if userFullName:            
                    apiKey = AccountMgr().regenerateApiKey(userFullName)
                    SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='RegenerateApiKey', msgType='Success', 
                                            msg=userFullName)  
                else:
                    status = 'failed'
                    statusCode = HtmlStatusCodes.error
                    errorMsg = 'You must provide the user full name'
                    SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='RegenerateApiKey', msgType='Error', 
                                            msg=errorMsg)                 
            except Exception as errMsg:
                errorMsg = str(errMsg)
                status = 'failed'
                statusCode = HtmlStatusCodes.error
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='RegenerateApiKey', msgType='Error', 
                                          msg=errorMsg, forDetailLogs=traceback.format_exc(None, errMsg))
            
        return Response({'apiKey': apiKey, 'status': status, 'errorMsg': errorMsg}, status=statusCode)
    
        
class GetPassword(APIView):
    @verifyUserRole()
    def post(self, request):
        """
        Get user Password
        """
        #from topbar.settings.accountMgmt.views import AccountMgr
        
        remoteController = request.data.get('remoteController', None)
        mainControllerIp, remoteControllerIp, ipPort = getMainAndRemoteControllerIp(request, remoteController)
        user = AccountMgr().getRequestSessionUser(request)
        userFullName = request.data.get('userFullName', None)
        statusCode = HtmlStatusCodes.success
        status = 'success'
        errorMsg = None
        password = "No privilege viewing other user passwords"
        
        try:
            if userFullName == user:
                password = AccountMgr().getPassword(userFullName)
                SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='GetPassword', msgType='Success', 
                                          msg=userFullName)  
            else:
               SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='GetPassword', msgType='Failed', 
                                         msg=f'{userFullName} does not have privilege to view other user passwords') 
                                       
        except Exception as errMsg:
            errorMsg = str(errMsg)
            status = 'failed'
            statusCode = HtmlStatusCodes.error
            SystemLogsAssistant().log(user=user, webPage=Vars.webpage, action='GetPassword', msgType='Error', 
                                      msg=errorMsg, forDetailLogs=traceback.format_exc(None, errMsg))

        return Response({'password': password, 'status':status, 'errorMsg':errorMsg}, status=statusCode)
    
    