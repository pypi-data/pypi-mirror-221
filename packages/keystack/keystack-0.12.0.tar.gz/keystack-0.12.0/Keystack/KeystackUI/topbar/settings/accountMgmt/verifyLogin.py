"""
Verify account DB for user login

How this is used:

  When user is logged in and authenticated, accountMgmt.py set requst.session['user'] = fullName

  In all the views, use the request.session to verify for the 'user' key:

     if verifyLogin.Account(request).isUserLoggedIn() == False:
         return HttpResponseRedirect(reverse('Login', args=[]))

"""
import os, sys

from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import reverse
from rest_framework.response import Response
            
from db import DB
from systemLogging import SystemLogsAssistant
from globalVars import GlobalVars
from keystackUtilities import readYaml
from topbar.settings.accountMgmt.accountMgr import AccountMgr

def verifyUserRoleHelper(user, userRole, params):
    failed = False
    
    if params.get('exclude', None):
        if userRole in params['exclude']:
            failed = True
            errorMsg = f"verifyUserRole: User is not authorized to {params['action']} {params['webPage']}"

    elif params.get('adminOnly', False):
        if userRole != 'admin':
            failed = True
            errorMsg = f"verifyUserRole: User is not authorized to {params['action']} {params['webPage']}"

    elif userRole not in ['admin', 'manager']:
        failed = True
        merrorMg = f"verifyUserRole: User is not authorized to {params['action']} {params['webPage']}"
    
    if failed:    
        print(f'\n{errorMsg}')
        SystemLogsAssistant().log(user=user, webPage=params['webPage'], action=params['action'], msgType='Failed', msg=errorMsg)
        return errorMsg

                             
class Account:
    """
    This class is called by decorator authenticateLogin()
    """
    def __init__(self, requestObj):
        self.request = requestObj
            
    def isUserLoggedIn(self):
        """
        Notes
          - self.request.session should contain keys(): dict_keys(['loginName', 'user', 'userGroups'])
          - When a session times out, the 'loginName' key is present, but the loginName becomes AnonymousUser.  
        """
        # Uncomment for debugging
        #print(f'\nverifyLogin: {self.request.session.keys()}')
        # verifyLogin: $dict_keys(['loginName', 'user', 'userRole'])

        if 'loginName' in self.request.session.keys():
            if self.request.session['loginName'] == 'AnonymousUser':
                return None
        
        # The 'user' key is not created. The user did not go through login page. User might've entered an endpoint URL.
        if 'user' not in self.request.session.keys():
            return None
        
        if 'user' in self.request.session:
            return True


def authenticateLogin(func):
    """
    A decorator for all URLs
    """
    def internals(theSelf, *args, **kwargs):
        """
        This functions calls the class in this file
        """
        # args[0] = view GET and POST request
        if Account(args[0]).isUserLoggedIn() is None:
            #return HttpResponseRedirect(reverse('login', args=[]))
            return HttpResponseRedirect('/login')
        else:
            return func(theSelf, *args, **kwargs)
        
    return internals


