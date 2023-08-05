from arvancloud.video.helpers.error import ApiError
from arvancloud.video.interfaces.query_params import QueryParams
from arvancloud.video.interfaces.campaign import Campaign
from arvancloud.video.interfaces.campaign_ad import CampaignAd

import requests

class Campaigns():
    def __init__(self, api_key=None, **kwargs) -> None:
        if not api_key:
            raise ApiError('Please supply an api_key')
        
        self.api_key = api_key
        self.base_url = 'https://napi.arvancloud.ir/vads/2.0'

    def get_single_channel_campaigns(self,channel_id: str = None, params: QueryParams = None):
        if not channel_id:
            raise ApiError('Please supply a channel_id')

        header = {
            'Content-Type': 'application/json',
            'Authorization': self.api_key
        }
        
        try:
            req = requests.get(url=f'{self.base_url}/channels/{channel_id}/campaigns', params=params, headers=header)
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

    def get_single_campaign_info(self, campaign_id: str = None):
        header = {
            'Content-Type': 'application/json',
            'Authorization': self.api_key
        }
        
        try:
            req = requests.get(url=f'{self.base_url}/campaigns/{campaign_id}', headers=header)
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

    def remove_single_campaign(self, campaign_id: str = None):
        header = {
            'Content-Type': 'application/json',
            'Authorization': self.api_key
        }
        
        try:
            req = requests.delete(url=f'{self.base_url}/campaigns/{campaign_id}', headers=header)
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

    def create_single_campaign(self, channel_id: str = None, data: Campaign = None):
        if not channel_id:
            raise ApiError('Please supply a channel_id')

        if not data:
            raise ApiError('Please supply a form')

        header = {
            'Content-Type': 'application/json',
            'Authorization': self.api_key
        }
        
        try:
            req = requests.post(url=f'{self.base_url}/channels/{channel_id}/campaigns', json=data, headers=header)
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

    def update_single_campaign(self, campaign_id: str = '', data: Campaign = None):
        if not campaign_id:
            raise ApiError('Please supply a campaign_id')

        if not data:
            raise ApiError('Please supply a form')

        header = {
            'Content-Type': 'application/json',
            'Authorization': self.api_key
        }
        
        try:
            req = requests.put(url=f'{self.base_url}/campaigns/{campaign_id}', json=data, headers=header)
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

    def get_all_ads_inside_campaign(self, campaign_id: str = None):
        if not campaign_id:
            raise ApiError('Please supply a campaign_id')

        
        header = {
            'Content-Type': 'application/json',
            'Authorization': self.api_key
        }
        
        try:
            req = requests.get(url=f'{self.base_url}/campaigns/{campaign_id}/ads', headers=header)
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

    def get_single_ad_in_single_campaign(self, campaign_id: str = None, ad_id: str = None):
        if not campaign_id:
            raise ApiError('Please supply a campaign_id')

        if not ad_id:
            raise ApiError('Please supply an ad_id')

        
        header = {
            'Content-Type': 'application/json',
            'Authorization': self.api_key
        }
        
        try:
            req = requests.get(url=f'{self.base_url}/campaigns/{campaign_id}/ads/{ad_id}', headers=header)
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

    def remove_single_ad_from_single_campaign(self, campaign_id: str = None, ad_id: str = None):
        if not campaign_id:
            raise ApiError('Please supply a campaign_id')

        if not ad_id:
            raise ApiError('Please supply an ad_id')

        
        header = {
            'Content-Type': 'application/json',
            'Authorization': self.api_key
        }
        
        try:
            req = requests.delete(url=f'{self.base_url}/campaigns/{campaign_id}/ads/{ad_id}', headers=header)
            if req.status_code == 204:
                return True
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

    def update_single_ad_in_single_campaign(self, campaign_id: str = None, ad_id: str = None, data: CampaignAd = None):
        if not campaign_id:
            raise ApiError('Please supply a campaign_id')
        if not ad_id:
            raise ApiError('Please supply an ad_id')
        if not data:
            raise ApiError('Please supply a form')

        header = {
            'Content-Type': 'application/json',
            'Authorization': self.api_key
        }
        
        try:
            req = requests.put(url=f'{self.base_url}/campaigns/{campaign_id}/ads/{ad_id}', json=data, headers=header)
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

    def add_single_ad_to_single_campaign(self, campaign_id: str = None, data: CampaignAd = None):
        if not campaign_id:
            raise ApiError('Please supply a campaign_id')

        if not data:
            raise ApiError('Please supply a form')

        header = {
            'Content-Type': 'application/json',
            'Authorization': self.api_key
        }
        
        try:
            req = requests.post(url=f'{self.base_url}/campaigns/{campaign_id}/ads', json=data, headers=header)
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


