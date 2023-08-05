from arvancloud.video.helpers.error import ApiError
import requests

class Domains():
    def __init__(self, api_key=None, **kwargs) -> None:
        if not api_key:
            raise ApiError('Please supply an api_key')
        
        self.api_key = api_key
        self.base_url = 'https://napi.arvancloud.ir/'

    def get_live_domains(self):
        """Get a list of live domains."""
        header = {
            'Content-Type': 'application/json',
            'Authorization': self.api_key
        }

        try:
            req = requests.get(url=f'{self.base_url}/live/2.0/domain', headers=header)
            if req.status_code == 200:
                return req.json()
            elif req.status_code == 401:
                raise ApiError('Unauthorized')
            elif req.status_code == 403:
                raise ApiError('Forbidden')
            elif req.status_code == 404:
                raise ApiError('Domain Not Found')
            elif req.status_code == 422:
                raise ApiError('Unprocessable Entity')
            elif req.status_code == 500:
                raise ApiError('Internal Server Error')
        except ConnectionError:
                raise ApiError('Connection Error')

    def create_new_live_domain(self, domain_name=''):
        """Create a new live domain."""
        if not domain_name:
            raise ApiError('Please supply a domain_name')

        header = {
            'Content-Type': 'application/json',
            'Authorization': self.api_key
        }

        try:
            req = requests.post(url=f'{self.base_url}/live/2.0/domain', headers=header, json={'subdomain': domain_name})
            if req.status_code == 200:
                return req.json()
            elif req.status_code == 401:
                raise ApiError('Unauthorized')
            elif req.status_code == 403:
                raise ApiError('Forbidden')
            elif req.status_code == 404:
                raise ApiError('Domain Not Found')
            elif req.status_code == 422:
                raise ApiError('Unprocessable Entity')
            elif req.status_code == 500:
                raise ApiError('Internal Server Error')
        except ConnectionError:
                raise ApiError('Connection Error')

    def get_vod_domains(self):
        """Get a list of VoD domains."""
        header = {
            'Content-Type': 'application/json',
            'Authorization': self.api_key
        }

        try:
            req = requests.get(url=f'{self.base_url}/vod/2.0/domain', headers=header)
            if req.status_code == 200:
                return req.json()
            elif req.status_code == 401:
                raise ApiError('Unauthorized')
            elif req.status_code == 403:
                raise ApiError('Forbidden')
            elif req.status_code == 404:
                raise ApiError('Domain Not Found')
            elif req.status_code == 422:
                raise ApiError('Unprocessable Entity')
            elif req.status_code == 500:
                raise ApiError('Internal Server Error')
        except ConnectionError:
                raise ApiError('Connection Error')

    def create_new_vod_domain(self, domain_name=''):
        """Create a new VoD domain."""
        if not domain_name:
            raise ApiError('Please supply a domain_name')

        header = {
            'Content-Type': 'application/json',
            'Authorization': self.api_key
        }

        try:
            req = requests.post(url=f'{self.base_url}/vod/2.0/domain', headers=header, json={'subdomain': domain_name})
            if req.status_code == 200:
                return req.json()
            elif req.status_code == 401:
                raise ApiError('Unauthorized')
            elif req.status_code == 403:
                raise ApiError('Forbidden')
            elif req.status_code == 404:
                raise ApiError('Domain Not Found')
            elif req.status_code == 422:
                raise ApiError('Unprocessable Entity')
            elif req.status_code == 500:
                raise ApiError('Internal Server Error')
        except ConnectionError:
                raise ApiError('Connection Error')

    def get_vads_domains(self):
        """Get a list of VAds domains."""
        header = {
            'Content-Type': 'application/json',
            'Authorization': self.api_key
        }

        try:
            req = requests.get(url=f'{self.base_url}/vads/2.0/domain', headers=header)
            if req.status_code == 200:
                return req.json()
            elif req.status_code == 401:
                raise ApiError('Unauthorized')
            elif req.status_code == 403:
                raise ApiError('Forbidden')
            elif req.status_code == 404:
                raise ApiError('Domain Not Found')
            elif req.status_code == 422:
                raise ApiError('Unprocessable Entity')
            elif req.status_code == 500:
                raise ApiError('Internal Server Error')
        except ConnectionError:
                raise ApiError('Connection Error')

    def create_new_vads_domain(self, domain_name=''):
        """Create a new VAds domain."""
        if not domain_name:
            raise ApiError('Please supply a domain_name')

        header = {
            'Content-Type': 'application/json',
            'Authorization': self.api_key
        }

        try:
            req = requests.post(url=f'{self.base_url}/vads/2.0/domain', headers=header, json={'subdomain': domain_name})
            if req.status_code == 200:
                return req.json()
            elif req.status_code == 401:
                raise ApiError('Unauthorized')
            elif req.status_code == 403:
                raise ApiError('Forbidden')
            elif req.status_code == 404:
                raise ApiError('Domain Not Found')
            elif req.status_code == 422:
                raise ApiError('Unprocessable Entity')
            elif req.status_code == 500:
                raise ApiError('Internal Server Error')
        except ConnectionError:
                raise ApiError('Connection Error')


