import os, re, sys
from dotenv import load_dotenv
from glob import glob

from globalVars import GlobalVars
from Services import Serviceware
from keystackUtilities import readYaml, writeToJson, execSubprocess, chownChmodFolder, getTimestamp

try:
    # If the test was executed by UI
    from execRestApi import ExecRestApi
except:
    # If test was executed from CLI
    from KeystackUI.execRestApi import ExecRestApi


def getHttpMethodIpAndPort():
    """ 
    Get the HTTP/HTTPS method, web server IP and IP Port
    from /path/KeystackSystem/keystackSystemSettings.env
    """
    load_dotenv(GlobalVars.keystackSystemSettingsFile)    
    httpIpAddress = os.environ.get('keystack_localHostIp', '0.0.0.0')
    keystackIpPort = os.environ.get('keystack_keystackIpPort', '28028')
    httpMethod = os.environ.get('keystack_httpMethod', 'http')
    
    if httpMethod == 'https':
        httpMethod2 = True
    else:
        httpMethod2 = False
        
    return httpIpAddress, keystackIpPort, httpMethod2
        
def isKeystackUIAlive(ip, port, headers=None, verifySslCert=False, https=False, timeout=3):
    """ 
    Check if the web UI server is alive.
    For EnvMgmt: If envs with parallelUsage=True
    """
    execRestApiObj = ExecRestApi(ip=ip, port=port, headers=None, verifySslCert=verifySslCert, https=https)
    try:
        response = execRestApiObj.post(restApi='/api/v1/system/ping', timeout=timeout, 
                                       maxRetries=1, ignoreError=True, silentMode=False)

        if response.status_code == 200:
            return True
        else:
            return False
        
    except Exception as errMsg:
        return False
                            
def groupExists(group):
    """ 
    Verify if the group exist
    """
    groupsFile = f'{GlobalVars.keystackSystemPath}/.DataLake/groups.yml'
    currentSystem = readYaml(groupsFile, retry=5)
    if group in currentSystem.keys():
        return True
         
# This function needs to be on its own so KeystackUI could use it too
def createTestResultTimestampFolder(group=None, playbookName=None, sessionId=None, debugMode=False):
    """ 
    Create a unique timestamp folder to store each test results and logs
    """
    resultsRootFolder = f'{GlobalVars.keystackTestRootPath}/Results'
    if os.path.exists(resultsRootFolder) == False:
        execSubprocess(['mkdir', '-p', resultsRootFolder], stdout=False)

    user = os.environ.get('USER')
    if user == None:
        user = execSubprocess(['whoami'])
        user = user[1].replace('\n', '')
        
    userGroup = os.environ.get('keystack_fileGroupOwnership', 'Keystack')

    if os.path.exists(resultsRootFolder) == False:
        chownChmodFolder(resultsRootFolder, user, userGroup, stdout=False)
        execSubprocess(['chmod', 'g+s', resultsRootFolder], stdout=False)
     
    resultsPlaybookLevelFolder = f'{resultsRootFolder}/GROUP={group}/PLAYBOOK={playbookName}'

    if os.path.exists(resultsPlaybookLevelFolder) == False:
        execSubprocess(['mkdir', '-p', resultsPlaybookLevelFolder], stdout=False)
        execSubprocess(['chmod', '770', resultsPlaybookLevelFolder], stdout=False)
        execSubprocess(['chown', f'{user}:{userGroup}', resultsPlaybookLevelFolder], stdout=False)
        execSubprocess(['chmod', 'g+s', resultsPlaybookLevelFolder], stdout=False)
            
    # Create a timestamp test folder
    todayFolder = getTimestamp()
        
    if debugMode:
        timestampFolder = f'{resultsPlaybookLevelFolder}/{todayFolder}_{sessionId}_debugMode'
    else:
        timestampFolder = f'{resultsPlaybookLevelFolder}/{todayFolder}_{sessionId}'

    if os.path.exists(timestampFolder) == False:
        execSubprocess(['mkdir', '-p', timestampFolder], stdout=False)

    return timestampFolder

