from django.shortcuts import render
from django.views import View
from django.http import JsonResponse

from topbar.settings.accountMgmt.verifyLogin import authenticateLogin
from globalVars import HtmlStatusCodes
    
    
class Playbook(View):
    @authenticateLogin
    def get(self, request):
        """
        Called by base.html sidebar/playbook <module>
        """
        user = request.session['user']
        #module = request.GET.get('module')
        group = request.GET.get('group')
        status = HtmlStatusCodes.success
        
        # {'activeResults': {'Default': ['/opt/KeystackTests/Results/GROUP=Default/PLAYBOOK=pythonSample', '/opt/KeystackTests/Results/GROUP=Default/PLAYBOOK=loadcoreSample']}, 'archiveResults': {'Default': []}}

        # return render(request, 'playbook.html',
        #               {'mainControllerIp': request.session['mainControllerIp'],
        #                'selectedPlaybookGroupToView': group,
        #                'topbarTitlePage': f'Playbooks',
        #                'user': user
        #               }, status=status)
        return render(request, 'playbook.html',
                      {'mainControllerIp': request.session['mainControllerIp'], 
                       'selectedPlaybookGroupToView': group,
                       'topbarTitlePage': f'Playbooks',
                       'user': user
                      }, status=status)
