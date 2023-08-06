"""
Description:
   This script does 3 different things:

      1> For new install:            python3 setupKeystack.py -setup docker|linux
      2> Update existing Keystack:   python3 setupKeystack.py -update docker|linux
      3> To generate sample scripts: python3 setupKeystack.py -getSamples -sampleDest .
                               This creates a folder called KeystackSamples 

   Setup Keystack environment:
      - Create a keystack user and a Keystack group on your Linux OS
      - Create keystack folders in the user specified path
           KeystackTests
              Envs
              Playbooks
              Modules
              Results
              ResultsArchive
           KeystackSystem
              keystackSystemSettings.env
              Logs
              ServiceStagingArea
              ResultDataHistory
              .loginCredentials.yml
  
   docker load -i dockerKeystack_v#.tar  <-- Install keystack docker container
    
   if docker-compose exists:           
        docker-compse will pull mongod:6.0.2
        start both docker containers using docker-compose
   else:     
        docker pull mongod:6.0.2
        docker run mongo
        docker run keystack

Requirements:
   - Must be a sudo user
   - Python 3.7+
   - Python pip install packages: dotenv
   - Docker
   - Know the path to put Keystack folders: Modules/Playbooks/Envs folders
   - Know the python full path. If you don't know this, enter: which <python>

For non Docker setup:
   - PIP install the keystack.whl file
   - sudo <your python full path> -m pip install keystack-<version>.whl
"""

import sys, os, re, subprocess, traceback, argparse, shutil
from time import sleep
from dotenv import load_dotenv

currentDir = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, currentDir.replace('/Setup', ''))

from keystackUtilities import execSubprocessInShellMode, execSubprocess2, readYaml, saveFileToBackupFile, mkdir, mkdir2, readFile, stopDockerContainer, removeDockerImage, verifyContainer
        
currentDir = os.path.abspath(os.path.dirname(__file__))

class SetupVar:
    keystackRootPath   = None
    keystackTestPath   = None
    keystackSystemPath = None
    userEnvSettings = readYaml(f'{currentDir}/userEnvSettings.yml')

    # Get the keystack version from the keystackSetup_<version> folder
    versionFile = currentDir.replace('/Setup', '/version')    
    keystackVersion = readYaml(versionFile)['keystackVersion']
    mongoVersion = '6.0.2'
    
    # Do not touch this variable: Docker's Python path
    # pythonFullPath = '/usr/bin/python3.8'
    dockerPythonFullPath = '/usr/bin/python3.8'
    pythonFullPath = None
    dockerHubUsername = 'hubertgee'
    
    # Internal setting.  Cannot be changed by user.
    keystackUserUid = 8000
    keystackGroupGid = 8001

    
