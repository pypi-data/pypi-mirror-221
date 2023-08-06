import sys, os, argparse, re 
from glob import glob

from dotenv import load_dotenv

from globalVars import GlobalVars
from Services import Serviceware
from commonLib import showVersion, groupExists
from keystackUtilities import execSubprocessInShellMode, readFile, readYaml, writeToYamlFile, readJson, chownChmodFolder, mkdir2
from keystack import Playbook

class Parse:
    def __init__(self, sysArgv):
        self.sysArgv = sysArgv
        self.argParse()
        self.timestampFolder = None
        
    def argParse(self):
        """
        If packaging keystack for a pip install, this standalone app doesn't work if these argparse are 
        located under _name__ == "__main__". 
        Must wrap the CLI commands in a def so this app could run as a standalone app installed by pip install.
        A 'keystack' cli command is created in the localhost /python_path/bin directory.
        """
        if len(self.sysArgv) < 1:
            sys.exit('\nkeystack.py requires the following parameters: -playbook')

        parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
        parser.add_argument('-sessionId', default=None, help='For KeystackUI only: to reference for the process ID on ps command line')
        
        # -playbook: keystack UI playbook names could have white spaces.  nargs will make the value into a list
        # To get the -playbook value: args.playbook[0]
        parser.add_argument('-playbook', nargs="+", default=None,
                                                help='The playbook name. If playbook in a subfolder, then subfolder/playbookName')
        parser.add_argument('-pipeline', nargs="+",  default=None, help='The pipeline name to run test')
        parser.add_argument('-group', nargs="+",  default=None, help='The group for the test')    
        parser.add_argument('-resultsFolder',     default=None, help='Internal usage: From KeystackUI')
        parser.add_argument('-emailResults',      default=False, action='store_true', help='Send email results at the end of the test')
        parser.add_argument('-pauseOnError',      default=False, action='store_true', help='Pause the test on failure and error for debugging')
        parser.add_argument('-holdEnvsIfFailed',  default=False, action='store_true', help='Hold the Envs for debugging if the test failed')
        parser.add_argument('-debug',             default=False, action='store_true', help='Label report test was in debug mode')
        parser.add_argument('-includeLoopTestPassedResults', default=False, action='store_true', help='By default loop test passed results are not saved to save storage.')
        parser.add_argument('-abortTestOnFailure', default=False, action='store_true', help='Abort the test immediately upon a failure')
        parser.add_argument('-trackResults',       default=None, action='store_true',  help='Record result in CSV for graph view')
        parser.add_argument('-isFromKeystackUI',   default=False, action='store_true', help='Internal usage: If test is executed from KeystackUI')
        parser.add_argument('-awsS3',              default=False, action='store_true', help='Upload results to AWS S3 data-lake')
        parser.add_argument('-jira',               default=False, action='store_true', help='Create Jira issues for new failures')
        parser.add_argument('-wireshark',          default=False, action='store_true', help='Enable Wirehsark packet capturing')
        parser.add_argument('-startLsu',           default=False, action="store_true", help='Start the LSU. Defaults to False to save time')

        parser.add_argument('-version',              default=None, action='store_true', help='Show the Keystack version')
        parser.add_argument('-createGroup', nargs="+",  default=None, help='Create a group')
        parser.add_argument('-rmGroup', nargs="+",   default=None, help='Remove a group')
        parser.add_argument('-showGroups',           default=False, action='store_true', help='Show groups')
        parser.add_argument('-showPipelines',        default=False, action='store_true', help='Show all Pipelines') 
        parser.add_argument('-showKeystackSettings', default=False, action='store_true', help='Show keystackSystemSettings')
        parser.add_argument('-showPlaybooks',        default=False, action='store_true', help='Show all Playbooks')
        parser.add_argument('-showPlaybookParams',   default=None, help='Show Playbook parameters')
        parser.add_argument('-showEnvs',             default=False, action='store_true', help='Show all Envs')
        parser.add_argument('-showEnvUsageList',     default=False, action='store_true', help='Show all Env usage')
        parser.add_argument('-showEnvUsage', nargs="+",  default=None, help='Show who is using the env, who is waiting, is it locked')
        parser.add_argument('-showEnvParams',        default=None,  help='Show Envs params')        
        parser.add_argument('-restartServices',      default=False, action='store_true', help='Restart all Keystack services')
        parser.add_argument('-stopServices',         default=False, action='store_true', help='Stop all Keystack services')
        parser.add_argument('-restartAwsS3',         default=False, action='store_true', help='Restart AWS S3 services')
        parser.add_argument('-stopAwsS3',            default=False, action='store_true', help='Stop the AWS S3 service')
        parser.add_argument('-restartLogs',          default=False, action='store_true', help='Restart log service')
        parser.add_argument('-stopLogs',             default=False, action='store_true', help='Stop the logs service')
        
        # ENV MGMT
        parser.add_argument('-getEnvs',              default=False, action='store_true', help='Using rest api to get envs')
        parser.add_argument('-resetEnv',             nargs="+", help='Reset Env usage by releasing all active and waiting users')
        parser.add_argument('-releaseEnvOnFailure',  nargs="+", help='Release the env on a failure. Requires <resultTimestampPath> <env> <sessionId> <stage> <module>.  To get param values, enter -showPipelines')
        parser.add_argument('-showEnvActiveUsers',   nargs="+", help='Show env active users. Requires <env>.')
        
        parser.add_argument('-removeEnvFromActiveUsers', nargs="+", default=None, help='First, use -showEnvActiveUsers to get info. Then pass in params env:<env name> user:<user>  sessionId:<sessionId>  stage:<stage name>  module:<module name>')


        self.args = parser.parse_args()

        if self.args.sessionId and len(self.args.sessionId.split(' ')) > 1:
            sys.exit('Error: The parameter -sessionId cannot have spaces\n')
            
        if self.args.version:
            showVersion()
            sys.exit()

        if self.args.showPipelines:
            for index,pipeline in enumerate(glob(f'{GlobalVars.pipelineFolder}/*.yml')):
                print(f'{index+1}: {pipeline.split("/")[-1].split(".")[0]}')
            sys.exit()
                        
        if self.args.showEnvUsageList:
            for index,env in enumerate(glob(f'{GlobalVars.keystackSystemPath}/.DataLake/.EnvMgmt/*')):
                if env.endswith('.json'):
                    print(f'{index+1}: {env.split("/")[-1].split(".")[0]}')
            sys.exit()
        
        if self.args.showEnvUsage:
            envPath = f'{GlobalVars.keystackSystemPath}/.DataLake/.EnvMgmt/{self.args.showEnvUsage[0]}.json'
            sys.exit(readJson(envPath))
                            
        if self.args.showKeystackSettings:
            systemSettingsFullPath = f'{GlobalVars.keystackSystemPath}/keystackSystemSettings.env'
            try:
                print(readFile(systemSettingsFullPath))
            except Exception as errMsg:
                sys.exit(errMsg)
            sys.exit()
                        
        if self.args.showPlaybooks:
            index = 1
            for root,dir,files in os.walk(f'{GlobalVars.keystackTestRootPath}/Playbooks'):
                match = re.search(f'{GlobalVars.keystackTestRootPath}/Playbooks/(.*)', root)
                if match:
                    playbookFolder = f'{match.group(1)}/'
                else:
                    playbookFolder = ''
                    
                for eachFile in files:
                    if bool(re.search('.*(\.yml|\.yaml)$', eachFile)):
                        print(f'{index}: {playbookFolder}{eachFile.split(".")[0]}')
                        index += 1
            sys.exit()

        if self.args.showPlaybookParams:
            if '.yml' not in self.args.showPlaybookParams:
                playbook = f'{self.args.showPlaybookParams}.yml'
            else:
                playbook = self.args.showPlaybookParams
                
            playbookFullPath = f'{GlobalVars.keystackTestRootPath}/Playbooks/{playbook}'
            try:
                print(readFile(playbookFullPath))
            except Exception as errMsg:
                sys.exit(errMsg)
                
            sys.exit()
            
        if self.args.showEnvs:
            index = 1
            for root,dir,files in os.walk(f'{GlobalVars.keystackTestRootPath}/Envs'):
                match = re.search(f'{GlobalVars.keystackTestRootPath}/Envs/(.*)', root)
                if match:
                    envFolder = f'{match.group(1)}/'
                else:
                    envFolder = ''
                    
                for eachFile in files:
                    if bool(re.search('.*(\.yml|\.yaml)$', eachFile)):
                        print(f'{index}: {envFolder}{eachFile.split(".")[0]}')
                        index += 1
            sys.exit()
            
        if self.args.showEnvParams:
            if '.yml' not in self.args.showEnvParams:
                env = f'{self.args.showEnvParams}.yml'
            else:
                env = self.args.showEnvParams
                
            envFullPath = f'{GlobalVars.keystackTestRootPath}/Envs/{env}'
            try:
                print(readFile(envFullPath))
            except Exception as errMsg:
                sys.exit(errMsg)
            sys.exit()
            
        if self.args.createGroup:
            if os.path.exists(f'{GlobalVars.keystackSystemPath}/.DataLake') == False:
                mkdir2(f'{GlobalVars.keystackSystemPath}/.DataLake', stdout=False)
                chownChmodFolder(f'{GlobalVars.keystackSystemPath}/.DataLake', 'keystack', 'Keystack', permission=770)
                
            groupsFile = f'{GlobalVars.keystackSystemPath}/.DataLake/groups.yml'
            
            if os.path.exists(groupsFile) == False:
                writeToYamlFile({'groups': {'Default': {'allow': []}}}, groupsFile, mode='w', retry=5)

            execSubprocessInShellMode(f'chown :Keystack {groupsFile}', showStdout=False)
            execSubprocessInShellMode(f'chmod 770 {groupsFile}', showStdout=False)
            currentSystem = readYaml(groupsFile, retry=5)
            
            if self.args.createGroup[0] not in currentSystem.keys():
                currentSystem.update( {self.args.createGroup[0]: {'allow': ["*"]}} )
                writeToYamlFile(currentSystem, groupsFile, mode='w+', retry=5)
                sys.exit(f'\nCreated group: {self.args.createGroup[0]}')         
            else:
                sys.exit(f'The group already exists: {self.args.createGroup[0]}')

        if self.args.showGroups:
            groupsFile = f'{GlobalVars.keystackSystemPath}/.DataLake/groups.yml'
            if os.path.exists(groupsFile) == False:
                sys.exit('\nNo group created\n')
            else:
                showGroups = readYaml(groupsFile)
                groups = [group for group in showGroups.keys()]
                sys.exit(f'\n{groups}\n')
        
        if self.args.rmGroup:
            groupsFile = f'{GlobalVars.keystackSystemPath}/.DataLake/groups.yml'
            groupData = readYaml(groupsFile)
            print(groupData)
            if self.args.rmGroup[0] in groupData.keys():
                 del groupData[self.args.rmGroup[0]]
                 writeToYamlFile(groupData, groupsFile)
                 sys.exit()
            else:
                sys.exit(f'\nNo such group exists: {self.args.rmGroup}\n')
                        
        # For now, use groups to group results
        if self.args.group is None:
            self.group = 'Default'
        else:
            self.group = self.args.group[0]
            if groupExists(self.group) is None:
                sys.exit(f'\nThe group does not exists. Please use -createGroup {self.group} to create the group first.\n')
        
        if self.args.restartServices:
            Serviceware.KeystackServices().restartServices()
            sys.exit()

        if self.args.stopServices:
            Serviceware.KeystackServices().stopServices()
            sys.exit()

        if self.args.stopAwsS3:
            Serviceware.KeystackServices().stopAwsS3Service()
            sys.exit()
                            
        if self.args.restartAwsS3:
            Serviceware.KeystackServices().restartAwsS3()
            sys.exit()

        if self.args.stopLogs:
            Serviceware.KeystackServices().stopLogsService()
            sys.exit()
                    
        if self.args.restartLogs:
            Serviceware.KeystackServices().restartLogsService()
            sys.exit()
        
        if self.args.getEnvs:
            Env().getEnvs()
            sys.exit()

        if self.args.resetEnv:
            Env().reset(env=self.args.resetEnv)
            sys.exit()

        if self.args.releaseEnvOnFailure:                 
            Env().releaseEnvOnFailure(self.args.releaseEnvOnFailure)
            sys.exit()
                         
        if self.args.showEnvActiveUsers:
            Env().showEnvActiveUsers(env=self.args.showEnvActiveUsers)
            sys.exit()
 
        # TODO: Not completely working yet
        if self.args.removeEnvFromActiveUsers:                 
            Env().removeEnvFromActiveUsers(self.args.removeEnvFromActiveUsers)
            sys.exit()
            
                                     
    def runPlaybook(self):
        if self.args.playbook:
            self.args.playbook = self.args.playbook[0]
        else:
            self.args.playbook = None
            
        if self.args.pipeline:
            if '.yml' not in self.args.pipeline[0]:
                pipeline = f'{self.args.pipeline[0]}.yml'
            else:
                pipeline = self.args.pipeline[0]
            
            pipelineFile = f'{GlobalVars.pipelineFolder}/{pipeline}'      
            if os.path.exists(pipelineFile) == False:
                sys.exit(f'\nError: No such pipeline: {pipeline}\n')
                
            pipelineArgs = readYaml(pipelineFile)
            for key,value in pipelineArgs.items():
                if key == 'pipelineName':
                    continue
                
                if value:
                    if key == 'playbook':
                        match = re.search('(.*/Playbooks/)?(.*)', value)
                        value = match.group(2)
                        
                    setattr(self.args, key, value)
         
        playbookObj = Playbook(group=self.group, playbook=self.args.playbook, abortTestOnFailure=self.args.abortTestOnFailure,
                               emailResults=self.args.emailResults,
                               debugMode=self.args.debug, timestampFolder=self.args.resultsFolder,
                               sessionId=self.args.sessionId, pauseOnError=self.args.pauseOnError, 
                               holdEnvsIfFailed=self.args.holdEnvsIfFailed, includeLoopTestPassedResults=self.args.includeLoopTestPassedResults,
                               isFromKeystackUI=self.args.isFromKeystackUI, trackResults=self.args.trackResults,
                               awsS3Upload=self.args.awsS3, jira=self.args.jira, wireshark=self.args.wireshark, 
                               startLsu=self.args.startLsu)
        
        self.timestampFolder = playbookObj.timestampFolder
        result = playbookObj.executeStages()
        if result == 'Passed':
            sys.exit(0)
        else:
            sys.exit(1)


