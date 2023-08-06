"""
keystack.py

Description
   An automation test framework that runs Keysight test tools as modules and manages automated testing.
   This framework also accepts plain Python scripts by using the CustomPythonScripts module.

Requirements
   - python 3.7+
   - requirements.txt
   - keystackSetup_<version>.py

CLI Usage:
   Minimum: keystack -playbook <playbook.yml> 
   
   Other options: -sessionId myTest -awsS3 -jira -debug -emailResults

Keystack designed and developed by: Hubert Gee

"""
import sys, os, traceback, datetime, yaml, re, json, time, traceback, csv
import subprocess, platform, operator, random
from zipfile import ZipFile
from shutil import rmtree, copy, copytree
from copy import deepcopy
from pathlib import Path
from platform import python_version
from glob import glob
from subprocess import Popen, PIPE
from dotenv import load_dotenv
import threading
import yaml
import runpy
from pprint import pprint

currentDir = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, currentDir)

from globalVars import GlobalVars
from commonLib import createTestResultTimestampFolder, showVersion, generateManifestFile, informAwsS3ServiceForUploads
from commonLib import validatePlaylistExclusions, validatePlaybook, getRunList, envFileHelper, isKeystackUIAlive, getHttpMethodIpAndPort

from keystackUtilities import execSubprocess2, mkdir2, readFile, writeToFile, writeToFileNoFileChecking, readYaml, writeToYamlFile, readJson, writeToJson, createNewFile, getDictItemFromList, sendEmail, getDictIndexList, getDictIndexFromList, convertStrToBoolean
from keystackUtilities import execSubprocessInShellMode, execSubprocess, makeFolder, getTimestamp, updateLogFolder, removePastFoldersBasedOnFolderTimestamp, getDate, chownChmodFolder, updateDict
from Services import Serviceware
from db import DB
from KeystackUI.execRestApi import ExecRestApi
from KeystackUI.systemLogging import SystemLogsAssistant

class KeystackException(Exception):
    def __init__(self, msg=None):
        message = f'[Keystack Exception]: {msg}'
        super().__init__(message)
        showErrorMsg = f'\n{message}\n'
        print(showErrorMsg)
                
                   
