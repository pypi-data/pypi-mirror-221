import os, sys, traceback

from django.shortcuts import render
from django.views import View
from django.http import JsonResponse

# /path/WebUI/ControlView/topbar/settings
# currentDir = os.path.abspath(os.path.dirname(__file__))
# sys.path.append(currentDir)

from db import DB
from baseLibs import getGroupSessions
from systemLogging import SystemLogsAssistant
from topbar.settings.accountMgmt.verifyLogin import authenticateLogin, verifyUserRole
from globalVars import GlobalVars, HtmlStatusCodes

class LoginCredentials(View):
    @verifyUserRole(webPage='loginCredentials', action='view', adminOnly=True)
    @authenticateLogin  
    def get(self, request):
        """
        Show keystackSystemSettings.env
        """
        user = request.session['user']
        statusCode = HtmlStatusCodes.success
                
        return render(request, 'loginCredentials.html',
                      {'mainControllerIp': request.session['mainControllerIp'],
                       'topbarTitlePage': f'Login Credentials',
                       'user': user,
                      }, status=statusCode)