def showVersion():
    """
    Show the Keystack version
    """
    if os.path.exists(GlobalVars.versionFile):
        contents = readYaml(GlobalVars.versionFile)
        print(f'\nkeystack version=={contents["keystackVersion"]}\n')
        return contents['keystackVersion']
   
def generateManifestFile(resultsTimestampFolder, s3BucketName, awsRegion):
    """ 
    Create manifest.mf for S3 URLS
    
    resultsTimestampFolder <str>: The test top-level result folder to walk through
    """
    s3ManifestFilePath = f'{resultsTimestampFolder}/MANIFEST.mf'
    open(s3ManifestFilePath, 'w').close()
    versionFileContents = readYaml(GlobalVars.versionFile)
    s3ManifestContents = {'keystackVersion': versionFileContents['keystackVersion']}
            
    #s3HttpHeader = f"https://{os.environ['keystack_awsS3BucketName']}.s3.{os.environ['keystack_awsRegion']}.amazonaws.com"
    s3HttpHeader = f"https://{s3BucketName}.s3.{awsRegion}.amazonaws.com"
    
    for root, dirs, files in os.walk(resultsTimestampFolder):
        if 'JSON_KPIs' in root:
            # Don't insert a S3 URL for every KPI. There are over 600 KPIs.
            # The manifest file becomes enormous and in a loop test, this slows down
            # the test drastically.
            continue
                
        # root: /path/KeystacTests/kResults/PLAYBOOK=L3Testing/05-10-2022-10:33:29:705277_<sessionId>/STAGE=Bringup_MODULE=Bringups_ENV=None/dut1
        match = re.search('.*(PLAYBOOK.*)', root)
        if match:
            folder = match.group(1)
            s3FolderUrlPath = f"{folder}".replace(':', '%3A').replace('=', '%3D')
                    
            if files:
                s3FileList = []
                for eachFile in files:
                    if 'metadata.json' in eachFile:
                        continue
                    
                    # s3UrlObj:
                    # https://<bucketName>.s3.<region>.amazonaws.com/PLAYBOOK%3DL3Testing/05-10-2022-07%3A55%3A49%3A276512_<sessionId>/STAGE%3DTeardown_MODULE%3DCustomPythonScripts_ENV%3DNone/moduleTestReport
                    s3FileObj = f"{s3HttpHeader}/{s3FolderUrlPath}/{eachFile}"
                    s3FileList.append(s3FileObj)
                    if 'MANIFEST' in eachFile:
                        awsS3ManifestUrl = s3FileObj
                        
                s3ManifestContents.update({folder: {'files': s3FileList}})

    writeToJson(s3ManifestFilePath, s3ManifestContents, mode='w')
    return s3ManifestFilePath
        
def informAwsS3ServiceForUploads(playbookName, sessionId, resultsTimestampFolder, listOfFilesToUpload,
                                 loginCredentialPath, loginCredentialKey, logFile=None):
    """ 
    Create a timestamp json file containing a list of result paths to upload to S3
    
    sessionId <str>: The sessionId to include in the json filename to identify 
                     from which test it came from.
                     
    listOfFilesToUpload: A list of files and/or folders to upload
    
    aloginCredentialKey: The login credential yml fil key to use.
    
    logFile: Testcase log file
    """
    # NOTE!!  This must be consistent with keystackAwsS3.py
    messageForAwsS3Service = f'{Serviceware.vars.awsS3StagingFolder}/PLAYBOOK={playbookName}_{getTimestamp()}.json'
    data = {'artifactsPath': listOfFilesToUpload, 'loginCredentialPath': loginCredentialPath, 'resultsTimestampFolder': resultsTimestampFolder,
            'playbookName':playbookName, 'sessionId': sessionId, 'loginCredentialKey': loginCredentialKey}
   
    awsS3ServiceObj = Serviceware.KeystackServices(typeOfService='awsS3')
    # NOTE!!  This must be consistent with keystackAwsS3.py 
    awsS3LogFile = f'{Serviceware.vars.keystackServiceLogsFolder}/PLAYBOOK={playbookName}_{resultsTimestampFolder}.json'
    msg = f'[informAwsS3ServiceForUploads]: {messageForAwsS3Service}'
    
    if awsS3ServiceObj.debugEnabled():
        awsS3ServiceObj.writeToServiceLogFile(msgType='debug', msg=msg, playbookName=playbookName, sessionId=sessionId, logFile=awsS3LogFile)
            
    for eachFile in listOfFilesToUpload:
        msg += f'\n\t- {eachFile}\n'
    print(f'informAwsS3ServiceForUploads: {msg}')
    
    # /opt/KeystackSystem/ServicesStagingArea/AwsS3Uploads/hgee2-04-10-2023-08:46:28:628596.json
    if os.path.exists(messageForAwsS3Service) == False:
        mode = 'w'
    else:
        mode = 'w+'
               
    writeToJson(jsonFile=messageForAwsS3Service, data=data, mode=mode)

