import os, sys, time, json, traceback, httpx

# /Keystack/KeystackUI/restApi
currentDir = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, currentDir)
from systemLogging import SystemLogsAssistant

from rest_framework.response import Response
from django.http import JsonResponse

class ExecRestApi(object):
    def __init__(self, ip, port=None, headers=None, verifySslCert=False, https=False):   
        """ 
        restObj = ExecRestApi(ip, port, headers, https=True)
        restObj.get(restApi)
        """ 
        from requests.exceptions import ConnectionError

        if headers:
            self.headers = headers
        else:
            self.headers = {"content-type": "application/json"}
            
        self.verifySslCert = verifySslCert
        
        if https:
            if port is None:
                self.httpBase = f'https://{ip}'
            elif port == str(443):
                self.httpBase = f'https://{ip}'
            else:
                self.httpBase = f'https://{ip}:{port}'
        else:
            if port is None:
                self.httpBase = f'http://{ip}'
            else:
                self.httpBase = f'http://{ip}:{port}'

                        
    def get(self, restApi, params={}, stream=False, showApiOnly=False, silentMode=False, ignoreError=False, timeout=10, maxRetries=2,
            user=None, webPage=None, action=None):
        """
        Description
            A HTTP GET function to send REST APIs.

        Parameters
           restApi: (str): The REST API URL.
           data: (dict): The data payload for the URL.
           silentMode: (bool):  To display on stdout: URL, data and header info.
           ignoreError: (bool): True: Don't raise an exception.  False: The response will be returned.
           maxRetries: <int>: The maximum amount of GET retries before declaring as server connection failure.
        """
        retryInterval = 3
        restExecutionFailures = 0
        restApi = f'{self.httpBase}{restApi}'
        
        while True:
            if silentMode is False:
                print(f'\n\tGET: {restApi}')
                if showApiOnly == False:
                    print(f'\n\tDATA: {params}')                    
                    print(f'\tHEADERS: {self.headers}')

            try:
                # For binary file
                if stream:
                    # response = self._session.request('GET', restApi, stream=True, headers=self.headers, timeout=timeout,
                    #                                  allow_redirects=True, verify=self.verifySslCert)
                    response = httpx.stream('GET', restApi, headers=self.headers, timeout=timeout,
                                            follow_redirects=True, verify=self.verifySslCert)
                    
                if stream == False:
                    try:
                        response = httpx.get(restApi, params=params, headers=self.headers, timeout=timeout,
                                            follow_redirects=True, verify=self.verifySslCert)
                    except Exception as errMsg:
                        print('GET Error:', errMsg)
                        return False
                    
                if self.headers.get('Authorization', None):
                    del self.headers['Authorization']
                message = f'GET: {restApi}<br>HEADERS: {self.headers}<br>STATUS_CODE: {response.status_code}'

                if silentMode is False:
                    for redirectStatus in response.history:
                        if '307' in str(response.history):
                            print(f'\t{redirectStatus}: {response.url}')

                    print(f'\tSTATUS CODE: {response.status_code}')

                if not str(response.status_code).startswith('2'):
                    msgType = 'Error'
                    if ignoreError == False:
                        if 'message' in response.json() and response.json()['messsage'] != None:
                            print(f"\nGET Error: {response.json()['message']}")
                else:
                    msgType = 'Info'
                
                if webPage:    
                    SystemLogsAssistant().log(user=user, webPage=webPage, action=action, msgType=msgType, msg=message, forDetailLogs='')

                return response

            except Exception as errMsg:
                if restExecutionFailures < maxRetries:
                    print(errMsg)
                    restExecutionFailures += 1
                    time.sleep(retryInterval)
                    continue
                
                if restExecutionFailures == maxRetries:
                    return response
                    
          
    def post(self, restApi, params={}, headers=None, silentMode=False, showApiOnly=False, ignoreError=False, 
             timeout=10, maxRetries=5, user=None, webPage=None, action=None):
        """
        Description
           A HTTP POST function to create and start operations.

        Parameters
           restApi: (str): The REST API URL.
           data: (dict): The data payload for the URL.
           headers: (str): The special header to use for the URL.
           silentMode: (bool):  To display on stdout: URL, data and header info.
           ignoreError: (bool): True: Don't raise an exception.  False: The response will be returned.
           maxRetries: <int>: The maximum amount of GET retries before declaring as server connection failure.
        """
        import json
                
        restApi = f'{self.httpBase}{restApi}'
        
        if headers != None:
            originalJsonHeader = self.headers
            self.headers = headers

        retryInterval = 1
        restExecutionFailures = 0
        while True:
            if silentMode == False:
                print(f'\n\tPOST: {restApi}')
                
                if showApiOnly == False:
                    print(f'\n\tDATA: {params}')
                    print(f'\tHEAHDERS: {self.headers}')

            try:
                response = httpx.post(restApi, json=params, headers=self.headers, 
                                      timeout=timeout, follow_redirects=True,
                                      verify=self.verifySslCert)

                if self.headers.get('Authorization', None):
                    del self.headers['Authorization']
                message = f'GET: {restApi}<br>HEADERS: {self.headers}<br>STATUS_CODE: {response.status_code}'

                # 200 or 201
                if silentMode == False:
                    for redirectStatus in response.history:
                        if '307' in str(response.history):
                            print(f'\t{redirectStatus}: {response.url}')

                    print(f'\tSTATUS CODE: {response.status_code}')

                if response.status_code == 500 or str(response.status_code).startswith('4'):
                    return response
                
                if response.status_code != 200:
                    msgType = 'Error'
                    if ignoreError == False:
                        if 'errors' in response.json():
                            errMsg = 'POST Exception error: {0}\n'.format(response.json()['errors'])
                            print(errMsg)

                        print(f'POST error: {response.text}\n')
                else:
                    msgType = 'Info'

                if webPage:    
                    SystemLogsAssistant().log(user=user, webPage=webPage, action=action, msgType=msgType, msg=message, forDetailLogs='')

                # Change it back to the original json header
                if headers != None:
                    self.headers = originalJsonHeader

                return response

            except Exception as errMsg:
                #print(f'execRestApi POST ERROR:', traceback.format_exc(None, errMsg))
                if restExecutionFailures < maxRetries:
                    if ignoreError == False:
                        print(errMsg)
                        
                    restExecutionFailures += 1
                    time.sleep(retryInterval)
                    continue
                
                if restExecutionFailures == maxRetries:
                    return response
    
    def delete(self, restApi, params={}, headers=None, maxRetries=5, user=None, webPage=None, action=None):
        """
        Description
            HTTP DELETE 

        Paramters
            restApi: (str): The REST API URL.
            data: (dict): The data payload for the URL.
            headers: (str): The headers to use for the URL.
            maxRetries: <int>: The maximum amount of GET retries before declaring as server connection failure.
        """
        restApi = f'{self.httpBase}{restApi}'
            
        if headers != None:
            originalJsonHeader = self.headers
            self.headers = headers
            
        retryInterval = 3
        restExecutionFailures = 0
        
        while True:
            print(f'\n\tDELETE: {restApi}\n\tDATA: {params}')

            try:
                response = httpx.delete(restApi, params=params, headers=self.headers, 
                                        follow_redirects=True, verify=self.verifySslCert)

                if self.headers.get('Authorization', None):
                    del self.headers['Authorization']            
                message = f'GET: {restApi}<br>HEADERS: {self.headers}<br>STATUS_CODE: {response.status_code}'
                
                for redirectStatus in response.history:
                    if '307' in str(response.history):
                        print(f'\t{redirectStatus}: {response.url}')

                print(f'\tSTATUS CODE: {response.status_code}')
                
                if not str(response.status_code).startswith('2'):
                    msgType = 'Error'
                    errMsg = f'DELETE Exception error: {response.text}\n'
                    print(errMsg)
                    return response
                else:
                    msgType = 'Info'
                        
                if webPage:    
                    SystemLogsAssistant().log(user=user, webPage=webPage, action=action, msgType=msgType, msg=message, forDetailLogs='')
                        
                # Change it back to the original json header
                if headers != None:
                    self.headers = originalJsonHeader
                                    
                return response

            #except (requests.exceptions.RequestException, Exception) as errMsg:
            except Exception as errMsg:
                errMsg = f'DELETE Exception error {restExecutionFailures}/{maxRetries} retries: {errMsg}\n'

                if restExecutionFailures < maxRetries:
                    print(errMsg)
                    restExecutionFailures += 1
                    time.sleep(retryInterval)
                    continue
                
                if restExecutionFailures == maxRetries:
                    return response
            
