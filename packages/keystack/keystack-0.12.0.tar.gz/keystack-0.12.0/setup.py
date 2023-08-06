import os

from setuptools import setup
import subprocess

currentDir = os.path.abspath(os.path.dirname(__file__))
rootPath = currentDir.replace('/PackageKeystack', '')

def execSubprocessInShellMode(command, showStdout=True):
    """
    Linux CLI commands
    """
    print(f'-> {command}')
    result = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    result,err = result.communicate()
    
    if showStdout:
        for line in result:
            if type(line) is bytes:
                line = line.decode('utf-8')
                print('line:', line)
    
    return result.decode('utf-8')

# Copy all required files to be packaged to a folder call Keystack
# in this local package folder /PackageKeystack/Keystack. Then the 
# MANIFEST.in file will do an include
execSubprocessInShellMode('mkdir Keystack')
execSubprocessInShellMode(f'cp {rootPath}/__init__.py Keystack')
execSubprocessInShellMode(f'cp {rootPath}/keystack.py Keystack')
execSubprocessInShellMode(f'cp {rootPath}/EnvMgmt.py Keystack')
execSubprocessInShellMode(f'cp {rootPath}/LICENSE Keystack')
execSubprocessInShellMode(f'cp {rootPath}/globalVars.py Keystack')
execSubprocessInShellMode(f'cp {rootPath}/commonLib.py Keystack')
execSubprocessInShellMode(f'cp {rootPath}/parseParams.py Keystack')
execSubprocessInShellMode(f'cp {rootPath}/keystackUtilities.py Keystack')
execSubprocessInShellMode(f'cp {rootPath}/version Keystack')
execSubprocessInShellMode(f'cp {rootPath}/db.py Keystack')
execSubprocessInShellMode(f'cp -r {rootPath}/KeystackUI Keystack')
execSubprocessInShellMode(f'cp -r {rootPath}/Services Keystack')
execSubprocessInShellMode(f'cp -r {rootPath}/Setup Keystack')
execSubprocessInShellMode(f'rm -rf Keystack/Setup/Apps/AirMosaic')

setup()