class Playbook:
    def __init__(self, group=None, playbook=None, emailResults=False, debugMode=False, sessionId=None, 
                 pauseOnError=False, holdEnvsIfFailed=False, timestampFolder=None, isFromKeystackUI=False,
                 awsS3Upload=False, jira=False, wireshark=False, startLsu=False,
                 trackResults=None, abortTestOnFailure=False, includeLoopTestPassedResults=False):
        """
        group:    <str>: Group the test.  Test results will go under this group name.  
        playbook: <str>: Dynamically-Created | <actual playbook name>
                         Dynamically created playbooks are done by using REST API.

        """
        try:
            # Initilize the overSummaryData with pretestError so all verifications
            # could append pretest errors for the Keystack UI to show the pretest problems.
            self.overallSummaryData = {'status': 'Started', 'pretestErrors': []}
                                           
            if sessionId is None:
                self.sessionId = random.sample(range(1,10000), 1)[0]
            else:
                self.sessionId = sessionId
           
            if group is None:
                self.testGroup = "Default"
            else:
                self.testGroup = group
            
            # Default: Dynamically-Created
            self.playbook = playbook
            
            if playbook != 'Dynamically-Created':
                if 'Playbooks/' in self.playbook:
                    match = re.search('.*Playbooks/(.*)(.yml)?', playbook)
                    playbook = match.group(1)

                if '.yml' not in playbook:
                    playbook = f'{playbook}.yml'
                    
                # Playbook full path:  /opt/KeystackTests/Playbooks/Samples/pythonSample.yml
                self.playbook = f'{GlobalVars.keystackTestRootPath}/Playbooks/{playbook}'
                if os.path.exists(self.playbook) == False:
                    if os.path.exists(self.playbook) == False:
                        errorMsg = f'No playbook found in: {self.playbook}'
                        self.overallSummaryData['pretestErrors'].append(errorMsg)
                        
                try:
                    readYaml(self.playbook)
                except Exception as errMsg:
                    errorMsg = f'The playbook yml file has syntax errors: {self.playbook}'
                    self.overallSummaryData['pretestErrors'].append(errorMsg)
                    
                # Samples-pythonSample -> For creating result timestamp folder name
                self.playbookAndNamespace = self.playbook.split(f'{GlobalVars.keystackTestRootPath}/Playbooks/')[1].split('.')[0].replace('/', '-')
                self.playbookName = self.playbookAndNamespace
                
            else:
                self.playbookName = 'Dynamically-Created'
           
            # abortTestOnFailure=True. Main.run() will set this to True if test failed.
            self.exitTest = False
            self.includeLoopTestPassedResults = includeLoopTestPassedResults 
            self.abortTestOnFailure = abortTestOnFailure
            self.restApiMods = {}
            self.restApiModsFolder = GlobalVars.restApiModsPath
            self.loginCredentialKey = None
            self.lock = None
            self.mainLogFileLock = None
            self.playbookGlobalSettings = None
            self.emailResults = emailResults
            self.debug = debugMode
            self.isFromKeystackUI = isFromKeystackUI
            self.pauseOnError = pauseOnError
            self.holdEnvsIfFailed = holdEnvsIfFailed
            self.jira = jira
            self.awsS3Upload = awsS3Upload
            self.wireshark = wireshark
            self.startLsu = startLsu ;# for airMosaic
            self.updateCsvDataFile = None
            self.envFileFullPath = None
            
            # Each module get tested in the Main() class and it calls generateModuleTestReport().
            # Most of these variable are set in generateModuleTestReport for the final test report.
            self.startTime = datetime.datetime.now()
            self.startTime.strftime('%m-%d-%Y %H:%M:%S')
            self.stopTime = ''
            self.duration = ''
            self.overallTestReportHeadings = ''
            self.overallTestReport = ''
            self.result = None
            self.totalCases = 0
            self.totalSkipped = 0
            self.overallResultList = []
            self.exceptionErrors = []
            self.putFailureDetailsAfterResults = []
            
            if self.jira or self.awsS3Upload:
                checkLoginCredentials = True
            else:
                checkLoginCredentials = False

            keystackSystemSettingsFileNotFound = False 
            if os.path.exists(GlobalVars.keystackSystemSettingsFile):
                self.keystackHttpIpAddress, self.keystackIpPort, self.httpMethod = getHttpMethodIpAndPort()
                if self.httpMethod:
                    self.https = True
                else:
                    self.https = False
            else:
                keystackSystemSettingsFileNotFound = True
                errorMsg = f'Could not located keystack system file: {GlobalVars.keystackSystemSettingsFile}'
                self.overallSummaryData['pretestErrors'].append(errorMsg)
                
            currentVersion = readYaml(GlobalVars.versionFile)
            self.user = os.environ.get('USER')
            if self.user == None:
                self.user = execSubprocess(['whoami'])
                self.user = self.user[1].replace('\n', '')
                
            if timestampFolder is None:
                self.timestampFolder = createTestResultTimestampFolder(self.testGroup,
                                                                       self.playbookAndNamespace,
                                                                       self.sessionId, debugMode)
            else:
                self.timestampFolder = timestampFolder
            
            execSubprocessInShellMode(f'chmod -R 770 {self.timestampFolder}', showStdout=False)
            self.timestampFolderName = self.timestampFolder.split('/')[-1]

            # Read the playbook yml file first. Then if rest api, overwrite the playbook settings
            if self.playbook != "Dynamically-Created":
                self.playbookTasks = readYaml(self.playbook, threadLock=self.lock)       
                if self.playbookTasks is None:
                    errorMsg = f'keystack.py: Playbook is empty.  Check ymal syntaxes: {self.playbook}'
                    self.overallSummaryData['pretestErrors'].append(errorMsg)
                else:
                    # This will validate playlist and envs
                    # Will abort test after self.overallSummaryData is created a little further down
                    validatePlaybookResult, validatePlaybookProblems = validatePlaybook(self.playbook, 
                                                                                        self.playbookTasks,
                                                                                        checkLoginCredentials=checkLoginCredentials)
                    if validatePlaybookResult == False:
                        self.overallSummaryData['pretestErrors'].append(validatePlaybookProblems)
            else:
                # This will get updated in getRestApiMods()
                # The playbook will get validated from restApi/playbookView
                self.playbookTasks = {}

            # Create supporting folders for test and internal usage.
            self.sessionDataFolder = f'{self.timestampFolder}/.Data'
            mkdir2(self.sessionDataFolder, stdout=False)
            self.envMgmtDataFolder = f'{self.sessionDataFolder}/EnvMgmt'
            mkdir2(self.envMgmtDataFolder, stdout=False)
            self.resultsMetaFolder = f'{self.sessionDataFolder}/ResultsMeta'
            mkdir2(self.resultsMetaFolder, stdout=False)
            self.artifactsRepo = f'{self.timestampFolder}/Artifacts'
            mkdir2(self.artifactsRepo, stdout=False)
            copy(self.playbook, f'{self.sessionDataFolder}/playbook_{self.playbookName}.yml') 
            chownChmodFolder(self.sessionDataFolder, self.user, GlobalVars.userGroup, stdout=False)
                                 
            # getRestApiMods will update playbookTasks with rest api mods
            self.getRestApiMods()
     
            # Set default settings: These parameters are all known options for playbooks.
            # Some of these settings could be overwritten in the stage and module properties
            self.playbookGlobalSettings = {'loginCredentialKey': None,
                                           'showResultDataLastDays': 10,
                                           'trackResults': False,
                                           'abortModuleFailure': False,
                                           'abortStageFailure': True,
                                           'reportHeadingAdditions': None,
                                           'verifyFailurePatterns': [],
                                           'env': None,
                                           'loadBalanceGroup': None,
                                           'app': None
                                          }
            # Overwrite defaults   
            if self.playbookTasks is not None:
                if 'globalSettings' in self.playbookTasks.keys():
                    """ 
                    globalSettings:
                        # General attributes for all Playbooks
                        trackResults: False
                        loginCredentialKey: main
                        abortModuleFailure: False
                        # Allow the test to continue even if there is a stage failure
                        abortStageFailure: False
                        abortModuleFailure: False
                        verifyFailurePatterns: ['Failed', 'SyntaxError']
                        env: <envName>
                        loadBalanceGroup: None
                        # A list of key/values to display in test reports
                        reportHeadingAdditions:
                            - key: 'value'

                        # AirMosaic specifics
                        testConfigMatrix: /path/Modules/AirMosaic/ConfigFiles/testConfigMatrix.yml
                        airMosaicIniFile: /path/Modules/AirMosaic/ConfigFiles/testParameters.ini
                        iniParameters:
                            TEST_EXECUTION:
                                global_variable: [{"name": "SESSION_REPETITION", "value": "1"},
                                                {"name": "DELAY_TIME", "value": "2000"}]
                    """
                    self.playbookGlobalSettings.update(self.playbookTasks['globalSettings'])
                
            # This will verify if test includes -awsS3|-jira and if true, store login detials in self.loginCredentials
            self.getLoginCredentials()

            self.trackResults       = self.playbookGlobalSettings.get('trackResults', False)
            self.abortStageFailure  = self.playbookGlobalSettings.get('abortStageFailure', True)
            self.abortModuleFailure = self.playbookGlobalSettings['abortModuleFailure']
            self.runList = []
            
            self.overallSummaryDataFile = f'{self.timestampFolder}/overallSummary.json'
            if len(self.overallSummaryData['pretestErrors']) > 0:
                status = 'Aborted'
            else:
                status = 'Started'
                self.runList = getRunList(self.playbookTasks)
            
            self.overallSummaryData.update({'sessionId': self.sessionId,
                                            'started': str(self.startTime),
                                            'stopped': '',
                                            'testDuration': '',
                                            'totalCases': self.totalCases,
                                            'totalFailures': 0,
                                            'totalPassed': 0,
                                            'totalFailed': 0,
                                            'totalSkipped': 0,
                                            'totalTestAborted': 0,
                                            'totalKpiPassed': 0,
                                            'totalKpiFailed': 0,
                                            'pausedOnError': None,
                                            'notes': [],
                                            'warnings': [],
                                            'exceptionErrors': [],
                                            'testAborted': False,
                                            'stageFailAborted': False,
                                            'status': status,
                                            'result': None,
                                            'topLevelResultFolder': self.timestampFolder,
                                            'group': self.testGroup,
                                            'processId': os.getpid(),
                                            'keystackVersion': currentVersion['keystackVersion'],
                                            'user': self.user,
                                            'playbook': self.playbook,
                                            'loginCredentialKey': self.loginCredentialKey,
                                            'trackResults': self.trackResults,
                                            'abortTestOnFailure': abortTestOnFailure,
                                            'holdEnvsIfFailed': self.holdEnvsIfFailed,
                                            'includeLoopTestPassedResults': includeLoopTestPassedResults,
                                            'stages': {},
                                            'runList': self.runList,
                                       })
            
            writeToJson(self.overallSummaryDataFile, data=self.overallSummaryData, mode='w')
            if len(self.overallSummaryData['pretestErrors']) > 0:
                if isFromKeystackUI:
                    SystemLogsAssistant().log(user=self.user, webPage='pipelines', action='runPlaybook', msgType='Error',
                                            msg=self.overallSummaryData["pretestErrors"],
                                            forDetailLogs='')
                errors = ''
                for line in self.overallSummaryData["pretestErrors"]:
                    errors += f'- {line}\n'                  
                sys.exit(f'\nErrors:\n{errors}')
                    
            # ALL PRE-TEST VALIDATION MUST BE DONE WITH BELOW METHOD. 
            #    pipelineView.py getTableData looks for overallSummaryData['status'] = Aborted
            #     and shows the self.overallSummaryData['exceptionErrors']
            #       
            # For env mgmt. Check if the webUI server is alive.
            # If not, env mgmt including env load balancing won't work because they require the MongoDB.
            # Only static env is supported
            self.isKeystackUIExists = isKeystackUIAlive(ip=self.keystackHttpIpAddress, port=self.keystackIpPort, https=self.httpMethod, timeout=3)
            self.execRestApiObj = None
            if self.isKeystackUIExists == False:
                if self.holdEnvsIfFailed:
                    self.abortTest('Error: Including param -holdEnvsIfFailed will not work unless the web UI docker container is running') 
            else:
                self.execRestApiObj = ExecRestApi(ip=self.keystackHttpIpAddress, port=self.keystackIpPort, https=self.https)

            if keystackSystemSettingsFileNotFound:
                self.abortTest(f'keystack.py error: Could not located file: {GlobalVars.keystackSystemSettingsFile}')
                   
            if awsS3Upload:
                # For logging awsS3 messages
                self.awsS3ServiceObj = Serviceware.KeystackServices(typeOfService='keystackAwsS3', isFromKeystackUI=self.isFromKeystackUI)

            removeLogsAfterDays = os.environ.get('keystack_removeLogsAfterDays', 3)
            updateLogFolder(logFolderSearchPath=f'{GlobalVars.keystackSystemPath}/Logs/*',
                            removeAfterDays=removeLogsAfterDays)

            # In case anybody added new files/folders.
            # Force all folders and files to be owned by group Keystack and permissions 770
            chownChmodFolder(GlobalVars.keystackTestRootPath, self.user, GlobalVars.userGroup, stdout=False)
            if os.path.exists(f'{GlobalVars.appsFolder}/keystackEnv.py') == False:
                execSubprocessInShellMode(f'echo "keystackObj = None" > {GlobalVars.appsFolder}/keystackEnv.py', showStdout=False)
                
            chownChmodFolder(GlobalVars.appsFolder, self.user, GlobalVars.userGroup, stdout=False)            

        except Exception as errMsg:
            print(traceback.format_exc(None, errMsg))

            # Playbook level exception
            self.abortTest(f'Playbook exception: {str(errMsg)}', detailedLogs=traceback.format_exc(None, errMsg))

    def abortTest(self, errorMsg, detailedLogs=None):
        self.overallSummaryData['testAborted'] = True
        self.overallSummaryData['status'] = 'Aborted'
        
        # This error message will be shown by pipelineView table data in the web UI 
        self.overallSummaryData['pretestErrors'].append(errorMsg)
        writeToJson(self.overallSummaryDataFile, data=self.overallSummaryData, mode='w')  
         
        if detailedLogs:
            details = detailedLogs
        else:
            details = ''
            
        if self.isFromKeystackUI:
            SystemLogsAssistant().log(user=self.user, webPage='pipelines', action='runPlaybook', msgType='Error',
                                      msg=f'sessionId: {self.sessionId} Errors:<br> {errorMsg}',
                                      forDetailLogs=details) 
        sys.exit(f'\n{errorMsg}\n')
                                           
    def executeStages(self):
        try:
            def runModulesHelper(stage):
                """ 
                Run the modules in the current stage
                """
                # METADATA
                self.overallSummaryData['stages'].update({stage: {'result': None, 'modules': []}})
                writeToJson(self.overallSummaryDataFile, data=self.overallSummaryData, mode='w')
                self.runModules(stage=stage)
                             
            runBringup = False
            runCustomStages = True
            self.abortedStages = []
            self.skippedStages = []
            
            for playbookStageKeyword in ['bringup', 'teardown']:
                if playbookStageKeyword in list(self.playbookTasks['stages'].keys()):
                    raise Exception(f'Playbook error: "{playbookStageKeyword}" stage needs to be uppercase {playbookStageKeyword[0].upper()}.')
            
            anyStageFailed = False                
            for key in self.playbookTasks.keys():           
                if key == 'stages':
                    stageFailed = False
                                   
                    if 'Bringup' in list(self.playbookTasks['stages'].keys()):
                        if self.playbookTasks['stages']['Bringup'].get('enable', True) in [True, 'True', 'true', 'yes', 'Yes']:
                            runModulesHelper('Bringup')
                            runBringup = True
                                                                
                    if runBringup:
                        # METADATA: Check bringup result
                        if self.overallSummaryData['stages']['Bringup']['result'] == 'Failed':
                           runCustomStages = False
                           stageFailed = True
                      
                    if stageFailed == False and runCustomStages:
                        runStageList = []   
                        
                        for stageName in list(self.playbookTasks['stages'].keys()):
                            if self.playbookTasks['stages'][stageName].get('enable', True) in [True, 'True', 'true', 'yes', 'Yes']:
                                if stageName not in ['Bringup', 'Teardown']:
                                    # Abort immediately after a testcase failure. 
                                    # abortTestOnFailure=True Main.run() will set exitTest=True if test failed
                                    if self.exitTest:
                                        stageFailed = True
                                        anyStageFailed = True
                                        self.abortedStages.append(stageName)
                                        self.skippedStages.append(stageName)
                                        continue
                                    
                                    # abortStageFailure default = True                                   
                                    if stageFailed and self.abortStageFailure:
                                        self.skippedStages.append(stageName)
                                        continue
                                    
                                    runStageList.append(stageName)
                                    runModulesHelper(stageName)
                                    stageResult = self.overallSummaryData['stages'][stageName]['result']
                                                
                                    # CI/CT/CD typically aborts when the stage fails    
                                    if stageFailed == False and stageResult in ['Failed', 'Aborted']:
                                        stageFailed = True
                                        anyStageFailed = True
                                        
                                        if self.abortStageFailure:
                                            self.abortedStages.append(stageName)
                                            
                                    # Must have a small delay in case back-to-back stages module use the same env.
                                    # Give it time to sessionMgmt to get up-to-date EnvMgmt data.
                                    time.sleep(.5)
                                    
                            else:
                                continue
                                                           
                    if 'Teardown' in list(self.playbookTasks['stages'].keys()):
                        if self.playbookTasks['stages']['Teardown'].get('enable', True) in  [True, 'True', 'true', 'yes', 'Yes']:
                            tearDownOnFailure = self.playbookTasks['stages']['Teardown'].get('teardownOnFailure', False)

                            if self.exitTest and tearDownOnFailure in [False, 'False', 'false', 'No', 'no']:
                                self.skippedStages.append('Teardown')
                                continue
                            
                            if anyStageFailed and tearDownOnFailure in [True, 'True', 'true', 'Yes', 'yes']:
                                runModulesHelper('Teardown')
                                
                            elif anyStageFailed and tearDownOnFailure in [False, 'False', 'false', 'No', 'no']:
                                self.skippedStages.append('Teardown')
                                continue
    
            # --- At this point, all stages are done ---
            # Handle all post test procedures starting here
            
            if self.overallSummaryData['stageFailAborted'] == True:
                self.overallSummaryData['status'] = 'StageFailAborted'
            else:
                self.overallSummaryData['status'] = 'Completed'
            writeToJson(self.overallSummaryDataFile, data=self.overallSummaryData, mode='w') 

            try:
                chownChmodFolder(self.timestampFolder, self.user, GlobalVars.userGroup, stdout=False)
            except:
                pass

            if self.awsS3Upload:
                self.s3ManifestFile = generateManifestFile(self.timestampFolder,
                                                           self.loginCredentials['S3BucketName'],
                                                           self.loginCredentials['region'])

                informAwsS3ServiceForUploads(playbookName=self.playbookAndNamespace, sessionId=self.sessionId,
                                             resultsTimestampFolder=self.timestampFolder,
                                             listOfFilesToUpload=[f'{self.timestampFolder}/MANIFEST.mf'],
                                             loginCredentialPath=self.credentialYmlFile,
                                             loginCredentialKey=self.loginCredentialKey)

            self.createTestReport()
            chownChmodFolder(topLevelFolder=self.timestampFolder, user=self.user, userGroup=GlobalVars.userGroup)
            self.recordResults()
            
            if self.awsS3Upload:
                informAwsS3ServiceForUploads(playbookName=self.playbookAndNamespace, sessionId=self.sessionId, 
                                             resultsTimestampFolder=self.timestampFolder,
                                             listOfFilesToUpload=[f'{self.timestampFolder}/testReport'],
                                             loginCredentialPath=self.credentialYmlFile,
                                             loginCredentialKey=self.loginCredentialKey)
                
            self.emailReport()

            # This must be the last step
            #if self.awsS3Upload and os.environ['keystack_platform'] == 'docker':
            if self.awsS3Upload and self.isFromKeystackUI:
                # For Docker, must wait for S3 to finish uploading.
                # Otherwise, the test exits too fast when done testing during S3 uploading .
                time.sleep(2)
                self.waitForS3UploadToComplete()
            
            return self.overallSummaryData['result']
                                             
        except Exception as errMsg:
            #msg = f'Playbook executeStages exception: {traceback.format_exc(None, errMsg)}'
            msg = f'Playbook executeStages exception: {str(errMsg)}'
            self.exceptionErrors.append(str(msg))
            stopTime = datetime.datetime.now()
            stopTime.strftime('%m-%d-%Y %H:%M:%S')
            self.overallSummaryData.update({'stopped': str(stopTime), 'status': 'Aborted'})
            writeToJson(self.overallSummaryDataFile, data=self.overallSummaryData, mode='w')
            #raise Exception(str(msg)) 
            self.abortTest(str(errMsg)) 
                                       
    def runModules(self, stage):             
        try:
            if self.playbookTasks['stages'][stage].get('enable', True) in ['False', 'false', False, 'no', 'No']:
                return
            
            threadList = []
            runModulesInParallel = False
            envFile = None
            env = None 
            loadBalanceGroup = None
            doOnceFlagForParallelLocks = True
            self.envFileFullPath = None
            runModulesInParallel = self.playbookTasks['stages'][stage].get('runModulesInParallel', False)
            stageProperties = {'stage': {stage: {}}}

            # First, set environment parameters from globalSettings.
            # Then overwrite them in the stage level and then the module level
            if 'globalSettings' in self.playbookTasks:
                stageProperties['stage'][stage].update(self.playbookTasks['globalSettings'])
                globalEnv = self.playbookTasks['globalSettings'].get('env', None)
                globalEnv = envFileHelper(globalEnv)
                globalLoadBalanceGroup = self.playbookTasks['globalSettings'].get('loadBalanceGroup', None)
                globalVerifyFailurePatterns = self.playbookTasks['globalSettings'].get('verifyFailurePatterns', [])
            
            if self.playbookTasks['stages'][stage].get('env', None) not in ['None', 'none', None]:
                stageEnv = self.playbookTasks['stages'][stage]['env']
                stageEnv = envFileHelper(stageEnv)
            else:
                stageEnv = None

            if self.playbookTasks['stages'][stage].get('loadBalanceGroup', None) not in ['None', 'none', None]:
                stageLoadBalanceGroup = self.playbookTasks['stages'][stage]['loadBalanceGroup']
            else:
                stageLoadBalanceGroup= None
                            
            stageVerifyFailurePatterns = self.playbookTasks['stages'][stage].get('verifyFailurePatterns', [])
                                          
            for module in self.playbookTasks['stages'][stage]['modules']:
                self.moduleSummaryData = {}
                # module: {'/Modules/CustomPythonScripts': {'enable': True, 'abortModuleFailure': False, 'env': 'test', 'playlist': ['/Modules/CustomPythonScripts/Testcases/bgp.yml'], 'innerLoop': {'allTestcases': 1}, 'dependencies': {'/Modules/CustomPythonScripts/Testcases/isis.yml': {'enable': False, 'dependOnCases': ['/Modules/CustomPythonScripts/Testcases/bgp.yml']}}}}
 
                for modulePath, moduleProperties in module.items():
                    if self.exitTest:
                        break
                    
                    # modulePath: /Modules/CustomPythonScripts
                    if moduleProperties.get('enable', True) in [False, 'False', 'false', 'No', 'no']:
                        continue
                    
                    regexMatch = re.search('.*(Modules/.*)', modulePath)
                    if regexMatch:
                        modulePath = f'{GlobalVars.keystackTestRootPath}/{modulePath}'
                                        
                    if os.path.exists(modulePath) == False:
                        raise Exception(f'playbook(): No such module found in path: {modulePath}')
                            
                    # The module name only   
                    moduleName = modulePath.split('/')[-1]
                    
                    if moduleProperties.get('env', None):
                        env = moduleProperties['env']
                        env = envFileHelper(env)
                    elif stageEnv:
                        env = stageEnv
                    elif globalEnv:
                        env = globalEnv
                    else:
                        env = None

                    if moduleProperties.get('loadBalanceGroup', None):
                        loadBalanceGroup = moduleProperties['loadBalanceGroup']
                    elif stageLoadBalanceGroup:
                        loadBalanceGroup = stageLoadBalanceGroup
                    elif globalLoadBalanceGroup:
                        loadBalanceGroup = globalLoadBalanceGroup
                    else:
                        loadBalanceGroup = None
                    
                    if loadBalanceGroup in ['None', 'none']:
                        loadBalanceGroup = None
                                                
                    if moduleProperties.get('verifyFailurePatterns', []):
                        verifyFailurePatterns = moduleProperties['verifyFailurePatterns'] 
                    elif stageVerifyFailurePatterns:
                        verifyFailurePatterns = stageVerifyFailurePatterns
                    elif globalVerifyFailurePatterns:
                        verifyFailurePatterns = globalVerifyFailurePatterns
                    else:
                        verifyFailurePatterns = []
                    
                    if env and env != 'bypass':
                        # Create an env mgmt file in:  /timestampFolder/.Data/EnvMgmt
                        # env: /opt/KeystackTests/Envs/Samples/qa.yml
                        self.envFileFullPath = env
                        # Get the env name with the namespace
                        regexMatch = re.search(f'.+/Envs/(.+)\.(yml|yaml)?', env)
                        if regexMatch:
                            env = regexMatch.group(1)
                        
                        envNameForResultPath = env.replace('/', '-')
                                           
                        if os.path.exists(self.envFileFullPath):
                            envDetails = readYaml(self.envFileFullPath)
                            isEnvParallelUsed = envDetails.get('parallelUsage', False)
                                                   
                        # Using envMgmt file to keep track of the env usage especially if -holdEnvsIfFailed was included.
                        # KeystackUI sessionMgmt creates an onclick button to release the envs when done debugging.
                        # Every stage/module/env has its own json envMgmt data file
                        envMgmtData = {'user':self.user, 'sessionId':self.timestampFolderName,
                                       'stage':stage, 'module':moduleName, 'env':env, 
                                       'envIsReleased': False, 'holdEnvsIfFailed': self.holdEnvsIfFailed, 'result': 'Failed'}
                        envMgmtDataFile = f'{self.envMgmtDataFolder}/STAGE={stage}_MODULE={moduleName}_ENV={envNameForResultPath}.json'
                        writeToJson(envMgmtDataFile, envMgmtData, mode='w') 
                        chownChmodFolder(envMgmtDataFile, self.user, GlobalVars.userGroup, stdout=False) 
                    else:
                        envMgmtDataFile = f'{self.envMgmtDataFolder}/STAGE={stage}_MODULE={moduleName}_ENV=None.json'
                        isEnvParallelUsed = ''
                        
                        if env == 'bypass':
                            envNameForResultPath = 'Bypass'
                            self.envFileFullPath = 'bypass'
                            env = 'bypass'
                        else:
                            envNameForResultPath = 'None'
                            self.envFileFullPath = None
                            env = None

                    # User might not have included some module params: env, loadBalanceGroup, verifyPatterns, etc.
                    # Have to include it for generateReport to state the env used.
                    # Have to manually include artifactsRepo for user's scripts to consume the path
                    moduleProperties.update({'env': env, 'loadBalanceGroup':loadBalanceGroup, 'artifactsRepo': self.artifactsRepo,
                                             'verifyFailurePatterns': verifyFailurePatterns})
                    moduleResultsFolder = f'{self.timestampFolder}/STAGE={stage}_MODULE={moduleName}_ENV={envNameForResultPath}'   
                    makeFolder(moduleResultsFolder, stdout=False)
                    
                    self.moduleSummaryDataFile = f'{moduleResultsFolder}/moduleSummary.json'
                    self.moduleSummaryData = {'user': self.user,
                                              'playbook': self.playbook,
                                              'stage': stage,
                                              'module': moduleName,
                                              'env': env,
                                              'loadBalanceGroup': loadBalanceGroup,
                                              'envPath': self.envFileFullPath,
                                              'isEnvParallelUsed': isEnvParallelUsed,
                                              'playlistExclusions': moduleProperties.get('playlistExclusions', []),
                                              'envParams': {},
                                              'status': 'Did-Not-Start',
                                              'result': None,
                                              'exceptionErrors': [],
                                              'pretestErrors': [],
                                              'moduleResultsFolder': moduleResultsFolder,
                                              'abortModuleFailure': self.abortModuleFailure,
                                              'showResultDataForNumberOfDays': 10,
                                              'currentlyRunning': None,
                                              'stopped': '',
                                              'testDuration': '',
                                              'totalPassed': 0,
                                              'totalFailed': 0,
                                              'totalFailures': 0,
                                              'pausedOnError': '',
                                              'totalTestAborted': 0,
                                              'totalSkipped': 0}

                    writeToJson(self.moduleSummaryDataFile, data=self.moduleSummaryData, mode='w')
                    
                    testcases = moduleProperties['playlist']
                    
                    if self.playbookTasks['stages'][stage].get('runModulesInParallel', False):
                        if runModulesInParallel and doOnceFlagForParallelLocks:                   
                            self.lock = threading.Lock()
                            self.mainLogFileLock = threading.Lock()
                            doOnceFlagForParallelLocks = False
            
                    # Run each Playbook module in its own instance 
                    self.mainObj = Main(playbookObj=self, playbook=self.playbook, module=moduleName,        
                                        envFile=self.envFileFullPath, stage=stage, moduleEnvMgmtFile=envMgmtDataFile,
                                        testcases=testcases, playbookGlobalSettings=self.playbookGlobalSettings,
                                        stageProperties=stageProperties, moduleProperties=moduleProperties,
                                        emailResults=self.emailResults,
                                        debugMode=self.debug, moduleResultsFolder=moduleResultsFolder, 
                                        timestampRootLevelFolder=self.timestampFolder, sessionId=self.sessionId,
                                        pauseOnError=self.pauseOnError, holdEnvsIfFailed=self.holdEnvsIfFailed,
                                        user=self.user, isFromKeystackUI=self.isFromKeystackUI,
                                        awsS3Upload=self.awsS3Upload, statusFileLock=self.lock,
                                        mainLogFileLock=self.mainLogFileLock, jira=self.jira, wireshark=self.wireshark,
                                        startLsu=self.startLsu, execRestApiObj=self.execRestApiObj)
                
                    if runModulesInParallel:
                        threadObj = threading.Thread(target=self.mainObj.run, name=f'{stage}-{moduleName}-{env}')
                        threadObj.start()
                        print(f'\nkeystack.py runPlaybook(): runInParallel starting: {threadObj.name}')
                        threadList.append(threadObj)
                    else:
                        self.lock = False
                        self.mainObj.run()
                    
                    # Delay each test in case the tests are using the same env and if they finish very fast.
                    # Not enough time to holdEnvsIfFailed.
                    time.sleep(.5)
                                                    
            if runModulesInParallel:
                while True:
                    breakoutCounter = 0

                    for eachJoinThread in threadList:
                        print(f'\nkeystack.py runPlaybook(): runInParallel thread completed: {eachJoinThread.name}')
                        eachJoinThread.join()
                    
                        if eachJoinThread.is_alive():
                            print(f'\n{eachJoinThread.name} is still alive\n')
                        else:
                            print(f'{eachJoinThread.name} alive == {eachJoinThread.is_alive}\n')
                            breakoutCounter += 1
        
                    if breakoutCounter == len(threadList):
                        print('\nAll threads are done\n')
                        break
                    else:
                        time.sleep(1)
                        continue
                    
        except Exception as errMsg:
            #msg = f'Playbook runModules exception: {traceback.format_exc(None, errMsg)}'
            msg = f'Playbook runModules exception: {str(errMsg)}'
            self.exceptionErrors.append(str(errMsg))
            writeToJson(self.overallSummaryDataFile, data=self.overallSummaryData, mode='w')
            raise Exception(msg)

    def createEnvMgmtDataFile(self, stage, moduleName, envFileFullPath):
        """ 
        This is a helper function that creates an envMgmt data file when a load balance 
        group selects an Env to use.
        
        Ex: /opt/KeystackTests/Results/GROUP=Default/PLAYBOOK=Samples-pythonSample/05-18-2023-13:45:25:548001_2445/.Data/EnvMgmt
        """                       
        # Create an env mgmt file in:  /timestampFolder/.Data/EnvMgmt
 
        # Get the env name with the namespace
        regexMatch = re.search(f'.+/Envs/(.+)\.(yml|yaml)?', envFileFullPath)
        if regexMatch:
            env = regexMatch.group(1)
        
        envNameForResultPath = env.replace('/', '-')
                                    
        if os.path.exists(envFileFullPath):
            envDetails = readYaml(envFileFullPath)
            isEnvParallelUsed = envDetails.get('parallelUsage', False)
                                    
        # Using envMgmt file to keep track of the env usage in case -holdEnvsIfFailed was included in the test.
        # KeystackUI sessionMgmt creates an onclick button to release the envs when done debugging.
        # Every stage/module/env has its own json envMgmt data file
        envMgmtData = {'user':self.user, 'sessionId':self.timestampFolderName,
                       'stage':stage, 'module':moduleName, 'env':env, 
                       'envIsReleased': False, 'holdEnvsIfFailed': self.holdEnvsIfFailed, 'result': 'Failed'}
        envMgmtDataFile = f'{self.envMgmtDataFolder}/STAGE={stage}_MODULE={moduleName}_ENV={envNameForResultPath}.json'
        writeToJson(envMgmtDataFile, envMgmtData, mode='w') 
        chownChmodFolder(envMgmtDataFile, self.user, GlobalVars.userGroup, stdout=False) 
         
        return envMgmtDataFile
             
    def getLoginCredentials(self):
        """ 
        Get the login details from file .loginCredentials.yml
        """
        isAnyEnabled = False
        for platform in [self.jira, self.awsS3Upload]:
            if platform:
                isAnyEnabled = True
                
        if isAnyEnabled == False:
            return

        if 'loginCredentialKey' not in self.playbookGlobalSettings:
            raise Exception(f'You did not set which loginCredentialKey to use in playbook.globalSettings.')

        self.credentialYmlFile = f'{GlobalVars.keystackSystemPath}/.loginCredentials.yml'

        if os.path.exists(self.credentialYmlFile) == False:
            raise Exception(f'Login credentials file not found: {self.credentialYmlFile}.')
        
        loginCredentialObj = readYaml(self.credentialYmlFile)
        self.loginCredentialKey = self.playbookGlobalSettings['loginCredentialKey']
        if self.loginCredentialKey not in loginCredentialObj:
            raise Exception(f'Playbook globalSettings:loginCredentialKey "{self.loginCredentialKey}" does not exists in the loginCredentials.yml file')
            
        self.loginCredentials = loginCredentialObj[self.loginCredentialKey]
        
    def getRestApiMods(self):
        """
        Allow users to create a dynamic Playbook from blank or 
        modify the Playbook, the Playbook module Pplaylist and
        the Playbook module Env.
        
        Overwrite the self.playbookTasks with rest api mods (playbookConfigs).
        The rest api include the param -isFromKeystackUI as a flag.
           
        feature: KeystackSystemEnv | testcase | env | playbook 
        """
        # <sessionId>_configurations.json
        for modFile in glob(f'{self.restApiModsFolder}/*'):
            if '~' in modFile:
                os.remove(modFile)
                continue

            # The rest api mod file timestamp folder: 11-14-2022-09:44:08:336539_dynamicPlaybook
            # must be the same as -resultFolder. playbookView/runPlaybook created a timestamp folder
            # for both to match
            timestampResultFolder = modFile.split('/')[-1]
            timestampFolderName = self.timestampFolder.split('/')[-1] # Incoming timestamp folder name

            if timestampFolderName == timestampResultFolder:
                modsObj = readJson(modFile)
                # {"KeystackSystemEnv": {}, "testcase": [], "env": {}, "playbook": {}, "createDynamicPlaybook": False}
                self.restApiMods.update(modsObj)
                os.remove(modFile)
       
                if self.restApiMods['createDynamicPlaybook'] == False:
                    # Playbook: Update with the playbook
                    if self.restApiMods['playbook']:
                        self.playbookTasks = updateDict(self.playbookTasks, self.restApiMods['playbook'])
                        writeToYamlFile(self.playbookTasks, f'{self.sessionDataFolder}/playbook_{self.playbookName}.yml')
                else:
                    # Create a dynamic playbook from scratch
                    self.playbookTasks = self.restApiMods['playbook']
                    writeToYamlFile(self.playbookTasks, f'{self.sessionDataFolder}/playbook_dynamically-created.yml')

                # Testcases: Will be updated in readYmlTestcaseFile() using testcaseDict 
                # Env: Will be updated in Main() class
                   
    def createTestReport(self):
        """ 
        Note:
            Most of these properties were created in the Main() class in the generateReport() 
            function using the self.playbookObj, which in this Playbook class.
        """
        # overallSummary: {'group': 'Default', 'processId': 1725064, 'keystackVersion': '0.10.0', 'user': 'hgee', 'playbook': '/opt/KeystackTests/Playbooks/Samples/pythonSample.yml', 'loginCredentialKey': None, 'trackResults': False, 'abortTestOnFailure': False, 'includeLoopTestPassedResults': False, 'testAborted': False, 'stageFailAborted': False, 'status': 'Completed', 'result': None, 'exceptionErrors': [], 'warnings': [], 'sessionId': 4231, 'topLevelResultFolder': '/opt/KeystackTests/Results/GROUP=Default/PLAYBOOK=Samples-pythonSample/06-29-2023-17:34:42:321074_4231', 'started': '2023-06-29 17:34:42.313590', 'stopped': '', 'testDuration': '', 'totalCases': 0, 'totalFailures': 0, 'totalPassed': 0, 'totalFailed': 0, 'totalSkipped': 0, 'totalTestAborted': 0, 'totalKpiPassed': 0, 'totalKpiFailed': 0, 'pausedOnError': None, 'holdEnvsIfFailed': False, 'stages': {'Test': {'result': None, 'modules': []}}, 'runList': [], 'notes': []}            
            
        try:
            self.stopTime = datetime.datetime.now()
            self.stopTime.strftime('%m-%d-%Y %H:%M:%S')
            self.duration = str((self.stopTime - self.startTime))

            if os.environ.get('keystack_reportSubject', None):
                reportSubject = os.environ['keystack_reportSubject']
            else:
                # Default report subject
                reportSubject = f"Keystack Report: PipelineId:{self.sessionId}   Result:{self.result}\n"
                reportSubject += f"{' ':17s}TotalCases:{self.totalCases}  TotalPassed:{self.overallSummaryData['totalPassed']}  TotalFailed:{self.overallSummaryData['totalFailed']}\n"
                reportSubject += f"{' ':17s}SkippedTestcases:{self.overallSummaryData['totalSkipped']}  AbortedTestcases:{self.overallSummaryData['totalTestAborted']} AbortedStages:{len(self.abortedStages)}"
                    
            # Allow users to customize the email subject line with these replacement values
            for replace in [{'{{datetime}}':         getTimestamp(includeMillisecond=False)},
                            {'{{totalPassed}}':      str(self.overallSummaryData['totalPassed'])},
                            {'{{totalFailed}}':      str(self.overallSummaryData['totalFailed'])},
                            {'{{totalTestAborted}}': str(self.overallSummaryData['totalTestAborted'])},
                            {'{{totalTestcases}}':   str(self.totalCases)},
                            {'{{totalSkipped}}':     str(self.overallSummaryData['totalSkipped'])},
                            {'{{result}}':           str(self.result)},
                            {'{{pipelineId}}':       str(self.sessionId)}]:
                
                reportSubject = reportSubject.replace(list(replace.keys())[0], list(replace.values())[0])    
                
            self.subjectLine = reportSubject
            useDefaultReportHeadings = True
            reportHeadingAdditions = ''
            
            if self.abortStageFailure:
                abortedStageMsg = f'Aborted Stages: ' 
                for stage in self.abortedStages:
                    abortedStageMsg += f'{stage} '
            
            if self.skippedStages:
                skippedStages = f'Skipped Stages: ' 
                for stage in self.skippedStages:
                    skippedStages += f'{stage} '
                                        
            # Additional report header tags from playbooks
            if self.playbookGlobalSettings.get('reportHeadingAdditions', None):
                for pairValue in self.playbookGlobalSettings['reportHeadingAdditions']:
                    for key,value in pairValue.items():
                        reportHeadingAdditions += f'{key}: {value}\n'

            if os.environ.get('keystack_reportHeadings', None):
                useDefaultReportHeadings = False
                self.overallTestReportHeadings = os.environ['keystack_reportHeadings']

                for replace in [{'{{totalTestcases}}':   str(self.totalCases)},
                                {'{{totalPassed}}':      str(self.overallSummaryData['totalPassed'])}, 
                                {'{{totalFailed}}':      str(self.overallSummaryData['totalFailed'])},
                                {'{{totalSkipped}}':     str(self.overallSummaryData['totalSkipped'])}, 
                                {'{{totalTestAborted}}': str(self.overallSummaryData['totalTestAborted'])},
                                {'{{startTime}}':        str(self.startTime)},
                                {'{{stopTime}}':         str(self.stopTime)},
                                {'{{duration}}':         str(self.duration)},
                                {'{{playbook}}':         self.playbookName},
                                {'{{testResultPath}}':   self.timestampFolder},
                                {'{{reportHeadingAdditions}}': reportHeadingAdditions},
                                {'{{pipelineId}}':             str(self.sessionId)}
                                ]:
                    
                    self.overallTestReportHeadings = self.overallTestReportHeadings.replace(list(replace.keys())[0], list(replace.values())[0])
            
            if useDefaultReportHeadings:
                # Default report header
                self.overallTestReportHeadings =  f"Playbook Executed: {self.playbookName}\n"
                self.overallTestReportHeadings += f'Test Result Path: {self.timestampFolder}\n'
                self.overallTestReportHeadings += f'Start Time: {self.startTime}\n'
                self.overallTestReportHeadings += f'Stop Time: {self.stopTime}\n'
                self.overallTestReportHeadings += f'Duration: {self.duration}\n'
                        
            if self.putFailureDetailsAfterResults:
                combineFailureDetails = ''
                for eachFailure in self.putFailureDetailsAfterResults:
                    for testcase, failureDesc in eachFailure.items():
                        combineFailureDetails += f'{failureDesc}\n'

                self.reportBody =  f'{self.subjectLine}\n\n'
                if self.abortStageFailure:
                    self.reportBody += f'{" ":17s}{abortedStageMsg}\n'
                if self.skippedStages:
                    self.reportBody += f'{" ":17s}{skippedStages}\n'                    
                self.reportBody += f'{self.overallTestReportHeadings}\n'     
                self.reportBody += f'{self.overallTestReport}\n\n'
                self.reportBody += f'Failure Details:\n\n{combineFailureDetails}\n'
            else:
                self.reportBody =  f'{self.subjectLine}\n'
                if self.abortStageFailure:
                    self.reportBody += f'{" ":17s}{abortedStageMsg}\n'
                if self.skippedStages:
                    self.reportBody += f'{" ":17s}{skippedStages}\n'
                self.reportBody += f'\n{self.overallTestReportHeadings}\n'       
                self.reportBody += f'{self.overallTestReport}'
        
            writeToFileNoFileChecking(f'{self.timestampFolder}/testReport', self.reportBody, mode='w')
            print(f'\n{self.reportBody}')

            self.overallSummaryData.update({'stopped': str(self.stopTime), 
                                            'testDuration': self.duration,
                                            'totalCases': self.totalCases,
                                            'result': self.result, 
                                            'status': self.overallSummaryData['status']})  
            
            writeToJson(self.overallSummaryDataFile, data=self.overallSummaryData, mode='w', retry=3)
        except Exception as errMsg:
            raise Exception('CreateTestReport: None. Test did not run successfully.')
            
    def emailReport(self):
        """ 
        Emailing depends on the Linux server running 
        Keystack having postfix installed and running
        """
        sendTo = None
        attachments = []
        
        if self.emailResults:
            if self.debug and 'keystack_devModeEmailTo' in os.environ:
                sendTo = os.environ['keystack_devModeEmailTo']
            else:
                if 'keystack_emailTo' in os.environ:
                    sendTo = os.environ['keystack_emailTo']
            
            if sendTo is None:
                print('\nNo Email sent.  keystack_emailTo was not defined in keystackSystemSettings.env\n')
                return

            if self.trackResults:
                attachments.append(self.updateCsvDataFile)
                
            sendEmail(emailTo=sendTo,
                      fromSender=os.environ['keystack_emailFrom'],
                      subject=self.subjectLine,
                      bodyMessage=self.reportBody,
                      emailAttachmentList=attachments) 
            print()
    
    def recordResults(self):
        """ 
        Track results for graphing
        """
        # TODO: Use mongoDB
        
        if self.trackResults == False or self.debug:
            return

        resultDataHistoryPath = f'{GlobalVars.resultHistoryPath}/{self.playbookName}'
        lockFile = f'{resultDataHistoryPath}/lock'
        
        if Path(resultDataHistoryPath).exists() == False:
            mkdir2(resultDataHistoryPath, stdout=False)
            chownChmodFolder(resultDataHistoryPath, self.user, GlobalVars.userGroup, stdout=False)
        
        daysToKeepData = os.environ.get('keystack_trackResultsForHowManyDays', 14)
        now = datetime.datetime.now()
        nowStringFormat = now.strftime('%m-%d-%Y %H:%M:%S')
        format = '%m-%d-%Y %H:%M:%S'
        resultData = dict()
        
        columnHeaders = ['dateTime', 'totalTestcases', 'result', 'totalPassed', 'totalFailed',
                         'totalAborted', 'totalSkipped', 'totalKpiPassed', 'totalKpiFailed']

        resultData = {'dateTime':       nowStringFormat, 
                      'totalTestcases': str(self.totalCases),
                      'result':         self.result, 
                      'totalPassed':    str(self.overallSummaryData['totalPassed']), 
                      'totalFailed':    str(self.overallSummaryData['totalFailed']),
                      'totalAborted':   str(self.overallSummaryData['totalTestAborted']),
                      'totalSkipped':   str(self.overallSummaryData['totalSkipped']),
                      'totalKpiPassed': str(self.overallSummaryData['totalKpiPassed']),
                      'totalKpiFailed': str(self.overallSummaryData['totalKpiFailed']),
                      }
                    
        selfRemovingLockCounter = 1
        breakLockCount = 10
        while True:
            try:
                if Path(lockFile).exists() and selfRemovingLockCounter <= breakLockCount:
                    print(f'recordResults: Track file is locked. Wait {selfRemovingLockCounter}/{breakLockCount} secs')
                    time.sleep(1)
                    selfRemovingLockCounter += 1
                    
                if Path(lockFile).exists() == False and selfRemovingLockCounter <= breakLockCount:
                    execSubprocessInShellMode(f'touch {lockFile}', showStdout=False)
                    execSubprocessInShellMode(f'chown {GlobalVars.user}:{GlobalVars.userGroup} {lockFile}', showStdout=False)
                    execSubprocessInShellMode(f'chmod 770 {lockFile}', showStdout=False)
                    selfRemovingLockCounter = 1
                    break

                if Path(lockFile).exists() and selfRemovingLockCounter == breakLockCount:
                    # Just take over and remove the lock when done
                    print(f'recordResults: {selfRemovingLockCounter}/{breakLockCount}: Taking over the lock for playbook: {self.playbookName}')
                    selfRemovingLockCounter = 1
                    break  
                
            except:
                # In case there is an I/O error clash between multiple instances 
                # trying to read/write to the same csv file
                time.sleep(1)
                continue        

        # Each playbook folder should only have one .csv file
        currentCsvFile = glob(f'{resultDataHistoryPath}/*.csv')
        
        if not currentCsvFile:
            # Initiate a new CSV file
            currentCsvFile = f'{resultDataHistoryPath}/{self.playbookName}.csv'
            
            # Create the header column names
            with open(currentCsvFile, 'w') as dataFileObj:
                writer = csv.DictWriter(dataFileObj, fieldnames=columnHeaders)
                writer.writeheader()  

        if type(currentCsvFile) is list:
            currentCsvFile = currentCsvFile[0] 
                    
        # Append the new result to the current csv file
        with open(currentCsvFile, 'a') as fileObj:
            writer = csv.DictWriter(fileObj, fieldnames=columnHeaders)
            writer.writerow(resultData)

        with open(currentCsvFile, 'r') as fileObj:    
            reader = csv.reader(fileObj)
            keepRowsList = []
            removeRowList = []
            
            for rowNumber, row in enumerate(reader, start=0):
                if rowNumber == 0: 
                    continue
    
                datetimeObj = datetime.datetime.strptime(row[0], format)
                deltaObj = now.date() - datetimeObj.date()
                days = deltaObj.days
                if days <= int(daysToKeepData):
                    # Keep the rows that are within the specified days to keep
                    keepRowsList.append(row)
                else:
                    removeRowList.append(row)
                    
        if len(removeRowList) > 0:
            # The next CSV file
            randomNumber = random.sample(range(1,1000), 1)[0]
            self.updateCsvDataFile = f'{resultDataHistoryPath}/{self.playbookName}_{randomNumber}.csv'

            with open(self.updateCsvDataFile, 'w') as fileObj:
                writer = csv.writer(fileObj)
                writer.writerow(columnHeaders)
                writer.writerows(keepRowsList)
            
            os.remove(currentCsvFile)
        else:
           self.updateCsvDataFile = currentCsvFile
        
        execSubprocessInShellMode(f'chown :Keystack {self.updateCsvDataFile}', showStdout=False)
        
        try:     
            os.remove(lockFile)
        except:
            # It is ok to error out because the while loop will remove the lock file
            # after the default timer
            pass
        
        # Clean up: Get a list of known Playbooks and remove all non-existing playbooks from
        # the /opt/KeystackSystems/resultDataHistory folder
        
    def waitForS3UploadToComplete(self):
        """
        For docker only.
        
        Once the test is done, Keystack container might exit immediately 
        while the S3 transfer was still transferring in the background.
        Need to verify the staging folder until the test results timestamp folder is 
        removed by the keystackAwsS3 background process. Otherwise, S3 will have missing files and folders.
        """
        # AWS S3 login credentials could be failing. Don't keep logging.
        # User must restore login issue and restart the keystackAwsS3 services manually.
        if self.awsS3ServiceObj.isServiceRunning('keystackAwsS3') == False:
            return
        
        print('\nwaitForS3UploadToComplete ...')
        filesToUpload = glob(f'{Serviceware.vars.awsS3StagingFolder}/*')
        self.awsS3ServiceObj.writeToServiceLogFile(msgType='info', msg=f'waitForS3UploadToComplete: {filesToUpload}',
                                                   playbookName=self.playbookName, sessionId=self.sessionId)
                        
        selfExitCounter = 1800
        counter = 0
        while True:
            currentAwsS3UploadFolder = glob(f'{Serviceware.vars.awsS3StagingFolder}/*')
            
            # S3 copy is not done as long as files exist in the staging folder  
            if counter < selfExitCounter and len(currentAwsS3UploadFolder) == 0:
                self.awsS3ServiceObj.writeToServiceLogFile(msgType='info', msg=f'waitForS3UploadToComplete: Done',
                                                           playbookName=self.playbookName, sessionId=self.sessionId)
                return 
            
            if counter < selfExitCounter and len(currentAwsS3UploadFolder) > 0:
                counter += 1
                time.sleep(1)
            
            if counter == selfExitCounter and len(currentAwsS3UploadFolder) > 0:
                # TODO: Write problem to /KeystackTests/KeystackSystem/Logs/awsS3ServiceLogs
                self.awsS3ServiceObj.writeToServiceLogFile(msgType='info', msg=f'waitForS3UploadToComplete error: It has been {counter}/{selfExitCounter} seconds and S3 transfer is still not done: {Serviceware.vars.awsS3StagingFolder}', playbookName=self.playbookName, sessionId=self.sessionId)
                break
            
                                                
