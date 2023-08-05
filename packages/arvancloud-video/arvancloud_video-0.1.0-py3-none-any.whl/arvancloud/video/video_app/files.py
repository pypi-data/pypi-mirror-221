from arvancloud.video.helpers.error import ApiError

from arvancloud.video.interfaces.query_params import QueryParams

import base64
import magic
import requests
import os

class VodFiles():
    def __init__(self, api_key=None, **kwargs) -> None:
        if not api_key:
            raise ApiError('Please supply an api_key')
        
        self.api_key = api_key
        self.base_url = 'https://napi.arvancloud.ir/vod/2.0'
    
    def get_files(self, channel_id: str = None, params: QueryParams = None):
        if not channel_id:
            raise ApiError('Please supply a channel_id')

        header = {
            'Content-Type': 'application/json',
            'Authorization': self.api_key
        }
        
        try:
            req = requests.get(url=f'{self.base_url}/channels/{channel_id}/files', params=params, headers=header)
            if req.status_code == 200:
                return req.json()
            elif req.status_code == 401:
                raise ApiError('Unauthorized')
            elif req.status_code == 403:
                raise ApiError('Forbidden')
            elif req.status_code == 404:
                raise ApiError('File Not Found')
            elif req.status_code == 422:
                raise ApiError('Unprocessable Entity')
            elif req.status_code == 500:
                raise ApiError('Internal Server Error')
        except ConnectionError:
                raise ApiError('Connection Error')
    
    def get_single_file(self, file_id: str = None):
        """Get a single file."""
        if not file_id:
            raise ApiError('Please supply a file_id')

        header = {
            'Content-Type': 'application/json',
            'Authorization': self.api_key
        }
        
        try:
            req = requests.get(url=f'{self.base_url}/files/{file_id}', headers=header)
            if req.status_code == 200:
                return req.json()
            elif req.status_code == 401:
                raise ApiError('Unauthorized')
            elif req.status_code == 403:
                raise ApiError('Forbidden')
            elif req.status_code == 404:
                raise ApiError('File Not Found')
            elif req.status_code == 422:
                raise ApiError('Unprocessable Entity')
            elif req.status_code == 500:
                raise ApiError('Internal Server Error')
        except ConnectionError:
                raise ApiError('Connection Error')
    
    def remove_single_file_from_channel(self, file_id: str = None):
        if not file_id:
            raise ApiError('Please supply a file_id')

        header = {
            'Content-Type': 'application/json',
            'Authorization': self.api_key
        }
        
        try:
            req = requests.delete(url=f'{self.base_url}/files/{file_id}', headers=header)
            if req.status_code == 200:
                return req.json()
            elif req.status_code == 401:
                raise ApiError('Unauthorized')
            elif req.status_code == 403:
                raise ApiError('Forbidden')
            elif req.status_code == 404:
                raise ApiError('File Not Found')
            elif req.status_code == 422:
                raise ApiError('Unprocessable Entity')
            elif req.status_code == 500:
                raise ApiError('Internal Server Error')
        except ConnectionError:
                raise ApiError('Connection Error')

    def create_new_file_for_specific_channel(self, channel_id: str = None, file_path: str = None):
        if not file_path or not channel_id:
            raise ApiError('Please supply a file_path or channel_id')

        if not os.path.exists(os.path.abspath(file_path)):
            raise ApiError('file does not exist')

        # Get File Size
        file_size = os.path.getsize(os.path.abspath(file_path))

        # Encode MimeType To Base64
        mime_type = magic.from_file(os.path.abspath(file_path), mime=True)
        file_type_bytes = mime_type.encode('ascii')
        file_type_base64_bytes = base64.b64encode(file_type_bytes)
        file_type_base64 = file_type_base64_bytes.decode('ascii')

        # Encode FileName To Base64
        file_name = os.path.basename(os.path.abspath(file_path))
        file_name_bytes = file_name.encode('ascii')
        file_name_base64_bytes = base64.b64encode(file_name_bytes)
        file_name_base64 = file_name_base64_bytes.decode('ascii')

        header = {
            'upload-length': f'{file_size}',
            'tus-resumable': '1.0.0',
            'upload-metadata': f'filename {file_name_base64},filetype {file_type_base64}',
            'Authorization': self.api_key
        }
        file_container_req = requests.post(f'{self.base_url}/channels/{channel_id}/files', headers=header)

        if file_container_req.status_code == 201 or file_container_req.status_code == 200:
            with open(os.path.abspath(file_path), 'rb') as file:
                upload_location = file_container_req.headers['Location']
                upload_file_header = {
                    'Content-Type': 'application/offset+octet-stream',
                    'upload-offset': '0',
                    'tus-resumable': '1.0.0',
                    'Authorization': self.api_key,
                }
                
                try:
                    upload_req = requests.patch(url=upload_location, headers=upload_file_header, data=file)
                    
                    if upload_req.status_code == 204:
                        return {
                            'success': True,
                            'message': 'File Uploaded Successfully',
                            'file_id': upload_location.split('/')[-1]
                        }
                    elif upload_req.status_code == 416:
                        raise ApiError('The Content-Length Is not as same as The Upload-Length')
                except ConnectionError:
                        raise ApiError('Connection Error')

