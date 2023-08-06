from django.shortcuts import render
from django.views import View

from globalVars import HtmlStatusCodes
from topbar.settings.accountMgmt.verifyLogin import authenticateLogin

class Vars:
    webpage = 'groups'
    
class Groups(View):
    @authenticateLogin   
    def get(self, request):
        """
        Group Mgmt
        """
        user = request.session['user']
        statusCode = HtmlStatusCodes.success
        
        return render(request, 'groups.html',
                      {'mainControllerIp': request.session['mainControllerIp'],
                       'topbarTitlePage': f'Groups',
                       'user': user,
                      }, status=statusCode)