class Main():
    def __init__(self, playbookObj=None, playbook=None, stage=None, module=None, envFile=None, moduleEnvMgmtFile=None,
                 testcases=None, playbookGlobalSettings=None, overallSummaryData=None, sessionId=None,
                 moduleProperties=None, stageProperties=None, emailResults=False, debugMode=False,
                 moduleResultsFolder=None, timestampRootLevelFolder=None, pauseOnError=False, holdEnvsIfFailed=False, 
                 user=None, awsS3Upload=False, wireshark=False, startLsu=False, isFromKeystackUI=False,
                 statusFileLock=None, mainLogFileLock=None, jira=False, execRestApiObj=None):
        """
        Keystack mainframe that runs a module playlist
        
        Parameters
            isFromKeystackUI <bool>:            If True, the job came from the UI (docker). Used internally to know which
                                                Python path to use: docker python path or local linux host python path.
            playbookObj <obj>:                  The Playbook object to pass data from Main to Playbook level.
            playbook <str>:                     The full path to the playbook to play.
            stage <str>:                        The stage the module is in.
            module <str>:                       Mandatory: The module to run for this test.  Just the module name without the path.
            envFile <ymal file>:                Optional: None | A full path test env .yml file that contains test env 
                                                IP addresses, login credentials, environment config settings.      
                                                credentials, etc, without the path.
            moduleEnvMgmtFile <str>:            The module's envMgmt file in /timstampResultFolder/.Data/EnvtMgmt.
                                                Use this file to track module result and holdEnvsIfFailed for ReleaseEnv to 
                                                utilize.
            testcases <folderPaths|yamlFiles>:  Mandatory: One or more folders containing testcase yaml files. Could also include
                                                individual yaml files. If it's a folder, all subfolders yaml files are
                                                executed also.
            playbookGlobalSettings:             The Playbook's global setting parameters.
            moduleProperties <dict>:            From playbook. Each module properties/values.
            stageProperties <dict>:             From Playbook. Each stage properties/values.
            emailResults <bool>:                Optional: Send email results at the end of the test.
            debugMode <bool>:                   Optional: True = State 'Dev-Mode' in email result subject line and state debugMode 
                                                on the test timestamp folder.
            overallSummaryData <dict>:          The initial overall summary data that goes at the top-level timestamp folder.
            pauseOnError <bool>:                Pause the test on failure for debugging.
            holdEnvsIfFailed <bool>:            Don't release the env setups if the test failed for debugging.
            sessionId <int>:                    Optional: For referencing the test in KeystackUI and results folder
            moduleResultsFolder <str>:          Results/Logs for the module.
            timestampRootLevelFolder <str>:     Ex: /KeystackTests/Results/Playbook_L3Testing/04-20-2022-12:29:57:258836_hgee
            user <str>:                         Optional: The logged in user.
            awsS3 <bool>:                       Upload results to AWS S3 Data-Lake
            statusFileLock <threadLock>:        File lock for overallSummary.json file
            mainLogFileLock <threadLock>:       File lock for the main debug log file and metadata.json
            execRestApiObj <None|Obj>:          Used for sending REST APIs. For EnvMgmt / holdEnvsIfFailed
        """
        try:
            self.lock = statusFileLock
            self.mainLogFileLock = mainLogFileLock
            if jira:
                self.jiraLogFileLock = threading.Lock()

            self.isFromKeystackUI = isFromKeystackUI
            self.execRestApiObj = execRestApiObj
            self.playbookObj = playbookObj
            self.stage = stage
            self.playbookName = playbook.split('/')[-1].split('.')[0]
            # The module name only
            self.module = module
            self.moduleEnvMgmtFile = moduleEnvMgmtFile
            self.keystackRootPath = GlobalVars.keystackRootPath
            self.keystackTestRootPath = GlobalVars.keystackTestRootPath
            self.keystackSystemPath = GlobalVars.keystackSystemPath
            self.modulePath = f"{GlobalVars.keystackTestRootPath}/Modules/{module}"
            sys.path.append(self.modulePath)
            self.moduleProperties = moduleProperties
            self.stageProperties = stageProperties
            
            # envFile could be either None or bypass or actual env file
            # Bypass is used in playbook modules to explicity exclude an Env if 
            # the env or loadBalanceGroup is set at globalSettings or stage
            self.envFile = envFile
            if envFile not in [None, 'bypass']:
                self.env = envFile.split('/Envs/')[-1].split('.')[0]
            if envFile is None:
                self.env = None
            if envFile == 'bypass':
                self.env = 'bypass'
  
            self.testcasesPath  = f"{self.modulePath}/Testcases"

            # For storing exported config files
            self.exportedConfigsFolder = f"{self.modulePath}/ExportedConfigs"
            # For script specific variables / data-model yml files
            self.dataFilesFolder = f"{self.modulePath}/DataFiles"
            # These configs are modifying the exported configs that are getting loaded at runtime
            # These params could also reside in the env file and testcase file under configParams
            self.configParametersFilePath = f"{self.modulePath}/ConfigParameters"
            
            self.testResultPlaybookPath = f'{GlobalVars.keystackTestRootPath}/Results/GROUP={self.playbookObj.testGroup}/PLAYBOOK={self.playbookName}'
            self.runTestcases = testcases
            self.testAbortions = 0
            self.pauseOnError = pauseOnError
            self.holdEnvsIfFailed = holdEnvsIfFailed
            self.emailResults = emailResults
            self.debug = debugMode
            self.awsS3UploadResults = awsS3Upload
            self.sessionId = sessionId
            self.jira = jira
            self.wireshark = wireshark ;# Currently for AirMosaic
            self.startLsu = startLsu ;# For AirMosaic
            self.user = user
            self.playbookObj.airMosaicCellList = [] ;# From airMosaic.py. Get the tested cells used and show in the report
            
            # The module results folder:
            # /Results/Playbook_L3Testing/04-20-2022-12:34:22:409096_<sessionId>/STAGE=Test_MODULE=PythonScripts_ENV=None
            self.moduleResultsFolder = moduleResultsFolder

            # For storing keystack_detailLogs: /KeystackTests/Results/Playbook_L3Testing/04-20-2022-12:29:57:258836_<sessionId>
            self.resultsTimestampFolder = timestampRootLevelFolder
            self.timestampFolderName = timestampRootLevelFolder.split('/')[-1]
            
            # A main debug log file used to show which test got executed, errors/abortions and end results
            self.debugLogFile   = f'{self.resultsTimestampFolder}/detailLogs' 
            self.testReportFile = f"{self.resultsTimestampFolder}/testReport" ;# overall test report
            self.moduleTestReportFile = f'{self.moduleResultsFolder}/moduleTestReport'

            if awsS3Upload:
                self.awsS3ServiceObj = Serviceware.KeystackServices(typeOfService='keystackAwsS3', isFromKeystackUI=isFromKeystackUI)
                self.s3StagingFolder = Serviceware.vars.awsS3StagingFolder
                if self.awsS3ServiceObj.isServiceRunning('keystackAwsS3') == False:
                    
                    # f'{currentDir}/Services/keystackAwsS3.py'
                    if self.isFromKeystackUI:
                        pythonPath = os.environ.get('keystack_dockerPythonPath', GlobalVars.dockerPythonPath)
                        cmd = f'{pythonPath} {Serviceware.vars.keystackAwsS3Service} -isFromKeystackUI > /dev/null 2>&1 &'
                    else:
                        pythonPath = os.environ.get('keystack_pythonPath', None)
                        cmd = f'{pythonPath} {Serviceware.vars.keystackAwsS3Service} > /dev/null 2>&1 &'
                        
                    self.awsS3ServiceObj.writeToServiceLogFile(msgType='info', msg=f'keystack: start keystackAwsS3 service: {cmd} ...',
                                                               playbookName=self.playbookObj.playbookName, sessionId=self.playbookObj.sessionId)
                    
                    try:
                        result = subprocess.call(cmd, shell=True)
                    except Exception as errMsg:
                        msg = f'Serviceware failed to start keystackAwsS3: {errMsg}'
                        self.awsS3ServiceObj.writeToServiceLogFile(msgType='error', msg=f'keystack: start keystackAwsS3 service: {msg}',
                                                                   playbookName=self.playbookObj.playbookName, sessionId=self.playbookObj.sessionId)  
                        raise Exception(msg)
                    
                    if self.awsS3ServiceObj.isServiceRunning('keystackAwsS3') == False:
                        msg = f'Serviceware failed to start keystackAwsS3'
                        self.awsS3ServiceObj.writeToServiceLogFile(msgType='failed', msg=msg,
                                                                   playbookName=self.playbookObj.playbookName, sessionId=self.playbookObj.sessionId)  
                        raise Exception(msg)
                    
            # These datetime are used in emailing result summary
            self.testStartTime = datetime.datetime.now()
            self.testStopTime = None 
                        
            # Initital envParams containing all module properties.
            # Testcases will be updated in getAllTestcaseFiles()
            self.envParams = {'playbook': playbook,
                              'modules': self.playbookObj.playbookTasks['stages']}

            if self.playbookName != 'Dynamically-Created':
                if 'playbook' in self.playbookObj.restApiMods and self.playbookObj.restApiMods['playbook']:
                    self.envParams['playbook'] = f'{playbook} - modified'
                
            # Env system settings have been read in runPlaybook
            for envParam,value in os.environ.items():
                if envParam.startswith('keystack_'):
                    envParam = envParam.replace('keystack_', '')
                    if value in ['True', 'true', 'yes', 'Yes']:
                        value = True
                    if value in ['False', 'false', 'no', 'No']:
                        value = False
                    if value in ['None', 'null']:
                        value = None
                        
                    self.envParams.update({envParam: value})

            # Update/overwrite envParams with Playbook global settings
            # This means that any params in the keystackSystemSettings.env could go in playbooks.
            self.envParams.update(playbookGlobalSettings)

            # These playbook params are common in globalSettings, stage and modules.
            for commonParam in ['abortModuleFailure', 'variables', 'verifyFailurePatterns', 'env', 'loadBalanceGroup']:
                # OVERWRITE globalSettings at stage level
                if commonParam in self.stageProperties['stage'][self.stage]:
                    self.envParams[commonParam] = self.stageProperties['stage'][self.stage][commonParam]
                        
                # OVERWRITE stage properties at module level
                if commonParam in self.moduleProperties:
                    self.envParams[commonParam] = self.moduleProperties[commonParam]
            
            # Env files could contain two type of resources:
            # 1> Env IP, login credentials, license server, etc.
            #    These env resources are stored in self.moduleProperties['envParams']
            # 2> It could also contain testcase "configs". Users put them in env files so the configs could apply to all testcases.
            #    To overwrite them, put specific configs in the testcase yml file's configs key.
            #    In the env file, use the key "configs" and these testcase configs are stored in self.moduleProperties['configs'].
            #    When reading testcase yml files, Keystack looks for "configs". If exists, overwrite self.moduleProperties['configs'] 
            
            # Use the stated env file in the playbook if no rest api env was not provided for this test module
            # Overwrite env's variables
            if self.envFile and self.envFile != 'bypass':
                testEnvParams = readYaml(yamlFile=self.envFile, threadLock=self.lock)
                if testEnvParams is None:
                    raise Exception(f'keystack.py: Syntax error in the env file: {self.envFile}')
            
                self.moduleProperties.update({'envParams': testEnvParams})
                    
                # Move the key "configs" to top level so testcaseDict could overwrite it if users defined 
                # the "configs" key in the testcase yml files.
                # And finally in the run() function, 'configs' in the testcase 'ConfigParametersFile' 
                # has highest overwrite precedence.
                if 'configs' in testEnvParams:
                    self.moduleProperties.update({'configParams': testEnvParams['configParams']})
            
            # Use Env settings provied by rest api CLI
            # "env": [
            #     {
            #         "stage": "Test",
            #         "module": "CustomPythonScripts",
            #         "envConfigs": {
            #             "login": false
            #         }
            #     }
            # ]
            if 'env' in self.playbookObj.restApiMods and \
                self.playbookObj.restApiMods['env'] != 'bypass' and \
                len(self.playbookObj.restApiMods['env']) > 0:   
                    for eachEnvMod in self.playbookObj.restApiMods['env']:
                        if eachEnvMod['stage'] == self.stage:
                            if eachEnvMod['module'] == self.module:
                                self.moduleProperties['envParams'].update(eachEnvMod['params'])
                                if self.envFile:
                                    self.moduleProperties.update({'env': f'{self.envFile} - modified'})

            try:
                # Some modules like AirMosaic don't have a config file folder
                self.configFileFolder = self.envParams['configFileFolder']
            except:
                pass

            self.testcaseDict = dict()    
            self.getAllTestcaseFiles(moduleProperties.get('playlistExclusions', []))
                   
            if 'kafkaClusterIp' in self.envParams and self.envParams['kafkaClusterIp'] != "None":
                self.connectToKafka(self.envParams['kafkaClusterIp'])
                
            if self.envParams.get('removeResultsFolder', 5) != 'never':
                removePastFoldersBasedOnFolderTimestamp(self.testResultPlaybookPath,
                                                        removeDaysOlderThan=self.envParams.get('removeResultsFolder', 5))

        except:
            raise

    def writeToTestcaseLogFile(self, msg, writeType='a', includeTimestamp=True, stdout=True): 
        if includeTimestamp:
            timestamp = getTimestamp()
            enhancedMsg = f'{timestamp}: {msg}'
        else:
            enhancedMsg = msg
        
        if stdout:    
            print(f'{enhancedMsg}')
            
        if self.testcaseDebugLogFile:
            with open(self.testcaseDebugLogFile, writeType) as logFile:
                logFile.write(f'\n{enhancedMsg}')
            
    def writeToMainLogFile(self, msg, writeType='a', includeTimestamp=True, printToStdout=True):
        """
        Main log file to show which tests were executed, show abortion error and end results.
        """
        # TODO: Need to remove writing to detailed.log
        return
    
        if self.mainLogFileLock:
            self.mainLogFileLock.acquire()
            
        if includeTimestamp:
            timestamp = getTimestamp()
            enhancedMsg = f'{timestamp}: {msg}'
        else:
            enhancedMsg = msg

        if printToStdout:
            print(f'{enhancedMsg}\n')
            
        with open(self.debugLogFile, writeType) as logFile:
            logFile.write(f'{enhancedMsg}\n\n')
        
        if self.mainLogFileLock:    
            self.mainLogFileLock.release()

    def logInfo(self, msg, includeTimestamp=True):
        """ 
        Log a testcase info to the test case test.log debug file.
        """
        self.writeToTestcaseLogFile(f'[INFO]: {msg}', includeTimestamp=includeTimestamp)
            
    def logWarning(self, msg, includeTimestamp=True):
        """ 
        Log debug messages to show if something had occured.
        All warnings will be appended to the overallSummary.json file for quick view.
        """
        self.writeToTestcaseLogFile(f'[WARNING]: {msg}', includeTimestamp=includeTimestamp)
        self.playbookObj.overallSummaryData['warnings'].append({'testcase': self.testcaseResultsFolder, 'message': msg})
        self.testcaseData['warnings'].append(msg)
        writeToJson(self.playbookObj.overallSummaryDataFile, data=self.playbookObj.overallSummaryData, mode='w')
            
    def logFailed(self, msg, includeTimestamp=True):
        """ 
        Log a testcase failure to the test case test.log debug file.
        """
        self.writeToTestcaseLogFile(f'[FAILED]: {msg}', includeTimestamp=includeTimestamp)
        self.testcaseResult = 'Failed'
        self.moduleSummaryData['totalFailures'] += 1
        self.testcaseData['totalFailures'] += 1
        self.playbookObj.overallSummaryData['totalFailures'] += 1
        self.testcaseData['failures'].append(msg)
    
        if self.pauseOnError:
            self.moduleSummaryData['pausedOnError'] = f'{self.moduleResultsFolder}/pausedOnError'
            self.moduleSummaryData['status'] = 'paused-on-error'
            self.testcaseData['pausedOnError'] = True
            self.testcaseData['status'] = 'paused-on-error'
            writeToJson(self.moduleSummaryFile, self.moduleSummaryData, mode='w', retry=5)
            self.pauseTestOnError()
            self.testcaseData['pausedOnError'] = ''
            self.moduleSummaryData['pausedOnError'] = ''
            self.testcaseData['status'] = 'Running'
            self.moduleSummaryData['status'] = 'Running'
            writeToJson(self.moduleSummaryFile, self.moduleSummaryData, mode='w', retry=5)

    def logDebug(self, msg, includeTimestamp=True):
        """ 
        Log a testcase debug message to the test case test.log debug file.
        """
        self.writeToTestcaseLogFile(f'[DEBUG]: {msg}', includeTimestamp=includeTimestamp)
        
    def logError(self, msg, includeTimestamp=True):
        """ 
        Log a testcase error message to the test case test.log debug file
        and abort the testcase.
        """
        self.writeToTestcaseLogFile(f'[ERROR]: {msg}', includeTimestamp=includeTimestamp)
        raise Exception(msg)

    def updateModuleStatusData(self, status):
        """
        Update the run time overallSummary.json file.
        """
        self.moduleSummaryData['status'] = status
        # Use mode='w' to always overwrite the old data with updated data
        writeToJson(self.moduleSummaryFile, self.moduleSummaryData, mode='w', 
                    threadLock=self.lock, retry=3)
                                         
    def readYmlTestcaseFile(self, ymlTestcaseFile):
        """
        Internal use only.  Read each testcase yml file and store data into a dict.
        
        ymlTestcaseFile: Ex: /opt/KeystackTests/Modules/CustomPythonScripts/Testcases/bgp.yml
        """
        testcaseData = readYaml(ymlTestcaseFile, threadLock=self.lock)
        if testcaseData is None:
            raise Exception(f'Synxtax error in testcase yml file: {ymlTestcaseFile}')
        
        self.testcaseDict[ymlTestcaseFile] = testcaseData

        # Check if the testcase is modified by rest api call
        if self.playbookObj.restApiMods:
            for testcaseModFileDict in self.playbookObj.restApiMods['testcases']:
                # {'/Modules/CustomPythonScripts/Testcases/bgp.yml': {'script': '/Modules/CustomPythonScripts/Scripts/ospf.py'}}
                for testcaseModFile, dataToModify in testcaseModFileDict.items():
                    if testcaseModFile in ymlTestcaseFile:
                        self.testcaseDict[ymlTestcaseFile].update(dataToModify)
                            
    def getAllTestcaseFiles(self, playlistExclusions=[]):
        """
        Collect all the testcases to run  
        """
        self.testcaseSortedOrderList = []

        problems, excludeTestcases = validatePlaylistExclusions(playlistExclusions)
        
        for eachPath in self.runTestcases:
            regexMatch = re.search('.*(Modules/.*)', eachPath)
            if regexMatch:
                eachPath = f'{GlobalVars.keystackTestRootPath}/{regexMatch.group(1)}'
            else:
                raise Exception(f'Playbook playlist must begin with /Modules. Not: {eachPath}')
            
            if Path(eachPath).is_dir():
                # Run all file in folders and subfolders

                for root, dirs, files in os.walk(eachPath):
                    # root ex: starting_path/subFolder/subFolder
                    if files:
                        # Store files in numerical/alphabetic order
                        for eachFile in sorted(files):
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
                                self.readYmlTestcaseFile(f'{eachFile}')
                            
                            self.testcaseSortedOrderList.append(f'{eachFile}')
                            
            else:
                if eachPath.endswith('.yml') or eachPath.endswith('.yaml'):
                    if eachPath in excludeTestcases:
                        continue
                    
                    # Run individual testcase yml file. Don't read .py files
                    self.readYmlTestcaseFile(eachPath)
                
                self.testcaseSortedOrderList.append(eachPath)

        # Keep track of overall test cases from every test module for final playbook report
        self.playbookObj.totalCases += len(self.testcaseSortedOrderList)
               
    def pauseTestOnError(self):
        """ 
        Pause the test when a failure is encountered.
        Remove the pauseOnError file in the result timestamp folder when done 
        debugging to resume testing.
        """
        pauseOnErrorFilePath = f'{self.moduleResultsFolder}/pausedOnError'
        with open(pauseOnErrorFilePath, 'w') as fileObj:
            fileObj.write('')
 
        chownChmodFolder(pauseOnErrorFilePath, self.user, GlobalVars.userGroup, permission=770)      
        
        print(f'\nTest is paused-on-error! Go debug the issue. When done, remove the file: {pauseOnErrorFilePath}\n')
        
        while True:
            if os.path.exists(pauseOnErrorFilePath):
                time.sleep(1)
                continue
            else:
                break

    def generateModuleTestReport(self, modulePretestAborted=False, cells=None):
        """
        Generate a "module" test report.
        An overall test report is combined in the Playbook class.executeTest()    
    
        Parameters
           cells <str>: For AirMosaic only
        """
        if self.debug:
            subjectHeader = 'Debug-Mode: '
        else:
            subjectHeader = ''

        totalSkippedTestcases = 0
        bodyMessage = ''
        self.jiraFailures = {}
        
        # v0.6.1f backward compatability: 
        # keystack_emailPutFailureDescriptionsAfterResultSummary
        if os.environ.get('keystack_emailPutFailureDescriptionsAfterResultSummary', None) in ['True', 'true', 'yes']:
            putFailureDescAtEnd = True
        else:
            putFailureDescAtEnd = False
            
        if os.environ.get('keystack_reportPutFailureDetailsAfterResultSummary', None) in ['True', 'true', 'yes']:
            putFailureDescAtEnd = True
        else:
            putFailureDescAtEnd = False
        
        if modulePretestAborted == False:  
            try:
                totalOuterLoopIterations = int(self.moduleProperties.get('outerLoop', 1))
                index = 0
                
                # For better visibility using string formatting
                longestStringLength = 0
                for tc in self.testcaseSortedOrderList:
                    shortenPath = tc.split(self.modulePath)[-1]
                    if len(shortenPath) > longestStringLength:
                        longestStringLength = len(shortenPath)
                
                # Test Summary
                # Note about totalFailed vs totalFailures:
                #     totalFailed   = testcase failures.
                #     totalFailures = The amount of failures within a testcases.  Uses KPI-Failed
                # /opt/KeystackTests/Results/GROUP=Default/PLAYBOOK=loadcoreSample/11-01-2022-07:27:02:355686_5423/STAGE=LoadCoreTest_MODULE=LoadCore_ENV=loadcoreSample
                
                # /opt/KeystackTests/Results/GROUP=Default/PLAYBOOK=pythonSample/12-03-2022-08:25:28:290086_2733/.Data/ResultsMeta/opt/KeystackTests/Modules/CustomPythonScripts/Samples/Teardowns/teardownDut.yml_1_1
                                
                for outerLoop in range(1, totalOuterLoopIterations+1):
                    for eachTestcase in self.testcaseSortedOrderList:
                        testcaseName = eachTestcase.split('/')[-1].split('.')[0]                       
                        testcaseShortenPath = eachTestcase.split(self.modulePath)[-1]
                        loopTestcaseTotal= self.getLoopTestcaseCount(eachTestcase)
                        for innerLoop in range(1, loopTestcaseTotal+1):
                            testcaseFileName = eachTestcase.split('/')[-1]
                            testcaseResultsMetaFolder = '/'.join(f'{self.playbookObj.resultsMetaFolder}{eachTestcase}'.split('/')[:-1])
                            testcaseResultsMetaFile = f'{self.testcaseResultsMetaFolder}/{testcaseFileName}_{outerLoop}_{innerLoop}'
                            
                            if os.path.exists(testcaseResultsMetaFile):
                                fileSize = os.path.getsize(testcaseResultsMetaFile)
                                if fileSize == 0:
                                    # Most likely a testcase did not run because dependent cases failed
                                    testcase = None
                                else:
                                    testcase = readJson(testcaseResultsMetaFile)
                            else:
                                # Getting here means abortModuleFailure=True
                                testcase = None   
                                
                            index += 1
                            count = f'{str(index)}:'
                            
                            try:
                                self.playbookObj.overallSummaryData['totalKpiPassed'] += len(testcase["passed"])
                                self.playbookObj.overallSummaryData['totalKpiFailed'] += testcase["totalFailures"]
                            except:
                                # If the testcase is skipped, there is no testcaseIndex.
                                pass
                            
                            if testcase is None:
                                # Getting here means abortModuleFailure = True
                                # Remaining tests were skipped
                                self.moduleSummaryData['totalSkipped'] += 1
                                self.playbookObj.overallSummaryData['totalSkipped'] += 1
                                self.playbookObj.totalSkipped += 1
                                
                                if os.environ.get('keystack_reportSummary', None):
                                    summary = os.environ['keystack_reportSummary']
                                    
                                    for replace in [{'{{enumerateTestcase}}': str(index)},
                                                    {'{{testcase}}': f'{testcaseShortenPath:{longestStringLength}s}'},
                                                    {'{{result}}': f"{'Skipped':8s}"}, 
                                                    {'{{aborted}}': "No"},
                                                    {'{{kpiPassed}}': ""}, 
                                                    {'{{kpiFailed}}': ""},
                                                    {'{{outerLoopCounter}}': ""}, 
                                                    {'{{innerLoopCounter}}': ""}
                                                    ]:
                                        
                                        summary = summary.replace(list(replace.keys())[0], list(replace.values())[0])
                                        
                                    bodyMessage += f'\t{summary}\n'
                                else:
                                    # Default format: print(f'{var:12s}')
                                    bodyMessage += f"\t{count:5s} {'Skipped':8s} {testcaseShortenPath:{longestStringLength}s} {testcase['outerLoop']} {testcase['innerLoop']}: [{testcase['testDuration']}]\n"
                                                            
                                continue
                            
                            if 'keystack_reportSummary' in os.environ and os.environ.get('keystack_reportSummary', None):
                                summary = os.environ['keystack_reportSummary']
                                
                                for replace in [{'{{enumerateTestcase}}': str(index)},
                                                {'{{testcase}}': f'{testcaseShortenPath:{longestStringLength}s}'},
                                                {'{{result}}': f'{testcase["result"]:8s}'}, 
                                                {'{{aborted}}': str(testcase["testAborted"])},
                                                {'{{kpiPassed}}': f'{str(len(testcase["passed"])):2s}'}, 
                                                {'{{kpiFailed}}': f'{str(testcase["totalFailures"]):2s}'},
                                                {'{{outerLoopCounter}}': f'{str(testcase["outerLoop"]):4s}'}, 
                                                {'{{innerLoopCounter}}': f'{str(testcase["innerLoop"]):6s}'}]:
                                    
                                    summary = summary.replace(list(replace.keys())[0], list(replace.values())[0])
                                bodyMessage += f'\t{summary}\n'
                            else:
                                # Default format
                                bodyMessage += f"\t{count:5s} {testcase['result']:10s} {testcaseShortenPath:{longestStringLength}s} {testcase['outerLoop']} {testcase['innerLoop']}: [{testcase['testDuration']}]\n"
                                    
                            # {{testcase}}  {{result}}  {{kpiPassed}}  {{kpiFailed}}  {{aborted}}  {{outerLoopCounter}}  {{innerLoopCounter}}
                            # {{startTime}}  {{stopTime}}  {{duration}}
                            if testcase['result'] == 'Skipped':
                                totalSkippedTestcases += 1
                                description = f"{'Skipped:':8s} Stage:{self.stage}  Module:{self.module:10s}  Env:{self.moduleProperties['env']}\n\t {testcaseShortenPath:{longestStringLength}s} {testcase['outerLoop']} {testcase['innerLoop']}: [{testcase['testDuration']}]\n"
                                
                                for msg in testcase['failures']:
                                    if putFailureDescAtEnd:
                                        description += f"\t {msg}\n\n"
                                        self.playbookObj.putFailureDetailsAfterResults.append({testcaseShortenPath: description})
                                    else:
                                        bodyMessage += f"\t   - {msg}\n\n"
                                continue
                                
                            if testcase['testAborted'] == "Yes":
                                description = f"{'Aborted:':8s} Stage:{self.stage}  Module:{self.module:10s}  Env:{self.moduleProperties['env']}\n\t {testcaseShortenPath:{longestStringLength}s} {testcase['outerLoop']} {testcase['innerLoop']}   \n"
                                
                                if putFailureDescAtEnd:
                                    for failureMsg in testcase['failures']:
                                        description += f"\t   - {failureMsg}\n"

                                    self.playbookObj.putFailureDetailsAfterResults.append({testcaseShortenPath: description})
                                else:
                                    for failureMsg in testcase['failures']:
                                        if 'abortModuleFailure is set to True. Aborting Test.' in failureMsg:
                                            failureMsg = 'abortModuleFailure=True. Aborting Test.\n'
                                        
                                        if failureMsg:    
                                            bodyMessage += f"\t   * {failureMsg}\n"

                                continue
                            
                            if testcase['status'] != 'Completed':
                                bodyMessage += f"{count:5s} Stage:{self.stage}  Module:{self.module:10s}  Env:{self.moduleProperties['env']}\n\t {testcase['status']:10s} {testcaseShortenPath:{longestStringLength}s} {testcase['outerLoop']} {testcase['innerLoop']}\n"
                                continue
                            
                            if len(testcase['warnings']) > 0:
                                description = f"{'Warning:':8s} Stage:{self.stage}  Module:{self.module:10s}  Env:{self.moduleProperties['env']}\n\t {testcaseShortenPath:{longestStringLength}s} {testcase['outerLoop']} {testcase['innerLoop']}: [{testcase['testDuration']}]\n"
                                
                                for warning in testcase['warnings']:
                                    if putFailureDescAtEnd:
                                        description += f"\t   - Warning: {warning}\n"
                                    else:
                                        bodyMessage += f"\t   - Warning: {warning}\n\n"
                                
                                if putFailureDescAtEnd:
                                    self.playbookObj.putFailureDetailsAfterResults.append({testcaseShortenPath: description})
                                                                                                
                            if testcase['result'] in ['Failed']:
                                self.jiraFailures[eachTestcase] = {}
                                jiraBodyHeader =  f'Playbook: {self.playbookName}\n'
                                jiraBodyHeader += f'Stage: {self.stage}\n'
                                jiraBodyHeader += f'Module: {self.module}\n'
                                jiraBodyHeader += f'Env used: {self.env}\n'
                                result = f'{testcase["result"]}:'

                                description = f"{result:8s} Stage:{self.stage}  Module:{self.module}  Env:{self.moduleProperties['env']}\n\t {testcaseShortenPath:{longestStringLength}s} {testcase['outerLoop']} {testcase['innerLoop']}: [{testcase['testDuration']}]\n"

                                if self.module == 'LoadCore':
                                    for failure in testcase['failures']:
                                        # For LoadCore, data structure: 
                                        #    failures:
                                        #        - ApplicationTrafficGeneral:
                                        #            Bits received/s: Result=failed  ExpectedValue=400000000-500000000  MaxValue=325926120.0
                                        for csvResultFile,values in failure.items():
                                            for kpi,value in values.items():
                                                self.jiraFailures[eachTestcase].update({'failed': f'{self.module}:{testcaseName} Env:{self.env} KPI:{kpi} -> {value}'})
                                                
                                                if putFailureDescAtEnd:
                                                    description += f"\t   - KPI:{kpi} -> {value}\n"
                                                else:
                                                    bodyMessage += f"\t   - KPI:{kpi} -> {value}\n"

                                    # Show the passed KPIs also for better understanding of the test failures
                                    if putFailureDescAtEnd:
                                        description += f"\n\t   Passed KPIs:\n"
                                    else:
                                        bodyMessage += f"\n\t   Passed KPIs:\n"
                                        
                                    for passed in testcase['passed']:
                                        for csvResultFile,values in passed.items():
                                            for kpi,value in values.items():
                                                if putFailureDescAtEnd:
                                                    description += f"\t\t- KPI:{kpi} -> {value}\n"
                                                else:
                                                    bodyMessage += f"\t\t- KPI:{kpi} -> {value}\n"
                                                    
                                    if putFailureDescAtEnd:
                                        self.playbookObj.putFailureDetailsAfterResults.append({testcaseShortenPath: description})
                                    
                                elif self.module == 'AirMosaic':
                                    for failure in testcase['failures']:
                                        # For AirMosaic, data structure: 
                                        #    failures:
                                        #        - Registration Request: Result=failed ExpectedValue==1  ReceivedMaxValue=3
                                        #        - Registration Complete: Result=failed ExpectedValue==1  ReceivedMaxValue=0
                                        for kpi,value in failure.items():
                                            self.jiraFailures[eachTestcase].update({'failed': f'{self.module}:{testcaseName} Env:{self.env} KPI:{kpi} -> {value}'})
                                            
                                            if putFailureDescAtEnd:
                                                description += f"\t   - KPI:{kpi} -> {value}\n"
                                            else:
                                                bodyMessage += f"\t   - KPI:{kpi} -> {value}\n"
                                        
                                    # Show the passed KPIs also for better understanding of the test failures
                                    if putFailureDescAtEnd:
                                        description += f"\n\t     Passed KPIs:\n"
                                    else:
                                        bodyMessage += f"\n\t     Passed KPIs:\n"
                                        
                                    for passed in testcase['passed']:
                                        for kpi,value in passed.items():
                                            if putFailureDescAtEnd:
                                                description += f"\t\t- KPI:{kpi} -> {value}\n"
                                            else:
                                                bodyMessage += f"\t\t- KPI:{kpi} -> {value}\n"
                                    
                                    if putFailureDescAtEnd:        
                                        self.playbookObj.putFailureDetailsAfterResults.append({testcaseShortenPath: description})
                                    
                                else:
                                    for failure in testcase['failures']:
                                        self.jiraFailures[eachTestcase].update({'failed': f"{self.module}:{testcaseName} Env:{self.env}: {failure.replace('Failed: ', '')}"})
                                        
                                        if putFailureDescAtEnd:
                                            description += f"\t   - {failure.strip()}\n"
                                        else:
                                            bodyMessage += f"\t   - {failure.strip()}\n\n"
                                    
                                    if putFailureDescAtEnd:
                                        self.playbookObj.putFailureDetailsAfterResults.append({testcaseShortenPath: description})
                                
                                if putFailureDescAtEnd:
                                    self.jiraFailures[eachTestcase].update({'bodyMessage': f'{jiraBodyHeader}\n\n{description}'})
                                else:
                                    self.jiraFailures[eachTestcase].update({'bodyMessage': f'{jiraBodyHeader}\n\n{bodyMessage}'})
                                        
            except KeystackException as errMsg:
                bodyMessage = f'\tNo summary data. Test did not run successfully: {errMsg}'
        
        if modulePretestAborted:
            bodyMessage = ''
            for errorMsg in self.moduleSummaryData['exceptionErrors']:
                bodyMessage += f'\t- {errorMsg}\n'
                
        stageHeadings = ''
        includeStageHeadings = True
        
        if 'keystack_reportIncludeStageHeadings' in os.environ:
            if os.environ['keystack_reportIncludeStageHeadings'] in ['False', 'false', 'no', 'No']:
                includeStageHeadings = False
        
        if includeStageHeadings:    
            stageHeadings += f'\nSTAGE:  {self.stage}\n'
            
            if self.moduleSummaryData['totalSkipped'] > 0:
                moduleResult = "Incomplete"
            else:
                moduleResult = self.moduleSummaryData['result']
    
            moduleStartTime        = self.moduleSummaryData['started']
            moduleStopTime         = self.moduleSummaryData['stopped']
            moduleDuration         = self.moduleSummaryData['testDuration']
            moduleTotalPassed      = self.moduleSummaryData['totalPassed']
            moduleTotalFailed      = self.moduleSummaryData['totalFailed'] ;# Overall test failures
            moduleTotalFailures    = self.moduleSummaryData['totalFailures'] ;# Total module failures
            moduleTotalSkipped     = self.moduleSummaryData['totalSkipped']
            moduleTotalTestAborted = self.moduleSummaryData['totalTestAborted']
                    
            if self.module == 'AirMosaic':
                # AirMosaic
                try:
                    stageHeadings += f"\tMODULE: {self.module}\n"
                    stageHeadings += f"\tCells: {self.airMosaicCellList}\n"
                    stageHeadings += f"\t{subjectHeader}Result:{moduleResult} Testcases={len(self.testcaseSortedOrderList)}  TotalPassed={moduleTotalPassed}  TotalFailed:{moduleTotalFailed}  KPI-Failed={moduleTotalFailures}  Skipped:{moduleTotalSkipped}  TestcaseAborted={moduleTotalTestAborted}\n\n"
                except Exception as errMsg:
                    stageHeaderMessage = f"\t{self.module} Module Report Error: {errMsg}\n\n"
                    
            elif self.module == 'LoadCore':
                try:
                    stageHeadings += f"MODULE: {self.module}\n\t{subjectHeader}\nENV:    {self.moduleSummaryData['env']}\n\tResult:{moduleResult}   Testcases={len(self.testcaseSortedOrderList)}  TotalPassed={moduleTotalPassed}  TotalFailed={moduleTotalFailed}  KPI-Failed={moduleTotalFailures}  Skipped:{moduleTotalSkipped}  TestcaseAborted={moduleTotalTestAborted}\n\n"
                except Exception as errMsg:
                    stageHeadings += f"MODULE: {self.module}\n\t{subjectHeader}Error: {errMsg}\n\n"
            else:
                try:
                    stageHeadings += f"MODULE: {self.module}\nENV:    {self.moduleSummaryData['env']}\n\t{subjectHeader}Result:{moduleResult}   Testcases={len(self.testcaseSortedOrderList)}  TotalPassed={moduleTotalPassed}  TotalFailed={moduleTotalFailed}  Skipped:{moduleTotalSkipped}  TestcaseAborted={moduleTotalTestAborted}\n\n"
                except Exception as errMsg:
                    stageHeaderMessage += f"MODULE: {self.module}\n\t{subjectHeader}Error: {errMsg}\n\n"

            if moduleResult in ['Failed', 'Incomplete']:
                stageHeadings += f"\tabortModuleFailure: {self.envParams['abortModuleFailure']}\n"
                stageHeadings += f"\tabortStageFailure: {self.envParams['abortStageFailure']}\n"
                stageHeadings += f"\tabortTestOnFailure: {self.playbookObj.abortTestOnFailure}\n"
                         
            stageHeadings += f"\tTest start time: {moduleStartTime}\n"
            stageHeadings += f"\tTest stop time: {moduleStopTime}\n"
            stageHeadings += f"\tTest duration {moduleDuration}\n\n"
            
            playlistExclusions = self.moduleProperties.get('playlistExclusions', [])
            if playlistExclusions:
                stageHeadings += f"\tPlaylist Exclusions:\n"
                
                for excludedTestcase in playlistExclusions:
                    stageHeadings += f"\t   - {excludedTestcase}\n"
            
                stageHeadings += '\n'
            
        # Keep track of passed/failed module test for top-level Playbook reporting
        self.playbookObj.overallResultList.append(self.moduleSummaryData['result'])
        overallResultList = [eachResult for eachResult in self.playbookObj.overallResultList if eachResult != 'Passed']
        
        if self.playbookObj.overallSummaryData['totalTestAborted'] > 0 or \
            self.playbookObj.overallSummaryData['totalSkipped'] > 0:
            self.playbookObj.result = 'Incomplete'
        else:
            if len(overallResultList) > 0:
                self.playbookObj.result = 'Failed'
            else:
                self.playbookObj.result = 'Passed'

        # Append the current testing module results to the overall test report
        self.playbookObj.overallTestReport += f'{stageHeadings}'
        self.playbookObj.overallTestReport += f'{bodyMessage}'
        self.playbookObj.abortModuleFailure = self.envParams['abortModuleFailure']
        self.playbookObj.abortStageFailure = self.envParams['abortStageFailure']  
        self.playbookObj.testResultFolder = self.moduleResultsFolder
               
        try:
            if putFailureDescAtEnd:
                combineFailureDescriptions = ''
                for eachFailure in self.playbookObj.putFailureDetailsAfterResults:
                    for testcase, failureDesc in eachFailure.items():
                        combineFailureDescriptions += f'{failureDesc}\n'
                    
                with open(self.moduleTestReportFile, 'w') as testReportFileObj: 
                    if combineFailureDescriptions:
                        msg = f'{stageHeadings}{bodyMessage}\n\nFailure Summary:\n{combineFailureDescriptions}\n'
                    else:
                        msg = f'{stageHeadings}{bodyMessage}'
 
                    testReportFileObj.write(msg)
            else:
                with open(self.moduleTestReportFile, 'w') as testReportFileObj: 
                    testReportFileObj.write(f'{stageHeadings}{bodyMessage}') 
                                   
        except Exception as errMsg:
            print(f'\ngenerateModuleTestReport error: {traceback.format_exc(None, errMsg)}')

    def generateModuleTestReport_backup(self, cells=None):
        """
        Generate a "module" test report.
        An overall test report is combined in the Playbook class.executeTest()    
    
        Parameters
           cells <str>: For AirMosaic only
        """
        if self.debug:
            subjectHeader = 'Debug-Mode: '
        else:
            subjectHeader = ''

        totalSkippedTestcases = 0
        bodyMessage = ''
        self.jiraFailures = {}
        
        # v0.6.1f backward compatability: 
        # keystack_emailPutFailureDescriptionsAfterResultSummary
        if os.environ.get('keystack_emailPutFailureDescriptionsAfterResultSummary', None) in ['True', 'true', 'yes']:
            putFailureDescAtEnd = True
        else:
            putFailureDescAtEnd = False
            
        if os.environ.get('keystack_reportPutFailureDetailsAfterResultSummary', None) in ['True', 'true', 'yes']:
            putFailureDescAtEnd = True
        else:
            putFailureDescAtEnd = False
          
        try:
            totalOuterLoopIterations = int(self.moduleProperties.get('outerLoop', 1))
            index = 0
            
            # For better visibility using string formatting
            longestStringLength = 0
            for tc in self.testcaseSortedOrderList:
                shortenPath = tc.split(self.modulePath)[-1]
                if len(shortenPath) > longestStringLength:
                    longestStringLength = len(shortenPath)
            
            # Test Summary
            # Note about totalFailed vs totalFailures:
            #     totalFailed   = testcase failures.
            #     totalFailures = The amount of failures within a testcases.  Uses KPI-Failed
            # /opt/KeystackTests/Results/GROUP=Default/PLAYBOOK=loadcoreSample/11-01-2022-07:27:02:355686_5423/STAGE=LoadCoreTest_MODULE=LoadCore_ENV=loadcoreSample
            
            # /opt/KeystackTests/Results/GROUP=Default/PLAYBOOK=pythonSample/12-03-2022-08:25:28:290086_2733/.Data/ResultsMeta/opt/KeystackTests/Modules/CustomPythonScripts/Samples/Teardowns/teardownDut.yml_1_1
                             
            for outerLoop in range(1, totalOuterLoopIterations+1):
                for eachTestcase in self.testcaseSortedOrderList:
                    testcaseName = eachTestcase.split('/')[-1].split('.')[0]                       
                    testcaseShortenPath = eachTestcase.split(self.modulePath)[-1]
                    loopTestcaseTotal= self.getLoopTestcaseCount(eachTestcase)
                    for innerLoop in range(1, loopTestcaseTotal+1):
                        testcaseFileName = eachTestcase.split('/')[-1]
                        testcaseResultsMetaFolder = '/'.join(f'{self.playbookObj.resultsMetaFolder}{eachTestcase}'.split('/')[:-1])
                        testcaseResultsMetaFile = f'{self.testcaseResultsMetaFolder}/{testcaseFileName}_{outerLoop}_{innerLoop}'
                        
                        if os.path.exists(testcaseResultsMetaFile):
                            fileSize = os.path.getsize(testcaseResultsMetaFile)
                            if fileSize == 0:
                                # Most likely a testcase did not run because dependent cases failed
                                testcase = None
                            else:
                                testcase = readJson(testcaseResultsMetaFile)
                        else:
                            # Getting here means abortModuleFailure=True
                            testcase = None   
                            
                        index += 1
                        count = f'{str(index)}:'
                        
                        try:
                            self.playbookObj.overallSummaryData['totalKpiPassed'] += len(testcase["passed"])
                            self.playbookObj.overallSummaryData['totalKpiFailed'] += testcase["totalFailures"]
                        except:
                            # If the testcase is skipped, there is no testcaseIndex.
                            pass
                        
                        if testcase is None:
                            # Getting here means abortModuleFailure = True
                            # Remaining tests were skipped
                            self.moduleSummaryData['totalSkipped'] += 1
                            self.playbookObj.overallSummaryData['totalSkipped'] += 1
                            self.playbookObj.totalSkipped += 1
                            
                            if os.environ.get('keystack_reportSummary', None):
                                summary = os.environ['keystack_reportSummary']
                                
                                for replace in [{'{{enumerateTestcase}}': str(index)},
                                                {'{{testcase}}': f'{testcaseShortenPath:{longestStringLength}s}'},
                                                {'{{result}}': f"{'Skipped':8s}"}, 
                                                {'{{aborted}}': "No"},
                                                {'{{kpiPassed}}': ""}, 
                                                {'{{kpiFailed}}': ""},
                                                {'{{outerLoopCounter}}': ""}, 
                                                {'{{innerLoopCounter}}': ""}
                                                ]:
                                    
                                    summary = summary.replace(list(replace.keys())[0], list(replace.values())[0])
                                    
                                bodyMessage += f'\t{summary}\n'
                            else:
                                # Default format: print(f'{var:12s}')
                                bodyMessage += f"\t{count:5s} {'Skipped':8s} {testcaseShortenPath:{longestStringLength}s} {testcase['outerLoop']} {testcase['innerLoop']}: [{testcase['testDuration']}]\n"
                                                        
                            continue
                        
                        if 'keystack_reportSummary' in os.environ and os.environ.get('keystack_reportSummary', None):
                            summary = os.environ['keystack_reportSummary']
                            
                            for replace in [{'{{enumerateTestcase}}': str(index)},
                                            {'{{testcase}}': f'{testcaseShortenPath:{longestStringLength}s}'},
                                            {'{{result}}': f'{testcase["result"]:8s}'}, 
                                            {'{{aborted}}': str(testcase["testAborted"])},
                                            {'{{kpiPassed}}': f'{str(len(testcase["passed"])):2s}'}, 
                                            {'{{kpiFailed}}': f'{str(testcase["totalFailures"]):2s}'},
                                            {'{{outerLoopCounter}}': f'{str(testcase["outerLoop"]):4s}'}, 
                                            {'{{innerLoopCounter}}': f'{str(testcase["innerLoop"]):6s}'}]:
                                
                                summary = summary.replace(list(replace.keys())[0], list(replace.values())[0])
                            bodyMessage += f'\t{summary}\n'
                        else:
                            # Default format
                            bodyMessage += f"\t{count:5s} {testcase['result']:10s} {testcaseShortenPath:{longestStringLength}s} {testcase['outerLoop']} {testcase['innerLoop']}: [{testcase['testDuration']}]\n"
                                 
                        # {{testcase}}  {{result}}  {{kpiPassed}}  {{kpiFailed}}  {{aborted}}  {{outerLoopCounter}}  {{innerLoopCounter}}
                        # {{startTime}}  {{stopTime}}  {{duration}}
                        if testcase['result'] == 'Skipped':
                            totalSkippedTestcases += 1
                            description = f"{'Skipped:':8s} Stage:{self.stage}  Module:{self.module:10s}  Env:{self.moduleProperties['env']}\n\t {testcaseShortenPath:{longestStringLength}s} {testcase['outerLoop']} {testcase['innerLoop']}: [{testcase['testDuration']}]\n"
                            
                            for msg in testcase['failures']:
                                if putFailureDescAtEnd:
                                    description += f"\t {msg}\n\n"
                                    self.playbookObj.putFailureDetailsAfterResults.append({testcaseShortenPath: description})
                                else:
                                    bodyMessage += f"\t   - {msg}\n\n"
                            continue
                            
                        if testcase['testAborted'] == "Yes":
                            description = f"{'Aborted:':8s} Stage:{self.stage}  Module:{self.module:10s}  Env:{self.moduleProperties['env']}\n\t {testcaseShortenPath:{longestStringLength}s} {testcase['outerLoop']} {testcase['innerLoop']}   \n"
                            
                            if putFailureDescAtEnd:
                                for failureMsg in testcase['failures']:
                                    description += f"\t   - {failureMsg}\n"

                                self.playbookObj.putFailureDetailsAfterResults.append({testcaseShortenPath: description})
                            else:
                                for failureMsg in testcase['failures']:
                                    if 'abortModuleFailure is set to True. Aborting Test.' in failureMsg:
                                        failureMsg = 'abortModuleFailure=True. Aborting Test.\n'
                                    
                                    if failureMsg:    
                                        bodyMessage += f"\t   * {failureMsg}\n"

                            continue
                        
                        if testcase['status'] != 'Completed':
                           bodyMessage += f"{count:5s} Stage:{self.stage}  Module:{self.module:10s}  Env:{self.moduleProperties['env']}\n\t {testcase['status']:10s} {testcaseShortenPath:{longestStringLength}s} {testcase['outerLoop']} {testcase['innerLoop']}\n"
                           continue
                        
                        if len(testcase['warnings']) > 0:
                            description = f"{'Warning:':8s} Stage:{self.stage}  Module:{self.module:10s}  Env:{self.moduleProperties['env']}\n\t {testcaseShortenPath:{longestStringLength}s} {testcase['outerLoop']} {testcase['innerLoop']}: [{testcase['testDuration']}]\n"
                            
                            for warning in testcase['warnings']:
                                if putFailureDescAtEnd:
                                    description += f"\t   - Warning: {warning}\n"
                                else:
                                    bodyMessage += f"\t   - Warning: {warning}\n\n"
                            
                            if putFailureDescAtEnd:
                                self.playbookObj.putFailureDetailsAfterResults.append({testcaseShortenPath: description})
                                                                                            
                        if testcase['result'] in ['Failed']:
                            self.jiraFailures[eachTestcase] = {}
                            jiraBodyHeader =  f'Playbook: {self.playbookName}\n'
                            jiraBodyHeader += f'Stage: {self.stage}\n'
                            jiraBodyHeader += f'Module: {self.module}\n'
                            jiraBodyHeader += f'Env used: {self.env}\n'
                            result = f'{testcase["result"]}:'

                            description = f"{result:8s} Stage:{self.stage}  Module:{self.module}  Env:{self.moduleProperties['env']}\n\t {testcaseShortenPath:{longestStringLength}s} {testcase['outerLoop']} {testcase['innerLoop']}: [{testcase['testDuration']}]\n"

                            if self.module == 'LoadCore':
                                for failure in testcase['failures']:
                                    # For LoadCore, data structure: 
                                    #    failures:
                                    #        - ApplicationTrafficGeneral:
                                    #            Bits received/s: Result=failed  ExpectedValue=400000000-500000000  MaxValue=325926120.0
                                    for csvResultFile,values in failure.items():
                                        for kpi,value in values.items():
                                            self.jiraFailures[eachTestcase].update({'failed': f'{self.module}:{testcaseName} Env:{self.env} KPI:{kpi} -> {value}'})
                                            
                                            if putFailureDescAtEnd:
                                                description += f"\t   - KPI:{kpi} -> {value}\n"
                                            else:
                                                bodyMessage += f"\t   - KPI:{kpi} -> {value}\n"

                                # Show the passed KPIs also for better understanding of the test failures
                                if putFailureDescAtEnd:
                                    description += f"\n\t   Passed KPIs:\n"
                                else:
                                    bodyMessage += f"\n\t   Passed KPIs:\n"
                                    
                                for passed in testcase['passed']:
                                    for csvResultFile,values in passed.items():
                                        for kpi,value in values.items():
                                            if putFailureDescAtEnd:
                                                description += f"\t\t- KPI:{kpi} -> {value}\n"
                                            else:
                                                bodyMessage += f"\t\t- KPI:{kpi} -> {value}\n"
                                                
                                if putFailureDescAtEnd:
                                    self.playbookObj.putFailureDetailsAfterResults.append({testcaseShortenPath: description})
                                
                            elif self.module == 'AirMosaic':
                                for failure in testcase['failures']:
                                    # For AirMosaic, data structure: 
                                    #    failures:
                                    #        - Registration Request: Result=failed ExpectedValue==1  ReceivedMaxValue=3
                                    #        - Registration Complete: Result=failed ExpectedValue==1  ReceivedMaxValue=0
                                    for kpi,value in failure.items():
                                        self.jiraFailures[eachTestcase].update({'failed': f'{self.module}:{testcaseName} Env:{self.env} KPI:{kpi} -> {value}'})
                                        
                                        if putFailureDescAtEnd:
                                            description += f"\t   - KPI:{kpi} -> {value}\n"
                                        else:
                                            bodyMessage += f"\t   - KPI:{kpi} -> {value}\n"
                                    
                                # Show the passed KPIs also for better understanding of the test failures
                                if putFailureDescAtEnd:
                                    description += f"\n\t     Passed KPIs:\n"
                                else:
                                    bodyMessage += f"\n\t     Passed KPIs:\n"
                                    
                                for passed in testcase['passed']:
                                    for kpi,value in passed.items():
                                        if putFailureDescAtEnd:
                                            description += f"\t\t- KPI:{kpi} -> {value}\n"
                                        else:
                                            bodyMessage += f"\t\t- KPI:{kpi} -> {value}\n"
                                
                                if putFailureDescAtEnd:        
                                    self.playbookObj.putFailureDetailsAfterResults.append({testcaseShortenPath: description})
                                
                            else:
                                for failure in testcase['failures']:
                                    self.jiraFailures[eachTestcase].update({'failed': f"{self.module}:{testcaseName} Env:{self.env}: {failure.replace('Failed: ', '')}"})
                                    
                                    if putFailureDescAtEnd:
                                        description += f"\t   - {failure.strip()}\n"
                                    else:
                                        bodyMessage += f"\t   - {failure.strip()}\n\n"
                                
                                if putFailureDescAtEnd:
                                    self.playbookObj.putFailureDetailsAfterResults.append({testcaseShortenPath: description})
                            
                            if putFailureDescAtEnd:
                                self.jiraFailures[eachTestcase].update({'bodyMessage': f'{jiraBodyHeader}\n\n{description}'})
                            else:
                                self.jiraFailures[eachTestcase].update({'bodyMessage': f'{jiraBodyHeader}\n\n{bodyMessage}'})
                                    
        except KeystackException as errMsg:
            bodyMessage = f'\tNo summary data. Test did not run successfully: {errMsg}'
            
        stageHeadings = ''
        includeStageHeadings = True
        
        if 'keystack_reportIncludeStageHeadings' in os.environ:
            if os.environ['keystack_reportIncludeStageHeadings'] in ['False', 'false', 'no', 'No']:
                includeStageHeadings = False
        
        if includeStageHeadings:    
            stageHeadings += f'\nSTAGE:  {self.stage}\n'
            
            if self.moduleSummaryData['totalSkipped'] > 0:
                moduleResult = "Incomplete"
            else:
                moduleResult = self.moduleSummaryData['result']
    
            moduleStartTime        = self.moduleSummaryData['started']
            moduleStopTime         = self.moduleSummaryData['stopped']
            moduleDuration         = self.moduleSummaryData['testDuration']
            moduleTotalPassed      = self.moduleSummaryData['totalPassed']
            moduleTotalFailed      = self.moduleSummaryData['totalFailed'] ;# Overall test failures
            moduleTotalFailures    = self.moduleSummaryData['totalFailures'] ;# Total module failures
            moduleTotalSkipped     = self.moduleSummaryData['totalSkipped']
            moduleTotalTestAborted = self.moduleSummaryData['totalTestAborted']
                    
            if self.module == 'AirMosaic':
                # AirMosaic
                try:
                    stageHeadings += f"\tMODULE: {self.module}\n"
                    stageHeadings += f"\tCells: {self.airMosaicCellList}\n"
                    stageHeadings += f"\t{subjectHeader}Result:{moduleResult} Testcases={len(self.testcaseSortedOrderList)}  TotalPassed={moduleTotalPassed}  TotalFailed:{moduleTotalFailed}  KPI-Failed={moduleTotalFailures}  Skipped:{moduleTotalSkipped}  TestcaseAborted={moduleTotalTestAborted}\n\n"
                except Exception as errMsg:
                    stageHeaderMessage = f"\t{self.module} Module Report Error: {errMsg}\n\n"
                    
            elif self.module == 'LoadCore':
                try:
                    stageHeadings += f"MODULE: {self.module}\n\t{subjectHeader}\nENV:    {self.moduleSummaryData['env']}\n\tResult:{moduleResult}   Testcases={len(self.testcaseSortedOrderList)}  TotalPassed={moduleTotalPassed}  TotalFailed={moduleTotalFailed}  KPI-Failed={moduleTotalFailures}  Skipped:{moduleTotalSkipped}  TestcaseAborted={moduleTotalTestAborted}\n\n"
                except Exception as errMsg:
                    stageHeadings += f"MODULE: {self.module}\n\t{subjectHeader}Error: {errMsg}\n\n"
            else:
                try:
                    stageHeadings += f"MODULE: {self.module}\nENV:    {self.moduleSummaryData['env']}\n\t{subjectHeader}Result:{moduleResult}   Testcases={len(self.testcaseSortedOrderList)}  TotalPassed={moduleTotalPassed}  TotalFailed={moduleTotalFailed}  Skipped:{moduleTotalSkipped}  TestcaseAborted={moduleTotalTestAborted}\n\n"
                except Exception as errMsg:
                    stageHeaderMessage += f"MODULE: {self.module}\n\t{subjectHeader}Error: {errMsg}\n\n"

            if moduleResult in ['Failed', 'Incomplete']:
                stageHeadings += f"\tabortModuleFailure: {self.envParams['abortModuleFailure']}\n"
                stageHeadings += f"\tabortStageFailure: {self.envParams['abortStageFailure']}\n"
                stageHeadings += f"\tabortTestOnFailure: {self.playbookObj.abortTestOnFailure}\n"
                         
            stageHeadings += f"\tTest start time: {moduleStartTime}\n"
            stageHeadings += f"\tTest stop time: {moduleStopTime}\n"
            stageHeadings += f"\tTest duration {moduleDuration}\n\n"
            
            playlistExclusions = self.moduleProperties.get('playlistExclusions', [])
            if playlistExclusions:
                stageHeadings += f"\tPlaylist Exclusions:\n"
                
                for excludedTestcase in playlistExclusions:
                    stageHeadings += f"\t   - {excludedTestcase}\n"
            
                stageHeadings += '\n'
            
        # Keep track of passed/failed module test for top-level Playbook reporting
        self.playbookObj.overallResultList.append(self.moduleSummaryData['result'])
        overallResultList = [eachResult for eachResult in self.playbookObj.overallResultList if eachResult != 'Passed']
        
        if self.playbookObj.overallSummaryData['totalTestAborted'] > 0 or \
            self.playbookObj.overallSummaryData['totalSkipped'] > 0:
            self.playbookObj.result = 'Incomplete'
        else:
            if len(overallResultList) > 0:
                self.playbookObj.result = 'Failed'
            else:
                self.playbookObj.result = 'Passed'

        # Append the current testing module results to the overall test report
        self.playbookObj.overallTestReport += f'{stageHeadings}'
        self.playbookObj.overallTestReport += f'{bodyMessage}'
        self.playbookObj.abortModuleFailure = self.envParams['abortModuleFailure']
        self.playbookObj.abortStageFailure = self.envParams['abortStageFailure']  
        self.playbookObj.testResultFolder = self.moduleResultsFolder
               
        try:
            if putFailureDescAtEnd:
                combineFailureDescriptions = ''
                for eachFailure in self.playbookObj.putFailureDetailsAfterResults:
                    for testcase, failureDesc in eachFailure.items():
                        combineFailureDescriptions += f'{failureDesc}\n'
                    
                with open(self.moduleTestReportFile, 'w') as testReportFileObj: 
                    if combineFailureDescriptions:
                        msg = f'{stageHeadings}{bodyMessage}\n\nFailure Summary:\n{combineFailureDescriptions}\n'
                    else:
                        msg = f'{stageHeadings}{bodyMessage}'
 
                    testReportFileObj.write(msg)
            else:
                with open(self.moduleTestReportFile, 'w') as testReportFileObj: 
                    testReportFileObj.write(f'{stageHeadings}{bodyMessage}')                
        except Exception as errMsg:
            print(f'\ngenerateModuleTestReport error: {traceback.format_exc(None, errMsg)}')

    def createJiraIssues(self):      
        if self.jira == False or self.overallResult == 'Passed':
            return

        self.jiraLogFileLock.acquire()
        issueList = []
        predefinedJiraIssueWithTestcases = False
          
        for testcase, properties in self.jiraFailures.items():
            # jiraTestcaseIssueKey are predefined opened jira issues that is used for logging bugs and set to active/opened
            if 'jiraTestcaseIssueKey' in self.testcaseDict[testcase] and self.testcaseDict[testcase]['jiraTestcaseIssueKey']:
                predefinedJiraIssueWithTestcases = True
                testcaseIssue = {'description': properties['bodyMessage']}
            else:
                testcaseIssue = {
                        'project': {'key': self.playbookObj.loginCredentials['jiraProject']}, 
                        'summary': properties['failed'],
                        'description': properties['bodyMessage'],
                        'issuetype': {'name': 'Bug'},
                        'assignee': {'name': self.playbookObj.loginCredentials['jiraAssignee']},
                        'priority': {'name': self.playbookObj.loginCredentials['jiraPriority']}               
                    }
                                
            issueList.append(testcaseIssue)
            
        try:
            from Services.JiraLib import Jira

            jiraObj = Jira(logFile=Serviceware.vars.jiraServiceLogFile, 
                           loginCredentialKey=self.playbookObj.loginCredentialKey)                    
            jiraObj.connect()
            
            if predefinedJiraIssueWithTestcases:
                predefinedIssueKey = self.testcaseDict[testcase]['jiraTestcaseIssueKey']
                self.writeToTestcaseLogFile(f'Jira: Using predefined issue key: {predefinedIssueKey}')
                
                for issue in issueList:
                    jiraObj.updateIssue(issueKey=predefinedIssueKey, 
                                        description=issue['description'], 
                                        setStatus=self.playbookObj.loginCredentials['jiraSetActiveStatus'])
                    
            if predefinedJiraIssueWithTestcases == False:
                if 'jiraAppendFailureToOpenedIssue' in self.playbookObj.loginCredentials:
                    # True | False
                    appendFailureToOpenedIssue = self.playbookObj.loginCredentials['jiraAppendFailureToOpenedIssue']
                
                self.writeToTestcaseLogFile(f'Jira: Creating issue: {issueList}')
                jiraObj.createIssueList(issueList=issueList, addCommentToExistingIssue=appendFailureToOpenedIssue)
                        
        except Exception as errMsg:
            self.writeToTestcaseLogFile(f'keystack.py: createJiraIssue: Exception: {traceback.format_exc(None, errMsg)}')
        
        self.jiraLogFileLock.release()
                  
    def getLoopTestcaseCount(self, eachTestcase):
        """
        Verify if users set any folders and/or testcases to loop testing more than one time
         
        Looping feature: 
           - Loop allTestcases
           - Loop all scripts inside folders and subfolders
           - Loop selected testcases
           - If no condition is met, default running testcases one time
           - Allows user to do all three. The loop count will increment in this case.
           
        Usage in the modulePreferences file:
           loop:
                # Set allTestcases to None to disable looping all test cases
                allTestcases: 2
                
                folders: 
                    # Run everything in a folder including subfolders
                    - /KeystackTests/Modules/SanityScripts/Testcases: 2
                    
                testcases:
                    # Selecting specific testcases
                    - /KeystackTests/Modules/SanityScripts/Testcases/bgp.py: 3
                    - /KeystackTests/Modules/SanityScripts/Testcases/isis.py: 5
        """
        loopTestcase = 0
        if 'innerLoop' in self.moduleProperties:
            if self.moduleProperties['innerLoop']['allTestcases'] not in ["None", '', 0]:
                loopTestcase = int(self.moduleProperties['innerLoop']['allTestcases'])
                
            if 'folders' in self.moduleProperties['innerLoop'] and \
                self.moduleProperties['innerLoop']['folders'] not in ["None", '', 0]:
                for eachFolderDict in self.moduleProperties['innerLoop']['folders']:
                    # eachFolderDict = {'/Modules/CustomPythonScripts/Testcases': 3}
                    folder = list(eachFolderDict.keys())[0]
                    if folder.startswith('/Modules/'):
                        folder = f'{self.keystackTestRootPath}{folder}'
                    if folder.startswith('Modules/'):
                        folder = f'{self.keystackTestRootPath}/{folder}'
                                        
                    for root, dirs, files in os.walk(folder):
                        if files:
                            for file in files:
                                if f'{root}/{file}' == eachTestcase:
                                    loopCount = list(eachFolderDict.values())[0]
                                    if loopTestcase > 0:
                                        loopTestcase += loopCount
                                    else:
                                        loopTestcase = loopCount
                                        
                                    break

            if 'testcases' in self.moduleProperties['innerLoop'] and \
                self.moduleProperties['innerLoop']['testcases'] not in ["None", '', 0]:
                try:
                    for tc in self.moduleProperties['innerLoop']['testcases']:
                        # tc = {'/Modules/CustomPythonScripts/Testcases/bgp.py': 4}
                        for eachDependentTestcase in tc.keys():
                            if eachDependentTestcase in eachTestcase:
                                loopCount = list(tc.values())[0]

                    if loopTestcase > 0:
                        loopTestcase += loopCount
                    else:
                        loopTestcase = loopCount             
                    
                except IndexError:
                    # User selected specified testcases from a folder.
                    # If a testcases isn't selected in the loop feature, then default the loop to run once only.
                    if loopTestcase == 0:
                        loopTestcase = 1

        if loopTestcase == 0:
            # Default to run testcases 1 one if no loop condition is met
            loopTestcase = 1
                    
        return loopTestcase
    
    def getTestcaseScript(self, typeOfScript='standalonePythonScript', testcase=None):
        """ 
        standalone python script | keystack integrated python script | shell/bash 
        
        typeOfScript:
             standalone python scripts: sttandalonePythonScript
             
             keystackIntegration scripts: pythonScript
             
             linux bash or shell scripts: bashScript
             
        Returns:
            Script full path
        """
        scriptTypeSearch = False       
        for eachType in ['pythonScript', 'standalonePythonScript', 'bashScript']:
            if eachType in self.testcaseDict[testcase]:
                scriptTypeSearch = True
        
        if scriptTypeSearch == False:
            self.abortTestCaseErrors.append(f"The testcase yml file '{testcase}' expects a type of script to run. Options: pythonScript, standalonePythonScript, bashScript. None founkd. Don't know which Python script to execute")
            return
        
        userDefinedPythonScript = self.testcaseDict[testcase][typeOfScript]
        
        # Scripts could be executed from a Module path or or the Apps path
        regexMatch = re.search('.*(Modules|Apps)/(.*)',  userDefinedPythonScript)
        if regexMatch:
            if 'Modules' in regexMatch.group(1):
                self.pythonScriptFullPath = f'{self.keystackTestRootPath}/Modules/{regexMatch.group(2)}'

            if 'Apps' in regexMatch.group(1):
                self.pythonScriptFullPath = f'{self.keystackSystemPath}/Apps/{regexMatch.group(2)}'
        else:
            self.abortTestCaseErrors.append(f'Testcase yml file requires the pythonScript|standalonePythonScript|bashScript key with a value beginning with either /Modules or /Apps')

        if os.path.exists(self.pythonScriptFullPath) == False:
            self.abortTestCaseErrors.append(f"No such type={typeOfScript} found stated in testcase '{testcase}': {self.pythonScriptFullPath}")
         
        return self.pythonScriptFullPath
                   
    def getTestcaseApp(self, testcaseYmlFile):
        """ 
        Every testcase yml file must state the app to use for running the script
        """
        data = readYaml(testcaseYmlFile)
        app = data.get('app', None)
        
        if app is None:
            self.abortTestCaseErrors.append(f'Testcase yml file is missing the app to use: {testcaseYmlFile}')
            return None
  
        if os.path.exists(f'{GlobalVars.appsFolder}/{app}') == False:
            self.abortTestCaseErrors.append(f'App does not exists: {app}. In testcase yml file: {testcaseYmlFile}')
            return None

        regexMatch = re.search('(.*)/(applet.*).py', app)
        if regexMatch:
            appName = regexMatch.group(1)
            applet = regexMatch.group(2)
            appPath = f'{GlobalVars.appsFolder}/{appName}'

            # ('/opt/KeystackSystem/Apps/CustomPython', 'applet_CustomPython')
            return (appPath, applet)
        else:
            self.abortTestCaseErrors.append(f'App does not exists: {app}')

    def getTestcaseAppLibraryPath(self, testcaseYmlFile):
        """ 
        Scripts want to import some app libraries.
        
        The testcase yml file uses a keyword importAppLibraries.
        The value needs to be a list of app names only. Exclude applets.
        """
        data = readYaml(testcaseYmlFile)
        appLibraryPaths = data.get('importAppLibraryPaths', None)
        if appLibraryPaths is None:
            return []
        
        if type(appLibraryPaths) is not list:
            self.abortTestCaseErrors.append(f'The appLibraryPaths value needs to be a list in testcase yml file beginning with /Apps or /Modules: {testcaseYmlFile}')  
            return []
        
        appPathList = []
        for appLibraryPath in appLibraryPaths:
            regexMatch = re.search('.*(Apps|Modules)/(.*)', appLibraryPath)
            if regexMatch:
                if 'Apps' in regexMatch.group(1):
                    appPath = f'{GlobalVars.appsFolder}/{regexMatch.group(2)}'
                    
                if 'Modules' in regexMatch.group(1):
                    appPath = f'{GlobalVars.keystackTestRootPath}/Modules/{regexMatch.group(2)}'
                     
                if os.path.exists(appPath) == False:
                    self.abortTestCaseErrors.append(f'No such app path: {appPath}') 
                else:
                    appPathList.append(appPath)
            
        return appPathList      
    
    def writeMetaDataToTopLevelResultsFolder(self):
        metadataFile = f'{self.resultsTimestampFolder}/metadata.json'
        metadata = readJson(metadataFile, threadLock=self.lock)
        metadata.update(self.stageReport)
        writeToJson(metadataFile, metadata, threadLock=self.lock)

    def reserveEnv(self, overallSummaryFile, env):
        """ 
        Put sessionId into active-user
        
        env: <str>: <envName> | <envGroup>/<envName>
        """
        if self.execRestApiObj:
            params = {'env': env, 'sessionId':self.timestampFolderName, 'overallSummaryFile':overallSummaryFile, 
                    'user':self.user, 'stage':self.stage, 'module':self.module, 'utilization':True, 'webhook':True}
            # Must use REST API instead of EnvMgmt. Has to go through the UI because this is where the DB is connected.
            response = self.execRestApiObj.post(restApi='/api/v1/env/reserve', params=params, showApiOnly=True) 
            if response.status_code != 200:
                self.playbookobj.overallSummaryData['exceptionErrors'].append(response.json["errorMsg"])
                writeToJson(self.playbookObj.overallSummaryDataFile, data=self.playbookObj.overallSummaryData, mode='w')
                raise KeystackException(f'reserveEnv failed: {response.json["errorMsg"]}')
    
    def releaseEnv(self, env):
        """ 
        Remove the sessionId from active-user
        
        env: <str>: <envName> | <envGroup>/<envName>
        """
        if self.execRestApiObj:
            params = {'env': env, 'sessionId':self.timestampFolderName,
                    'user':self.user, 'stage':self.stage, 'module':self.module, 'webhook':True}
            # Must use REST API instead of EnvMgmt. Has to go through the UI because this is where the DB is connected.
            response = self.execRestApiObj.post(restApi='/api/v1/env/removeFromActiveUsersListUI', showApiOnly=True, params=params)
            if response.status_code != 200:
                raise KeystackException(f'releaseEnv failed: {response.json["errorMsg"]}')
              
    def lockAndWaitForEnv(self, sessionId, overallSummaryFile, user, stage, module):
        """ 
        This is for runPlaybook only.
        Playbooks cannot expect the env is available for usage at any time.
        This function checks if the env is avaiable.
        If not, go to wait-list and wait until 
        the test sessionId is next in line to use the env.
        """
        if self.execRestApiObj is None:
            return
        
        doOnce = False
        
        try:
            try:
                # Samples-pytthonSample
                if '-' in self.moduleProperties['env']:
                    env = self.moduleProperties['env'].replace('-', '/')
                else:
                    env = self.moduleProperties['env']
                    
                reserveEnvStatus = 'success'
                params = {'env': env, 'sessionId':sessionId, 'overallSummaryFile':overallSummaryFile, 
                          'user':user, 'stage':stage, 'module':module, 'utilization':False, 'webhook':True}
                
                # Must use REST API instead of EnvMgmt. Has to go through the UI because this is where the DB is connected.
                response = self.execRestApiObj.post(restApi='/api/v1/env/reserve', params=params, showApiOnly=True)
                if response.status_code != 200:
                    reserveEnvStatus = 'failed'
                    
            except Exception as errMsg:
                reserveEnvStatus = 'failed'
                
            if reserveEnvStatus == 'failed':
                self.abortTheTest(f'lockAndWaitForEnv: Failed. Called /api/v1/env/reserve. Status code {response.status_code}')
                return
            
            params = {'sessionId':sessionId, 'env': env, 'user':user,
                      'stage':stage, 'module':module, 'webhook':True}
                
            while True:
                # Must use REST API instead of EnvMgmt. Has to go through the UI because this is where the DB is connected.
                response = self.execRestApiObj.post(restApi='/api/v1/env/amINext', params=params, showApiOnly=True)
                if response.json()['status'] == 'failed':
                    self.abortTheTest(f'lockAndWaitForEnv: Failed. Called /api/v1/env/amINext. Status code {response.status_code}')
                    return
                
                if response.json()['result']:
                    # I am next to run
                    self.moduleSummaryData.update({'status': 'Running'})
                    break
                else:
                    if doOnce == False:
                        self.moduleSummaryData.update({'status': 'Waiting-For-Env'})
                        writeToJson(self.moduleSummaryFile, self.moduleSummaryData, mode='w', threadLock=self.lock)
                        doOnce = True
                        
                    #print(f'\nlockAndWaitForEnv: Waiting for env {env} availability ...')
                    time.sleep(5)
                    continue
                
        except Exception as errMsg:
            #print('Error: lockAndWaitForEnv:', traceback.format_exc(None, errMsg))
            self.abortTheTest(str(errMsg))
                                 
    def envLoadBalance(self):
        """ 
        Using env load balance requires the webUI/MongoDB.
        If this is not running, use static env.
        """
        isEnvAvailable = False
        waitInterval = 10
        showErrorOnce = 0
        timeout = 10
        counter = 0
        
        if self.execRestApiObj is None:
            self.abortTheTest(errorMsg=f'The module {self.module} uses loadBalanceGroup {self.moduleSummaryData["loadBalanceGroup"]}, but this requires the webUI/MongoDB which is not running. Either enable the webUI or use a static env with parallelUsage=True.')
            return
        
        while True:
            # Get load balance group envs.  Select an env to use
            response = self.execRestApiObj.post(restApi='/api/v1/env/loadBalanceGroup/getEnvs', showApiOnly=True, 
                                                params={'webhook':True, 'loadBalanceGroup': self.moduleSummaryData['loadBalanceGroup']})

            if response.status_code == 406:
                # Could be no such load balance group
                self.abortTheTest(response.json()['errorMsg'])
                return
            
            if response.status_code == 200:
                if len(response.json()['loadBalanceGroupEnvs']) == 0:
                    self.abortTheTest(f'The load balance group "{self.moduleSummaryData["loadBalanceGroup"]}" does not have any env defined for stage:{self.stage} module:{self.module}.')
                    return
                
                # ['loadcoreSample', 'pythonSample', 'Samples/bobafett']
                for env in response.json()['loadBalanceGroupEnvs']:
                    result = self.execRestApiObj.post(restApi='/api/v1/env/isEnvAvailable', showApiOnly=True, 
                                                              params={'webhook':True, 'env': env})

                    isEnvAvailable = result.json()['isAvailable']
                    if isEnvAvailable:
                        self.env = env
                        self.envFile = f'{GlobalVars.keystackTestRootPath}/Envs/{env}.yml'
                        if os.path.exists(self.envFile) == False:
                            self.abortTheTest(f'The load balance {self.moduleSummaryData["loadBalanceGroup"]} provided the env "{self.env}" to use, but the env file does not exists.  Please make sure to create an env yml file in the /ENVS path')
                            
                        # Assign an available Env from the load balance group
                        self.moduleProperties.update({'env':env})
                        contents = readYaml(self.envFile)   
                        self.moduleProperties.update({'envParams': contents})
                        currentModuleResultsFolder = self.moduleResultsFolder
                        moduleEnvMgmtFileReplacement = self.playbookObj.createEnvMgmtDataFile(stage=self.stage, moduleName=self.module,
                                                                                              envFileFullPath=self.envFile)
                        self.moduleEnvMgmtFile = moduleEnvMgmtFileReplacement       
                        moduleEnvMgmtData = readJson(self.moduleEnvMgmtFile)
                        moduleEnvMgmtData['env'] = env
                        writeToJson(self.moduleEnvMgmtFile, moduleEnvMgmtData)
                        chownChmodFolder(self.moduleEnvMgmtFile, self.user, GlobalVars.userGroup)
                        
                        envNameForResultFolder = env.replace('/', '-')
                        self.moduleResultsFolder = deepcopy(self.moduleResultsFolder.replace('ENV=None', f'ENV={envNameForResultFolder}'))
                    
                        execSubprocess2(['mv', currentModuleResultsFolder, self.moduleResultsFolder], shell=False, cwd=None, showStdout=False)
                        self.moduleTestReportFile = f'{self.moduleResultsFolder}/moduleTestReport'
                        # Update the moduleSummary file with the updated moduleResulsFolder
                        self.moduleSummaryFile = f'{self.moduleResultsFolder}/moduleSummary.json'
                        
                        # Update the runList: "runList": [{"stage": "Test", "module": "CustomPythonScripts","env": null}]
                        currentRunList = self.playbookObj.overallSummaryData['runList']
                        updatedRunList = []
                        for eachTest in currentRunList:
                            if eachTest['stage'] == self.stage and eachTest['module'] == self.module:
                                updatedRunList.append({'stage':self.stage, 'module':self.module, 'env':env})
                            else:
                                updatedRunList.append(eachTest)
                        
                        self.playbookObj.overallSummaryData['runList'] = updatedRunList
                        
                        envParallelUsage = self.moduleProperties['envParams'].get('parallelUsage', False)
                        self.moduleSummaryData.update({'status': 'Waiting-For-Env', 'isEnvParallelUsed': envParallelUsage})
                        break
            else:
                if showErrorOnce == 0:
                    self.abortTheTest(f'Lost server connection waiting for LBG env. Stage={self.stage} Module={self.module}')
                    showErrorOnce = 1
                    
                if counter < timeout:
                    time.sleep(waitInterval)
                    
                if counter == timeout:
                    self.abortTheTest(f'Giving up on connecting to server. Aborting test.')
                    return
                
            if isEnvAvailable:
                break
            else:    
                # Wait 10 seconds to check again for an available env
                time.sleep(waitInterval)
                continue
            
    def abortTheTest(self, errorMsg: str, overallSummaryData: bool=True, moduleSummaryData: bool=True) -> None:
        # if overallSummaryData:
        #     self.playbookObj.overallSummaryData['exceptionErrors'].append(errorMsg)
        #     writeToJson(self.playbookObj.overallSummaryDataFile, data=self.playbookObj.overallSummaryData, mode='w', threadLock=self.lock)
        
        if moduleSummaryData:
            self.moduleSummaryData['exceptionErrors'].append(errorMsg)
            writeToJson(self.moduleSummaryFile, self.moduleSummaryData, mode='w', threadLock=self.lock)
                
    def runStandAloneScript(self, typeOfScript='python', scriptFullPath=None):
        """ 
        Run plain Python scripts and shell scripts and show output in real time
        
        Requirements:
            - The testcase yaml files must set "standalonePythonScript: True" or "bashScript: True"
        
            - In the playbook, use verifyFailurePatterns to look for failures:
                verifyFailurePatterns: ['Failed', 'SyntaxError']
             
        https://earthly.dev/blog/python-subprocess/
        """
        from os import fdopen
        
        if typeOfScript == 'python':
            command = f'{sys.executable} {scriptFullPath}'
                
        if typeOfScript == 'shell':
            command = f'bash {scriptFullPath}'

        # Note, bufsize=1 won't work without text=True or universal_newlines=True.        
        with subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, bufsize=1, text=True) as output:
            # Flush stdout
            with fdopen(sys.stdout.fileno(), 'wb', closefd=False) as stdout:
                for line in output.stdout:
                    print(line.strip())            
                    self.writeToTestcaseLogFile(line.strip(), includeTimestamp=False, stdout=False)
                    
                    match = re.search('^keystack-Warning:?(.*)', line, re.I)
                    if match:
                        self.testcaseData['warnings'].append(match.group(1))
                        
                    match = re.search('^keystack-Exception:?(.*)', line, re.I)
                    if match:
                        self.playbookObj.overallSummaryData['exceptionErrors'].append(match.group(1))
                        self.moduleSummaryData['exceptions'].append(match.group(1))
                        self.testcaseData['exceptions'].append(match.group(1))
                        
                    if self.moduleProperties.get('verifyFailurePatterns', None):
                        for eachFailurePattern in self.moduleProperties['verifyFailurePatterns']:
                            
                            if bool(re.search(eachFailurePattern, line)):
                                self.writeToTestcaseLogFile(f'[Found failure pattern]: module:{self.module} env:{self.env}: {eachFailurePattern}')

                                self.testcaseResult = 'Failed'
                                self.playbookObj.overallSummaryData['totalFailures'] += 1
                                self.moduleSummaryData['totalFailures'] += 1
                                self.testcaseData['totalFailures'] += 1
                                self.testcaseData['failures'].append(line)

                                if self.pauseOnError:
                                    self.moduleSummaryData['pausedOnError'] = f'{self.moduleResultsFolder}/pausedOnError'
                                    self.moduleSummaryData['status'] = 'paused-on-error'
                                    self.testcaseData['pausedOnError'] = True
                                    self.testcaseData['status'] = 'paused-on-error'
                                    writeToJson(self.moduleSummaryFile, self.moduleSummaryData, mode='w', retry=5)
                                    self.pauseTestOnError()
                                    self.testcaseData['pausedOnError'] = ''
                                    self.moduleSummaryData['pausedOnError'] = ''
                                    self.testcaseData['status'] = 'Running'
                                    self.moduleSummaryData['status'] = 'Running'
                                    writeToJson(self.moduleSummaryFile, self.moduleSummaryData, mode='w', retry=5)

    def run(self):
        """
        Execute each testcase based on the collected yaml testcase files
        """
        try:
            if 'waitTimeBetweenTests' in self.moduleProperties:
                self.waitTimeBetweenTests = self.moduleProperties['waitTimeBetweenTests']
            else:
                self.waitTimeBetweenTests = 0
            
            if 'outerLoop' in self.moduleProperties:
                self.totalOuterLoopIterations = int(self.moduleProperties['outerLoop'])
                if self.totalOuterLoopIterations == 0:
                    self.totalOuterLoopIterations = 1
                    
                if self.totalOuterLoopIterations > 1:
                    totalOuterLoopCounter = self.totalOuterLoopIterations
                else:
                    totalOuterLoopCounter = 0
            else:
                self.totalOuterLoopIterations = 1
                totalOuterLoopCounter = 0
            
            totalIterations = 0
            for outerLoop in range(1, self.totalOuterLoopIterations+1):            
                for index,eachTestcase in enumerate(self.testcaseSortedOrderList):
                    testcaseInnerLoopCount = self.getLoopTestcaseCount(eachTestcase)
                    totalIterations += testcaseInnerLoopCount
                
            doOneTimeOnly = 0
            self.testcaseDebugLogFile = None
            self.emailAttachmentList = []
            currentTestcaseConfigParams = {}
            self.testStart = datetime.datetime.now()
            
            # This self.moduleSummaryFile could get overwritten in envLoadBalance with a different folder with ENV=<env>
            self.moduleSummaryFile = f'{self.moduleResultsFolder}/moduleSummary.json'
            self.moduleSummaryData = readJson(self.moduleSummaryFile)
            
            # moduleProperties: {'enable': True, 'abortOnFailure': False, 'bridgeEnvParams': True, 'env': 'Samples/loadcoreSample', 'loadBalanceGroup': 'qa', 'variables': {'serverName': 'regressionServer', 'serverIp': '10.10.10.1'}, 'playlist': ['/Modules/CustomPythonScripts/Samples/BridgeEnvParams/dynamicVariableSample.yml'], 'app': 'CustomPython', 'artifactsRepo': '/opt/KeystackTests/Results/GROUP=Default/PLAYBOOK=Samples-pythonSample/05-15-2023-12:02:54:277306_5565/Artifacts', 'envParams': {'parallelUsage': False, 'server1': '192.168.28.6', 'serverIp': '1.1.1.2', 'login': 'admin', 'description': 'test'}}
            if self.env is None and self.moduleSummaryData['loadBalanceGroup']:
                    if self.playbookObj.isKeystackUIExists:
                        # This will set self.env with an available env to use
                        self.envLoadBalance()
                    else:
                        self.abortTheTest(errorMsg=f'The module {self.module} uses loadBalanceGroup {self.moduleSummaryData["loadBalanceGroup"]}, but this requires the webUI/MongoDB which is not running. Either enable the docker container webUI or use a static env.')

            # self.env: Samples/loadcoreSample
            if self.env and self.env != 'bypass':
                # Only if the env is NOT parallel used, need to reserve and wait
                if self.moduleProperties['envParams'].get('parallelUsage', False) == False:
                    if 'envParams' in self.moduleProperties:
                        if self.execRestApiObj:
                            self.lockAndWaitForEnv(sessionId=self.timestampFolderName,
                                                   overallSummaryFile=f'{self.resultsTimestampFolder}/overallSummary.json', 
                                                   user=self.user, 
                                                   stage=self.stage, module=self.module)

                        if self.execRestApiObj is None:
                            if self.moduleProperties['envParams'].get('parallelUsage', False) == False:
                                errorMsg = f'The module {self.module} uses env {self.env} that has parallelUsage=False. Cannot run this test because managing Env usage requires the Keystack web UI/MongoDB docker container especially if parallelUsage=False, which is disabled.'
                                self.abortTheTest(errorMsg)
                
                # The env is parallel used                   
                if self.moduleProperties['envParams'].get('parallelUsage', False) == True:
                    # Update env active user
                    if self.execRestApiObj:
                        self.reserveEnv(overallSummaryFile=f'{self.resultsTimestampFolder}/overallSummary.json',
                                        env=self.moduleProperties['env'])

            # Note: The stage/module xpath were initialized in the playbook class in:
            #       executeStages().runModuleHelper()
            self.playbookObj.overallSummaryData['stages'][self.stage]['modules'].append(
                {self.module: {'result':None, 'env': self.env, 'currentlyRunning': None}})
                
            # The self.moduleResultsFolder could be updated in the envLoadBalance() function with updated ENV=<env>
            self.moduleSummaryData.update({'status': 'Started',
                                           'result': 'Not-Ready',
                                           'cases': dict(),
                                           'env': self.env,
                                           'envPath': self.envFile,
                                           'sessionId': self.sessionId,
                                           'totalLoopIterations': totalIterations,
                                           'outerLoop': self.totalOuterLoopIterations,
                                           'topLevelResultFolder': self.resultsTimestampFolder,
                                           'moduleResultsFolder': self.moduleResultsFolder,
                                           'currentlyRunning': None,
                                           'progress': f'0/{totalIterations}',
                                           'totalCases': len(self.testcaseSortedOrderList),
                                           'pausedOnError': False,
                                           'started': self.testStart.strftime('%m-%d-%Y %H:%M:%S:%f'),
                                           'abortModuleFailure': self.envParams['abortModuleFailure'], 
                                           }) 
            
            writeToJson(self.moduleSummaryFile, self.moduleSummaryData, mode='w', threadLock=self.lock)
                
        except (KeystackException, Exception) as errMsg:
            self.abortTheTest(str(errMsg))
        
        # Verify all exceptionErrors.  Don't go beyond this point if there is any exception error
        
        dictIndexList = getDictIndexList(self.playbookObj.overallSummaryData['stages'][self.stage]['modules'], self.module)
        if dictIndexList == []:
            self.playbookObj.overallSummaryData['stages'][self.stage]['modules'].append(
                {self.module: {'result':None, 'env': self.env, 'currentlyRunning': None}})
         
        if len(self.moduleSummaryData['exceptionErrors']) != 0:
                self.testStopTime = datetime.datetime.now()
                self.testDeltaTime = str((self.testStopTime - self.testStartTime))
                self.moduleSummaryData['stopped'] = self.testStopTime.strftime('%m-%d-%Y %H:%M:%S:%f')
                self.moduleSummaryData['testDuration'] = self.testDeltaTime
                self.moduleSummaryData['status'] = 'Aborted'
                self.moduleSummaryData['result'] = 'None'
                self.moduleSummaryData['totalTestAborted'] += 1
                self.moduleSummaryData['currentlyRunning'] = None
                writeToJson(self.moduleSummaryFile, self.moduleSummaryData, mode='w', threadLock=self.lock)
                
                self.playbookObj.overallSummaryData['currentlyRunning'] = None
                self.playbookObj.overallSummaryData['status'] = 'Aborted'
                self.playbookObj.overallSummaryData['totalTestAborted'] += 1
                self.playbookObj.overallSummaryData['result'] = 'None' 
                writeToJson(self.playbookObj.overallSummaryDataFile, data=self.playbookObj.overallSummaryData, mode='w')
                self.generateModuleTestReport(modulePretestAborted=True)
                return
                            
        # For Keystack sessionMgmt
        testcaseCounter = 0
        
        # Not-Ready | Passed | Failed
        self.overallResult = 'Not-Ready'

        # For test with loops
        self.excludePassedResults = False
        
        # For KPI analyzing
        self.operators = {'>': operator.gt, '<': operator.lt, '<=': operator.le, '>=': operator.ge, '=': operator.eq}

        # This will allow scripts to import keystackEnv in order for scripts to use test parameters from env, testcases, playbook
        sys.path.append(GlobalVars.appsFolder)
        
        for outerLoop in range(1, self.totalOuterLoopIterations+1):
            self.outerLoop = outerLoop
            
            for eachTestcase in self.testcaseSortedOrderList:                
                self.abortTestCaseErrors = []
                self.loopTestcase = self.getLoopTestcaseCount(eachTestcase)
                
                # Playbook Modules could run scripts from another module. So, cannot parse by using self.module
                regexMatch = re.search(f'{GlobalVars.keystackTestRootPath}/Modules/.+?/(.+)\..+', eachTestcase)
                if regexMatch:
                    self.testcaseYmlFilename = regexMatch.group(1)

                self.testcaseAppLibraryPathsToImport = self.getTestcaseAppLibraryPath(eachTestcase)
                 
                # Keystack integrated Python scripts
                if self.testcaseDict[eachTestcase].get('pythonScript', None):
                    self.testcasePythonScript = self.getTestcaseScript(typeOfScript='pythonScript', testcase=eachTestcase)
                else:
                    self.testcasePythonScript = False

                # Standalone Python scripts
                if self.testcaseDict[eachTestcase].get('standalonePythonScript', None):
                    self.testcaseStandalonePythonScript = self.getTestcaseScript(typeOfScript='standalonePythonScript', testcase=eachTestcase)
                else:
                    self.testcaseStandalonePythonScript = False
                
                # Shell/Bash scripts                        
                if self.testcaseDict[eachTestcase].get('bashScript', None):
                    self.testcaseBashScript = self.getTestcaseScript(typeOfScript='bashScript', testcase=eachTestcase)
                else:
                    self.testcaseBashScript = False
             
                self.eachTestcase = eachTestcase
                self.innerLoopCounter = 1

                while True:
                    if self.innerLoopCounter > self.loopTestcase:
                        break
                    
                    try:
                        # Result: Passed, Failed, Incomplete
                        # Status: Did-Not-Start, Started, Running, Aborted, Terminated
                        # Each testcase summary report
                        self.testcaseData = {'testcase': eachTestcase,
                                             'timeStart': None,
                                             'timeStop': None,
                                             'testDuration': None,
                                             'status': 'Did-Not-Start',
                                             'outerLoop': f'{self.outerLoop}/{self.totalOuterLoopIterations}',
                                             'innerLoop': f'{self.innerLoopCounter}/{self.loopTestcase}',
                                             'currentInnerOuterLoop': f'{self.outerLoop}/{self.innerLoopCounter}',
                                             'testConfiguredDuration': None,
                                             'testModule': self.module,
                                             'testSessionId': None,
                                             'testSessionIndex': None,
                                             'pythonScript': self.testcasePythonScript,
                                             'standaloneScript': self.testcaseStandalonePythonScript,
                                             'bashScript': self.testcaseBashScript,
                                             'result': 'Not-Ready',
                                             'totalFailures': 0,
                                             'KPIs': dict(),
                                             'testcaseResultsFolder': None,
                                             'testAborted': 'No',
                                             'pausedOnError': '',
                                             'exceptionError': [],
                                             'warnings': [],
                                             'failures': [],
                                             'passed': [],
                                             'skipped': False}
                        
                        testcaseCounter += 1
                        self.moduleSummaryData['currentlyRunning'] = eachTestcase
                        self.moduleSummaryData['progress'] = f'{testcaseCounter}/{totalIterations}'
                        self.testcaseResult = 'Not-Ready'
                        self.testcaseStart = datetime.datetime.now() # for test time delta
                        self.testcaseData['timeStart'] = self.testcaseStart.strftime('%m-%d-%Y %H:%M:%S:%f')
                        
                        # 'modules' field contains a list. In order to update the current module, must get the index,
                        # make the updates and insert it back to the same index position in the list.
                        # Note: The module properties were initialized in the playbook class in:
                        #       executeStages().runModuleHelper()
                        dictIndexList = getDictIndexList(self.playbookObj.overallSummaryData['stages'][self.stage]['modules'], self.module)
                        index = getDictIndexFromList(dictIndexList, key='env', value=self.moduleProperties['env'])
                        runningModule = {self.module: {'result':   self.moduleSummaryData['result'], 
                                                       'env':      self.moduleProperties['env'], 
                                                       'progress': self.moduleSummaryData['progress'],
                                                       'currentlyRunning': eachTestcase}}
                        self.playbookObj.overallSummaryData['stages'][self.stage]['modules'].pop(index)
                        self.playbookObj.overallSummaryData['stages'][self.stage]['modules'].insert(index, runningModule)
                        writeToJson(self.playbookObj.overallSummaryDataFile, data=self.playbookObj.overallSummaryData, mode='w', 
                                    threadLock=self.lock)

                        if self.module not in ['AirMosaic']:
                            # AirMosaic result folder has additional cell vendor folder. Created in airMosaic.py.
                            # moduleResultsFolder: /Results/Playbook_L3Testing/04-20-2022-12:34:22:409096_<sessionId>/STAGE=Test_MODULE=PythonScripts_ENV=None
                            self.testcaseResultsFolder = f'{self.moduleResultsFolder}/{self.testcaseYmlFilename}_{str(self.outerLoop).rjust(4, "0")}x_{str(self.innerLoopCounter).rjust(4, "0")}x'
                            self.testcaseData['testcaseResultsFolder'] = self.testcaseResultsFolder
                            self.testcaseDebugLogFile  = f'{self.testcaseResultsFolder}/test.log' 
                            self.testSummaryFile       = f'{self.testcaseResultsFolder}/testSummary.json'
                            execSubprocess(['mkdir', '-p', self.testcaseResultsFolder], stdout=False)
                            chownChmodFolder(self.resultsTimestampFolder, self.playbookObj.user, GlobalVars.userGroup, stdout=False)
                            
                            # Create testcase results meta folder for /.Data/ResultsMeta
                            testcaseFileName = eachTestcase.split('/')[-1]
                            self.testcaseResultsMetaFolder = '/'.join(f'{self.playbookObj.resultsMetaFolder}{eachTestcase}'.split('/')[:-1])
                            loopStrFormat = self.testcaseData["currentInnerOuterLoop"].replace('/', '_')
                            self.testcaseResultsMetaFile = f'{self.testcaseResultsMetaFolder}/{testcaseFileName}_{loopStrFormat}'
                            mkdir2(self.testcaseResultsMetaFolder, stdout=False)
                            execSubprocessInShellMode(f'touch {self.testcaseResultsMetaFile}', showStdout=False)
                            chownChmodFolder(self.playbookObj.resultsMetaFolder, user=self.playbookObj.user,
                                             userGroup=GlobalVars.userGroup, stdout=False)
                            execSubprocess(['chmod', '-R', '774', self.resultsTimestampFolder], stdout=False)
                            self.writeToTestcaseLogFile(f'[STARTING CASE]: {eachTestcase}...Iterating: {self.outerLoop}:{self.innerLoopCounter}/{self.loopTestcase}x', writeType='w')
                 
                        # TEST CASE CONFIGS:
                        self.testcaseConfigParams = {}
                        self.testcaseConfigParams['configParams'] = {}
                        
                        # 1of3: Keystack reads Env keyword "configParams" and store them in moduleProperties['envParams']['configParams'] first.
                        # Then below this, testcase yml files overwrite them if keyword 'configParams' exists.
                        if self.moduleProperties.get('envParams', None):
                            # Need to read the env file configParams again because LoadCore del agents['agent']
                            if 'configParams' in self.moduleProperties['envParams']:
                                envFileContents = readYaml(self.envFile)
                                self.moduleProperties['envParams'].update({'configParams': envFileContents['configParams']})
                                self.testcaseConfigParams['configParams'].update(self.moduleProperties['envParams']['configParams'])
     
                        # 2of3: For modules such as LoadCore: Each testcase must make a new copy of the key 'configParams' 
                        # because LoadCore MW.reassignPorts() does a del agents['agent'] in the key 'configParam'                       
                        # If testcase yml file has 'configParams', overwrite the configParams from Env file
                        freshCopy = deepcopy(self.testcaseDict[eachTestcase])
                        for key,value in freshCopy.items():
                            if key == 'configParams':
                                continue
                            self.testcaseConfigParams.update({key: value})

                        if 'configParams' in self.testcaseDict[eachTestcase]:
                            self.testcaseConfigParams['configParams'].update(self.testcaseDict[eachTestcase]['configParams'])

                        # 3of3: Ultimately, confgiParams are overwritten by ConfigParameters file if the testcase includes it.
                        #       Location: /Modules/<name>/ConfigParameters
                        #       Used for: Passing in variables into scripts / data-model file
                        configParametersFile = self.testcaseDict[eachTestcase].get("configParametersFile", None)
                        if configParametersFile not in ['', 'None', 'none', None, 'null']:
                            match = re.search('(.*ConfigParameters/)?(.*)', configParametersFile)
                            self.configParamsFileFullPath = f'{self.configParametersFilePath}/{match.group(2)}'
                            if os.path.exists(self.configParamsFileFullPath) == False:
                                raise Exception(f'keystack: The configuration parameters file does not exists: {self.configParamsFileFullPath}')
                            
                            configs = readYaml(self.configParamsFileFullPath)
                            self.testcaseConfigParams['configParams'] = configs

                        # Location: /Modules/<name>/ExportedConfigs                    
                        exportedConfigFileName = self.testcaseDict[eachTestcase].get("exportedConfigFile", None)
                        if exportedConfigFileName not in ['', 'None', 'none', None, 'null']:
                            regexMatch = re.search('(.*ExportedConfigs/)?(.*)', exportedConfigFileName)
                            if regexMatch:
                                self.exportedConfigFullPath = f'{self.exportedConfigsFolder}/{regexMatch.group(2)}'
                                if os.path.exists(self.exportedConfigFullPath) == False:
                                    self.writeToTestcaseLogFile(f'Keystack: The exported config file does not exists: {self.exportedConfigFullPath}')
                                    raise KeystackException(f'Keystack: The exported config file does not exists: {self.exportedConfigFullPath}')

                        # Verify test case dependecies
                        dependencySkipTestcase = False
                       
                        # moduleProperties: {'enable': True, 'env': 'None', 'playlist': ['/Modules/CustomPythonScripts/Bringups']}
                        if 'dependencies' in self.moduleProperties:                     
                            for isCurrentTestcase in self.moduleProperties['dependencies'].keys():
                                if isCurrentTestcase in eachTestcase:
                                    if 'enable' in self.moduleProperties['dependencies'][isCurrentTestcase] and \
                                        self.moduleProperties['dependencies'][isCurrentTestcase]['enable'] == False:
                                            continue

                                    self.testcaseData.update(self.moduleProperties['dependencies'][isCurrentTestcase])
                                    dependOnCases = self.moduleProperties['dependencies'][isCurrentTestcase]['dependOnCases']
                                    
                                    # dependencies:
                                    #     /Modules/CustomPythonScripts/Samples/Testcases/isis.yml:
                                    #     enable: False
                                    #         dependOnCases:
                                    #             - /Modules/CustomPythonScripts/Samples/Testcases/bgp.yml
                                    for eachDependentCase in dependOnCases:
                                        if eachDependentCase.startswith('/Modules/'):
                                            eachDependentCase = f'{self.keystackTestRootPath}{eachDependentCase}'
                                        if eachDependentCase.startswith('Modules/'):
                                            eachDependentCase = f'{self.keystackTestRootPath}/{eachDependentCase}'

                                        # Iterate all looped test case result files:
                                        for resultFile in glob(f'{self.playbookObj.resultsMetaFolder}{eachDependentCase}*'):
                                            currentDependecyData = readJson(f'{resultFile}')
                                            # The dependent testcase had ran and finished already
                                            result = currentDependecyData['result']

                                            self.writeToTestcaseLogFile(f'[DEPENDENCY]: {eachDependentCase}:  Result={result}') 
                                            if result != 'Passed':
                                                # Update the current running testcase. Pop it and insert updated data.
                                                self.testcaseData.update({'result': 'Skipped', 
                                                                          'status': 'Skipped', 
                                                                          'skipped': True,
                                                                         })
                                                match = re.search('(/Modules.+)', eachDependentCase)
                                                if match:
                                                    theModule = match.group(1)
                                                else:
                                                    theModule = eachDependentCase
                                                    
                                                msg = f"Dependent case failed: {theModule}"
                                                self.testcaseData['failures'].append(msg)
                                                writeToJson(self.testcaseResultsMetaFile, self.testcaseData)
                                                self.writeToTestcaseLogFile(f'[SKIPPING TESTCASE]: Dependency failed: {eachDependentCase}')
                                                dependencySkipTestcase = True
                                                self.playbookObj.moduleSummaryData['totalSkipped'] += 1
                            
                        writeToJson(self.moduleSummaryFile, self.moduleSummaryData, mode='w', threadLock=self.lock, retry=5)
                     
                        # The current testcase depends on a testcase that failed. Skip this testcase
                        if dependencySkipTestcase:
                            break

                        # Skip this testcase if there is any exception errors
                        if self.abortTestCaseErrors:
                            raise KeystackException(self.abortTestCaseErrors)

                        # Additional library modules to import that supports the test case
                        for appLibraryPath in self.testcaseAppLibraryPathsToImport:
                            sys.path.append(appLibraryPath)
                                
                        self.testcaseData['status'] = 'Running'
                        self.updateModuleStatusData(status="Running")
                
                        if self.testcaseBashScript:
                            self.runStandAloneScript(typeOfScript='shell', scriptFullPath=self.testcaseBashScript)
                            
                        if self.testcaseStandalonePythonScript:
                            self.runStandAloneScript(typeOfScript='python', scriptFullPath=self.pythonScriptFullPath)
                         
                        if self.testcasePythonScript:
                            if 'keystackEnv' in sys.modules:
                                del sys.modules['keystackEnv']
                            
                            sys.path.append(f'{GlobalVars.keystackSystemPath}/Apps')
                        
                            #import keystackEnv
                            #keystackEnv.keystackObj = self
                            __import__('keystackEnv').keystackObj = self
                            runpy.run_path(path_name=self.pythonScriptFullPath)
                                       
                        # Getting means the testcase is done successfully
                        self.testcaseData['status']  = 'Completed'
                         
                        if self.testcaseResult == 'Failed':
                            self.moduleSummaryData['totalFailed'] += 1
                            self.playbookObj.overallSummaryData['totalFailed'] += 1
                            self.testcaseData['result'] = 'Failed'
                            self.moduleSummaryData['result'] = 'Failed'
                            # Overwrite the overallResult to Failed if there is a failure
                            self.overallResult = 'Failed'                        

                        if self.testcaseResult != 'Failed':
                            self.testcaseResult = 'Passed'
                            self.testcaseData['result'] = 'Passed'
                            self.moduleSummaryData['totalPassed'] += 1
                            self.playbookObj.overallSummaryData['totalPassed'] += 1
                            
                        # Update the current overall result. 
                        if self.moduleSummaryData['totalFailures'] == 0:
                            if self.overallResult != 'Failed':
                                self.overallResult = 'Passed'
                                self.testcaseData['result'] = 'Passed'
         
                        self.testcaseStop = datetime.datetime.now()
                        self.testcaseData['timeStop'] = self.testcaseStop.strftime('%m-%d-%Y %H:%M:%S:%f')
                        self.testcaseData['testDuration'] = str((self.testcaseStop - self.testcaseStart))
                        
                        self.moduleSummaryData['currentlyRunning'] = None
                                
                        writeToJson(self.testSummaryFile, self.testcaseData, mode='w', threadLock=self.lock, retry=5)
                        writeToJson(self.testcaseResultsMetaFile, self.testcaseData, mode='w', threadLock=self.lock)
                       
                        if self.testcaseResult == 'Failed' and self.envParams['abortModuleFailure']:
                            raise KeystackException('abortModuleFailure is set to True. Aborting Test.')
                                                            
                        if self.waitTimeBetweenTests > 0:
                            time.sleep(int(self.waitTimeBetweenTests))

                        self.writeToTestcaseLogFile(f'[CASE COMPLETED]: STAGE:{self.stage} MODULE:{self.module} CASE:{eachTestcase} {self.outerLoop}/{self.totalOuterLoopIterations}x {self.innerLoopCounter}/{self.loopTestcase}x [CASE RESULT]: {self.testcaseResult}')

                    except (AssertionError, KeystackException, Exception) as errMsg:
                        if self.testcaseData['status'] == 'Did-Not-Start':
                            self.writeToTestcaseLogFile(f'[CASE DID NOT RUN]: STAGE:{self.stage} MODULE:{self.module} CASE:{eachTestcase} {self.outerLoop}/{self.totalOuterLoopIterations}x {self.innerLoopCounter}/{self.loopTestcase}x')
                            
                        trace = ''
                        if sys.exc_info()[0] == KeystackException:
                            trace = str(errMsg)
                        else:
                            # -8 for two levels up
                            for eachTrace in traceback.format_exc().splitlines()[:]:
                                trace += f'{eachTrace}\n'
                            if trace == '': trace = None
                                                            
                        self.testcaseStop = datetime.datetime.now()
                        self.testcaseResult = 'Aborted'
                        self.testcaseData['timeStop'] = self.testcaseStop.strftime('%m-%d-%Y %H:%M:%S:%f')
                        self.testcaseData['result'] = 'Aborted'
                        self.testcaseData['testAborted'] = 'Yes'
                        self.testcaseData['status'] = 'Aborted'

                        self.testcaseData['exceptionErrors'].append(trace)
                        self.testcaseData['failures'].append(trace)

                        writeToJson(self.testSummaryFile, self.testcaseData, mode='w', threadLock=self.lock, retry=5)                  
                        self.moduleSummaryData['status'] = 'Aborted'
                        self.moduleSummaryData['result'] = 'Incomplete'
                        self.moduleSummaryData['totalTestAborted'] += 1
                        self.moduleSummaryData['currentlyRunning'] = None
                        self.moduleSummaryData['exceptionErrors'].append(trace)     
                        writeToJson(self.moduleSummaryFile, self.moduleSummaryData, mode='w', threadLock=self.lock)
                        
                        try:
                            self.writeToTestcaseLogFile(trace)
                        except:
                            # It is ok to fail to write to the testcase log file because
                            # it might not exists yet.
                            pass
                        
                        self.playbookObj.overallSummaryData['totalTestAborted'] += 1
                        self.playbookObj.overallSummaryData['exceptionErrors'].append(f'TestAborted: Stage={self.stage} Module={self.module} Testcase={self.testcaseYmlFilename} Exception: {errMsg}')
                        self.playbookObj.overallSummaryData['result'] = 'Incomplete'   
                                                
                        writeToJson(self.testcaseResultsMetaFile, self.testcaseData, mode='w', threadLock=self.lock)
                        
                        if self.envParams['abortModuleFailure']:
                            # Abort the test and don't run anymore testcases so user could debug the state of the test
                            self.writeToTestcaseLogFile('[ABORT-ON-FAILURE] abortModuleFailure is set to True. Aborting test. The session is remained open for debugging.')
   
                    finally:
                        # Clean up sys path
                        try:
                            for appLibraryPath in self.testcaseAppLibraryPathsToImport:
                                index = sys.path.index(appLibraryPath)
                                del sys.path[index]
                                
                            if 'keystackEnv' in sys.modules:
                                del sys.modules['keystackEnv']    
                        except:
                            # It's ok to fail here
                            pass
                        
                        chownChmodFolder(topLevelFolder=self.resultsTimestampFolder, user=self.user, userGroup=GlobalVars.userGroup)
                        
                        if self.awsS3UploadResults:
                            uploadToS3 = True
                            
                            # For loop tests, don't upload all the passed logs and artifacts to save space.
                            if self.totalOuterLoopIterations > 1 or self.loopTestcase > 1:
                                if self.testcaseData['result'] == 'Passed' and self.stage not in ['Bringup', 'Teardown']:
                                    uploadToS3 = False
                                    
                                    if self.playbookObj.includeLoopTestPassedResults:
                                        # Allow users to overwrite the default
                                        uploadToS3 = True

                            if uploadToS3:
                                # /opt/KeystackSystem/ServicesStagingArea/AwsS3Uploads/07-04-2022-18:55:00:743939
                                # self.testcaseResultsFolder = /path/KeystackTests/Results/GROUP=Default/PLAYBOOK=Samples-pythonSample/04-10-2023-08:40:11:952322_<sessionId>/STAGE=Test_MODULE=CustomPythonScripts_ENV=pythonSample/bgp_0001x_0001x
                                # self.timestampFolderName = 04-13-2023-13:36:52:855428_hgee9
                                
                                informAwsS3ServiceForUploads(playbookName=self.playbookObj.playbookAndNamespace, sessionId=self.sessionId,
                                                             resultsTimestampFolder=self.resultsTimestampFolder,
                                                             listOfFilesToUpload=[self.testcaseResultsFolder],
                                                             loginCredentialPath=self.playbookObj.credentialYmlFile,
                                                             loginCredentialKey=self.playbookObj.loginCredentialKey,
                                                             logFile=self.testcaseDebugLogFile)
                        
                        if self.testcaseData['result'] == 'Passed' and self.stage not in ['Bringup', 'Teardown'] and \
                            self.playbookObj.includeLoopTestPassedResults == False:
                            if self.totalOuterLoopIterations > 1 or self.loopTestcase > 1:
                                execSubprocessInShellMode(f'rm -rf {self.testcaseResultsFolder}', showStdout=False)
                                self.excludePassedResults = True
                                
                        if self.moduleSummaryData['status'] == 'Aborted' and self.envParams['abortModuleFailure']:
                            # Break ouf of the innerLoop while loop
                            break
                        else:
                            self.innerLoopCounter += 1
                
                        if self.testcaseData['result'] in ['Failed', 'Aborted']:
                            if self.playbookObj.abortTestOnFailure:
                                self.playbookObj.exitTest = True
                                self.logWarning('-abortTestOnFailure was enabled. Aborting test.')
                                
                                self.moduleSummaryData['status'] = 'Aborted'
                        
                                self.testcaseData['status'] = 'Aborted'
                                self.testcaseData['testAborted'] = 'Yes'
                                writeToJson(self.testcaseResultsMetaFile, self.testcaseData, mode='w', threadLock=self.lock)
                            
                                self.playbookObj.overallSummaryData['testAborted'] = True
                                self.playbookObj.overallSummaryData['status'] = 'Aborted'
                            
                            if self.playbookObj.abortStageFailure:
                                self.playbookObj.overallSummaryData['testAborted'] = True
                                self.playbookObj.overallSummaryData['stageFailAborted'] = True
                            
                            writeToJson(self.playbookObj.overallSummaryDataFile, data=self.playbookObj.overallSummaryData, mode='w')    
                            break
                            
                # Inner while loop        
                if self.moduleSummaryData['status'] == 'Aborted' and self.envParams['abortModuleFailure']:
                   # Break out of the testcase for loop
                   break
                
                if self.playbookObj.exitTest:
                    break
            
            # Outer loop testcases                        
            if self.moduleSummaryData['status'] == 'Aborted' and self.envParams['abortModuleFailure']:
                # Break out of the outerLoop iteration for loop
                break
        
            if self.playbookObj.exitTest:
                break
                        
        # When the module is done, upload the module folder files:
        if self.awsS3UploadResults:
            informAwsS3ServiceForUploads(playbookName=self.playbookObj.playbookAndNamespace, sessionId=self.sessionId,
                                         resultsTimestampFolder=self.resultsTimestampFolder,
                                         listOfFilesToUpload=[f'{self.moduleResultsFolder}/moduleTestReport',
                                                              f'{self.moduleResultsFolder}/moduleSummary.json'],
                                         loginCredentialPath=self.playbookObj.credentialYmlFile,
                                         loginCredentialKey=self.playbookObj.loginCredentialKey)
                                               
        # Test is over.  Close it up.       
        self.testStopTime = datetime.datetime.now()
        self.testDeltaTime = str((self.testStopTime - self.testStartTime))

        if self.moduleSummaryData['status'] != 'Aborted':
            self.updateModuleStatusData(status='Completed')
            self.moduleSummaryData['result'] = self.overallResult
        else:
            if self.playbookObj.exitTest == False:
                self.moduleSummaryData['result'] = 'Incomplete'
            else:
                 self.moduleSummaryData['result'] = 'Failed'
        
        self.moduleSummaryData['currentlyRunning'] = None
        self.moduleSummaryData['stopped'] = self.testStopTime.strftime('%m-%d-%Y %H:%M:%S:%f')
        self.moduleSummaryData['testDuration'] = self.testDeltaTime
        writeToJson(self.moduleSummaryFile, self.moduleSummaryData, mode='w', threadLock=self.lock)
                
        # METADATA: for KeystackUI
        # self.playbookObj.overallSummaryData['stages'][self.stage]['modules'][self.module].update({
        #     'result': self.moduleSummaryData['result'], 'env': self.moduleProperties['env'], 'currentlyRunning': None})
        dictIndexList = getDictIndexList(self.playbookObj.overallSummaryData['stages'][self.stage]['modules'], self.module)
        index = getDictIndexFromList(dictIndexList, key='env', value=self.moduleProperties['env'])
        runningModule = {self.module: {'result':self.moduleSummaryData['result'], 
                                       'env': self.moduleProperties['env'], 
                                       'currentlyRunning': None}}
        
        if self.overallResult ==' Passed':
            self.playbookObj.overallSummaryData['stages'][self.stage]['result'] = 'Passed'
        elif self.moduleSummaryData['status'] == 'Aborted':
            self.playbookObj.overallSummaryData['stages'][self.stage]['result'] = 'Aborted'
        else:
            self.playbookObj.overallSummaryData['stages'][self.stage]['result'] = self.overallResult
        self.playbookObj.overallSummaryData['stages'][self.stage]['modules'].pop(index)
        self.playbookObj.overallSummaryData['stages'][self.stage]['modules'].insert(index, runningModule)
        writeToJson(self.playbookObj.overallSummaryDataFile, data=self.playbookObj.overallSummaryData, mode='w', 
                    threadLock=self.lock)
                        
        # Release the env if module passed.
        if self.env and self.env != 'bypass':
            if self.moduleProperties['envParams'].get('parallelUsage', False) == True:
                self.releaseEnv(env=self.moduleProperties['env']) 
                
            if self.moduleProperties['envParams'].get('parallelUsage', False) == False:
                if self.execRestApiObj:
                    if self.excludePassedResults == False:
                        self.writeToTestcaseLogFile(f'Releasing Env: STAGE={self.stage} MODULE={self.module} ENV={self.moduleProperties["env"]}')
                        
                    moduleEnvMgmtData = readJson(self.moduleEnvMgmtFile)
                    
                    if '-' in self.moduleProperties['env']:
                        env = self.moduleProperties['env'].replace('-', '/')
                    else:
                        env = self.moduleProperties['env']
                        
                    params = {'env': env, 'sessionId':self.timestampFolderName,
                              'user':self.user, 'stage':self.stage, 'module':self.module, 'webhook':True}

                    if self.moduleSummaryData['result'] == 'Passed':
                        moduleEnvMgmtData['result'] = 'Passed'
                        self.releaseEnv(env=env)
                        # moduleEnvMgmtData['envIsReleased'] = True
                        # writeToJson(self.moduleEnvMgmtFile, moduleEnvMgmtData)
                    else:
                        moduleEnvMgmtData['result'] = 'Failed'
                        if self.holdEnvsIfFailed == False:
                            self.releaseEnv(env=env)
                            # moduleEnvMgmtData['envIsReleased'] = True
                            # writeToJson(self.moduleEnvMgmtFile, moduleEnvMgmtData)
           
        self.generateModuleTestReport()                        
        self.createJiraIssues()

        index = sys.path.index(f'{GlobalVars.appsFolder}')
        del sys.path[index]
        
        print(f'\nTest results are in: {self.resultsTimestampFolder}\n')
        return None
    
