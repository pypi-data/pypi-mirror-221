from commonLib import showVersion

from django.urls import include, path, re_path
from django.conf import settings
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from topbar.docs.restApi.views import RestAPI

from topbar.docs.restApi.system import GetSystemSettings, ModifySystemSettings, GetSystemPaths, GetServerTime, GetInstantMessages, Ping, WebsocketDemo
from topbar.docs.restApi.systemLogs import GetLogMessages, DeleteLogs
from topbar.docs.restApi.accountMgmtViews import GetApiKey
from topbar.docs.restApi.loginCredentials  import LoginCredentials

from topbar.docs.restApi.groups import GetGroups, CreateGroup, DeleteGroups
from topbar.docs.restApi.controllers import AddController, DeleteControllers, GetControllers, GetControllerList, RegisterRemoteAccessKey, GetAccessKeys, RemoveAccessKeys, GenerateAccessKey
from topbar.docs.restApi.accountMgr import AddUser, DeleteUser, GetUserAccountTableData, GetUserDetails, ModifyUserAccount, GetApiKey, GetPassword, RegenerateApiKey

from topbar.docs.restApi.fileMgmtViews import GetFileContents, ModifyFile

from topbar.docs.restApi.pipelineViews import GetSessions, GetSessionGroups, GetSessionDetails, GetPipelines, GetPipelineTableData, GetPipelinesDropdown, SavePipeline, RunPipeline, DeletePipelineSessions, DeletePipelines, GetTestReport,GetTestLogs, TerminateProcessId, ResumePausedOnError, ShowGroups, ScheduledJobs, AddJobSchedule,  DeleteScheduledJob, GetJobSchedulerCount, GetCronScheduler

from topbar.docs.restApi.playbookViews import GetPlaybooks, CreatePlaybook, DeletePlaybooks, IsExists, RunPlaybook, GetPlaybookDetails, GetPlaybookEnvDetails, GetPlaybookPlaylist, PlaybookTemplate, PlaybookGroups, GetPlaybookNames

from topbar.docs.restApi.pipelineStatusViews import GetPipelineStatus, Pipelines, Report

from topbar.docs.restApi.envViews import GetEnvTableData, CreateEnv, DeleteEnvs, GetEnvs, EnvGroups, GetEnvGroups, DeleteEnvGroups, ViewEditEnv, EnvGroupsTableForDelete, IsEnvAvailableRest, GetActiveUsers, ReserveEnvUI, GetWaitList, AmINext, Reset, RemoveFromActiveUsersListUI, RemoveEnvFromWaitList, GetActiveUsersList, RemoveFromActiveUsersList, ReserveEnv, ReleaseEnv, ReleaseEnvOnFailure, ResetEnv 

from topbar.docs.restApi.loadBalanceEnvs import  CreateNewLoadBalanceGroup, DeleteLoadBalanceGroup, AddEnvsToLoadBalancGroup, GetLoadBalanceGroups, GetAllEnvs, GetLoadBalanceGroupEnvs, GetLoadBalanceGroupEnvsUI, RemoveAllEnvsFromLoadBalanceGroup, RemoveSelectedEnvsRest, ResetLoadBalanceGroupRest

from topbar.docs.restApi.testcaseViews import GetTestcaseDetails

from topbar.docs.restApi.modules import GetModules, GetModuleDetails

from topbar.docs.restApi.appsViews import GetApps, RemoveApps, GetAvailableApps, GetAppDescription, GetAppStoreAppDescription, UpdateApps, InstallApps

from topbar.docs.restApi.testResults import SidebarTestResults, GetNestedFolderFiles, GetTestResultPages, ArchiveResults, DeleteAllInGroup, DeleteAllInPlaybook, DeleteResults, DownloadResults

from topbar.docs.restApi.awsS3 import GetAwsS3Uploads, DeleteAwsS3Uploads, RestartAwsS3Service, StopAwsS3Service, IsAwsS3ServiceRunning, GetAwsS3Logs, ClearAwsS3Logs, DisableAwsS3DebugLogs, EnableAwsS3DebugLogs, IsAwsS3DebugEnabled, GetPipelineAwsS3LogFiles

