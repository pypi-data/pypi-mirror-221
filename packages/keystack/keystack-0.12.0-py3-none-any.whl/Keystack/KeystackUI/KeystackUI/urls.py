"""KeystackUI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path

from sidebar.views import GetModuleFolderFiles
from sidebar.sessionMgmt.apiViews import Sessions, SessionId
from topbar.settings.accountMgmt.views import Login, Logout

urlpatterns = [
    #path('admin/', admin.site.urls),
    
    # Uncomment this for live login
    re_path('^logout$', Logout.as_view(), name='logout'),
    re_path('^login$', Login.as_view(), name='loginRedirect'),
    re_path('^$', Login.as_view(), name='login'),
    #re_path('', include('topbar.settings.accountMgmt.urls')),
    
    # Default go to session without login
    #path('', include('sidebar.sessionMgmt.urls')),

    path('playbooks/',        include('sidebar.playbook.urls')),
    path('setups/',           include('sidebar.setups.urls')),
    path('testResults/',      include('sidebar.testResults.urls')),
    path('sessionMgmt/',      include('sidebar.sessionMgmt.urls')),
    path('debug/systemLogs/', include('topbar.debug.systemLogs.urls')),
    path('debug/awsS3/',      include('topbar.debug.awsS3.urls')),
    path('utilizations/',     include('topbar.utilizations.urls')),

    path('settings/accountMgmt/',      include('topbar.settings.accountMgmt.urls')),
    path('settings/controllers/',      include('topbar.settings.controllers.urls')),
    path('settings/groups/',           include('topbar.settings.groups.urls')),
    path('settings/systemSettings/',   include('topbar.settings.systemSettings.urls')),
    path('settings/loginCredentials/', include('topbar.settings.loginCredentials.urls')),   
    path('settings/keystackApps/',     include('topbar.settings.keystackApps.urls')),
    
    path('api/',        include('topbar.docs.restApi.urls')),
    path('userGuides/', include('topbar.docs.userGuides.urls')),
    
    re_path(r'getModuleFolderFiles/(.*)$', GetModuleFolderFiles.as_view(), name='getModuleFolderFiles')
]
