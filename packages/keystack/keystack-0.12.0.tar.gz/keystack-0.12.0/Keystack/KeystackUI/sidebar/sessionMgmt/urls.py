from django.urls import include, path, re_path
from sidebar.sessionMgmt.views import SessionMgmt, SessionDetails
#from sidebar.sessionMgmt.views import  WebsocketDemo

# DeletePipelines, GetSessions, GetTestReport, GetTestLogs, GetCronScheduler, JobScheduler, GetJobSchedulerCount, TerminateProcessId, ArchiveResults, ResumePausedOnError, ShowGroups, GetSessionGroups, GetPipelinesDropdown, GetPipelinesForJobScheduler, SavePipeline, GetPipelineTableData, GetServerTime,

urlpatterns = [
    #re_path(r'(?P<module>(.*))/(?P<testResultFolder>(.*))', TestResults.as_view(), name='testResults'),
    path(r'sessionDetails', SessionDetails.as_view(), name='sessionDetails'),
    re_path(r'^$', SessionMgmt.as_view(), name='sessionMgmt'),

    #path(r'getSessions', GetSessions.as_view(), name='getSessions'),
    #path(r'getTestReport', GetTestReport.as_view(), name='getTestReport'),
    #path(r'getTestLogs', GetTestLogs.as_view(), name='getTestLogs'),
    #path(r'getCronScheduler', GetCronScheduler.as_view(), name='getCronScheduler'),
    #path(r'jobScheduler', JobScheduler.as_view(), name='jobScheduler'),
    #path(r'getJobSchedulerCount', GetJobSchedulerCount.as_view(), name='getJobSchedulerCount'),
    #path(r'terminateProcessId', TerminateProcessId.as_view(), name='terminateProcessId'),
    #path(r'archiveResults', ArchiveResults.as_view(), name='archiveResults'),
    #path(r'resumePausedOnError', ResumePausedOnError.as_view(), name='resumePausedOnError'),
    #path(r'showGroups', ShowGroups.as_view(), name='showGroups'),
    #path(r'getSessionGroups', GetSessionGroups.as_view(), name='getSessionGroups'),
    
    #path(r'savePipeline', SavePipeline.as_view(), name='savePipeline'),
    #path(r'getPipelinesDropdown', GetPipelinesDropdown.as_view(), name='getPipelinesDropdown'),
    #path(r'getPipelinesForJobScheduler', GetPipelinesForJobScheduler.as_view(), name='getPipelinesForJobScheduler'),
    
    #path(r'getPipelineTableData', GetPipelineTableData.as_view(), name='getPipelineTableData'),
    #path(r'deletePipelines', DeletePipelines.as_view(), name='deletePipelines'),
    #path(r'getServerTime', GetServerTime.as_view(), name='getServerTime'),
    
    #path(r'websocketDemo', WebsocketDemo.as_view(), name='websocketDemo'),
]