from topbar.docs.restApi.utilitilizations import GetEnvBarChart, GetUserUsageBarChart

from django.views.generic import RedirectView

schemaView = get_schema_view(
    openapi.Info(
        basePath='/api/v1/restAPI',
        title="Keystack ReST APIs",
        default_version=showVersion(),
        #description="Automating test with Keystack",
        #terms_of_service="https://www.keysight.com",
        contact=openapi.Contact(email="hubert.gee@keysight.com"),
        #license=openapi.License(name="Keysight License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
    
# REST APIs
urlpatterns = [
    path('v1/modules',                            GetModules.as_view(),                    name='getModules'),
    path('v1/modules/details',                    GetModuleDetails.as_view(),              name='getModuleDetails'),

    path('v1/getGroups',                          GetGroups.as_view(),                     name='getGroups'),
    path('v1/createGroup',                        CreateGroup.as_view(),                   name='createGroup'),
    path('v1/deleteGroups',                       DeleteGroups.as_view(),                   name='deleteGroups'),

    path('v1/fileMgmt/getFileContents',           GetFileContents.as_view(),               name='getFileContents'),
    path('v1/fileMgmt/modifyFile',                ModifyFile.as_view(),                    name='modifyFile'),

    path('v1/results/pages',                      GetTestResultPages.as_view(),            name='getTestResultPages'),
    path('v1/results/nestedFolderFiles',          GetNestedFolderFiles.as_view(),          name='getNestedFolderFiles'),
    #path('v1/results/fileContents',               GetTestResultFileContents.as_view(),     name='getTestResultFileContents'),
    path('v1/results/sidebarMenu',                SidebarTestResults.as_view(),            name='sidebarTestResults'),
    path('v1/results/archive',                    ArchiveResults.as_view(),                name='archiveResults'),
    path('v1/results/deleteAllInGroup',           DeleteAllInGroup.as_view(),              name='testResultsDeleteAllInGroup'),
    path('v1/results/deleteAllInPlaybook',        DeleteAllInPlaybook.as_view(),           name='testResultsDeleteAllInPlaybook'),
    path('v1/results/delete',                     DeleteResults.as_view(),                 name='deleteResults'),
    path('v1/results/downloadResults',            DownloadResults.as_view(),               name='downloadResults'),
       
    #path('v1/playbook/login',                    RedirectView.as_view(url='http://192.168.28.7:8000')),        
    path('v1/playbook/groups',                    PlaybookGroups.as_view(),                name='playbookGroups'),
    path('v1/playbook/template',                  PlaybookTemplate.as_view(),              name='getPlaybookTemplate'),
    path('v1/playbook/isExists',                  IsExists.as_view(),                      name='isPlaybookExists'),
    path('v1/playbook/details',                   GetPlaybookDetails.as_view(),            name='getPlaybookDetails'),
    path('v1/playbook/playlist',                  GetPlaybookPlaylist.as_view(),           name='getPlaybookPlaylist'),   
    path('v1/playbook/env/details',               GetPlaybookEnvDetails.as_view(),         name='getPlaybookEnvDetails'), 
    path('v1/playbook/run',                       RunPlaybook.as_view(),                   name='runPlaybook'),
    path('v1/playbook/names',                     GetPlaybookNames.as_view(),              name='getPlaybookNames'),
    path('v1/playbook/get',                       GetPlaybooks.as_view(),                  name='getPlaybooks'),
    path('v1/playbook/create',                    CreatePlaybook.as_view(),                name='createPlaybook'),
    path('v1/playbook/delete',                    DeletePlaybooks.as_view(),               name='deletePlaybooks'),  
       
    path('v1/pipeline/status',                    GetPipelineStatus.as_view(),             name='getPipelineStatus'),
    path('v1/pipeline/report',                    Report.as_view(),                        name='report'),
    path('v1/pipelines',                          Pipelines.as_view(),                     name='pipelines'),
    path('v1/pipeline/getPipelines',              GetSessions.as_view(),                   name='getSessions'),
    path('v1/pipeline/getSessionDetails',         GetSessionDetails.as_view(),             name='getSessionDetails'),     
    path('v1/pipeline/run',                       RunPipeline.as_view(),                   name='runPipeline'),
    path('v1/pipelinesUI',                        GetPipelines.as_view(),                  name='getPipelines'),
    path('v1/pipelines/tableData',                GetPipelineTableData.as_view(),          name='getPipelineTableData'),
    path('v1/pipelines/dropdown',                 GetPipelinesDropdown.as_view(),          name='getPipelinesDropdown'),
    path('v1/pipelines/deletePipelineSessions',   DeletePipelineSessions.as_view(),        name='deletePipelineSessions'),
    path('v1/pipelines/delete',                   DeletePipelines.as_view(),               name='deletePipelines'),
    path('v1/pipelines/getTestReport',            GetTestReport.as_view(),                 name='getTestReport'),
    path('v1/pipelines/getTestLogs',              GetTestLogs.as_view(),                   name='getTestLogs'),
    path('v1/pipelines/terminateProcessId',       TerminateProcessId.as_view(),            name='terminateProcessId'),
    path('v1/pipelines/save',                     SavePipeline.as_view(),                  name='savePipeline'),    
    path('v1/pipelines/resumePausedOnError',      ResumePausedOnError.as_view(),           name='resumePausedOnError'),
    path('v1/pipelines/showGroups',               ShowGroups.as_view(),                    name='showGroups'),
    path('v1/pipelines/getSessionGroups',         GetSessionGroups.as_view(),              name='getSessionGroups'),
    
    path('v1/pipelines/jobScheduler/getCronScheduler',     GetCronScheduler.as_view(),     name='getCronScheduler'),
    path('v1/pipelines/jobScheduler/getJobSchedulerCount', GetJobSchedulerCount.as_view(), name='getJobSchedulerCount'),
    path('v1/pipelines/jobScheduler/scheduledJobs',        ScheduledJobs.as_view(),        name='scheduledJobs'),
    path('v1/pipelines/jobScheduler/add',                  AddJobSchedule.as_view(),       name='addJobSchedule'),
    path('v1/pipelines/jobScheduler/delete',               DeleteScheduledJob.as_view(),   name='deleteScheduledJob'), 
                
    path('v1/testcase/details',                   GetTestcaseDetails.as_view(),            name='getTestcaseDetails'),

    path('v1/env/getEnvTableData',                GetEnvTableData.as_view(),               name='getEnvTableData'),
    path('v1/env/create',                         CreateEnv.as_view(),                     name='createEnv'),     
    path('v1/env/delete',                         DeleteEnvs.as_view(),                    name='deleteEnvs'),    
    path('v1/env/groups',                         GetEnvGroups.as_view(),                  name='getEnvGroups'),
    path('v1/env/envGroups',                      EnvGroups.as_view(),                     name='envGroups'),
    path('v1/env/deleteEnvGroups',                DeleteEnvGroups.as_view(),               name='deleteEnvGroups'),
    path('v1/env/viewEditEnv',                    ViewEditEnv.as_view(),                   name='viewEditEnv'),
    path('v1/env/envGroupsTableForDelete',        EnvGroupsTableForDelete.as_view(),       name='envGroupsTableForDelete'),
    path('v1/env/list',                           GetEnvs.as_view(),                       name='getEnvs'),
    path('v1/env/envWaitList',                    GetWaitList.as_view(),                   name='envWaitList'),
    path('v1/env/amINext',                        AmINext.as_view(),                       name='amINext'),
    path('v1/env/isEnvAvailable',                 IsEnvAvailableRest.as_view(),            name='isEnvAvailableRest'),
    path('v1/env/removeEnvFromWaitList',          RemoveEnvFromWaitList.as_view(),         name='removeEnvFromWaitList'),
    path('v1/env/getActiveUsersList',             GetActiveUsersList.as_view(),            name='getActiveUsersList'),
    path('v1/env/removeEnvFromActiveUsersList',   RemoveFromActiveUsersList.as_view(),     name='removeEnvFromActiveUsersList'),
    path('v1/env/reserveEnv',                     ReserveEnv.as_view(),                    name='reserveEnv'),
    path('v1/env/releaseEnv',                     ReleaseEnv.as_view(),                    name='releaseEnv'),
    path('v1/env/releaseEnvOnFailure',            ReleaseEnvOnFailure.as_view(),           name='releaseEnvOnFailure'),
    path('v1/env/resetEnv',                       ResetEnv.as_view(),                      name='resetEnv'),
    path('v1/env/reserve',                        ReserveEnvUI.as_view(),                  name='reserve'),
    path('v1/env/reset',                          Reset.as_view(),                         name='reset'),
    path('v1/env/activeUsers',                    GetActiveUsers.as_view(),                name='activeUsers'),
    #path('v1/env/releaseEnvOnFailureRest',        ReleaseEnvOnFailureRest.as_view(),       name='releaseEnvOnFailureRest'),
    path('v1/env/removeFromActiveUsersListUI',    RemoveFromActiveUsersListUI.as_view(),   name='removeFromActiveUsersList'),
    
    path('v1/env/loadBalanceGroup/create',        CreateNewLoadBalanceGroup.as_view(),     name='createNewLoadBalanceGroup'),    
    path('v1/env/loadBalanceGroup/delete',        DeleteLoadBalanceGroup.as_view(),        name='deleteLoadBalanceGroup'),
    path('v1/env/loadBalanceGroup/addEnvs',       AddEnvsToLoadBalancGroup.as_view(),      name='addEnvsToLoadBalanceGroup'), 
    path('v1/env/loadBalanceGroup/get',           GetLoadBalanceGroups.as_view(),          name='getLoadBalanceGroups'),
    path('v1/env/loadBalanceGroup/getAllEnvs',    GetAllEnvs.as_view(),                    name='getAllEnvs'),  
    path('v1/env/loadBalanceGroup/getEnvsUI',     GetLoadBalanceGroupEnvsUI.as_view(),     name='getLoadBalanceGroupEnvsUI'),
    path('v1/env/loadBalanceGroup/getEnvs',       GetLoadBalanceGroupEnvs.as_view(),       name='getLoadBalanceGroupEnvs'),
    path('v1/env/loadBalanceGroup/removeAllEnvs', RemoveAllEnvsFromLoadBalanceGroup.as_view(), name='removeAllEnvsFromLoadBalanceGroup'),
    path('v1/env/loadBalanceGroup/removeEnvs',    RemoveSelectedEnvsRest.as_view(),        name='removeSelectedEnvs'),
    path('v1/env/loadBalanceGroup/reset',         ResetLoadBalanceGroupRest.as_view(),     name='resetLoadBalanceGroup'),

    path('v1/apps',                               GetApps.as_view(),                       name='getApps'),
    path('v1/apps/remove',                        RemoveApps.as_view(),                    name='removeApps'),
    path('v1/apps/getAvailableApps',              GetAvailableApps.as_view(),              name='getAvailableApps'),
    path('v1/apps/description',                   GetAppDescription.as_view(),             name='getAppDescription'),
    path('v1/apps/getAppStoreAppDescription',     GetAppStoreAppDescription.as_view(),     name='getAppStoreAppDescription'),
    path('v1/apps/update',                        UpdateApps.as_view(),                    name='updateApps'),
    path('v1/apps/install',                       InstallApps.as_view(),                   name='installApps'),

    path('v1/debug/awsS3/getUploads',             GetAwsS3Uploads.as_view(),               name='getAwsS3Uploads'),
    path('v1/debug/awsS3/deleteUploads',          DeleteAwsS3Uploads.as_view(),            name='deleteAwsS3Uploads'),
    path('v1/debug/awsS3/restartService',         RestartAwsS3Service.as_view(),           name='restartAwsS3Service'),
    path('v1/debug/awsS3/stopService',            StopAwsS3Service.as_view(),              name='stopAwsS3Service'),
    path('v1/debug/awsS3/isServiceRunning',       IsAwsS3ServiceRunning.as_view(),         name='isAwsS3ServiceRunning'),
    path('v1/debug/awsS3/getLogs',                GetAwsS3Logs.as_view(),                  name='getAwsS3Logs'),
    path('v1/debug/awsS3/clearLogs',              ClearAwsS3Logs.as_view(),                name='clearAwsS3Logs'),
    path('v1/debug/awsS3/enableDebugLogs',        EnableAwsS3DebugLogs.as_view(),          name='enableAwsS3DebugLogs'),
    path('v1/debug/awsS3/disableDebugLogs',       DisableAwsS3DebugLogs.as_view(),         name='disableAwsS3DebugLogs'),
    path('v1/debug/awsS3/isDebugEnabled',         IsAwsS3DebugEnabled.as_view(),           name='isAwsS3DebugEnabled'),
    path('v1/debug/awsS3/getPipelineLogFiles',    GetPipelineAwsS3LogFiles.as_view(),      name='getPipelineAwsS3LogFiles'),

    path('v1/system/paths',                       GetSystemPaths.as_view(),                name='getSystemPaths'),

    path('v1/system/getSystemSettings',           GetSystemSettings.as_view(),             name='getSystemSettings'),
    path('v1/system/modifySystemSettings',        ModifySystemSettings.as_view(),          name='modifySystemSettings'),        
    path('v1/system/getInstantMessages',          GetInstantMessages.as_view(),            name='getInstantMessages'),
    path('v1/system/ping',                        Ping.as_view(),                          name='ping'),
    path('v1/system/serverTime',                  GetServerTime.as_view(),                 name='getServerTime'),
    path('v1/system/websocketDemo',               WebsocketDemo.as_view(),                 name='websocketDemo') ,
    path('v1/system/getLogMessages',              GetLogMessages.as_view(),                name='getLogMessages'),
    path('v1/system/deleteLogs',                  DeleteLogs.as_view(),                    name='deleteLogs'),
    
    path('v1/system/account/add',                 AddUser.as_view(),                       name='addUser'),
    path('v1/system/account/delete',              DeleteUser.as_view(),                    name='deleteUser'),
    path('v1/system/account/modify',              ModifyUserAccount.as_view(),             name='modifyUserAccount'),
    path('v1/system/account/tableData',           GetUserAccountTableData.as_view(),       name='getUserAccountTableData'),
    path('v1/system/account/getUserDetails',      GetUserDetails.as_view(),                name='getUserDetails'),

    path('v1/system/account/getApiKey',           GetApiKey.as_view(),                     name='getApiKey'),
    path('v1/system/account/getPassword',         GetPassword.as_view(),                   name='getPassword'),
    path('v1/system/account/gregenerateApiKey',   RegenerateApiKey.as_view(),              name='regenerateApiKey'),
    path('v1/system/accountMgmt/apiKey',          GetApiKey.as_view(),                     name='getApiKeyForRestApi'),
    path('v1/system/loginCredentials',            LoginCredentials.as_view(),              name='loginCredentialsRest'),
    
    path('v1/system/controller/add',                     AddController.as_view(),           name='addController'),
    path('v1/system/controller/delete',                  DeleteControllers.as_view(),       name='deleteControllers'),
    path('v1/system/controller/getControllers',          GetControllers.as_view(),          name='getControllers'),
    path('v1/system/controller/getControllerList',       GetControllerList.as_view(),       name='getControllerList'),
    path('v1/system/controller/generateAccessKey',       GenerateAccessKey.as_view(),       name='generateAccessKey'),
    path('v1/system/controller/registerRemoteAccessKey', RegisterRemoteAccessKey.as_view(), name='registerRemoteAccessKey'),
    path('v1/system/controller/getAccessKeys',           GetAccessKeys.as_view(),           name='getAccessKeys'),
    path('v1/system/controller/removeAccessKeys',        RemoveAccessKeys.as_view(),        name='removeAccessKeys'),    
          
    path('v1/utilization/envsBarChart',           GetEnvBarChart.as_view(),                name='getEnvBarChart'),
    path('v1/utilization/usersBarChart',          GetUserUsageBarChart.as_view(),          name='getUserUsageBarChart'),
      
    # Swagger-UI in keystack vie
    re_path('^v1/restAPI$',                       RestAPI.as_view(),                       name='restAPI'),

    # Backdoor to the rest api
    re_path(r'v1/restAPI/docs/$', schemaView.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
            
    # default renderers are swagger, redoc, redoc-old
    #re_path(r'^swagger(?P<format>\.json|\.yaml)$', schemaView.without_ui(cache_timeout=0), name='schema-json'),
    #re_path(r'^redoc/$', schemaView.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]
