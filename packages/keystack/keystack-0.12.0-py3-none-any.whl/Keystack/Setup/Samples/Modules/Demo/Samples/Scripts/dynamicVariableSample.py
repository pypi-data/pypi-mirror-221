import time, sys, json
from keystackEnv import keystackObj

# Instead of using print, use the followings which will get logged into testcase test.log:
#    keystackObj.logInfo
#    keystackObj.logWarning
#    keystackObj.logDebug
#    keystackObj.logFailed
#    keystackObj.logError  <- This will abort the test immediately.

# Get dynamic variables from the Env parameter/values that was used in the playbook 
keystackObj.logInfo(f': {keystackObj.moduleProperties["envParams"]["server1"]}')

# Get dynamic variables passed in from the playbook                  
keystackObj.logInfo(f'ServerName from Playbook: {keystackObj.moduleProperties["variables"]["serverName"]}')
keystackObj.logInfo(f'ServerIp from Playbook: {keystackObj.moduleProperties["variables"]["serverIp"]}')

keystackObj.logWarning('dynamicVariableSample warning message')
keystackObj.logDebug('debug message')

# Create a failure
#keystackObj.logFailed('Failed: This is a sample test failed message')

# Create artifacts and put them in a shared location for other tests to access them
jsonFile = f'{keystackObj.moduleProperties["artifactsRepo"]}/myTestData.json'
data = {'test': 'server', 'result': 'Passed'}
with open(jsonFile, mode='w', encoding='utf-8') as fileObj:
          json.dump(data, fileObj)

time.sleep(0)

# Supports running multi thread jobs
import threading

def print_cube(num):
    # function to print cube of given num
    print("Cube: {}" .format(num * num * num))

def print_square(num):
    # function to print square of given num
    print("Square: {}" .format(num * num))

t1 = threading.Thread(target=print_square, args=(10,))
t2 = threading.Thread(target=print_cube, args=(10,))

# starting thread 1
t1.start()
# starting thread 2
t2.start()

# wait until thread 1 is completely executed
t1.join()
# wait until thread 2 is completely executed
t2.join()

# both threads completely executed
print("Done!")

