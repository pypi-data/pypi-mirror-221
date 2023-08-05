from arvancloud.video.helpers.error import ApiError
from arvancloud.video.interfaces.query_params import QueryParams
from arvancloud.video.interfaces.video import Video

import requests
import os
import magic

class VodVideos():
    def __init__(self, api_key=None, **kwargs) -> None:
        if not api_key:
            raise ApiError('Please supply an api_key')

        self.api_key = api_key
        self.base_url = 'https://napi.arvancloud.ir/vod/2.0'

    def get_single_channel_videos(self, channel_id: str = None, params: QueryParams = None):
        if not channel_id:
            raise ApiError('Please supply a channel_id')

        header = {
            'Content-Type': 'application/json',
            'Authorization': self.api_key
        }

        try:
            req = requests.get(url=f'{self.base_url}/channels/{channel_id}/videos', params=params, headers=header)
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

    def remove_single_video_from_channel(self, video_id: str = None):
        if not video_id:
            raise ApiError('Please supply a video_id')

        header = {
            'Content-Type': 'application/json',
            'Authorization': self.api_key
        }

        try:
            req = requests.delete(url=f'{self.base_url}/videos/{video_id}', headers=header)
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

    def save_file_as_video(self, channel_id: str = None, data: Video = None):
        if not channel_id:
            raise ApiError('Please supply a channel_id')

        header = {
            'Content-Type': 'application/json',
            'Authorization': self.api_key
        }

        try:
            req = requests.post(url=f'{self.base_url}/channels/{channel_id}/videos', json=data, headers=header)
            if req.status_code == 200 or req.status_code == 201:
                return req.json()
            elif req.status_code == 401:
                raise ApiError('Unauthorized')
            elif req.status_code == 403:
                raise ApiError('Forbidden')
            elif req.status_code == 404:
                raise ApiError('Video Not Found')
            elif req.status_code == 422:
                raise ApiError('Unprocessable Entity')
            elif req.status_code == 500:
                raise ApiError('Internal Server Error')
        except ConnectionError:
                raise ApiError('Connection Error')

    def get_all_video_subtitles(self, video_id: str = None):
        if not video_id:
            raise ApiError('Please supply a video_id')

        header = {
            'Content-Type': 'application/json',
            'Authorization': self.api_key
        }

        try:
            req = requests.get(url=f'{self.base_url}/videos/{video_id}/subtitles', headers=header)
            if req.status_code == 200:
                return req.json()
            elif req.status_code == 401:
                raise ApiError('Unauthorized')
            elif req.status_code == 403:
                raise ApiError('Forbidden')
            elif req.status_code == 404:
                raise ApiError('Video Not Found')
            elif req.status_code == 422:
                raise ApiError('Unprocessable Entity')
            elif req.status_code == 500:
                raise ApiError('Internal Server Error')
        except ConnectionError:
                raise ApiError('Connection Error')

    def add_subtitle_to_single_video(self, video_id: str = None, lang: str = None, subtitle_file: str = None):
        if not subtitle_file or not video_id:
            raise ApiError('Please supply a watermark_file or title')

        if not os.path.exists(os.path.abspath(subtitle_file)):
            raise ApiError('Subtitle file does not exist')

        mime_type = magic.from_file(subtitle_file, mime=True)
        file_name = os.path.basename(os.path.abspath(subtitle_file))

        header = {
            'Authorization': self.api_key
        }

        files = [('subtitle', (file_name, open(os.path.abspath(subtitle_file), 'rb'), mime_type))]
        data = {
            'lang': lang,
        }

        try:
            req = requests.post(
                url=f'{self.base_url}/videos/{video_id}/subtitles',
                headers=header,
                data=data,
                files=files,
            )
            if req.status_code == 200 or req.status_code == 201:
                return req.json()
            elif req.status_code == 401:
                raise ApiError('Unauthorized')
            elif req.status_code == 403:
                raise ApiError('Forbidden')
            elif req.status_code == 404:
                raise ApiError('Video Not Found')
            elif req.status_code == 422:
                raise ApiError('Unprocessable Entity')
            elif req.status_code == 500:
                raise ApiError('Internal Server Error')
        except ConnectionError:
            raise ApiError('Connection Error')

    def remove_subtitle_from_single_video(self, subtitle_id: str = None):
        """Remove a subtitle from a video."""
        header = {
            'Content-Type': 'application/json',
            'Authorization': self.api_key
        }

        try:
            req = requests.delete(url=f'{self.base_url}/subtitles/{subtitle_id}', headers=header)
            if req.status_code == 200:
                return req.json()
            elif req.status_code == 401:
                raise ApiError('Unauthorized')
            elif req.status_code == 403:
                raise ApiError('Forbidden')
            elif req.status_code == 404:
                raise ApiError('Subtitle Not Found')
            elif req.status_code == 422:
                raise ApiError('Unprocessable Entity')
            elif req.status_code == 500:
                raise ApiError('Internal Server Error')
        except ConnectionError:
                raise ApiError('Connection Error')

    def get_all_video_sound_tracks(self, video_id: str = None):
        header = {
            'Content-Type': 'application/json',
            'Authorization': self.api_key
        }

        try:
            req = requests.get(url=f'{self.base_url}/videos/{video_id}/audio-tracks', headers=header)
            if req.status_code == 200:
                return req.json()
            elif req.status_code == 401:
                raise ApiError('Unauthorized')
            elif req.status_code == 403:
                raise ApiError('Forbidden')
            elif req.status_code == 404:
                raise ApiError('Video Not Found')
            elif req.status_code == 422:
                raise ApiError('Unprocessable Entity')
            elif req.status_code == 500:
                raise ApiError('Internal Server Error')
        except ConnectionError:
                raise ApiError('Connection Error')

    def add_sound_track_to_single_video(self, video_id: str = None, lang: str = None, sound_track_file: str = None):
        if not sound_track_file or not video_id:
            raise ApiError('Please supply a sound_track_file or title')

        if not os.path.exists(os.path.abspath(sound_track_file)):
            raise ApiError('Sound Track file does not exist')

        mime_type = magic.from_file(sound_track_file, mime=True)
        file_name = os.path.basename(os.path.abspath(sound_track_file))

        header = {
            'Authorization': self.api_key
        }
        files=[('audio_track', (file_name, open(os.path.abspath(sound_track_file), 'rb'), mime_type))]
        data = {
            'lang': lang,
        }

        try:
            req = requests.post(url=f'{self.base_url}/videos/{video_id}/audio-tracks', headers=header, data=data, files=files)
            if req.status_code == 200 or req.status_code == 201:
                return req.json()
            elif req.status_code == 401:
                raise ApiError('Unauthorized')
            elif req.status_code == 403:
                raise ApiError('Forbidden')
            elif req.status_code == 404:
                raise ApiError('Video Not Found')
            elif req.status_code == 422:
                raise ApiError('Unprocessable Entity')
            elif req.status_code == 500:
                raise ApiError('Internal Server Error')
        except ConnectionError:
                raise ApiError('Connection Error')

    def remove_sound_track_from_single_video(self, sound_track_id: str = None):
        header = {
            'Content-Type': 'application/json',
            'Authorization': self.api_key
        }

        try:
            req = requests.delete(url=f'{self.base_url}/audio-tracks/{sound_track_id}', headers=header)
            if req.status_code == 200:
                return req.json()
            elif req.status_code == 401:
                raise ApiError('Unauthorized')
            elif req.status_code == 403:
                raise ApiError('Forbidden')
            elif req.status_code == 404:
                raise ApiError('Sound Track Not Found')
            elif req.status_code == 422:
                raise ApiError('Unprocessable Entity')
            elif req.status_code == 500:
                raise ApiError('Internal Server Error')
        except ConnectionError:
                raise ApiError('Connection Error')


