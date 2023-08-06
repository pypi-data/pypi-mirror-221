import os
from dotenv import load_dotenv

from django.shortcuts import render
from django.views import View

from systemLogging import SystemLogsAssistant
from topbar.settings.accountMgmt.verifyLogin import authenticateLogin
from globalVars import HtmlStatusCodes


class SystemLogs(View):
    @authenticateLogin
    def get(self, request):
        user = 'Unknown'
        logCategoryTitles = ''
        
        try:
            user = request.session['user']
            statusCode = HtmlStatusCodes.success
            logCategoryTitles = SystemLogsAssistant().getLogTitles()
        except Exception as errMsg:
            statusCode = HtmlStatusCodes.error
            
        return render(request, 'systemLogs.html',
                      {'mainControllerIp': request.session['mainControllerIp'],
                       'deleteLogs': os.environ.get('keystack_removeLogsAfterDays', 5),
                       'logSelectionButtons': logCategoryTitles,
                       'topbarTitlePage': 'System Logs',
                       'user': user
                      }, status=statusCode)


    