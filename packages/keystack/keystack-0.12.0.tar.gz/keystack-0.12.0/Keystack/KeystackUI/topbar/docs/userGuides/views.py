from email.errors import NonASCIILocalPartDefect
from email.headerregistry import ParameterizedMIMEHeader
import os, sys, subprocess, json
from glob import glob
from time import sleep

# /Keystack/KeystackUI/restApi
currentDir = os.path.abspath(os.path.dirname(__file__))

from topbar.settings.accountMgmt.verifyLogin import authenticateLogin

from django.conf import settings
from django.views import View
from django.shortcuts import render
from baseLibs import getGroupSessions
        
class UserGuides(View):
    @authenticateLogin
    def get(self, request):
        """
        """
        user = request.session['user']
        status = 200

        return render(request, 'userGuides.html',
                      {'mainControllerIp': request.session['mainControllerIp'],
                       'topbarTitlePage': f'User Guides',
                       'user': user,
                      }, status=status)
        

