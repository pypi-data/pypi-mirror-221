from django.shortcuts import render
from django.views import View

from topbar.settings.accountMgmt.verifyLogin import authenticateLogin
    
class GetModuleFolderFiles(View):
    @authenticateLogin
    def get(self, request, module):
        """
        Get all the top-level folders for each module for users to dig into.
        When a user clicks on a module folder, the content page has a dropdown menu
        to select subfolders and files to view or modify.
        """
        user = request.session['user'] 
        
        #  {'activeResults': {'Default': ['/opt/KeystackTests/Results/GROUP=Default/PLAYBOOK=pythonSample']}, 'archiveResults': {'Default': ['/opt/KeystackTests/ResultsArchive/GROUP=Default/PLAYBOOK=pythonSample', '/opt/KeystackTests/ResultsArchive/GROUP=Default/PLAYBOOK=loadcoreSample'], 'ho': ['/opt/KeystackTests/ResultsArchive/GROUP=ho/PLAYBOOK=pythonSample']}}
        
        return render(request, 'fileMgmt.html',
                      {'mainControllerIp': request.session['mainControllerIp'],
                       'topbarTitlePage': f'Module: {module}',
                       'module': module,
                       'user': user
                      })        
