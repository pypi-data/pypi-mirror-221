import os, re, sys, json, traceback, secrets

from db import DB

class Vars:
    # This must be the same in accountMgmt Vars.webpage
    # It uses the same DB collection name
    webpage = 'accountMgmt'
    

class AccountMgr():
    def addUser(self, fullName:str, loginName:str, password:str, email:str, userRole:str):
        response = DB.name.insertOne(collectionName=Vars.webpage, 
                                     data={'fullName': fullName, 'loginName': loginName, 'password': password,
                                           'email': email, 'userRole': userRole, 'isLoggedIn': False,
                                           'apiKey': secrets.token_urlsafe(16),
                                           'defaultDomain': None, 'domains': [], 'userPreferences': {}})
        if response.acknowledged:
            return True
                        
    def isUserExists(self, key:str, value:str):
        isExists = DB.name.isDocumentExists(Vars.webpage, key=key, value=value, regex=False)
        if isExists:        
            return True

    def deleteUser(self, fullName):
        if fullName in ['Administrator', 'root']:
            return
        
        DB.name.deleteOneDocument(collectionName=Vars.webpage, fields={'fullName': fullName})

    def getUserDetails(self, key:str, value:str):
        """
        key: field. Example: fullName | loginName
        value: value
        """
        userDetails = DB.name.getDocuments(collectionName=Vars.webpage, fields={key: value.strip()}, includeFields={'_id':0})
        if userDetails.count() == 0:
            return None
        else:
            return userDetails[0]

    def updateUser(self, fullName, modifyFields):
        result = DB.name.updateDocument(collectionName=Vars.webpage, queryFields={'fullName': fullName}, updateFields=modifyFields) 
        # True | False
        return result
        
    def isUserLoggedIn(self, loginName:str):
        userDB = DB.name.getDocuments(collectionName=Vars.webpage,
                                      fields={'loginName': loginName}, includeFields={'_id':0})[0]
        if userDB['isLoggedIn']:
            return True
  
    def getApiKey(self, fullName=None, login=None):
        try:
            if fullName:
                userDB = DB.name.getDocuments(collectionName=Vars.webpage,
                                              fields={'fullName': fullName}, includeFields={'_id':0})[0]
                return userDB['apiKey']
            
            if login:
                userDB = DB.name.getDocuments(collectionName=Vars.webpage,
                                              fields={'login': login}, includeFields={'_id':0})[0]
                return userDB['apiKey']
                        
        except:
            return None

    def getApiKeyUser(self, apiKey):
        """ 
        Get the user full name with the api key
        """
        userDB = DB.name.getDocuments(collectionName=Vars.webpage,
                                      fields={'apiKey': apiKey}, includeFields={'_id':0})[0]
        return userDB['fullName']

    def getRequestSessionUser(self, request):
        """ 
        Used internally by rest api views.
         
        rest api views could be viewed by Keystack UI logins or by rest apis.
        If user is logged into the UI, the request.session should have the 'user' name.
        If user is using rest api, an api-key is required.
        """
        if 'user' in request.session:
            # Keystack UI logged in
            user = request.session['user']
        elif 'API-Key' in request.headers:
            # REST API
            apiKey = request.headers.get('API-Key')
            #user = AccountMgr().getApiKeyUser(apiKey=apiKey)
            user = self.getApiKeyUser(apiKey=apiKey)
        else:
            # Not logged in
            user = None
        
        return user
                          
    def getPassword(self, fullName):
        try:
            userDB = DB.name.getDocuments(collectionName=Vars.webpage,
                                          fields={'fullName': fullName}, includeFields={'_id':0})[0]
            return userDB['password']
        except:
            return None
 
    def regenerateApiKey(self, fullName):
        newApiKey = secrets.token_urlsafe(16)
        
        try:
            self.updateUser(fullName, {'apiKey': newApiKey})
        except Exception as errMsg:
            return None

        return newApiKey
    