def argParse():
    """ 
    This function is created exclusively for setup.cfg
    
    [options.entry_points]
    console_scripts =
    keystack = Keystack.keystack:argParse
    """
    from parseParams import Parse  
    playbookObj = Parse(sys.argv)
    playbookObj.runPlaybook()

     
if __name__ == "__main__":
    try:
        from parseParams import Parse
        isTestAborted = False
        runObj = Parse(sys.argv)
        runPlaybookObj = runObj.runPlaybook()
        
    except KeyboardInterrupt:
        isTestAborted = True
        if runObj.timestampFolder:
            overallSummaryDataFile = f'{runObj.timestampFolder}/overallSummary.json'
            if os.path.exists(overallSummaryDataFile):
                overallSummaryData = readJson(overallSummaryDataFile)
                testStopTime = datetime.datetime.now()
                processId = overallSummaryData['processId']
                sessionId = overallSummaryData['sessionId']
                overallSummaryData['status'] = 'Terminated'
                overallSummaryData['result'] = 'Incomplete'
                overallSummaryData['stopped'] = testStopTime.strftime('%m-%d-%Y %H:%M:%S:%f')
                overallSummaryData['currentlyRunning'] = ''
                overallSummaryData['testAborted'] = True
                overallSummaryData['exceptionErrors'].append('CTRL-C was entered')
                writeToJson(overallSummaryDataFile, data=overallSummaryData, mode='w')
                        
                httpIpAddress, keystackIpPort, httpMethod = getHttpMethodIpAndPort()
                execRestApiObj = ExecRestApi(ip=httpIpAddress, port=keystackIpPort, https=httpMethod)
                                
                # keystasck_httpUrl = 'http://0.0.0.0'
                # httpUrl  = os.environ.get('keystack_httpUrl', GlobalVars.keystackHttpUrl)
                # httpIpAddress = httpUrl.split('http://')[-1]
                # execRestApiObj = ExecRestApi(ip=httpIpAddress, port=keystackIpPort, https=False)
                
                if execRestApiObj:
                    for envMgmtDataFile in glob(f'{runObj.timestampFolder}/.Data/EnvMgmt/*.json'):
                        envMgmtData = readJson(envMgmtDataFile)
                        env = envMgmtData['env']
                        envSessionId = envMgmtData['sessionId']
                        envUser = envMgmtData['user']
                        envStage = envMgmtData['stage']
                        envModule = envMgmtData['module']
                        params = {'user':envUser, 'sessionId':envSessionId, 'stage':envStage, 'module':envModule, 'env':env, 'webhook':True}

                        execRestApiObj.post(restApi='/api/v1/env/removeFromActiveUsersListUI', params=params, showApiOnly=True)
                        execRestApiObj.post(restApi='/api/v1/env/removeFromWaitList', params=params, showApiOnly=True)
                    
                # Terminate the running the process
                if os.environ['keystack_platform'] == 'linux':
                    result, process = execSubprocessInShellMode(f'sudo kill -9 {processId}')
                    
                if os.environ['keystack_platform'] == 'docker':
                    result, process = execSubprocessInShellMode(f'kill -9 {processId}')
                                
    except Exception as errMsg:
        if runObj and runObj.timestampFolder:
            overallSummaryDataFile = f'{runObj.timestampFolder}/overallSummary.json'
            if os.path.exists(overallSummaryDataFile):
                testStopTime = datetime.datetime.now()
                overallSummaryData = readJson(overallSummaryDataFile)
                overallSummaryData['status'] = 'Aborted'
                overallSummaryData['result'] = 'Incomplete'
                overallSummaryData['stopped'] = testStopTime.strftime('%m-%d-%Y %H:%M:%S:%f')
                overallSummaryData['currentlyRunning'] = ''
                overallSummaryData['testAborted'] = True
                overallSummaryData['exceptionErrors'].append(traceback.format_exc(None, errMsg))
                writeToJson(overallSummaryDataFile, data=overallSummaryData, mode='w')
                
        sys.exit(f'\nkeystack.py Exception: {traceback.format_exc(None, errMsg)}')