def validatePlaylistExclusions(playlistExclusionList):
    """ 
    Verify playbook module playlist exclusions
    
    Return:
        1> problems
        2> excludeTestcases (list)
    """
    problems = []
    excludeTestcases = []
    
    # Verify excludes
    for eachExcludedTestcase in playlistExclusionList:
        regexMatch = re.search('.*(Modules/.*)', eachExcludedTestcase)
        if regexMatch:
            eachPath = f'{GlobalVars.keystackTestRootPath}/{regexMatch.group(1)}'

            if os.path.isfile(eachPath):
                if os.path.exists(eachPath) == False:
                    problems.append(f'excludeInPlaylist error: No such path: {eachPath}')
                else:
                    excludeTestcases.append(eachPath)
       
            if os.path.isdir(eachPath):
                for root, dirs, files in os.walk(eachPath):
                    # root ex: starting_path/subFolder/subFolder
                    if files:
                        for eachFile in files:
                            if root[-1] == '/':
                                excludeTestcases.append(f'{root}{eachFile}')
                            else:
                                excludeTestcases.append(f'{root}/{eachFile}')
        else:
            problems.append(f'excludeInPlaylist error: Exepcting /Modules, but got {eachExcludedTestcase}')

    return problems, excludeTestcases
        
def validatePlaylist(playlist, playlistExclusions=[]):
    """
    Validate each testcase yaml file for ymal error.

    Parameters:
        exclude: <list|None>: If the playlist is a folder, users could 
                 exclude a list of testcase subfolders and files
    """
    from pathlib import Path
    
    testcaseSortedOrderList = []
    playlistProblems = []
    
    verifyExclusionsProblems, excludeTestcases = validatePlaylistExclusions(playlistExclusions)
    
    for eachPath in playlist:
        regexMatch = re.search('.*(Modules/.*)', eachPath)
        if regexMatch:
            eachPath = f'{GlobalVars.keystackTestRootPath}/{regexMatch.group(1)}'
        else:
            playlistProblems.append(f'{eachPath}: Must begin with /Modules.')
            continue
        
        if Path(eachPath).is_dir():
            # Run all file in folders and subfolders

            for root, dirs, files in os.walk(eachPath):
                # root ex: starting_path/subFolder/subFolder
                if files:
                    # Store files in numerical/alphabetic order
                    for eachFile in sorted(files):
                        if eachFile[-1] == '/':
                            # Testcase folder.  Not a file
                            eachFile = f'{root}{eachFile}'
                        else:
                            if root[-1] == '/':
                                eachFile = f'{root}{eachFile}'
                            else:
                                eachFile = f'{root}/{eachFile}'
                            
                        # Testcases/Nokia/nokia.yml
                        currentFilename = eachFile.split('/')[-1]

                        if eachFile in excludeTestcases:
                            continue
                                                
                        if bool(re.search('.*(#|~|backup|readme|__init__|pyc)', currentFilename, re.I)):
                            continue

                        # Not all testcases use the yml file method.  Such as custom python scripts.
                        if eachFile.endswith('.yml') or eachFile.endswith('.yaml'):
                            try:
                                readYaml(eachFile)
                            except Exception as errMsg:
                                playlistProblems.append(f'{eachFile}: {errMsg}')
                                
                        testcaseSortedOrderList.append(f'{eachFile}')
                        
        else:
            if eachPath.endswith('.yml') or eachPath.endswith('.yaml'):
                if eachPath in excludeTestcases:
                    continue
                
                if os.path.exists(eachPath) == False:
                    playlistProblems.append(f'Testcase path does not exists: {eachPath}')
                else:
                    # Run individual testcase yml file. Don't read .py files
                    try:
                        readYaml(eachPath)
                    except Exception as errMsg:
                        playlistProblems.append(f'{eachPath}: {errMsg}')
    
            testcaseSortedOrderList.append(eachPath)
               
    return playlistProblems
        
