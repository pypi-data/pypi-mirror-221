from arvancloud.video.helpers.error import ApiError

from arvancloud.video.interfaces.query_params import QueryParams
from arvancloud.video.interfaces.watermark import Watermark

import requests
import magic
import os

class VodWatermarks():
    def __init__(self, api_key=None, **kwargs) -> None:
        if not api_key:
            raise ApiError('Please supply an api_key')
        
        self.api_key = api_key
        self.vod_base_url = 'https://napi.arvancloud.ir/vod/2.0'
        self.live_base_url = 'https://napi.arvancloud.ir/live/2.0'

    def get_single_channel_watermarks(self, channel_id: str = None, params: QueryParams = None):
        header = {
            'Content-Type': 'application/json',
            'Authorization': self.api_key
        }
        
        try:
            req = requests.get(url=f'{self.vod_base_url}/channels/{channel_id}/watermarks', params=params, headers=header)
            if req.status_code == 200:
                return req.json()
            elif req.status_code == 401:
                raise ApiError('Unauthorized')
            elif req.status_code == 403:
                raise ApiError('Forbidden')
            elif req.status_code == 404:
                raise ApiError('Channel Not Found')
            elif req.status_code == 422:
                raise ApiError('Unprocessable Entity')
            elif req.status_code == 500:
                raise ApiError('Internal Server Error')
        except ConnectionError:
                raise ApiError('Connection Error')

    def get_single_watermark(self, watermark_id: str = None):
        header = {
            'Content-Type': 'application/json',
            'Authorization': self.api_key
        }
        
        try:
            req = requests.get(url=f'{self.vod_base_url}/watermarks/{watermark_id}', headers=header)
            if req.status_code == 200:
                return req.json()
            elif req.status_code == 401:
                raise ApiError('Unauthorized')
            elif req.status_code == 403:
                raise ApiError('Forbidden')
            elif req.status_code == 404:
                raise ApiError('Watermark Not Found')
            elif req.status_code == 422:
                raise ApiError('Unprocessable Entity')
            elif req.status_code == 500:
                raise ApiError('Internal Server Error')
        except ConnectionError:
                raise ApiError('Connection Error')

    def remove_single_watermark_from_channel(self, watermark_id: str = None):
        header = {
            'Content-Type': 'application/json',
            'Authorization': self.api_key
        }
        
        try:
            req = requests.delete(url=f'{self.vod_base_url}/watermarks/{watermark_id}', headers=header)
            if req.status_code == 200:
                return req.json()
            elif req.status_code == 401:
                raise ApiError('Unauthorized')
            elif req.status_code == 403:
                raise ApiError('Forbidden')
            elif req.status_code == 404:
                raise ApiError('Channel Not Found')
            elif req.status_code == 422:
                raise ApiError('Unprocessable Entity')
            elif req.status_code == 500:
                raise ApiError('Internal Server Error')
        except ConnectionError:
                raise ApiError('Connection Error')

    def create_new_watermark_for_specific_channel(self, channel_id: str = None, watermark_file: str = None, data: Watermark = None):
        if not watermark_file or not data["title"]:
            raise ApiError('Please supply a watermark_file or title')

        if not os.path.exists(os.path.abspath(watermark_file)):
            raise ApiError('Watermark file does not exist')
        
        mime_type = magic.from_file(watermark_file, mime=True)
        file_name = os.path.basename(os.path.abspath(watermark_file))

        header = {
            'Authorization': self.api_key
        }
        files=[('watermark', (file_name, open(os.path.abspath(watermark_file), 'rb'), mime_type))]

        try:
            req = requests.post(url=f'{self.vod_base_url}/channels/{channel_id}/watermarks', headers=header, data=data, files=files)
            
            if req.status_code == 200 or req.status_code == 201:
                return req.json()
            elif req.status_code == 401:
                raise ApiError('Unauthorized')
            elif req.status_code == 403:
                raise ApiError('Forbidden')
            elif req.status_code == 404:
                raise ApiError('Channel Not Found')
            elif req.status_code == 422:
                raise ApiError('Unprocessable Entity')
            elif req.status_code == 500:
                raise ApiError('Internal Server Error')
        except ConnectionError:
                raise ApiError('Connection Error')

    def update_single_watermark(self, watermark_id=None, data: Watermark = None):
        if not watermark_id or not data["title"]:
            raise ApiError('Please supply a watermark_id or title')

        header = {
            'Content-Type': 'application/json',
            'Authorization': self.api_key
        }

        try:
            req = requests.patch(url=f'{self.vod_base_url}/watermarks/{watermark_id}', json=data, headers=header)
            
            if req.status_code == 200:
                return req.json()
            elif req.status_code == 401:
                raise ApiError('Unauthorized')
            elif req.status_code == 403:
                raise ApiError('Forbidden')
            elif req.status_code == 404:
                raise ApiError('Watermark Not Found')
            elif req.status_code == 422:
                raise ApiError('Unprocessable Entity')
            elif req.status_code == 500:
                raise ApiError('Internal Server Error')
        except ConnectionError:
                raise ApiError('Connection Error')

    def get_all_live_watermarks(self, params: QueryParams = None):
        header = {
            'Content-Type': 'application/json',
            'Authorization': self.api_key
        }

        try:
            req = requests.get(url=f'{self.live_base_url}/watermarks', headers=header, params=params)
            
            if req.status_code == 200:
                return req.json()
            elif req.status_code == 401:
                raise ApiError('Unauthorized')
            elif req.status_code == 403:
                raise ApiError('Forbidden')
            elif req.status_code == 404:
                raise ApiError('Watermark Not Found')
            elif req.status_code == 422:
                raise ApiError('Unprocessable Entity')
            elif req.status_code == 500:
                raise ApiError('Internal Server Error')
        except ConnectionError:
                raise ApiError('Connection Error')

    def get_single_live_watermark(self, watermark_id: str = None):
        header = {
            'Content-Type': 'application/json',
            'Authorization': self.api_key
        }
        
        try:
            req = requests.get(url=f'{self.live_base_url}/watermarks/{watermark_id}', headers=header)
            if req.status_code == 200:
                return req.json()
            elif req.status_code == 401:
                raise ApiError('Unauthorized')
            elif req.status_code == 403:
                raise ApiError('Forbidden')
            elif req.status_code == 404:
                raise ApiError('Watermark Not Found')
            elif req.status_code == 422:
                raise ApiError('Unprocessable Entity')
            elif req.status_code == 500:
                raise ApiError('Internal Server Error')
        except ConnectionError:
                raise ApiError('Connection Error')

    def create_new_live_watermark(self, watermark_file: str = None, data: Watermark = None):
        if not watermark_file or not data["title"]:
            raise ApiError('Please supply a watermark_file or title')

        if not os.path.exists(os.path.abspath(watermark_file)):
            raise ApiError('Watermark file does not exist')
        
        mime_type = magic.from_file(watermark_file, mime=True)
        file_name = os.path.basename(os.path.abspath(watermark_file))

        header = {
            'Authorization': self.api_key
        }
        files=[('watermark', (file_name, open(watermark_file, 'rb'), mime_type))]

        try:
            req = requests.post(url=f'{self.live_base_url}/watermarks', headers=header, data=data, files=files)
            
            if req.status_code == 201 or req.status_code == 200:
                return req.json()
            elif req.status_code == 401:
                raise ApiError('Unauthorized')
            elif req.status_code == 403:
                raise ApiError('Forbidden')
            elif req.status_code == 422:
                raise ApiError('Unprocessable Entity')
            elif req.status_code == 500:
                raise ApiError('Internal Server Error')
        except ConnectionError:
                raise ApiError('Connection Error')

    def remove_single_live_watermark(self, watermark_id: str = None):
        if not watermark_id:
            raise ApiError('Please supply a watermark_id')

        header = {
            'Authorization': self.api_key
        }

        try:
            req = requests.delete(url=f'{self.live_base_url}/watermarks/{watermark_id}', headers=header)
            
            if req.status_code == 200:
                return req.json()
            elif req.status_code == 401:
                raise ApiError('Unauthorized')
            elif req.status_code == 403:
                raise ApiError('Forbidden')
            elif req.status_code == 404:
                raise ApiError('Watermark Not Found')
            elif req.status_code == 422:
                raise ApiError('Unprocessable Entity')
            elif req.status_code == 500:
                raise ApiError('Internal Server Error')
        except ConnectionError:
                raise ApiError('Connection Error')

    def update_single_live_watermark(self, watermark_id: str = None, data: Watermark = None):
        if not watermark_id or not data["title"]:
            raise ApiError('Please supply a watermark_id or title')

        header = {
            'Content-Type': 'application/json',
            'Authorization': self.api_key
        }
        data={
            'title': title,
            'description': description,
        }

        try:
            req = requests.put(url=f'{self.live_base_url}/watermarks/{watermark_id}', headers=header, json=data)
            
            if req.status_code == 200:
                return req.json()
            elif req.status_code == 401:
                raise ApiError('Unauthorized')
            elif req.status_code == 403:
                raise ApiError('Forbidden')
            elif req.status_code == 404:
                raise ApiError('Watermark Not Found')
            elif req.status_code == 422:
                raise ApiError('Unprocessable Entity')
            elif req.status_code == 500:
                raise ApiError('Internal Server Error')
        except ConnectionError:
                raise ApiError('Connection Error')