def verifyUserRole(**params):
    """
    For all Rest Framework executables
    
    Parameters:
       action <str>: Short camelBack description of the action 
       webPage <str>: The sidebar web link
       adminOnly <bool>: If set to True, only users with admin role has access
       exclude <list>: A list of userRole to unauthorize
    """
    def outer(func):        
        def internals(*args, **kwargs):
            # params: {'webPage': 'playbooks', 'action': 'Add'}    
            if args:
                sessionRequest = args[1]

                if 'user' in sessionRequest.session:
                    user = sessionRequest.session['user']
                    userRole = sessionRequest.session['userRole']
                
                    errorMsg = verifyUserRoleHelper(user, userRole, params)
                    if errorMsg:
                        return JsonResponse({'status': 'failed', 'errorMsg': errorMsg}, status=403)
                    
                    # Allow
                    return func(*args, **kwargs)
                
                # Scheduled jobs will include the parameter webhook=true because
                # scheduled jobs don't require the api-key.  It would be a security issue if any api-key
                # is exposed to cron.  Plus, in order to schedule a job, users must be logged in.
                elif 'webhook' in sessionRequest.data or 'webhook' in sessionRequest.GET:
                    return func(*args, **kwargs)

                elif 'Access-Key' in sessionRequest.headers:
                    # From a remote-controller.  This is not an API-Key.  It's an access-key generated when adding a remote controller by an Admin.
                    # Since an admin created the access-key, it is opened daylight.
                    accessKey = sessionRequest.headers.get('Access-Key')
                    controllerRegistryPath = f'{GlobalVars.controllerRegistryPath}'
                    controllerAccessKeyFile = f'{controllerRegistryPath}/accessKeys.yml'
                    if os.path.exists(controllerAccessKeyFile) == False:
                        return Response(data={'status': 'failed', 'errorMsg': f'Access-Key not authenticated connecting to: {sessionRequest.headers["Host"]}'}, status=404)
                    
                    accessKeys = readYaml(controllerAccessKeyFile)
                    if accessKey in accessKeys.keys():
                        return func(*args, **kwargs)
                    else:
                        return Response(data={'status': 'failed', 'errorMsg': f'Invalid Access-Key connecting to:{sessionRequest.headers["Host"]}'}, status=404)   
                                
                elif 'Api-Key' in sessionRequest.headers:
                    apiKey = sessionRequest.headers.get('Api-Key')
                    if apiKey is None:
                        error = f"Missing API-Key connecting to: {sessionRequest.headers['Host']}"
                        return Response(data={'status': 'failed', 'errorMsg': error}, status=401)

                    # {'fullName': 'Hubert Gee', 'loginName': 'hgee', 'password': 'password', 'apiKey': 'iNP29xnXdlnsfOyausD_EQ', 'email': 'hubert.gee@keysight.com', 'userRole': 'admin', 'isLoggedIn': True, 'defaultDomain': None, 'domains': [], 'userPreferences': {}}
                    userDetails = AccountMgr().getUserDetails(key='apiKey', value=apiKey)
                    if userDetails is None:
                        error = f"Api-Key is not authorized:{apiKey}. Controller:{sessionRequest.headers['Host']}"
                        return Response(data={'status': 'failed', 'errorMsg': error}, status=401)
                    
                    # Verify user role
                    if params:
                        errorMsg = verifyUserRoleHelper(userDetails['fullName'], userDetails['userRole'], params)
                        if errorMsg:
                            return JsonResponse({'status': 'failed', 'errorMsg': errorMsg}, status=403)
                    
                    return func(*args, **kwargs)
                
                else:
                    return JsonResponse({'status': 'failed', 'errorMsg': 'User is not logged in'}, status=403)
            else:
                return HttpResponseRedirect(params['webPage'])
           
        return internals
    return outer


def verifyUserRole_backup(**params):
    """
    For front page views only.  Not for rest api views.
    
    Parameters:
       action <str>: Short camelBack description of the action 
       webPage <str>: The sidebar web link
       adminOnly <bool>: If set to True, only users with admin role has access
       exclude <list>: A list of userRole to unauthorize
    """
    def outer(func):   
        def internals(*args, **kwargs):
            # params: {'webPage': 'playbooks', 'action': 'Add'}
            if args:
                sessionRequest = args[1]
                
                if 'user' in sessionRequest.session:
                    user = sessionRequest.session['user']
                    userRole = sessionRequest.session['userRole']
                
                    errorMsg = verifyUserRoleHelper(user, userRole, params)
                    if errorMsg:
                        return JsonResponse({'status': 'failed', 'errorMsg': errorMsg}, status=403)
                    
                    # Allow
                    return func(*args, **kwargs)
                else:   
                    return JsonResponse({'status': 'failed', 'errorMsg': 'User is not logged in'}, status=403)
            else:
                return HttpResponseRedirect(params['webPage'])
           
        return internals
    return outer


