import os, re, sys, json, traceback, secrets

from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import UserModel

# /path/Keystack/KeystackUI/topbar/settings/accountMgmt
currentDir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(currentDir)

#sys.path.append(currentDir.replace('/topbar/settings/accountMgmt', '/topbar/docs/restApi'))
from topbar.settings.accountMgmt.accountMgr import AccountMgr
from db import DB
from systemLogging import SystemLogsAssistant

import loginForm
from topbar.settings.accountMgmt.verifyLogin import authenticateLogin, verifyUserRole

class Vars:
    webpage = 'accountMgmt'
    
userRoles = ['admin', 'manager', 'engineer']


class AccountMgmt(View):
    @authenticateLogin   
    def get(self, request):
        """
        UserLevel: user:      RX everything in its home domains.
                   manager:   RWX everything in its home domains including creating user/eng users. RW its own domain logs.
                   admin:     RWX all domains, system settings, create users, upgrade, 
        """
        user = request.session['user']
        statusCode = 200

        return render(request, 'accountMgmt.html',
                      {'mainControllerIp': request.session['mainControllerIp'],
                       'topbarTitlePage': f'User Account Mgmt',
                       'user': user,
                      }, status=statusCode)
    
    
class Login(View):
    """
    Login page
    """
    def get(self, request):
        form = loginForm.UserLoginForm()
        return render(request, 'login.html', {'form': form})
    
    def post(self, request):
        # Everything user submits will get stored in request.POST
        form = loginForm.UserLoginForm(data=request.POST)

        if form.is_valid():    
            isAuthenticated = False

            loginName = form.cleaned_data['loginName']
            password = form.cleaned_data['password']

            if AccountMgr().isUserExists(key='loginName', value=loginName):
                userDB = AccountMgr().getUserDetails(key='loginName', value=loginName)
                
                if userDB['password'] == password:
                    isAuthenticated = True
                    DB.name.updateDocument(collectionName='accountMgmt',
                                                  queryFields={'loginName': loginName},
                                                  updateFields={'isLoggedIn': True})

                    # When a session key cookie ages out, a new request coming in could have a session key = None.
                    # Need to create a new session key for the session.
                    if request.session.session_key is None:
                        request.session.create()

                    # Each session has a unique session key.  When a session ages out, the session key is gone.
                    #accountObj.login(request.session._session_key)
                    request.session['loginName'] = userDB['loginName'] ;# Create a session user to know which account to logout.
                    request.session['user']      = userDB['fullName']
                    request.session['userRole']  = userDB['userRole']
                else:
                    loginFailedMessage = 'Wrong password. Try again.'
            else:
                if loginName == 'admin':
                    # First time using Keystack.  Automatically create admin account.
                    AccountMgr().addUser(fullName='Administrator', loginName='admin', password='admin',
                                          email=None, userRole='admin')
                    
                    if password !='admin':
                        loginFailedMessage = 'Wrong password. Try again.'
                    else:
                        if request.session.session_key is None:
                            request.session.create()

                        request.session['loginName'] = 'admin'
                        request.session['user']      = 'Administrator'
                        request.session['userRole']  = 'admin'
                        request.session.modified = True
                        isAuthenticated = True
                        
                elif loginName == 'root':
                    if password == 'SuperRoot!':
                        isAuthenticated = True
                        if request.session.session_key is None:
                            request.session.create()

                        request.session['loginName'] = 'root'
                        request.session['user']      = 'root'
                        request.session['userRole']  = 'admin'
                        request.session.modified = True
                    else:
                        loginFailedMessage = 'Wrong password. Try again.'
                else:
                    loginFailedMessage = 'No such login name. Try again.'
                            
        if isAuthenticated:
            # When adding or setting a key in request.session, must set this to True or else request.session
            # becomes None.
            # If supporting multiple browsers when logging out. The created key 'user' will not be found.
            request.session.modified = True
                    
            # http://192.168.28.7:8000
            mainControllerIp = request._current_scheme_host.split('//')[-1]
            request.session['mainControllerIp'] = mainControllerIp
                  
            return HttpResponseRedirect(reverse('sessionMgmt'))
        else:
            form = loginForm.UserLoginForm()
            return render(request, 'login.html', {'form': form, 'loginFailed': loginFailedMessage})

        
class Logout(View):     
    def get(self, request): 
        if 'user' in request.session:
            form = loginForm.UserLoginForm()
            DB.name.updateDocument(collectionName='accountMgmt',
                                          queryFields={'loginName': request.session['user']},
                                          updateFields={'isLoggedIn': False})

            del request.session['user']
            del request.session['loginName']
            del request.session['userRole']
            
        return HttpResponseRedirect(reverse('login'))
