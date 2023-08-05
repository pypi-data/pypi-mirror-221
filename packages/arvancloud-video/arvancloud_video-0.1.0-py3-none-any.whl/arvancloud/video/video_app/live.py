from arvancloud.video.helpers.error import ApiError

from arvancloud.video.interfaces.query_params import QueryParams
from arvancloud.video.interfaces.stream import Stream

import requests

class LiveStreams():
    def __init__(self, api_key=None, **kwargs) -> None:
        if not api_key:
            raise ApiError('Please supply an api_key')
        
        self.api_key = api_key
        self.base_url = 'https://napi.arvancloud.ir/live/2.0'
    
    def get_all_streams(self, params: QueryParams = None):
        header = {
            'Content-Type': 'application/json',
            'Authorization': self.api_key
        }
        
        try:
            req = requests.get(url=f'{self.base_url}/streams', params=params, headers=header)
            if req.status_code == 200:
                return req.json()
            elif req.status_code == 401:
                raise ApiError('Unauthorized')
            elif req.status_code == 403:
                raise ApiError('Forbidden')
            elif req.status_code == 404:
                raise ApiError('Stream Not Found')
            elif req.status_code == 422:
                raise ApiError('Unprocessable Entity')
            elif req.status_code == 500:
                raise ApiError('Internal Server Error')
        except ConnectionError:
                raise ApiError('Connection Error')

    def get_single_stream(self, stream_id: str = None):
        if not stream_id:
            raise ApiError('Please supply a stream_id')

        header = {
            'Content-Type': 'application/json',
            'Authorization': self.api_key
        }

        try:
            req = requests.get(url=f'{self.base_url}/streams/{stream_id}', headers=header)
            if req.status_code == 200:
                return req.json()
            elif req.status_code == 401:
                raise ApiError('Unauthorized')
            elif req.status_code == 403:
                raise ApiError('Forbidden')
            elif req.status_code == 404:
                raise ApiError('Stream Not Found')
            elif req.status_code == 422:
                raise ApiError('Unprocessable Entity')
            elif req.status_code == 500:
                raise ApiError('Internal Server Error')
        except ConnectionError:
                raise ApiError('Connection Error')

    def create_new_stream(self, data: Stream = None):
        if not data:
            raise ApiError('Please supply a form')

        header = {
            'Content-Type': 'application/json',
            'Authorization': self.api_key
        }

        try:
            req = requests.post(url=f'{self.base_url}/streams', data=data, headers=header)
            if req.status_code == 200 or req.status_code == 201:
                return req.json()
            elif req.status_code == 401:
                raise ApiError('Unauthorized')
            elif req.status_code == 403:
                raise ApiError('Forbidden')
            elif req.status_code == 404:
                raise ApiError('Stream Not Found')
            elif req.status_code == 422:
                raise ApiError('Unprocessable Entity')
            elif req.status_code == 500:
                raise ApiError('Internal Server Error')
        except ConnectionError:
                raise ApiError('Connection Error')

    def remove_single_stream(self, stream_id: str = None):
        if not stream_id:
            raise ApiError('Please supply a stream_id')

        header = {
            'Content-Type': 'application/json',
            'Authorization': self.api_key
        }

        try:
            req = requests.delete(url=f'{self.base_url}/streams/{stream_id}', headers=header)
            if req.status_code == 200:
                return req.json()
            elif req.status_code == 401:
                raise ApiError('Unauthorized')
            elif req.status_code == 403:
                raise ApiError('Forbidden')
            elif req.status_code == 404:
                raise ApiError('Stream Not Found')
            elif req.status_code == 422:
                raise ApiError('Unprocessable Entity')
            elif req.status_code == 500:
                raise ApiError('Internal Server Error')
        except ConnectionError:
                raise ApiError('Connection Error')

    def update_single_stream(self, stream_id: str = None, data: Stream = None):
        if not stream_id:
            raise ApiError('Please supply a stream_id')

        if not data:
            raise ApiError('Please supply a form')

        header = {
            'Content-Type': 'application/json',
            'Authorization': self.api_key
        }

        try:
            req = requests.put(url=f'{self.base_url}/streams/{stream_id}', json=data, headers=header)
            if req.status_code == 200:
                return req.json()
            elif req.status_code == 401:
                raise ApiError('Unauthorized')
            elif req.status_code == 403:
                raise ApiError('Forbidden')
            elif req.status_code == 404:
                raise ApiError('Stream Not Found')
            elif req.status_code == 422:
                raise ApiError('Unprocessable Entity')
            elif req.status_code == 500:
                raise ApiError('Internal Server Error')
        except ConnectionError:
                raise ApiError('Connection Error')

    def start_record_single_stream(self, stream_id: str = None):
        if not stream_id:
            raise ApiError('Please supply a stream_id')

        header = {
            'Content-Type': 'application/json',
            'Authorization': self.api_key
        }

        try:
            req = requests.get(url=f'{self.base_url}/streams/{stream_id}/start-record', headers=header)
            if req.status_code == 200:
                return req.json()
            elif req.status_code == 401:
                raise ApiError('Unauthorized')
            elif req.status_code == 403:
                raise ApiError('Forbidden')
            elif req.status_code == 404:
                raise ApiError('Stream Not Found')
            elif req.status_code == 422:
                raise ApiError('Unprocessable Entity')
            elif req.status_code == 500:
                raise ApiError('Internal Server Error')
        except ConnectionError:
                raise ApiError('Connection Error')

    def stop_record_single_stream(self, stream_id: str = None):
        if not stream_id:
            raise ApiError('Please supply a stream_id')

        header = {
            'Content-Type': 'application/json',
            'Authorization': self.api_key
        }

        try:
            req = requests.get(url=f'{self.base_url}/streams/{stream_id}/stop-record', headers=header)
            if req.status_code == 200:
                return req.json()
            elif req.status_code == 401:
                raise ApiError('Unauthorized')
            elif req.status_code == 403:
                raise ApiError('Forbidden')
            elif req.status_code == 404:
                raise ApiError('Stream Not Found')
            elif req.status_code == 422:
                raise ApiError('Unprocessable Entity')
            elif req.status_code == 500:
                raise ApiError('Internal Server Error')
        except ConnectionError:
                raise ApiError('Connection Error')