def verifyApiKey(**params):
    """
    Intercepts the rest api to verify the api-key
    """
    def outer(func):
        def internals(request, *args, **kwargs):
            """
            Description: 
                This decoration checks for request.session['user'].  
                True = using UI. False = using rest-api
                
                For rest api, use requestSession.headers.get('API-Key')
            
            Parameters:
            request <obj>: The get|post request, in which this decorator will
                            need to return back to the originating get|post function.
            
            Use arg[0] to get the request|rest framework request object to get the header API-Key
            """
            # requestSession: {'Content-Length': '', 'Content-Type': 'text/plain', 'Host': '192.168.28.7:8000', 'User-Agent': 'curl/7.61.1', 'Accept': '*/*', 'Api-Key': 'iNP29xnXdlnsfOyausD_EQ'}
            requestSession = args[0]
            
            # Uncomment to debug
            # {'webPage': 'pipelines', 'action': 'JobScheduler', 'exclude': ['engineer']}
            # print(f'\n--- VerifyApiKey params: {params}')
            # print(f'\n--- VerifyApiKey headers: {requestSession.headers}')
            # print(f'\n--- VerifyApiKey request.data: {requestSession.data}')
            # Rest API params goes through .GET
            #print(f'\n--- VerifyApiKey request.GET: {requestSession.GET}')
            #print(f'\n--- VerifyLogin request.META: {requestSession.META}')
            
            # User is logged in. Don't need to verify user's API-Key
            if 'user' in requestSession.session:
                return func(request, *args, **kwargs)

            # Scheduled jobs will include the parameter webhook=true because
            # scheduled jobs don't require the api-key.  It would be a security issue if any api-key
            # is exposed to cron.  Plus, in order to schedule a job, users must be logged in.
            elif 'webhook' in requestSession.data or 'webhook' in requestSession.GET:
                return func(request, *args, **kwargs)
                    
            # Using REST APIs.  Expecting api-key. rest api goes through request.GET.
            elif 'webhook' not in requestSession.data or 'webhook' not in requestSession.GET:
                # <rest_framework.request.Request: POST '/api/v1/playbook/run?playbook=pythonSample&sessionId=awesomeTest2&awsS3=true'>
                statusCode = 401

                if 'Api-Key' in requestSession.headers:
                    apiKey = requestSession.headers.get('Api-Key')
                    if apiKey is None:
                        error = f"Missing API-Key connecting to: {requestSession.headers['Host']}"
                        return Response(data={'status': 'failed', 'errorMsg': error}, status=statusCode)

                    # {'fullName': 'Hubert Gee', 'loginName': 'hgee', 'password': 'password', 'apiKey': 'iNP29xnXdlnsfOyausD_EQ', 'email': 'hubert.gee@keysight.com', 'userRole': 'admin', 'isLoggedIn': True, 'defaultDomain': None, 'domains': [], 'userPreferences': {}}
                    userDetails = AccountMgr().getUserDetails(key='apiKey', value=apiKey)
                    if userDetails is None:
                        error = f"Api-Key is not authorized:{apiKey}. Controller:{requestSession.headers['Host']}"
                        return Response(data={'status': 'failed', 'errorMsg': error}, status=statusCode)
                    
                    userRole = userDetails['userRole']
                    user     = userDetails['fullName']
                    print('\n--- verifyApiKey:', user, userRole)
                    
                    # errorMsg = verifyUserRoleHelper(user, userRole, params)
                    # if errorMsg:
                    #     print('\n--- verifyApiKey errorMsg:', errorMsg)
                    #     return JsonResponse({'status': 'failed', 'errorMsg': errorMsg}, status=403)
                             
                    # User is authenticated
                    return func(request, *args, **kwargs)
                
                elif 'Access-Key' in requestSession.headers:
                    # From a remote-controller.  This is not an API-Key.  It's an access-key generated when adding a remote controller by an Admin.
                    # Since an admin created the access-key, it is opened daylight.
                    accessKey = requestSession.headers.get('Access-Key')
                    controllerRegistryPath = f'{GlobalVars.controllerRegistryPath}'
                    controllerAccessKeyFile = f'{controllerRegistryPath}/accessKeys.yml'
                    if os.path.exists(controllerAccessKeyFile) == False:
                        return Response(data={'status': 'failed', 'errorMsg': f'Access-Key not authenticated connecting to: {requestSession.headers["Host"]}'}, status=404)
                    
                    accessKeys = readYaml(controllerAccessKeyFile)
                    if accessKey in accessKeys.keys():
                        return func(request, *args, **kwargs)
                    else:
                        return Response(data={'status': 'failed', 'errorMsg': f'Invalid Access-Key connecting to:{requestSession.headers["Host"]}'}, status=404)           
                else:
                    # UI comes here if user pressed runPlaybook and session has timed-out
                    return Response(data={'status': 'failed', 'errorMsg': f'Missing API-Key connecting to:{requestSession.headers["Host"]}'}, status=statusCode)
                
            else:
                #return HttpResponseRedirect(reverse('login', args=[]))
                return HttpResponseRedirect('login')
        
        return internals
    return outer



