import os

from keystackUtilities import readYaml
 
currentDir = os.path.abspath(os.path.dirname(__file__))
                                                         
class GlobalVars:        
    sessionTimestampFolder = ''
    versionFile = f'{currentDir}/version'

    if os.path.exists('/etc/keystack.yml') == False:
        raise Exception('/etc/keystack.yml not found')

    etcKeystackYml = readYaml('/etc/keystack.yml')
    if os.path.exists(etcKeystackYml['keystackTestRootPath']) == False:
        raise Exception(f'/etc/keystack.py keystackTestRootPath path not found: {etcKeystackYml["keystackTestRootPath"]}')
    
    user = 'keystack'
    userGroup = 'Keystack'
    
    # # Default httpUI port
    # keystackHttpUrl        = 'http://0.0.0.0'
    # keystackIpPort         = '8028'
    # dockerPythonPath       = '/usr/bin/python3.8'
        
    keystackRootPath       = etcKeystackYml['keystackRootPath']
    keystackTestRootPath   = etcKeystackYml['keystackTestRootPath']    
    keystackSystemPath     = etcKeystackYml['keystackSystemPath']
    
    resultsFolder          = f'{keystackTestRootPath}/Results'
    archiveResultsFolder   = f'{keystackTestRootPath}/ResultsArchive'
    pipelineFolder         = f'{keystackTestRootPath}/Pipelines'
    playbooks              = f'{keystackTestRootPath}/Playbooks'
    envPath                = f'{keystackTestRootPath}/Envs'
        
    keystackSystemSettingsFile = f'{keystackSystemPath}/keystackSystemSettings.env'
    appsFolder                 = f'{keystackSystemPath}/Apps'
    keystackServiceLogPath     = f'{keystackSystemPath}/Logs'
    keystackAwsS3Logs          = f'{keystackServiceLogPath}/keystackAwsS3.json'
    awsS3DebugFile             = f'{keystackSystemPath}/ServicesStagingArea/debuggingAwsS3'
    resultHistoryPath          = f'{keystackSystemPath}/ResultDataHistory'
    restApiModsPath            = f'{keystackSystemPath}/RestApiMods'
    controllerRegistryPath     = f'{keystackSystemPath}/.Controllers'
    loginCredentials           = f'{keystackSystemPath}/.loginCredentials.yml'
    testGroupsFile             = f'{keystackSystemPath}/.DataLake/groups.yml'
    envMgmtPath                = f'{keystackSystemPath}/.DataLake/.EnvMgmt'
    debugLogFilePath           = f'{keystackServiceLogPath}/devDebugLogs'
    

class HtmlStatusCodes:
    # Request is successful
    success = 200
    # Successfully created
    created = 201
    # Request received but not acted upon
    ok = 202
    # Bad request
    badRequest = 400
    # Unauthorized
    unauthorized = 401
    # Forbidden & unauthorized
    forbidden = 403
    # URL is not recognized
    urlNotRecognized = 404
    # Method is not allowed
    notAllowed = 405
    # Request is received but there is an error as result
    error = 406
    # Conflict with the current state of the server
    conflict = 409
    
    