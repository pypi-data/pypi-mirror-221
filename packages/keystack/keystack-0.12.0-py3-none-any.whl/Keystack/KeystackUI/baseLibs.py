import os, yaml, sys, traceback
from shutil import rmtree
from re import search
from glob import glob
from datetime import datetime

from django.conf import settings

from keystackUtilities import readYaml, chownChmodFolder
from globalVars import GlobalVars

# /opt/Keystack/KeystackUI
currentDir = os.path.abspath(os.path.dirname(__file__)) 
from systemLogging import SystemLogsAssistant

def getPlaybookNames():
    """ 
    Get all playbooks
    
    Used by sessionMgmt for Playbook dropdown selection for play action:
    
    #  [('pythonSample.yml', '/opt/KeystackTests/Playbooks/pythonSample.yml'), ('loadcoreSample.yml', '/opt/KeystackTests/Playbooks/loadcoreSample.yml'), ('airMosaic.yml', '/opt/KeystackTests/Playbooks/airMosaic.yml'), ('loadcore_5Loops.yml', '/opt/KeystackTests/Playbooks/loadcore_5Loops.yml'), ('playbookTemplate.yml', '/opt/KeystackTests/Playbooks/playbookTemplate.yml'), ('/qa/qa1.yml', '/opt/KeystackTests/Playbooks/qa/qa1.yml)'), ('/qa/dev/dev1.yml', '/opt/KeystackTests/Playbooks/qa/dev/dev1.yml)')]
    """  
    
    playbooksPath = f"{GlobalVars.keystackTestRootPath}/Playbooks"
    playbooks = []
    
    for root, dirs, files in os.walk(playbooksPath):
        relativePath = root.split(playbooksPath)[-1]
        if files:
            for file in files:
                if file[0] in ['.', '#']:
                    continue
                
                if file.endswith('yml') or file.endswith('yaml'):
                    if '/' in relativePath:
                        playbooks.append((f'{relativePath}/{file}', f'{root}/{file}'))
                    else:
                        playbooks.append((f'{file}', f'{root}/{file}'))

    return playbooks
    
def getSetups():
    """ 
    Get all setups from /$keystackTestsRootPath/Envs
    
    Note: Originally called setup.  Now called envs.
    """
    setupsPath = f"{GlobalVars.keystackTestRootPath}/Envs"
    envs = []
    
    for root, dirs, files in os.walk(setupsPath):
        relativePath = root.split(setupsPath)[-1]
        
        for file in files:
            if file.endswith('yml') or file.endswith('yaml'):
                if '/' in relativePath:
                    envs.append(f'{relativePath}/{file}')
                else:
                    envs.append(f'{file}')
    
    return envs
    
def buildModulesDict(topLevelFolder):
    """ 
    Get all Module folders and files
    """
    modulesDict = {}
    
    for modulePath in glob(f'{topLevelFolder}/Modules/*'):
        moduleName = modulePath.split('/')[-1]
        modulesDict[moduleName] = {}
                    
        keystackFolders = []
        for folder in glob(f'{modulePath}/*'):
            if '__pycache__' in folder: continue
            
            if os.path.isdir(folder):
                keystackFolders.append(folder)
        # Just Added ends
        
        for folderPath in keystackFolders:
            keystackFolderName = folderPath.split('/')[-1]
            modulesDict[moduleName][keystackFolderName] = {}

            for root, dirs, files in os.walk(folderPath):
                if '__pycache__' in root: continue

                fileList = []

                if files == []:
                    modulesDict[moduleName][keystackFolderName].update({root: fileList})
                    continue

                for file in files:
                    flag = False
                    for ignoreChar in ['#', '~']:
                        if ignoreChar in file:
                            flag = True
                            break

                    if flag == False:
                        fileList.append(file)

                modulesDict[moduleName][keystackFolderName].update({root: fileList})

    return modulesDict

          
def getGroupSessions(user, group='all'):
    try:
        groupSessionsFolder = f'{GlobalVars.keystackTestRootPath}/Results' 
        groups = []

        for groupPath in glob(f"{groupSessionsFolder}/GROUP*"):
            groupName = groupPath.split('/')[-1].split('=')[-1]
            groups.append(groupName)
        
        if groups == []:
            groups.append('Default')
        if 'Default' not in groups:
            groups.insert(0, 'Default')
            
        groups.sort()
        return groups
       
    except Exception as errMsg:
        SystemLogsAssistant().log(user=user, webPage='sidebarMenu', action='GetGroupSessions',
                                  msgType=f'Error', msg=f'{errMsg}',
                                  forDetailLogs=f'{traceback.format_exc(None, errMsg)}')  
    