class Setup:
    def generateSamples(self, keystackRootPath=None, destinationPath=None, alreadyBackedUpSystemFiles=False):
        """ 
        This function serves -setup and -getSamples
        
        Bundle up all samples.
        Dynamically generate a docker sample script with dynamic user defined path

        keystackRootPath: The Keystack folder location. This is automatically obtained by 
                          reading the /etc/keystack.py looking the the path to KeystackTests.
                          For ex: /opt/KeystackTests
        destinationPath: The path to where to put the generated samples
        """
        if destinationPath is None:
            # Called by -setup
            setup = True
            # Default
            samplesTargetPath = f'{keystackRootPath}/KeystackTests'
        else:
            # Called by -getSamples
            # User wants to get samples
            setup = False
            if os.path.exists(destinationPath) == False:
                sys.exit(f'\nYour stated dest path does not exists: {destinationPath}')

            samplesTargetPath = f'{destinationPath}/KeystackSamples'
            user = execSubprocessInShellMode('whoami')[-1]
            mkdir2(samplesTargetPath)

        # The included/excluded Modules are done by packageRelease already. So what ever is in the Samples are it. 
        execSubprocessInShellMode(f'sudo cp -R {currentDir}/Samples/* {samplesTargetPath}')        

        # Backup
        if setup == False:
            # Get samples
            execSubprocessInShellMode(f'sudo cp {currentDir}/Templates/keystackSystemSettings.env {samplesTargetPath}/keystackSystemSettings.env')
            execSubprocessInShellMode(f'sudo cp {currentDir}/Templates/.loginCredentials.yml {samplesTargetPath}/.loginCredentials.yml')
            
        # Docker test samples
        for dockerFile in [f'{currentDir}/Samples/Samples/Docker/dockerQuickTest', 
                           f'{currentDir}/Samples/Samples/Docker/dockerLoadcoreSample']:            
            filenameOnly = dockerFile.split('/')[-1]
            dockerSampleTemplateFile = dockerFile
            dockerSampleTemplate = readFile(dockerSampleTemplateFile).strip()
            dockerSampleTemplate = dockerSampleTemplate.replace('{path}', keystackRootPath)
            execSubprocessInShellMode(f"sudo echo '{dockerSampleTemplate}\n' | sudo tee {samplesTargetPath}/Docker/{filenameOnly}.sh")

        if setup == False:
           execSubprocessInShellMode(f'sudo chown -R {user}:{user} {samplesTargetPath}')
           execSubprocessInShellMode(f'sudo chmod -R 770 {samplesTargetPath}')  
           print(f'\ngetSamples: Done. Samples are in {samplesTargetPath}\n')
                    
        # Clean up
        execSubprocessInShellMode(f'sudo rm {SetupVar.keystackRootPath}/KeystackTests/Modules/__init__.py')        

    def installDockerImageKeystack(self, dockerBuildImagePath=None):
        """
        Install the docker image and start the container

        dockerBuildImagePath: The full path including file name to the docker tar file 
                         that gets installed as a docker image
        """
        ipPort = SetupVar.userEnvSettings["keystackPort"]
        keystackSecuredPort = SetupVar.userEnvSettings["keystackSecuredPort"]      
        dockerKeystackFilePath = currentDir.replace('/Setup', '')
        dockerKeystackFile = f'dockerKeystack_{SetupVar.keystackVersion}.tar'

        if dockerBuildImagePath is None:
            dockerBuildImagePath = f'{currentDir}/{dockerKeystackFile}'            

        if os.path.exists(dockerBuildImagePath):
            execSubprocessInShellMode(f'sudo docker load -i {dockerBuildImagePath}')
            sleep(2)

    def startDockerContainerKeystack():
        """ 
        Start the Keystack container with Docker run.
        Not by docker-compose
        """
        ipPort = SetupVar.userEnvSettings["keystackPort"]
        keystackSecuredPort = SetupVar.userEnvSettings["keystackSecuredPort"]  
        execSubprocessInShellMode(f'sudo docker run -p {ipPort}:{ipPort} -p {keystackSecuredPort}:{keystackSecuredPort} -d -v {SetupVar.keystackTestPath}:{SetupVar.keystackTestPath} -v {SetupVar.keystackSystemPath}:{SetupVar.keystackSystemPath} --name keystack --rm keystack:{SetupVar.keystackVersion}')
                        
    def installAndStartDockerContainers(self, mongoIp=None, dockerBuildImagePath=None):
        if dockerBuildImagePath:
            # User has no internet to install from docker hub
            # docker.tar file needs to be provided to the user to build the docker image on the host
            # docker load -i <keystack:version>
            self.installDockerImageKeystack(dockerBuildImagePath=dockerBuildImagePath)

        # Auto-Generate the docker-compose.yml file
        # docker compose will pull the mongoDB

        dockerComposeTemplateFile = f'{currentDir}/Templates/docker-compose.yml'
        dockerComposeTemplate = readFile(dockerComposeTemplateFile)
        for replacement in [('{keystackVersion}',     SetupVar.keystackVersion),
                            ('{mongoVersion}',        SetupVar.mongoVersion),
                            ('{mongoPort}',           SetupVar.userEnvSettings["mongoPort"]),
                            ('{keystackTestPath}',    SetupVar.keystackTestPath),
                            ('{keystackSystemPath}',  SetupVar.keystackSystemPath),
                            ('{mongoDpIp}',           mongoIp),
                            ('{keystackIp}',          SetupVar.userEnvSettings["keystackIp"]),
                            ('{keystackSecuredPort}', SetupVar.userEnvSettings["keystackSecuredPort"]),
                            ('{keystackPort}',        SetupVar.userEnvSettings["keystackPort"]),
                        ]:
            dockerComposeTemplate = dockerComposeTemplate.replace(replacement[0], str(replacement[1]))

        if dockerBuildImagePath is None:
            dockerComposeTemplate = dockerComposeTemplate.replace('{dockerHubUsername}', f'{SetupVar.dockerHubUsername}/')
        else:
            dockerComposeTemplate = dockerComposeTemplate.replace('{dockerHubUsername}', '')

        execSubprocessInShellMode(f'sudo echo "{dockerComposeTemplate}" | sudo tee {currentDir}/docker-compose.yml')
        execSubprocessInShellMode(f'sudo docker compose up -d')

        # If no docker compose, do it manually
        #    self.dockerPullMongo()
        #    self.dockerStartMongo()
            
        #    # Using docker run to start the container
        #    self.startDockerContainerKeystack()

    def dockerPullKeystack():
        """ 
        Pull from Docker hub
        """
        pass
    
    def dockerPullMongo():
        execSubprocessInShellMode(f'sudo docker pull mongo:{SetupVar.mongoVersion}')
        
    def dockerStartMongo():
        execSubprocessInShellMode(f'sudo docker run -d -p {SetupVar.userEnvSettings["mongoPort"]}:{SetupVar.userEnvSettings["mongoPort"]} -v {SetupVar.keystackSystemPath}/MongoDB:/data/db --name mongo --rm mongo:{SetupVar["mongoVersion"]}')
                    
    def askUserForIpAddress(self):
        """
        This is for -setup linux
        
        If using Docker without docker-compose or kubernettes to bring up
        the Keystack and Mongo containers, connecting to MongoDB requires
        a static IP address.  localhost, 0.0.0.0 and dns will not work.
        """                                                                                                        
        while True:
            mongoIp = input('\nWhich IP address on your host server should Keystack use? ')
            match = re.search('[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+', mongoIp)
            if not match:
                print(f'The IP format is incorrect. Please try again ...')
            else:
                break 

        return mongoIp

    def setup(self, platform=None, dockerBuildImagePath=None):     
        try:                
            # Verify if user has sudo priviledges
            whoami = execSubprocessInShellMode('whoami')[-1]
            isUserSudo = execSubprocessInShellMode(f'sudo -l -U {whoami}')[-1]
            if 'is not allowed' in isUserSudo:
                raise Exception(f'User {whoami} is not a sudo user. You must be a sudo user to setup Keystack. Also, if you must enter sudo password for each system wide command, then install this as the root user.')

            # Show instructions in the terminal
            os.system('clear')
            print('\n--- YOU MUST HAVE SUDO PRIVILEGES TO SETUP KEYSTACK! ---')
            print('\nSetting up Keystack requires you to answer a few questions:\n')
            # print('\t1> Are you using Keystack in docker? Default=docker')
            print('\t- Where do you want to put Keystack Playbooks/Modules/Envs/TestResult folders?')
            print('\t   (Ex: /, /opt, /usr/local)\n')
            print('\t- What is the Python full path that you use for running Python?')
            print('\t   (Ex: /usr/local/python3.10.0/bin/python3.10')
            print('\n\t   If you don\'t know, enter "which python3.10" on the CLI.\n\t   Copy and paste the full string.')
            print('\n\t   python3.10 is just an example.  It could be different in your system.')
            print('\n\nLets begin the setup ...')

            # Verify if the path exists
            while True:
                keystackRootPath = input('\nWhere do you want to install Keystack folders? (Ex: /, /opt, /usr/local. Default=/opt): ')
                if keystackRootPath == '':
                    keystackRootPath = '/opt'
                    print('\nDefaulting to /opt')
                    break
                else:
                    if os.path.exists(keystackRootPath) == False:
                        print('\nThere is no such path. Please try again ...')
                        continue
                    else:
                        break

            if os.path.isdir(keystackRootPath) == False:
                raise Exception(f'No such folder exists: {keystackRootPath}\n')
            
            keystackSystemPath = f'{keystackRootPath}/KeystackSystem'
            keystackTestsPath = f'{keystackRootPath}/KeystackTests'
            SetupVar.keystackRootPath = keystackRootPath
            SetupVar.keystackTestPath = keystackTestsPath
            SetupVar.keystackSystemPath = keystackSystemPath
            
            # /etc/keystack.yml
            execSubprocessInShellMode(f'sudo echo "keystackRootPath: {keystackRootPath}\nkeystackTestRootPath: {keystackTestsPath}\nkeystackSystemPath: {keystackSystemPath}\n" | sudo tee /etc/keystack.yml')

            while True:
                if os.path.exists(f'{keystackSystemPath}/MongoDB/WiredTiger'):
                    response = input(f'\nThere is an existing Keystack database. Do you want to wipe it out?  (y or n): ')
                    if response.lower() not in ['y', 'n']:
                        print(f'\nYou entered "{response}". Please enter either y or n.')
                        continue

                    if response.lower().startswith('y'):
                        execSubprocessInShellMode(f'sudo rm -rf {keystackSystemPath}/MongoDB')
                        break
                    else:
                        break
                else:
                    break

            # NOTE: Don't ask for IP address anymore. Don't expect MongoDB on Linux host. Use MongoDB Container
            # if platform == 'linux':
            #     mongoIp = self.askUserForIpAddress()

            while True:
                # The Python path is used for running Serviceware background process python files 
                SetupVar.pythonFullPath = input('\nWhat is the localhost Python execution full path? ')
                if os.path.exists(SetupVar.pythonFullPath) == False:
                    print(f'\nNo such Python path found in: {SetupVar.pythonFullPath}. Please try again ...')
                else:
                    break

            if platform == 'docker':
                # mongoIp = self.askUserForIpAddress()
                mongoIp = SetupVar.userEnvSettings['mongoIp']
                 
                # This will verify if Keystack container is currently running.
                # Stop the container if it is running.  If the container is the same version, remove the docker image
                stopDockerContainer(containerName='keystack', removeContainer=True, sudo=True)
                stopDockerContainer(containerName='mongo', removeContainer=True, sudo=True)
                removeDockerImage(SetupVar.keystackVersion, sudo=True)
                self.killListeningIpPorts()

            # Create keystack user
            isKeystackUserExists = execSubprocessInShellMode(f'sudo useradd -u {SetupVar.keystackUserUid} keystack')[-1]
            if 'already exists' in isKeystackUserExists:
                print('Keystack user already exists')
                # TODO: verify the user uid and correct accordingly if necessary
            else:
                print('Keystack user does not exists')

            # Create Keystack group
            # hgee wheel docker Keystack
            isKeystackGroupExists = execSubprocessInShellMode('groups')[-1]
            print('isKeystackGroupExists:', isKeystackGroupExists.replace('\n', '').split(' '))
 
            if 'Keystack' in isKeystackGroupExists.replace('\n', '').split(' '):
                print('Keystack group already exists')
                isKeystackGroupExists2 = True  
                # TODO: verify the user uid and correct accordingly if necessary
            else:
                print('Keystack group does not exists. Creating Keystack group ...')
                execSubprocessInShellMode(f'sudo groupadd -g {SetupVar.keystackGroupGid} Keystack')
                isKeystackGroupExists2 = False  

            # hgee : hgee wheel docker Keystack
            addedSetupUser = False
            for user in ['keystack', whoami]:
                isUserInKeystackGroup = execSubprocessInShellMode(f'groups {user}')[-1]

                if 'Keystack' not in isUserInKeystackGroup.split(':')[-1]:
                    print(f'User {user} is not in group Keystack')
                    result = execSubprocessInShellMode(f'sudo usermod -aG Keystack {user}')[-1]
                    print(f'Verifying user {user} in Keystack group ...')
                    isUserInKeystackGroup = execSubprocessInShellMode(f'groups {user}')[-1]

                    if 'Keystack' not in isUserInKeystackGroup.split(':')[-1]:
                        raise Exception(f'Failed to add user {user} to user group Keystack')
                    else:
                        print(f'Successfully added user {user} to user group Keystack')
                        addedSetupUser = True
                else:
                    print(f'The user {user} is already in group Keystack')

            if isKeystackGroupExists2 == False:
                 # Activate the new group now so no need to logout/login
                execSubprocessInShellMode(f'sudo newgrp Keystack')

            # Create a list of Keystack folders
            keystackFolderList = [f'{keystackTestsPath}/Playbooks',
                                  f'{keystackTestsPath}/Playbooks/Samples',
                                  f'{keystackTestsPath}/Docker',
                                  f'{keystackTestsPath}/Envs',
                                  f'{keystackTestsPath}/Envs/Samples',
                                  f'{keystackTestsPath}/Modules',
                                  f'{keystackTestsPath}/Results',
                                  f'{keystackTestsPath}/ResultsArchive',
                                  f'{keystackSystemPath}/Apps',
                                  f'{keystackSystemPath}/.DataLake',
                                  f'{keystackSystemPath}/Logs',
                                  f'{keystackSystemPath}/RestApiMods',
                                  f'{keystackSystemPath}/MongoDB',
                                  f'{keystackSystemPath}/MongoDB/storageData',
                                  f'{keystackSystemPath}/MongoDB/loggingData',
                                  f'{keystackSystemPath}/ResultDataHistory',
                                  f'{keystackSystemPath}/ServicesStagingArea/AwsS3Uploads',
                                ]

            for keyFolder in [keystackTestsPath, keystackSystemPath]:
                execSubprocessInShellMode(f'sudo mkdir -p {keyFolder}')

            for eachKeystackTestFolder in keystackFolderList:
                execSubprocessInShellMode(f'sudo mkdir -p {eachKeystackTestFolder}')

            # # Auto-generate keystackSystemSettings.env
            keystackSystemSettings = readFile(f"{currentDir}/Templates/keystackSystemSettings.env")
            systemSettingReplacements = [('{pythonFullPath}', SetupVar.pythonFullPath),
                                         ('{dockerPythonFullPath}', SetupVar.dockerPythonFullPath),
                                         ('{platform}', platform),
                                         ('{mongoIp}', mongoIp),
                                         ('{mongoPort}', SetupVar.userEnvSettings["mongoPort"]),
                                         ('{keystackIp}', SetupVar.userEnvSettings["keystackIp"]),
                                         ('{keystackPort}', SetupVar.userEnvSettings["keystackPort"])
                                         ]

            for replacement in systemSettingReplacements:
                keystackSystemSettings = keystackSystemSettings.replace(replacement[0], str(replacement[1]))

            keystackSystemSettingsFileExists = False

            # Backup existing data files with a timestamp
            keystackSystemSettingsFile        = f'{keystackSystemPath}/keystackSystemSettings.env'
            keystackSystemLoginCredentialFile = f'{keystackSystemPath}/.loginCredentials.yml'
            keystackSystemGroups              = f'{keystackSystemPath}/.DataLake/groups.yml'

            # Backup system data files before overwrite
            if os.path.exists(keystackSystemSettingsFile):
                backupSystemSettingsFile = saveFileToBackupFile(keystackSystemSettingsFile, sudo=True)    
                backupLoginCredentialsFile = saveFileToBackupFile(keystackSystemLoginCredentialFile, sudo=True)
                backupSystemGroups = saveFileToBackupFile(keystackSystemGroups, sudo=True)
                
                keystackSystemSettingsFileExists = True
                execSubprocessInShellMode(f'sudo echo "{keystackSystemSettings}" | sudo tee {keystackSystemPath}/keystackSystemSettings.env')   
            else:
                execSubprocessInShellMode(f'sudo echo "{keystackSystemSettings}" | sudo tee {keystackSystemPath}/keystackSystemSettings.env')

            execSubprocessInShellMode(f'sudo cp {currentDir}/Templates/.loginCredentials.yml {SetupVar.keystackSystemPath}')
            execSubprocessInShellMode(f'sudo cp {currentDir}/Templates/groups.yml {SetupVar.keystackSystemPath}/.DataLake')

            # Transfer samples to the created Keystack folders
            self.generateSamples(keystackRootPath=keystackRootPath, destinationPath=None, alreadyBackedUpSystemFiles=True)

            execSubprocessInShellMode(f'sudo cp -R {currentDir}/Apps {keystackSystemPath}')
            execSubprocessInShellMode(f'sudo rm {keystackTestsPath}/Modules/__init__.py')     
            execSubprocessInShellMode(f'sudo chmod -R 660 {keystackSystemPath}/.loginCredentials.yml')

            for keystackPath in [SetupVar.keystackTestPath, SetupVar.keystackSystemPath]:
                execSubprocessInShellMode(f'sudo chmod -R 770 {keystackPath}')
                execSubprocessInShellMode(f'sudo chown -R keystack:Keystack {keystackPath}')
                execSubprocessInShellMode(f'sudo chmod g+s {keystackPath}')

            execSubprocessInShellMode(f'sudo chmod -R 660 {SetupVar.keystackSystemPath}/.loginCredentials.yml')
            
            if platform == 'docker':
                # This will start the keystack and mongo containers
                self.installAndStartDockerContainers(mongoIp, dockerBuildImagePath=dockerBuildImagePath)
                if self.verifyContainers() == False:
                    sys.exit('Keystack containers failed!')
                    
            self.removeKeystackRunningServices()
            # from Services import Serviceware
            #awsS3ServiceObj = Serviceware.KeystackServices(typeOfService='keystackAwsS3') 
            #awsS3ServiceObj.startAwsS3Service()
        
            print('\nKeystack installation is done')

            if addedSetupUser:
                print(f'\nYOU MUST LOG OUT AND LOG BACK IN to use Keystack.  Otherwise, you cannot enter Keystack folders\n')
                
            if keystackSystemSettingsFileExists:
                print(f'\nNOTE! Found existing keystackSystemSettings.env file. Backed it up to: {backupSystemSettingsFile}')

            print(f'\nNOTE! If you will be using AWS S3 and/or Jira with Keystack, you need to edit the following to add your login credentials: {keystackSystemPath}/.loginCredentials.yml\n')
        
            sys.exit(f'\nKeystack folders are installed at: {keystackTestsPath} and {keystackSystemPath}\n\n')

        except Exception as errMsg:
            sys.exit(f'\nsetupKeystack.py error: {traceback.format_exc(None,errMsg)}\n')

    def update(self, platform=None, dockerBuildImagePath=None):
        """
        Update existing Keystack
           - Update the existing keystackSystemSettings.env file with new parameters.
           - Update apps and samples
           - Restart AWS-S3 and Logs services if they're running.e
           - Install new Keystack Docker image.
        """
        from dotenv import load_dotenv
        from re import search

        if os.path.exists('/etc/keystack.yml'):
            etcKeystackYml     = readYaml('/etc/keystack.yml')
            SetupVar.keystackRootPath   = etcKeystackYml['keystackRootPath']
            SetupVar.keystackTestPath   = etcKeystackYml['keystackTestRootPath']
            SetupVar.keystackSystemPath = etcKeystackYml['keystackSystemPath']
        
        currentKeystackSystemSettingsFile = f'{SetupVar.keystackSystemPath}/keystackSystemSettings.env'
        if os.path.exists(currentKeystackSystemSettingsFile) == False:
            raise Exception(f'setupKeystack update: Not found: {currentKeystackSystemSettingsFile}')

        # Should not cp -r Samples/*. Has to be individually copied because not every setup
        # has LoadCore, AirMosaic, IxNetwork, IxLoad, etc
        execSubprocessInShellMode(f'cp -r Apps/* {SetupVar.keystackSystemPath}/Apps')
        execSubprocessInShellMode(f'cp -r Samples/Playbooks/* {SetupVar.keystackTestPath}/Playbooks')
        execSubprocessInShellMode(f'cp -r Samples/Envs/* {SetupVar.keystackTestPath}/Envs')
        
        if os.path.exists(f'{SetupVar.keystackTestPath}/Modules/Demo'):
            execSubprocessInShellMode(f'cp -r Samples/Modules/Demo/* {SetupVar.keystackTestPath}/Modules/Demo')
            
        if os.path.exists(f'{SetupVar.keystackTestPath}/Modules/LoadCore'):
            execSubprocessInShellMode(f'cp -r Samples/Modules/LoadCore/* {SetupVar.keystackTestPath}/Modules/LoadCore')

        execSubprocessInShellMode(f'cp Templates/restApiSamples {SetupVar.keystackTestPath}/Samples')
        execSubprocessInShellMode(f'sudo chmod -R 770 {SetupVar.keystackSystemPath}')
        execSubprocessInShellMode(f'sudo chmod -R 770 {SetupVar.keystackTestPath}')
        execSubprocessInShellMode(f'sudo chown -R :Keystack {SetupVar.keystackSystemPath}')
        execSubprocessInShellMode(f'sudo chown -R :Keystack {SetupVar.keystackTestPath}')

        # Get current list of keystack system settings parameteres
        currentKeystackSystemSettingKeys = []
        currentKeystackSystemSettings = readFile(currentKeystackSystemSettingsFile)

        for line in currentKeystackSystemSettings.split('\n'):
            match = search('.*(keystack_.+)=', line)
            if match:
                currentKeystackSystemSettingKeys.append(match.group(1))

        # Get updated list of parameters
        latestKeystackSystemSettings = readFile(f'{currentDir}/Templates/keystackSystemSettings.env')
        latestKeystackSystemSettingsDict = dict()
        latestKeystackSystemSettingKeys = []

        for line in latestKeystackSystemSettings.split('\n'):
            match = search('.*(keystack_.+)=(.*)', line)
            if match:
                latestKeystackSystemSettingKeys.append(match.group(1))
                latestKeystackSystemSettingsDict[match.group(1)] = match.group(2)

        diff = list(set(latestKeystackSystemSettingKeys) - set(currentKeystackSystemSettingKeys))

        # Add new Keystack parameters to the bottom of the file
        if len(diff) > 0:
            print(f'\nAdding new Keystack params to the bottom of your existing file: {currentKeystackSystemSettingsFile}: {diff}')
            execSubprocessInShellMode(f'echo "\n#Added new params from Keystack version={SetupVar.keystackVersion} update" >> {currentKeystackSystemSettingsFile}\n')
            for newParam in diff:
                execSubprocessInShellMode(f'echo "{newParam}={latestKeystackSystemSettingsDict[newParam]}" >> {currentKeystackSystemSettingsFile}\n')

        self.removeKeystackRunningServices()
        
        if platform == 'docker':
            # This will verify if Keystack container is currently running.
            # Stop the container if it is running.  If the container is the same version, remove the docker image
            stopDockerContainer(containerName='keystack', removeContainer=True, sudo=True)
            stopDockerContainer(containerName='mongo', removeContainer=True, sudo=True)
            removeDockerImage(SetupVar.keystackVersion, sudo=True)

            #mongoIp = self.askUserForIpAddress()
            mongoIp = SetupVar.userEnvSettings['mongoIp']
            self.killListeningIpPorts()

            self.installAndStartDockerContainers(mongoIp, dockerBuildImagePath=dockerBuildImagePath)
            if self.verifyContainers() == False:
                sys.exit('Keystack containers failed!')
                
        sys.exit('\nKeystack update is done\n')

    def killListeningIpPorts(self):
        # Kill the Keystack port and Mongo port if they exist
        ipPortExistList = [f'{SetupVar.userEnvSettings["keystackPort"]}', f'{SetupVar.userEnvSettings["mongoPort"]}']
        for eachIpPort in ipPortExistList:
            isKeystackPortExists = execSubprocessInShellMode(f'sudo lsof -i tcp:{eachIpPort}')
            if isKeystackPortExists[-1]:
                execSubprocessInShellMode(f'sudo kill -9 {eachIpPort}')
                            
    def removeKeystackRunningServices(self):
        from Services import Serviceware
        
        print('\nVerifying if Keytack services are running ...')  
        serviceObj = Serviceware.KeystackServices()
        if serviceObj.isServiceRunning('keystackAwsS3'):
            serviceObj.stopService('keystackAwsS3')

        if serviceObj.isServiceRunning('keystackLogs'):
            serviceObj.stopService('keystackLogs')
    
    def verifyContainers(self):
        areUp = True
        for container in ['keystack', 'mongo']:
            if verifyContainer(container) == False:
                print(f'\nverifyContainer: {container} is down')
                areUp = False
            else:
                print(f'\nverifyContainer: {container} is up')
        
        return areUp        
                             