def validatePlaybook(playbook, playbookObj, checkLoginCredentials=False):
    """ 
    playbookObj: <dict>
    checkLoginCredentials: <bool>: If the test includes -awsS3 and or -jira
    
    - Validate the Yaml files for Playbook and the Envs
    
    - It is illegal to create a playbook with the same module and same env within the same stage
      because the results folder will be overwritten by the latter:
        STAGE=Test_MODULE=CustomPythonScripts_ENV=qa
    
        Solution: 
            - Simply add the testcase to the playlist
            - Or put the module under a different stage 
    """
    checkList = ''
    validationPassed = True
    
    # Gather up all the Stage/Modules to run
    runList = []
    # A list of all the problems
    problems = []
    
    if playbookObj is None:
        problems.append(f'The playbook is empty: {playbook}')
        return False, problems
    
    globalApp = playbookObj['globalSettings'].get('app', None)   
    globalEnv = playbookObj['globalSettings'].get('env', None)
    loginCredentialKey = playbookObj['globalSettings'].get('loginCredentialKey', None)
    
    if globalEnv and '-' in globalEnv:
        problems.append(f'Global Settings: Env name cannot have dashes: {globalEnv}')
        
    # Validate login credentials
    if checkLoginCredentials:
        if loginCredentialKey is None:
            problems.append('- You included -awsS3 and/or -jira, but the playbook loginCredentials in globalSettings did not set which login credential key to use.')
    
        if os.path.exists(GlobalVars.loginCredentials) == False:
            problems.append('- The loginCredentials file does not exists.')
        else:
            loginCredentials = readYaml(GlobalVars.loginCredentials)
            if loginCredentialKey not in loginCredentials:
                problems.append(f'- The loginCredentialKey "{loginCredentialKey}" that you stated in the playbook to use for the test does not exist in loginCredentials file.')
                             
    for stage in playbookObj['stages'].keys():
        if playbookObj['stages'][stage].get('enable', True) in [False, 'False', 'false', 'No', 'no']:
            continue
        
        stageEnv = playbookObj['stages'][stage].get('env', None)
        stageApp = playbookObj['stages'][stage].get('app', None)
        checkIt = []
        
        if stageEnv and '-' in stageEnv:
            problems.append(f'Stage {stage}: Env name cannot have dashes: {stageEnv}')
        
        # Validate apps and envs     
        for module in playbookObj['stages'][stage]['modules']:
            # {'/Modules/CustomPythonScripts': {'enable': True, 'env': 'None', 'playlist': ['/Modules/CustomPythonScripts/Samples/Bringups']}}
            for moduleName, properties in module.items():
                if properties.get('enable', True) in [False, 'False', 'false', 'No', 'no']:
                    continue
                
                #print(f'\tvalidatePlaybook module: {moduleName}')
                #print(f'\tvalidatePlaybook properties: {properties}')  
                moduleEnv = properties.get('env', None)
                                
                if 'env' in properties:
                    if moduleEnv and '-' in moduleEnv:
                        problems.append(f'Playbook Module {module}: Env name cannot have dashes: {moduleEnv}')
            
                    if properties['env'] in ['None', None, 'none', '']:
                        if moduleEnv:
                            checkIt.append(moduleEnv)
                        elif stageEnv:
                            checkIt.append(stageEnv)
                        elif globalEnv:
                            checkIt.append(globalEnv)
                    else:
                        checkIt.append(properties['env'])
                else:
                    if moduleEnv:
                        checkIt.append(moduleEnv)
                    elif stageEnv:
                        checkIt.append(stageEnv)
                    elif globalEnv:
                        checkIt.append(globalEnv)

                playlistExclusions = properties.get('excludeInPlaylist', [])
                problems += validatePlaylist(playlist=properties['playlist'], playlistExclusions=playlistExclusions)
                          
    if validationPassed and len(problems) == 0:
        return True, None
    
    if validationPassed == False:
        problems.append(f'- User error. Modules in each stage must use a different env. You might have set the env in globalSettings or at the Stage level that defaulted to all the Modules within a Stage: {checkList}')
               
    if len(problems) > 0:
        print(f'ValidatePlaybook Problems: {problems}')
        return False, problems
    
