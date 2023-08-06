import os, sys, traceback
from re import search
from operator import itemgetter
from keystackUtilities import readYaml, readJson, writeToJson, mkdir2, chownChmodFolder
from db import DB
from globalVars import GlobalVars

currentDir = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, f'{currentDir}/KeystackUI/topbar/utilizations')
from EnvUtilizationDB import EnvUtilizationDB


class Vars:
    collectionName = 'envMgmt'


class ManageEnv():
    def __init__(self, env=None):
        """
        Create a env mgmt file for each env in KeystackSystem/.DataLake/.EnvMgmt
        
        env: <str>|<str(None)>: Env name. Could be full path.  Include the env group if the env is within a group
        """
        if env == 'None':
            env = None
        
        if env:
            # Parse out just the envGroup/envName
            regexMatch = search(f'({GlobalVars.keystackTestRootPath})?(/)?(Envs)?(/)?(.+)', env)
            if regexMatch:
                env = regexMatch.group(5)
                if '.yml' in env or '.yaml' in env:
                    env = env.split('.')[0]

        # env must include the group -> qa/rack1    
        self._setenv = env
        
        etcKeystackYml = readYaml('/etc/keystack.yml')
        self.keystackTestRootPath = etcKeystackYml['keystackTestRootPath']    
        self.keystackSystemPath   = etcKeystackYml['keystackSystemPath']
        self.envPath = f'{self.keystackTestRootPath}/Envs'
        if env:
            self.setenvFiles()

    @property
    def setenv(self):
        # getter function
        return self._setenv

    @setenv.setter
    def setenv(self, env):
        """
        Let users reset the env
        
        Usage:
            envObj = ManageEnv()
            envObj.setenv = <env name>
        """
        if env is None:
            # None if the module doesn't use an Env
            return 

        # Parse out just the envGroup/envName
        regexMatch = search(f'({GlobalVars.keystackTestRootPath})?(/)?(Envs)?(/)?(.+)', env)
        if regexMatch:
            env = regexMatch.group(5)
            if '.yml' in env or '.yaml' in env:
                env = env.split('.')[0]
                            
        self._setenv = env
        self.setenvFiles()
    
    def setenvFiles(self):
        if '-' in self.setenv:
            env = self.setenv.replace('-', '/')
        else:
            env = self.setenv
            
        self.envFullPath = f'{self.envPath}/{env}.yml'
        
    def isEnvExists(self):
        try:
            dbObj = DB.name.isDocumentExists(Vars.collectionName, key='env', value=self._setenv, regex=False)
            return dbObj

        except Exception as errMsg:
            return errMsg
        
    def addEnv(self):
        try:
            data = {'env': self._setenv, 'available': True, 'loadBalanceGroups':[], 'activeUsers': [], 'waitList': []}      
            dbObj = DB.name.insertOne(collectionName=Vars.collectionName, data=data)
                    
        except Exception as errMsg:
            return errMsg
                      
    def isEnvParallelUsage(self):
        """ 
        parallelUsage is read from the env file in /KeystackTests/Envs. 
        Not read from the env mgmt file.
        
        env: <str>: Full path env file
        """
        try:
            if self._setenv is None:
                # envData is None if the module doesn't use an Env
                return True 
            
            envData = readYaml(self.envFullPath)
            
            if 'parallelUsage' in envData:
                return envData['parallelUsage']
            else:
                # Default to True
                return True
            
        except Exception as errMsg:
            return errMsg
            
    def getEnvDetails(self):
        """ 
        Note: This will not work if test was executed on CLI because DB.name is not set.
              DB.name is set in the web server. 
        """
        try:
            dbObj = DB.name.getOneDocument(Vars.collectionName, fields={'env': self._setenv})
            return dbObj
  
        except Exception as errMsg:
            return None
    
    def getLoadBalanceGroups(self):
        try:
            dbObj = DB.name.getOneDocument(Vars.collectionName, fields={'env': self._setenv})
            return dbObj.get('loadBalanceGroups', None)
  
        except Exception as errMsg:
            return None
                    
    def removeEnv(self):
        try:
            dbObj = DB.name.deleteOneDocument(Vars.collectionName, key='env', value=self._setenv)

        except Exception as errMsg:
            return None
                                                                      
    def isEnvAvailable(self):
        try:
            envData = self.getEnvDetails()
            
            if envData:
                if self.isEnvParallelUsage():
                    return True
                else:
                    # Not shareable
                    if envData['available']:
                        return True
                    else:
                        return False
            else:
                # No env mgmt file exists.
                #self.addEnv()
                return True
            
        except Exception as errMsg:
            return False
        
    def isEnvNextInLine(self, sessionId, user=None, stage=None, module=None):
        """ 
        Check the env waitlist if the sessionId is next.
        If it is next:
            - Remove the sessionid from the wait list
            - Add the sessionId to the activeUsers list
            - set 'available' to False
        """
        try:
            envData = self.getEnvDetails()
            iAmNext = False
            
            if envData is None:
                # envData is None if the module doesn't use an Env
                return True
            
            for index,nextWaiting in enumerate(envData['waitList']):
                # {"module": "LoadCore",
                #  "stage": "Test",
                #  "sessionId": "11-01-2022-04:21:00:339301_rocky_200Loops",
                #  "user": "rocky"}
                nextSessionId = nextWaiting['sessionId']
                nextUser = nextWaiting['User']
                nextStage = nextWaiting['stage']
                nextModule = nextWaiting['module']
                
                if sessionId == nextSessionId:
                    if stage is None:
                        # Manually reserved env is next to use it
                        iAmNext = True
                        break
                    
                    if user == nextUser and stage == nextStage and module == nextModule:
                        iAmNext = True
                        break
                    
            if iAmNext:
                dbObj = DB.name.updateDocument(Vars.collectionName, queryFields={'env': self._setenv}, 
                                               updateFields={'activeUsers': {'user': user, 'sessionId': sessionId, 
                                                                             'module': module},
                                                                             'available': False}, 
                                               appendToList=True)
                
                dbObj = DB.name.updateDocument(Vars.collectionName, queryFields={'env': self._setenv}, 
                                               updateFields={'waitList': {'sessionId': nextSessionId, 'user': nextUser,
                                                                          'stage': nextStage, 'module': nextModule}}, 
                                               removeFromList=True)
                
                EnvUtilizationDB().insert(self._setenv, user)
                return True
            else:
                return False
                   
        except Exception as errMsg:
            return False
        
    def getActiveUsers(self):
        """
        Return a list of user or test sessions using the env.
        
        "activeUsers": [{"module": "LoadCore",
                         "sessionId": "11-01-2022-03:24:46:924785_rocky_1Test",
                         "user": "rocky"}]
                         
         envData with active users = {'_id': ObjectId('6445be5889e17be32c818fcc'), 'env': 'Samples/hubert', 'available': False, 'activeUsers': [{'sessionId': '05-17-2023-15:49:07:297406_5432', 'overallSummaryFile': '/opt/KeystackTests/Results/GROUP=Default/PLAYBOOK=Samples-pythonSample/05-17-2023-15:49:07:297406_5432/overallSummary.json', 'user': 'hgee', 'stage': 'Test', 'module': 'CustomPythonScripts2'}], 'waitList': [], 'loadBalanceGroups': []}
         
        envData with no active users = {'_id': ObjectId('64455f78f7b6150a4142c785'), 'env': 'Samples/loadcoreSample', 'available': True, 'activeUsers': [], 'waitList': [], 'loadBalanceGroups': []}

        """
        try:
            envData = self.getEnvDetails()
            if envData is None:
                # envData is None if the module doesn't use an Env
                return None

            return envData['activeUsers']
        except Exception as errMsg:
            return errMsg
        
    def isUserInActiveUsersList(self, user):
        for eachUser in self.getActiveUsers():
            if eachUser['stage'] == None:
                if eachUser['user'] == user:
                    return True
                
    def isUserInWaitList(self, user):
        for eachUser in self.getWaitList():
            if eachUser['stage'] == None:
                if eachUser['user'] == user:
                    return True
        
    def amIRunning(self, user, sessionId, stage, module):
        """ 
        (A.K.A = amINext)
        Get the top active user
        
        Return
            True | False | ('failed', errMsg, traceback)
        """
        try:        
            if self.isEnvParallelUsage():
                EnvUtilizationDB().insert(self._setenv, user)
                return True
            
            if self.isEnvParallelUsage() == False:
                envData = self.getEnvDetails()
                
                if envData is None:
                    # envData is None if the module doesn't use an Env
                    return True
                
                if len(envData['activeUsers']) > 0:
                    currentActiveUser = envData['activeUsers'][0]
                    if user == currentActiveUser['user'] and sessionId == currentActiveUser['sessionId'] and \
                        stage == currentActiveUser['stage'] and module == currentActiveUser['module']:
                        EnvUtilizationDB().insert(self._setenv, user)
                        return True
                    else:
                        return False
                    
                if len(envData['activeUsers']) == 0:
                    self.refreshEnv(self, envData=None)
                    envData = self.getEnvDetails()
                    if len(envData['activeUsers']) > 0:
                        currentActiveUser = envData['activeUsers'][0]
                        if user == currentActiveUser['user'] and sessionId == currentActiveUser['sessionId'] and \
                            stage == currentActiveUser['stage'] and module == currentActiveUser['module']:
                            EnvUtilizationDB().insert(self._setenv, user)
                            return True
                        else:
                            return False
                        
        except Exception as errMsg:
            return ('failed', str(errMsg), traceback.format_exc(None, errMsg))
            
    def goToWaitList(self, sessionId=None, user=None, stage=None, module=None):
        dbObj = DB.name.updateDocument(Vars.collectionName, queryFields={'env': self._setenv}, 
                                      updateFields={'waitList': {'sessionId': sessionId, 'user': user, 
                                                                 'stage': stage, 'module': module}},
                                      appendToList=True)
          
    def getWaitList(self):
        """
        Return a list of people or test sessions using the env.

        "waitList": [
        {
            "module": "LoadCore",
            "sessionId": "11-01-2022-04:21:00:339301_rocky_200Loops",
            "stage": "LoadCoreTest",
            "user": "rocky"
        }
        """
        try:
            envData = self.getEnvDetails()
            if envData:
                # envData is None if the module doesn't use an Env
                return envData['waitList']
        except Exception as errMsg:
            return errMsg
        
    def removeFromWaitList(self, sessionId, user=None, stage=None, module=None):
        """ 
        For manual reserves, only sessionId is set.
        Automated test will include stage and module
        """
        #print(f'EnvMgmt.removeFromWaitList: env:{self._setenv}  sessionId:{sessionId} user:{user}')
        
        try:
            envData = self.getEnvDetails()
            if envData is None:
                # envData is None if the module doesn't use an Env
                return
            
            for index,userData in enumerate(envData['waitList']):
                nextUser = userData['user']
                nextSessionId = userData['sessionId']
                nextStage = userData['stage']
                nextModule = userData['module']
                
                if stage in [None, 'None']:
                    # Manual user
                    if sessionId == nextSessionId and user == nextUser:
                        dbObj = DB.name.updateDocument(Vars.collectionName, queryFields={'env': self._setenv},
                                                       updateFields={'waitList': {'sessionId':nextSessionId, 'user': nextUser,
                                                                                  'stage': nextStage, 'module': nextModule}},
                                                       removeFromList=True)
                        # {'n': 1, 'nModified': 1, 'ok': 1.0, 'updatedExisting': True} 
                        return dbObj['updatedExisting']
                else:
                    # Automated test
                    if sessionId == nextSessionId and stage == nextStage and module == nextModule:
                        dbObj = DB.name.updateDocument(Vars.collectionName, 
                                                       queryFields={'env': self._setenv},
                                                       updateFields={'waitList': {'sessionId':nextSessionId, 'user': nextUser,
                                                                                  'stage': nextStage, 'module': nextModule}},
                                                       removeFromList=True)
                        # {'n': 1, 'nModified': 1, 'ok': 1.0, 'updatedExisting': True}                        
                        return dbObj['updatedExisting']                      
                    
        except Exception as errMsg:
            return str(errMsg)
        
    def removeFromActiveUsersList(self, removeList):
        """ 
        This function will:
           - Remove the sessionId from the active list
           - Get the next sessionId in the wait list and put it into the active user list.
           - Set avaiable = False
           
        removeList: [{'user':user, 'sessionId':sessionId, 'stage':stage, 'module':module}]
        
        Return
            success | error message
        """
        try:
            removeFlag = False
            openOneTimeOnly = False
            
            for activeUser in removeList:
                sessionId = activeUser['sessionId']
                
                if activeUser['stage'] == 'None': 
                    stage = None
                else:
                    stage = activeUser['stage']
                    
                if activeUser['module'] == 'None':
                    module = None
                else:
                    module = activeUser['module']  

                if openOneTimeOnly == False:
                    envData = self.getEnvDetails()
                    openOneTimeOnly = True 

                # envData:
                #     envData: {'_id': ObjectId('6445be5889e17be32c818fcc'), 'env': 'Samples/hubert', 'available': False, 'activeUsers': [{'sessionId': '04-23-2023-16:44:54:605093_hgee', 'overallSummaryFile': '/opt/KeystackTests/Results/GROUP=Default/PLAYBOOK=Samples-pythonSample/04-23-2023-16:44:54:605093_hgee/overallSummary.json', 'user': 'hgee', 'stage': 'Bringup', 'module': 'CustomPythonScripts'}], 'waitList': []}
                if envData:
                    if len(envData['activeUsers']) > 0:
                        for index, user in enumerate(envData['activeUsers']):
                            if user['sessionId'] == sessionId and \
                                user['stage'] == stage and \
                                user['module'] == module:
                                    envData['activeUsers'].pop(index)
                                    removeFlag = True

            if removeFlag:
                return self.refreshEnv(envData)
        
        except Exception as errMsg:
            errorMsg = f'EnvMgmt.removeFromActiveUsersList: error: {traceback.format_exc(None, errMsg)}'
            return errorMsg

    def refreshEnv(self, envData=None):
        """ 
        Get the next user in the waitlist and set it as the activeUser.
        """
        if envData is None:
            envData = self.getEnvDetails()
        
        # envData is None if the module doesn't use an Env
        if envData is None:
            return 
            
        # Now get the next in line 
        waitList = envData['waitList']

        # Get next in line
        if self.isEnvParallelUsage():
            envData['available'] = True
            envData['activeUsers'] += waitList[:]
            envData['waitList'] = []
        else:
            if len(envData['activeUsers']) == 0 and len(waitList) == 0:
                envData['available'] = True
                
            # Somebody or a session is still using it. Set the availabe accurately.
            if len(envData['activeUsers']) > 0:
                envData['available'] = False
                
            if len(envData['activeUsers']) == 0: 
                # if the activeUsers list is 0  
                if len(waitList) > 0:
                    # Get the next in line 
                    envData['activeUsers'].append(waitList[0])
                    envData['waitList'].pop(0)
                    envData['available'] = False

        dbObj = DB.name.updateDocument(Vars.collectionName,
                                       queryFields={'env': self._setenv},
                                       updateFields=envData)
        # True|False
        return dbObj
        
    def reserveEnv(self, sessionId=None, overallSummaryFile=None, user=None, stage=None, module=None, utilization=True):
        """ 
        Manually reserve the env and amINext()
        
        utilization <bool>: For keystack.py.lockAndWaitForEnv().  This function calls reserveEnv() and amIRunning().
                            Both functions increment env utilization. We want to avoid hitting it twice.
                            So exclude hitting it here in reserveEnv and let amIRunning hit it.
        """
        try:
            message = 'No Env used'
            envData = self.getEnvDetails()
            
            # envData is None if the module doesn't use an Env
            if envData:
                if self.isEnvParallelUsage():
                    envData['available'] = True
                    envData['activeUsers'].append({'sessionId': sessionId, 'overallSummaryFile': overallSummaryFile,
                                                    'user': user, 'stage': stage, 'module': module})
                    message = f'Reserved env as active-user:{self._setenv} user:{user} session:{sessionId} stage:{stage} module:{module}'
                    if utilization:
                        useObj = EnvUtilizationDB().insert(self._setenv, user) 
                else: 
                    if len(envData['activeUsers']) == 0:
                        envData['available'] = False 
                        envData['activeUsers'].append({'sessionId': sessionId, 'overallSummaryFile': overallSummaryFile,
                                                    'user': user, 'stage': stage, 'module': module})
                        message = f'Reserving env as active-user:{self._setenv} user:{user} session:{sessionId} stage:{stage} module:{module}'
                        if utilization:
                            useObj = EnvUtilizationDB().insert(self._setenv, user) 
                    else:
                        envData['waitList'].append({'sessionId': sessionId, 'overallSummaryFile': overallSummaryFile, 
                                                    'user': user, 'stage': stage, 'module': module})
                        message = f'Env is not available: {self._setenv}. Joined waitlist.'
                
                dbObj = DB.name.updateDocument(Vars.collectionName,
                                               queryFields={'env': self._setenv},
                                               updateFields=envData)
                
            return ('success', message)
        
        except Exception as errMsg:
            print('\nEnvMgmt: reserveEnv error:', traceback.format_exc(None, errMsg))
            return ('failed', str(errMsg))
                                            
    def releaseEnv(self):
        """ 
        The Release button. For manual release only.
        Mostly likely the env is in a stuck or weird state that needs to be updated. 
        Release the current activeUsers session/person on the env
        """
        try:
            envData = self.getEnvDetails()
            if envData:
                if len(envData['activeUsers']) > 0:
                    envData['activeUsers'].pop(0)
                    
                    if len(envData['waitList']) > 0:
                        envData['activeUsers'].append(envData['waitList'][0])
                        envData['waitList'].pop(0)
                        
                        if self.isEnvParallelUsage():
                            envData.update({'available': True})
                        else:
                            envData.update({'available': False})
                    else:
                        envData.update({'available': True})

                dbObj = DB.name.updateDocument(Vars.collectionName,
                                               queryFields={'env': self._setenv},
                                               updateFields=envData)
            return 'success'
        
        except Exception as errMsg:
            return ('failed', str(errMsg))
        
    def resetEnv(self):
        """
        Blank out the env by removing it.
        
        Return
            True|False
        """
        result = DB.name.updateDocument(Vars.collectionName, queryFields={'env':self._setenv},
                                        updateFields={'available':True, 'activeUsers':[], 'waitList':[]})
