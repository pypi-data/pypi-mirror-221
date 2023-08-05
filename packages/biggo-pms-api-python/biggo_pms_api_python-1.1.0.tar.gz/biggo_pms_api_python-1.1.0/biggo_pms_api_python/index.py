import json
import os
import requests
import base64
import time
from datetime import datetime
from biggo_pms_api_python.error import BigGoAuthError, BigGoError

class BiggoAPIPMS:
    def __init__(self, clientID: str, clientSecret: str):
        self.clientID = clientID
        self.clientSecret = clientSecret
        self.accessToken = ''
        self.tokenType = 'Bearer'
        self.expiresAt = 0
        self.baseURL = 'https://api.biggo.com/api/v1/pms'

    def set_client_id(self, clientID: str) -> 'BiggoAPIPMS':
        self.clientID = clientID
        return self
    
    def set_client_secret(self, clientSecret: str) -> 'BiggoAPIPMS':
        self.clientSecret = clientSecret
        return self

    def set_token(self, token: str, expiresAt: datetime, tokenType: str = 'Bearer') -> 'BiggoAPIPMS':
        self.accessToken = token
        self.tokenType = tokenType
        self.expiresAt = int(expiresAt.timestamp())
        return self

    def is_token_expired(self) -> bool:
        return self.accessToken == '' or self.expiresAt < int(time.time())

    async def get_token(self):
        if not self.accessToken or self.is_token_expired():
            await self._renew_token()
        return self.accessToken

    async def _renew_token(self):
        self.accessToken = ''
        self.tokenType = 'Bearer'
        self.expiresAt = 0
        basic_auth_header = f"Basic {base64.b64encode(f'{self.clientID}:{self.clientSecret}'.encode()).decode()}"

        try:
            response = requests.post('https://api.biggo.com/auth/v1/token', data={
                'grant_type': 'client_credentials'
            }, headers={
                'Authorization': basic_auth_header,
                'Content-Type': 'application/x-www-form-urlencoded'
            })

            response_data = response.json()

            if 'error' in response_data:
                raise BigGoAuthError(response_data['error']['message'], response_data['error']['code'])

            access_token = response_data['access_token']
            token_type = response_data['token_type'].lower() if 'token_type' in response_data else 'bearer'
            expires_in = response_data['expires_in'] if 'expires_in' in response_data else 0

            self.accessToken = access_token
            self.tokenType = 'Bearer' if token_type == 'bearer' else token_type
            self.expiresAt = int(time.time()) + expires_in - 30
        except requests.exceptions.RequestException as err:
            raise BigGoAuthError(str(err))
        except BigGoAuthError as err:
            raise err
        except Exception as err:
            raise BigGoAuthError(str(err))
    
    def is_token_expired(self) -> bool:
        return time.time() >= self.expiresAt

    async def request(self, prams):
        headers = {
            'Authorization': f"{self.tokenType} {await self.get_token()}",
            **prams.get('extraHeaders', {})
        }

        try:
            response = requests.request(
                prams['method'],
                f"{self.baseURL}{prams['path']}",
                headers=headers,
                params=prams.get('extraParams'),
                json=prams.get('body'),
            )
            response.raise_for_status()
            
            res_text = response.content.decode('utf-8-sig')
            data = json.loads(res_text)

            if data.get('error_code') or data.get('result') == False:
                raise BigGoError(f"{data.get('error') or data.get('message')}", data.get('error_code'))

            return data
        except requests.exceptions.RequestException as err:
            raise BigGoError(str(err))
        except BigGoError as err:
            raise err
        except Exception as err:
            raise BigGoError(str(err))
        
    async def fileRequest(self, prams):
        headers = {
            'Authorization': f"{self.tokenType} {await self.get_token()}",
            **prams.get('extraHeaders', {})
        }

        try:
            response = requests.request(
                prams['method'],
                f"{self.baseURL}{prams['path']}",
                headers=headers,
                params=prams.get('extraParams'),
                json=prams.get('body'),
            )
            response.raise_for_status()
            return response

        except requests.exceptions.RequestException as err:
            raise BigGoError(str(err))
        except BigGoError as err:
            raise err
        except Exception as err:
            raise BigGoError(str(err))

    async def get_platform_list(self):
        data = await self.request({
            'path': '/platform',
            'method': 'GET',
        })
        return [
            {
                'id': platform['_id'],
                'name': platform['platform_name'],
                'status': platform['status'],
                'userList': platform['userid_list'],
                'emailList': platform['email_list']
            }
            for platform in data['data']
        ]

    async def get_group_list(self, platformID):
        data = await self.request({
            'path': '/group',
            'method': 'GET',
            'extraParams': {
                'pms_platformid': platformID
            }
        })
        return [
            {
                'id': group['_id'],
                'schedule': group['crontab_setting'],
                'isScheduleOn': group['crontab'] == 'true',
                'name': group['group_name'],
                'district': group['district'],
                'status': group['status'],
                'exportCount': group['export_count'],
                'sampleCount': group['sample_count']
            }
            for group in data['data']
        ]
    
    async def get_report_list(self, platformID, options=None):
        options = options or {}
        extra_params = {
            'pms_platformid': platformID,
            'size': options.get('size', 5000),
            'in_sort': options.get('sort', 'desc'),
            'in_form': options.get('startIndex', 0),
            'in_opt': {
                'pms_groupid': ','.join(options.get('groupID', [])),
                'start': options.get('startDate') and options['startDate'].strftime('%Y-%m-%d'),
                'end': options.get('endDate') and options['endDate'].strftime('%Y-%m-%d'),
            } if options.get('groupID') or options.get('startDate') or options.get('endDate') else None
        }
        data = await self.request({
            'path': '/export',
            'method': 'GET',
            'extraParams': extra_params
        })
        return [
            {
                'id': report['_id'],
                'createTime': report['createtime'],
                'groupID': report['pms_groupid'],
                'groupName': report['group_name'],
                'district': report['district'],
                'sampleSize': report['sample_size']
            }
            for report in data['data']
        ]

    async def get_report(self, platformID, reportID, fileType, options=None):
        options = options or {}
        res = await self.fileRequest({
            'path': f'/export/{reportID}',
            'method': 'GET',
            'extraParams': {
                'pms_platformid': platformID,
                'file_type': fileType,
            },
            'responseType': 'arraybuffer' if fileType == 'excel' else None
        })

        file_content = b''
        if fileType == 'csv':
            file_content = b'\xEF\xBB\xBF' + res.content
        elif fileType == 'json':
            file_content = json.dumps(res.json(), indent=2).encode('utf-8')
        elif fileType == 'excel':
            file_content = res.content

        if not options.get('saveAsFile'):
            return file_content

        file_name = options.get('fileName') or res.headers.get('content-disposition', '').split('filename=')[1].strip('"') or f'output.{fileType}'
        save_dir = options.get('saveDir') or '.'
        if not os.path.exists(save_dir):
            os.makedirs(save_dir, exist_ok=True)

        file_path = os.path.join(save_dir, file_name)
        with open(file_path, 'wb') as file:
            file.write(file_content)

        return file_path
