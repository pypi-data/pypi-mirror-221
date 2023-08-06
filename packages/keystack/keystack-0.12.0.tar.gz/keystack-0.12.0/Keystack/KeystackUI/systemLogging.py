import os, sys
from datetime import datetime
from glob import glob
from shutil import rmtree

# /Keystack/KeystackUI
currentDir = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, currentDir.replace('/KeystackUI', ''))
from db import DB

class GlobalVars:
    collectionName = 'logs'
    

class SystemLogsAssistant:
    def getDatetime(self):
        now = datetime.now()
        return now.strftime('%m-%d-%Y')

    def getLogTitles(self):
        """
        Get all documents (logPages) in the logs collection
        """
        logTitlesList = []
        try:
            if DB.name is None:
                import db
                dbName  = db.ConnectMongoDB(ip=os.environ.get('keystack_mongoDbIp', 'localhost'),
                                            port=int(os.environ.get('keystack_dbIpPort', 27017)),
                                            dbName=db.DB.dbName)
                DB.name = dbName
                
            logTitlesObj = DB.name.getDocuments(collectionName=GlobalVars.collectionName, fields={})

            from functools import reduce
            
            logTitlesList = list(reduce( lambda all_keys, rec_keys: all_keys | set(rec_keys), map(lambda d: d.keys(), logTitlesObj), set() ))
            logTitlesList.remove('_id')
        except Exception as errMsg:
            # No logs
            pass

        return logTitlesList
    
    def getInstantMessages(self, webPage):
        logObj = DB.name.getDocuments(collectionName=GlobalVars.collectionName, 
                                      fields={f'{webPage}.{self.getDatetime()}': {'$exists': True}}, 
                                      includeFields={'_id':0})
        
        if logObj.count() > 0:
            messages = logObj[0]
        else:
            messages = None
        
        html = ''
  
        if messages:
            for date, messageList in messages[webPage].items():
                if date == self.getDatetime():
                    for message in reversed(messageList):
                        html += f"""<tr>
                                    <td style="text-align:center">{message['datetime']}</td>
                                    <td style="text-align:center">{message['user']}</td>
                                    <td style="text-align:center">{message['action']}</td>
                                    <td style="text-align:center">{message['msgType']}</td>
                                    <td style="text-align:left">{message['msg']}</td>
                                </tr>"""        
        return html

    def getLogMessages(self, webPage:str) -> str:
        """
        Called by systemLogs.views.py.GetLogMessages()
        """
        logObj = DB.name.getDocuments(collectionName=GlobalVars.collectionName, fields={webPage: {'$exists': True}}, 
                                      includeFields={'_id':0})
        
        if logObj.count() > 0:
            messages = logObj[0]
        else:
            messages = None
            
        html = ''
        
        if messages:
            # for date, messageList in reversed(messages[webPage].items()):
            #     for message in reversed(messageList):
            #         detailedMessage = f'{message["msg"]}\n{message["forDetailLogs"]}'
                    
            #         html += f"""<tr>
            #                     <td style="text-align:center">{message['datetime']}</td>
            #                     <td style="text-align:center">{message['user']}</td>
            #                     <td style="text-align:center">{message['action']}</td>
            #                     <td style="text-align:center">{message['msgType']}</td>
            #                     <td style="text-align:left">{detailedMessage}</td>
            #                 </tr>"""  
            reversedOrderList = []      
            for date, messageList in messages[webPage].items():
                reversedOrderList.append(messageList)
                
            for msg in reversed(reversedOrderList):
                for message in reversed(msg): 
                    detailedMessage = f'{message["msg"]}\n{message["forDetailLogs"]}'
                    
                    html += f"""<tr style="width:100%">
                                <td class="col-2 textAlignCenter">{message['datetime']}</td>
                                <td class="col-1 textAlignCenter">{message['user']}</td>
                                <td class="col-1 textAlignCenter">{message['action']}</td>
                                <td class="col-1 textAlignCenter">{message['msgType']}</td>
                                <td class="col-md-auto textAlignLeft">{detailedMessage}</td>
                            </tr>"""   

        return html
        
    def log(self, user:str, webPage:str, action:str, msgType:str, msg:str, forDetailLogs='') -> None:
        """
        collection = logs
        
        todayInstantMessages: [{'datetime': timestamp, 'user': user, 'module': None, 'action': action.capitalize(), 'msgType': msgType.capitalize(), 'msg': msg}]
        playbook:
            date: [{'datetime': timestamp, 'user': user, 'module': None, 'action': action.capitalize(), 'msgType': msgType.capitalize(), 'msg': msg}]
        sessions:
            date: []
        results:
            date: []
        
        webPage: options: todayInstantMessages, playbooks, sessions, results, 
        action:  options: get, create, modify, delete 
        msgType: options: info, debug, warning, error, success, failed
        forDetailLogs: A filter to log in detailLogs.  Don't show in todayInstantMessages.
        
        datetime, user, action, webPage, msgType, msg
        """
        now = datetime.now()
        timestamp = now.strftime('%m-%d %H:%M:%S')
        date = now.strftime('%m-%d-%Y')
        
        logData = {'datetime':timestamp, 'user':user, 'action':action, 'webPage':webPage,
                   'msgType':msgType.capitalize(), 'msg':msg, 'forDetailLogs':forDetailLogs}
        
        try:
            # Append log to today's date folder
            result = DB.name.updateDocument(collectionName=GlobalVars.collectionName, 
                                            queryFields={f'{webPage}.{date}': {'$exists': True}},
                                            updateFields={f'{webPage}.{date}': logData}, appendToList=True)

            # {'n': 0, 'nModified': 0, 'ok': 1.0, 'updatedExisting': False}
            if result['updatedExisting'] == False:
                # Getting here means the today's date folder might not exists. Create a new date folder.
                result = DB.name.updateDocument(collectionName=GlobalVars.collectionName, 
                                                queryFields={f'{webPage}': {'$exists': True}},
                                                updateFields={f'{webPage}.{date}': logData}, appendToList=True)
                
                if result['updatedExisting'] == False:
                    # The collection doesn't exist. Go to Exception to create a new collection.
                    raise
            
        except Exception as errMsg:
            result = DB.name.insertOne(collectionName='logs', data={'_id': webPage, webPage: {date: [logData]}})

    def delete(self, logPage):
        """
        Delete all the logs of a log category
        """
        result = DB.name.deleteOneDocument(collectionName=GlobalVars.collectionName, fields={'_id': logPage})

    def deletePastLogs(self):
        """ 
        Remove past logs based on keystack_removeLogsAfterDays=<days> in keystackSystemSettings.env.
        Defaults to 1 day old logs
        
        Mainly used by keystackLogs.py
        """
        from dotenv import load_dotenv
        from keystackUtilities import readYaml
        
        etcKeystackYml = readYaml('/etc/keystack.yml')
        load_dotenv(f'etcKeystackYml["keystackSystemPath"]/keystackSystemSettings.env')
        removeLogsAfterDays = os.environ.get('keystack_removeLogsAfterDays', 3)
        
        # ['results', 'accountMgmt', 'modules', 'sessions']
        allLogCategories = self.getLogTitles()
        print('\nsystemLogging.deletePastLogs() allLogsCategory:', allLogCategories)
        today = datetime.now()
        
        for logCategory in allLogCategories:
            logs = DB.name.getDocuments(collectionName=GlobalVars.collectionName, fields={logCategory: {'$exists': True}}, 
                                        includeFields={'_id':0})
            
            # logs[0]: {'accountMgmt': {}}
            if logs.count() > 0:
                for recordedDate in logs[0][logCategory]:
                    #print(f'\nsystemLogging.deletePastLogs() log dates: {recordedDate}')
                    format = '%m-%d-%Y'
                    datetimeObj = datetime.strptime(recordedDate, format)
                    daysDelta = today.date() - datetimeObj.date()
                    daysRecorded = daysDelta.days
                    
                    print(f'logs:{logCategory}  daysRecorded:{daysRecorded}   removeLogsAfterDays:{removeLogsAfterDays}')
                    if int(daysRecorded) >= int(removeLogsAfterDays):
                        print('systemLogging.deletePastLogs() removing:', recordedDate)
                        DB.name.removeKeyFromDocument(collectionName=GlobalVars.collectionName,
                                                      queryFields={'_id': logCategory}, 
                                                      updateFields={"$unset": {f'{logCategory}.{recordedDate}': 1}})

if __name__ == "__main__":
    SystemLogsAssistant().deletePastLogs()
    