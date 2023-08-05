from arvancloud.video.helpers.error import ApiError

from arvancloud.video.interfaces.query_params import QueryParams
from arvancloud.video.interfaces.profile import Profile

import requests

class VodProfiles():
    def __init__(self, api_key=None, **kwargs) -> None:
        if not api_key:
            raise ApiError('Please supply an api_key')
        
        self.api_key = api_key
        self.base_url = 'https://napi.arvancloud.ir/vod/2.0'
    
    def get_profiles(self, channel_id: str = None, params: QueryParams = None):
        """Get a list of profiles."""
        if not channel_id:
            raise ApiError('Please supply a channel_id')

        header = {
            'Content-Type': 'application/json',
            'Authorization': self.api_key
        }
        
        try:
            req = requests.get(url=f'{self.base_url}/channels/{channel_id}/profiles', params=params, headers=header)
            if req.status_code == 200:
                return req.json()
            elif req.status_code == 401:
                raise ApiError('Unauthorized')
            elif req.status_code == 403:
                raise ApiError('Forbidden')
            elif req.status_code == 404:
                raise ApiError('Profile Not Found')
            elif req.status_code == 422:
                raise ApiError('Unprocessable Entity')
            elif req.status_code == 500:
                raise ApiError('Internal Server Error')
        except ConnectionError:
                raise ApiError('Connection Error')

    def get_single_profile(self, profile_id: str = None):
        if not profile_id:
            raise ApiError('Please supply a profile_id')

        header = {
            'Content-Type': 'application/json',
            'Authorization': self.api_key
        }
        
        try:
            req = requests.get(url=f'{self.base_url}/profiles/{profile_id}', headers=header)
            if req.status_code == 200:
                return req.json()
            elif req.status_code == 401:
                raise ApiError('Unauthorized')
            elif req.status_code == 403:
                raise ApiError('Forbidden')
            elif req.status_code == 404:
                raise ApiError('Profile Not Found')
            elif req.status_code == 422:
                raise ApiError('Unprocessable Entity')
            elif req.status_code == 500:
                raise ApiError('Internal Server Error')
        except ConnectionError:
                raise ApiError('Connection Error')

    def remove_single_profile_from_channel(self, profile_id: str = None):
        if not profile_id:
            raise ApiError('Please supply a profile_id')

        header = {
            'Content-Type': 'application/json',
            'Authorization': self.api_key
        }
        
        try:
            req = requests.delete(url=f'{self.base_url}/profiles/{profile_id}', headers=header)
            if req.status_code == 200:
                return req.json()
            elif req.status_code == 401:
                raise ApiError('Unauthorized')
            elif req.status_code == 403:
                raise ApiError('Forbidden')
            elif req.status_code == 404:
                raise ApiError('Profile Not Found')
            elif req.status_code == 422:
                raise ApiError('Unprocessable Entity')
            elif req.status_code == 500:
                raise ApiError('Internal Server Error')
        except ConnectionError:
                raise ApiError('Connection Error')

    def create_new_profile_for_channel(self, channel_id: str = None, data: Profile = None):
        if not channel_id:
            raise ApiError('Please supply a channel_id')

        header = {
            'Content-Type': 'application/json',
            'Authorization': self.api_key
        }
        
        try:
            req = requests.post(url=f'{self.base_url}/channels/{channel_id}/profiles', headers=header, json=data)
            if req.status_code == 200 or req.status_code == 201:
                return req.json()
            elif req.status_code == 401:
                raise ApiError('Unauthorized')
            elif req.status_code == 403:
                raise ApiError('Forbidden')
            elif req.status_code == 404:
                raise ApiError('Profile Not Found')
            elif req.status_code == 422:
                raise ApiError('Unprocessable Entity')
            elif req.status_code == 500:
                raise ApiError('Internal Server Error')
        except ConnectionError:
                raise ApiError('Connection Error')
    
    def update_single_profile(self, profile_id: str = None, data: Profile = None):
        if not profile_id:
            raise ApiError('Please supply a profile_id')

        header = {
            'Content-Type': 'application/json',
            'Authorization': self.api_key
        }
        
        try:
            req = requests.patch(url=f'{self.base_url}/profiles/{profile_id}', headers=header, json=data)
            if req.status_code == 200:
                return req.json()
            elif req.status_code == 401:
                raise ApiError('Unauthorized')
            elif req.status_code == 403:
                raise ApiError('Forbidden')
            elif req.status_code == 404:
                raise ApiError('Profile Not Found')
            elif req.status_code == 422:
                raise ApiError('Unprocessable Entity')
            elif req.status_code == 500:
                raise ApiError('Internal Server Error')
        except ConnectionError:
                raise ApiError('Connection Error')