from topbar.settings.accountMgmt.verifyLogin import authenticateLogin, verifyUserRole
from globalVars import HtmlStatusCodes

from django.views import View

class RestAPI(View):
    @authenticateLogin
    def get(self, request):
        """
        In order for swagger-ui to be displayed in a view,
        the initial topbar api url must go here to state the .html
        file to open.
        
        In the swagger-ui.html file, use JS to call the schema-swagger-ui url 
        that will render the rest api contents.
        
        Called by base.html sidebar/playbook <module>
        """
        from django.shortcuts import render
        user = 'Unknown'
        
        try:
            user = request.session['user']
            module = request.GET.get('module')
        except Exception as errMsg:
            statusCode = HtmlStatusCodes.error
            
        return render(request, 'swagger-ui.html',
                      {'mainControllerIp': request.session['mainControllerIp'],
                       'topbarTitlePage': f'ReST APIs',
                       'user': user,
                      }, status=HtmlStatusCodes.success)
        