class Base:
    def __init__(self):
        from KeystackUI.execRestApi import ExecRestApi
        
        #load_dotenv(GlobalVars.keystackSystemSettingsFile)
        # 88028 | 443
        keystackUIPort = os.environ.get('keystack_keystackIpPort', 28028)
        self.execRestApiObj = ExecRestApi(ip='0.0.0.0', port=keystackUIPort, https=False)
 
class Env(Base):
    def getEnvs(self):
        response = self.execRestApiObj.get(restApi='/api/v1/env/list', params={'webhook': True})
        print()
        for env in response.json()['envs']:
            print(env)
        print()
    
    def reset(self, env=None):
        """
        Reset the Env
        
        /api/v1/env/reset
        
        Usage:
             keystack -resetEnv <env>
        """ 
        env = env[0]

        response = self.execRestApiObj.post(restApi='/api/v1/env/reset', params={'env':env, 'webhook': True})
        if response.status_code != 200:
            print('\nError\n')
            return
        else:
            print('\nSuccess\n')
            return
            
    def showEnvActiveUsers(self, env=None):
        """ 
        Returns: 
           {'sessionId': '04-24-2023-20:08:36:005025_9982', 'overallSummaryFile': '/opt/KeystackTests/Results/GROUP=Default/PLAYBOOK=Samples-pythonSample/04-24-2023-20:08:36:005025_9982/overallSummary.json', 'user': 'hgee', 'stage': 'Test', 'module': 'CustomPythonScripts'}

        """
        env = env[0]
        response = self.execRestApiObj.get(restApi='/api/v1/env/activeUsers', params={'env':env, 'webhook': True})
        if response.status_code != 200:
            print('\nError\n')
            return
            
        for env in response.json()['activeUsers']:
            testResult = env["overallSummaryFile"].split('Results')[-1].split('/overallSummary.json')[0]
            print(f'\n\tresultPath: {testResult}\n\tpipelineId: {env["sessionId"]}\n\tuser: {env["user"]}\n\tstage: {env["stage"]}\n\tmodule: {env["module"]}')
        print()

    def removeEnvFromActiveUsers(self, *args):
        """
        *args: env=<env name>   user=<user>   sessionId=<sessionId>   stage=<stage name>   module=<module name>
        
        POST https://0.0.0.0/api/v1/env/removeFromActiveUsersList
        """
        requiredParams = ['env', 'user', 'sessionId', 'stage', 'module']            
        params = {'env': None, 'sessionId':None,
                  'user':None, 'stage':None, 'module':None, 'webhook':True}
        
        try:
            for param in args[0]:
                key = param.split('=')[0]
                value =  param.split('=')[1]
                params[key] = value
                
        except Exception as errMsg:
            print(f'\nError: {errMsg}')
            return
        
        response = self.execRestApiObj.post(restApi='/api/v1/env/removeFromActiveUsersList', params=params, showApiOnly=False)
        if response.status_code != 200:
            print('\nError\n')
        else:
            print('\nSuccess\n')
        
    def releaseEnvOnFailure(self, *args):
        """
        args: resultTimestampPath=resultTimestampPath sessionId=sessionId  
               user=user stage=stage module=module env=env
               
        POST https://0.0.0.0/api/v1/env/releaseEnvOnFailure
        """         
        params = {'resultTimestampPath':None, 'sessionId':None,
                  'user':None, 'stage':None, 'module':None, 'env':None, 'webhook':True}

        try:
            for param in args[0]:
                key = param.split('=')[0]
                value =  param.split('=')[1]
                
                regexMatch = re.search(f'resultTimestampPath=(.+)', param)
                if regexMatch:
                    key = 'resultTimestampPath'
                    value = f'/opt/KeystackTests/Results/{regexMatch.group(1)}'
                
                regexMatch = re.search(f'env=(.+)', param)
                if regexMatch:
                    key = 'env'
                    value = regexMatch.group(1).replace('/', '-')
                    
                params[key] = value
                
        except Exception as errMsg:
            print(f'\nError: {errMsg}')
            return 
  
        response = self.execRestApiObj.post(restApi='/api/v1/env/releaseEnvOnFailure', params=params, showApiOnly=False)
        if response.status_code != 200:
            print('\nError\n')
        else:
            print('\nSuccess\n')