def argParse():
    """
    For a new installation, you have to prime your the server with the followings:
        - Keystack folder structure
        - Add /etc/keystack.yml
        - Add keystackSystemSettings.env
    """    
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-setup',  nargs="?", default='docker', type=str, help='Setup initial Keystack environment. docker or linux')
    parser.add_argument('-update', nargs="?", default='docker', type=str, help='Update existing Keystack. docker or linux')
    parser.add_argument('-dockerBuildImagePath', nargs="?", default=None, type=str, help='Where is the full path to the docker tar file to be installed as a docker image')
    
    parser.add_argument('-restart', default=False, action='store_true', help='Restart the Keystack container')
    parser.add_argument('-stop',    default=False, action='store_true', help='Stop and remove the Keystack container')
    
    parser.add_argument('-getSamples', default=False, action='store_true', help='Generate sample scripts. Must include the -sampleTarget param stating the path to put the samples')
    parser.add_argument('-sampleDest', nargs="+", default=None, help='Provide a destination path for the sample files')
    args = parser.parse_args()
    
    if args.setup:
        if args.dockerBuildImagePath is not None:
            if os.path.exists() == False:
                sys.exit(f'\nError: -dockerBuildImagePath cannot be located: {args.dockerBuildImagePath}')

        Setup().setup(platform=args.setup, dockerBuildImagePath=args.dockerBuildImagePath)
        
    elif args.update:
        if args.dockerBuildImagePath is not None:
            if os.path.exists() == False:
                sys.exit(f'\nError: -dockerBuildImagePath cannot be located: {args.dockerBuildImagePath}')
            
        Setup().update(platform=args.update, dockerBuildImagePath=args.dockerBuildImagePath)
        
    elif args.getSamples:
        if args.sampleDest is None:
            sys.exit('\nYou must include the -sampleDest parameter that states the path to put the sample files.\n')
            
        Setup().generateSamples(destinationPath=args.sampleDest[0])
    
    elif args.restart:
        restart()
        
    elif args.stop:
        stop()
        
    else:
        sys.exit('\nA parameter is required: -setup | -update | -getSamples -sampleDest\n')

def setup():
    """
    This is an entry-point for the CLI command setupKeystack
    
    By default, if dockerImagePath is None, setup and update will default to downloading
    the Keystack image from docker hub
    
    setupKeystack -setup docker 
     
    setupKeystack -setup docker|linux -dockerImagePath <full path to docker tar file>
    setupKeystack -update docker|linux -dockerImagePath <full path to docker tar file>   
    """
    result, output = execSubprocessInShellMode('which docker')
    if bool(re.search('.*docker', output)) == False:
        sys.exit('\nError: docker needs to be installed in this Linux host.\n')
        
    argParse()

def restart():
    """ 
    This is an entry-point for the CLI command restartKeystack in setup.cfg
    """
    execSubprocessInShellMode('docker compose down')
    sleep(2)
    execSubprocessInShellMode('docker compose up -d')
    print('\nKeystack docker container is restarted\n')

def stop():
    """ 
    This is an entry-point for the CLI command stopKeystack in setup.cfg
    """
    execSubprocessInShellMode('docker compose down')
    print('\nKeystack docker container is stopped and removed\n')
 
def help():
    pass
                          
if __name__ == "__main__":
    argParse()
    
    


