from arvancloud.video.helpers.error import ApiError

from arvancloud.video.interfaces.query_params import QueryParams
from arvancloud.video.interfaces.ad import Ad

import requests
import magic
import os

class Ads():
    def __init__(self, api_key=None, **kwargs) -> None:
        if not api_key:
            raise ApiError('Please supply an api_key')
        
        self.api_key = api_key
        self.base_url = 'https://napi.arvancloud.ir/vads/2.0'

    def get_all_channel_ads(self, channel_id: str = None, params: QueryParams = None):
        """Get a list of ads inside a channel."""
        if not channel_id:
            raise ApiError('Please supply a channel_id')

        header = {
            'Content-Type': 'application/json',
            'Authorization': self.api_key
        }
        
        try:
            req = requests.get(url=f'{self.base_url}/channels/{channel_id}/ads', params=params, headers=header)
            if req.status_code == 200:
                return req.json()
            elif req.status_code == 401:
                raise ApiError('Unauthorized')
            elif req.status_code == 403:
                raise ApiError('Forbidden')
            elif req.status_code == 404:
                raise ApiError('Campaign Not Found')
            elif req.status_code == 422:
                raise ApiError('Unprocessable Entity')
            elif req.status_code == 500:
                raise ApiError('Internal Server Error')
        except ConnectionError:
                raise ApiError('Connection Error')

    def get_single_ad(self, ad_id: str = ''):
        """Get a single ad"""
        if not ad_id:
            raise ApiError('Please supply an ad_id')

        header = {
            'Content-Type': 'application/json',
            'Authorization': self.api_key
        }
        
        try:
            req = requests.get(url=f'{self.base_url}/ads/{ad_id}', headers=header)
            if req.status_code == 200:
                return req.json()
            elif req.status_code == 401:
                raise ApiError('Unauthorized')
            elif req.status_code == 403:
                raise ApiError('Forbidden')
            elif req.status_code == 404:
                raise ApiError('Campaign Not Found')
            elif req.status_code == 422:
                raise ApiError('Unprocessable Entity')
            elif req.status_code == 500:
                raise ApiError('Internal Server Error')
        except ConnectionError:
                raise ApiError('Connection Error')

    def remove_single_ad(self, ad_id: str = ''):
        """Remove a single ad"""
        if not ad_id:
            raise ApiError('Please supply an ad_id')

        header = {
            'Content-Type': 'application/json',
            'Authorization': self.api_key
        }
        
        try:
            req = requests.delete(url=f'{self.base_url}/ads/{ad_id}', headers=header)
            if req.status_code == 200:
                return req.json()
            elif req.status_code == 401:
                raise ApiError('Unauthorized')
            elif req.status_code == 403:
                raise ApiError('Forbidden')
            elif req.status_code == 404:
                raise ApiError('Campaign Not Found')
            elif req.status_code == 422:
                raise ApiError('Unprocessable Entity')
            elif req.status_code == 500:
                raise ApiError('Internal Server Error')
        except ConnectionError:
                raise ApiError('Connection Error')

    def update_single_ad(self, ad_id: str = '', data: Ad = None):
        if not ad_id:
            raise ApiError('Please supply an ad_id')

        header = {
            'Content-Type': 'application/json',
            'Authorization': self.api_key
        }
        
        try:
            req = requests.put(url=f'{self.base_url}/ads/{ad_id}', json=data, headers=header)
            if req.status_code == 200:
                return req.json()
            elif req.status_code == 401:
                raise ApiError('Unauthorized')
            elif req.status_code == 403:
                raise ApiError('Forbidden')
            elif req.status_code == 404:
                raise ApiError('Campaign Not Found')
            elif req.status_code == 422:
                raise ApiError('Unprocessable Entity')
            elif req.status_code == 500:
                raise ApiError('Internal Server Error')
        except ConnectionError:
                raise ApiError('Connection Error')

    def create_single_ad(self, channel_id: str = '', data: Ad = None, media_file_path: str = None):
        if not channel_id:
            raise ApiError('Please supply an channel_id')

        if not os.path.exists(os.path.abspath(media_file_path)):
            raise ApiError('Watermark file does not exist')

        mime_type = magic.from_file(media_file_path, mime=True)
        file_name = os.path.basename(os.path.abspath(media_file_path))

        header = {
            'Authorization': self.api_key
        }
        files=[('media_file', (file_name, open(os.path.abspath(media_file_path), 'rb'), mime_type))]
        
        try:
            req = requests.post(url=f'{self.base_url}/channels/{channel_id}/ads', data=data, headers=header, files=files)
            if req.status_code == 200 or req.status_code == 201:
                return req.json()
            elif req.status_code == 401:
                raise ApiError('Unauthorized')
            elif req.status_code == 403:
                raise ApiError('Forbidden')
            elif req.status_code == 404:
                raise ApiError('Campaign Not Found')
            elif req.status_code == 422:
                raise ApiError('Unprocessable Entity')
            elif req.status_code == 500:
                raise ApiError('Internal Server Error')
        except ConnectionError:
                raise ApiError('Connection Error')