def getRunList(playbookTasksObj):
    """
    Get a list of all the enabled Stages/Modules/Envs for sessionMgmt
    to show what is expected to run next
    """
    runList = []
    
    if 'globalSettings' in playbookTasksObj and playbookTasksObj['globalSettings'].get('env', None):
        globalEnv = playbookTasksObj['globalSettings']['env']
        globalEnv = envFileHelper(globalEnv)
    else:
        globalEnv = None
        
    for stage in playbookTasksObj['stages'].keys():
        if playbookTasksObj['stages'][stage].get('enable', True) == False:
            continue
 
        if playbookTasksObj['stages'][stage].get('env', None):
            stageEnv = playbookTasksObj['stages'][stage]['env']
            stageEnv = envFileHelper(stageEnv)
        else:
            stageEnv = None
        
        print(f'\tStage:{stage} env:{stageEnv}')
            
        autoTaskName = 1   
        for module in playbookTasksObj['stages'][stage]['modules']:
            # {'/Modules/CustomPythonScripts': {'enable': True, 'env': 'None', 
            #  'playlist': ['/Modules/CustomPythonScripts/Samples/Bringups']}}
            for moduleName, properties in module.items():
                if properties.get('enable', True) in [False, 'False', 'false', 'No', 'no']:
                    continue
        
                moduleName = moduleName.split('/')[-1]
                
                if properties.get('env', None):
                    env = properties['env']
                    env = envFileHelper(env)    
                elif stageEnv:
                    env = stageEnv
                elif globalEnv:
                    env = globalEnv
                else:
                    env = None
                
                taskName = properties.get('taskName', None)
                if taskName:
                    task = f'{autoTaskName}-{taskName}'
                else:
                    task = autoTaskName

                #print(f'\t\tmodule:{moduleName}: env:{env}\n')                      
                if env:
                    # Get the env name with the namespace
                    regexMatch = re.search(f'.+/Envs/(.+)\.(yml|yaml)?', env)
                    if regexMatch:
                        env = regexMatch.group(1)
                
                autoTaskName += 1
                        
                runList.append({'stage': stage, 'module': moduleName, 'env': env})
      
    return runList
                
def envFileHelper(envFile):
    """
    Helper function for the Playbook class.  Returns the env file full path.
    """
    # envFile = Just the env name: Example: qa/loadcoresample
    if envFile in ['None', None, '']:
        return None
        
    if envFile == 'bypass':
        return 'bypass'
    
    if 'yml' not in envFile:
        envFile = f'{envFile}.yml'
    
    # Get just the file name    
    match = re.search('(.*Envs/)?(.*)(\.yml)?', envFile)
    if match:
        envFile = match.group(2)

    envFile = f'{GlobalVars.keystackTestRootPath}/Envs/{envFile}'
    if os.path.exists(envFile) == False:
        raise Exception(f'No such env found in: {envFile}')
    
    return envFile