def testResultTimestampFolders(resultFolderPath):
    testResultTimestampFolders = []
    
    try:
        testResultTimestampFolders = glob(f'{resultFolderPath}/*')
    except:
        status = 404

    try:
        # Initial HTML markups
        html = '<nav class="keystackSidebar card mt-3 py-3 px-3 mb-0">'
        html = f'{html}\n\t<ul class="nav flex-column" id="nav_accordion">'
        
        '''
        <nav class="sidebar keystackSidebar card py-0 mb-0">
            <ul class="nav flex-column" id="nav_accordion">
            
                <li class="nav-item">
                    <a class="nav-link" href="#"> Link name </a>
                </li>
                
                <li class="nav-item has-submenu">
                    <a class="nav-link" href="#"> resultFolder </a>
                    <ul class="submenu collapse">
                        <li><a class="nav-link" href="#"> File 1 </a></li>
                        <li><a class="nav-link" href="#"> File 2 </a></li>
                        <li><a class="nav-link" href="#"> File 3 </a> </li>
                    </ul>
                </li>
            </ul>
        </nav>
        '''
        
        # Get test results in a reversed list
        datetimeList = []
        for eachTimestampFolder in testResultTimestampFolders:
            datetimeList.append(eachTimestampFolder)
            
        # Got a sorted list
        datetimeList = sorted(datetimeList, key=lambda fileName: datetime.strptime(fileName.split('/')[-1].split('_')[0], "%m-%d-%Y-%H:%M:%S:%f"))
        
        # Reverse the list here using reversed()
        for eachResultFolderFullPath in list(reversed(datetimeList)): 
            timestampResultFolder = eachResultFolderFullPath.split('/')[-1]
            
            # Create the submenu header.  result folder files are added next.
            html = f'{html}\n\t\t<li class="nav-item has-submenu">'
            
            html = f'{html}\n\t\t\t<input type="checkbox" name="testResultCheckbox" value="{eachResultFolderFullPath}" />&emsp;<button type=submit class="btn btn-sm btn-outline-primary p-0 px-2" name="getSelectedTestResult" value={eachResultFolderFullPath}><i class="fas fa-cloud-arrow-down"></i></button>&ensp;<a class="nav-link" style="display:inline-block" href="#"><i class="fa-regular fa-folder pr-2"></i>{timestampResultFolder}</a>'
            
            html = f'{html}\n\t\t\t<ul class="submenu collapse">'
            html = f'{html}<br>'
            
            subMenuFlag = 0
            # Dig into each timestamp result folder
            for root, dirs, files in os.walk(eachResultFolderFullPath):
                if root:
                    subFolderName = root.split('/')[-1]
                    html = f'{html}\n\t\t\t\t\t<li class="nav-item has-submenu">'
                    if subMenuFlag == 0:
                        tab = ''
                        subMenuFlag = 1
                    else:
                        tab = "&emsp;&emsp;"
                        
                    html = f'{html}\n\t\t\t\t\t\t<a class="nav-link" style="display:inline-block" href="#">{tab}<i class="fa-regular fa-folder pr-2"></i>{subFolderName}</a>'
                    html = f'{html}\n\t\t\t\t\t\t\t<ul class="submenu collapse">'

                if files:
                    #  class="fas fa-file-alt"
                    for file in files:
                        if '.pdf' in file:   
                            html = f'{html}\n\t\t\t\t\t\t\t<li><a style="line-height:1" class="nav-link ml-5" target="_blank" data-value="{root}/{file}" href="/testResults/getTestResultFileContents?testResultFile={root}/{file}">&emsp;<i class="fa-regular fa-file-lines pr-2"></i>{file}</a></li>'
                        else:
                            # This method will do a POST to GetTestResultFileContents() and return <pre>fileContents</pre> to a fetch() response and javascript will insert the fileContents using innerHtml.
                            #html = f'{html}\n\t\t\t\t\t\t\t<li><a style="line-height:1" class="nav-link" onclick="readTestResultFile(this)" data-value="{root}/{file}" href="#">&emsp;&emsp;&emsp;{file}</a></li>'
                            
                            # This method will do a GET to GetTestResultFileContents() and show plain text contents on a new tab
                            html = f'{html}\n\t\t\t\t\t\t\t<li><a style="line-height:1" class="nav-link ml-5" data-value="{root}/{file}" target="_blank" href="/testResults/getTestResultFileContents?testResultFile={root}/{file}">&emsp;<i class="fa-regular fa-file-lines pr-2"></i>{file}</a></li>'
                
                html = f'{html}\n\t\t\t\t\t\t\t</ul>'
                html = f'{html}\n\t\t\t\t\t</li>'
                
            html = f'{html}<br>'
            html = f'{html}\n\t\t\t</ul>'    
            html = f'{html}\n\t\t</li>'
            
        html = f'{html}\n\t</ul>\n</nav>'
        SystemLogsAssistant().log(user='hgee', webPage='results', action='testResultTimestampFolders', msgType='Success', msg='', forDetailLogs=True)
        
    except Exception as errMsg:
        SystemLogsAssistant().log(user='hgee', webPage='results', action='testResultTimestampFolders', msgType='Error', msg=traceback.format_exc(None, errMsg))
         
    return html

def removeEmptyTestResultFolders(user, timestampResultsFolder):
    """
    Check if the folder is empty. If empty, remove it.
    Used in sessionMgmt.views and testResults.views
    """
    match = search('((.*/GROUP=.*)/PLAYBOOK=.+)/.+', timestampResultsFolder)
    if match:
        playbookPath = match.group(1)
        groupPath = match.group(2)
        
        if len(glob(f'{playbookPath}/*')) == 0:
            # SystemLogsAssistant().log(user=user, webPage='results', action='Delete', msgType='Info',
            #                           msg=f'Playbook results folder is empty. Removing: {playbookPath}', forDetailLogs='')
            rmtree(playbookPath)

        if len(glob(f'{groupPath}/*')) == 0:
            # SystemLogsAssistant().log(user=user, webPage='results', action='Delete', msgType='Info',
            #                           msg=f'Group results folder is empty. Removing: {groupPath}', forDetailLogs='')
            rmtree(groupPath)


def debugMessaging(msg):
    if os.path.exists(GlobalVars.debugLogFilePath) == False:
        open(GlobalVars.debugLogFilePath).close()
        chownChmodFolder(GlobalVars.debugLogFilePath, GlobalVars.user, GlobalVars.group)
     
    with open(GlobalVars.debugLogFilePath) as fileObj:
        fileObj.write(f'{msg}\n')
            
        