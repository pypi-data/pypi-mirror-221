""" Arvan Video Platform API """
'''
For ArvanCloud VOD API documentation, visit: https://www.arvancloud.ir/docs/api/vod/2.0/
For ArvanCloud Live API documentation, visit: https://www.arvancloud.ir/docs/api/live/2.0/
For ArvanCloud Vads API documentation, visit: https://www.arvancloud.ir/docs/api/vads/2.0/
'''

__author__ = 'Amirhossein Douzandeh Zenoozi <amirzenoozi72@gmail.com>'
__version__ = '0.1.0'

from arvancloud.video.video_app.watermarks import VodWatermarks
from arvancloud.video.video_app.videos import VodVideos
from arvancloud.video.video_app.profiles import VodProfiles
from arvancloud.video.video_app.live import LiveStreams
from arvancloud.video.video_app.files import VodFiles
from arvancloud.video.video_app.domains import Domains
from arvancloud.video.video_app.channels import VodChannels
from arvancloud.video.video_app.campaigns import Campaigns
from arvancloud.video.video_app.audios import VodAudios
from arvancloud.video.video_app.ads import Ads

from arvancloud.video.helpers.error import ApiError

from arvancloud.video.interfaces.query_params import QueryParams
from arvancloud.video.interfaces.channel import Channel
from arvancloud.video.interfaces.video import Video
from arvancloud.video.interfaces.audio import Audio
from arvancloud.video.interfaces.watermark import Watermark
from arvancloud.video.interfaces.profile import Profile
from arvancloud.video.interfaces.stream import Stream
from arvancloud.video.interfaces.vads_channel import VadsChannel
from arvancloud.video.interfaces.campaign import Campaign
from arvancloud.video.interfaces.campaign_ad import CampaignAd
from arvancloud.video.interfaces.ad import Ad


class VideoClient():
    def __init__(self, api_key: str = None, **kwargs,):
        if not api_key:
            raise ApiError('Please supply an api_key')

        self.domains = Domains(api_key=api_key)
        self.channel = VodChannels(api_key=api_key)
        self.videos = VodVideos(api_key=api_key)
        self.audios = VodAudios(api_key=api_key)
        self.watermarks = VodWatermarks(api_key=api_key)
        self.profiles = VodProfiles(api_key=api_key)
        self.files = VodFiles(api_key=api_key)
        self.live = LiveStreams(api_key=api_key)
        self.campaign = Campaigns(api_key=api_key)
        self.ads = Ads(api_key=api_key)


    # Domains APIs
    def get_domains(self, domain_type: str = ''):
        """
        Get a list of domains.

        Parameters:
            domain_type (str): This Parameter Will Indicate The Domain Type
        """
        if domain_type == 'live':
            return self.domains.get_live_domains()
        elif domain_type == 'vod':
            return self.domains.get_vod_domains()
        elif domain_type == 'vads':
            return self.domains.get_vads_domains()
        else:
            raise ApiError('You Just Need To Specify A Type Of Domain (live, vod, vads)')

    def create_domain(self, domain_type: str = '', domain_name: str = ''):
        """
        Create a domain.

        Parameters:
            domain_type (str): This Parameter Will Indicate The Domain Type
            domain_name (str): This Parameter Will Indicate Your Domain Name
        """
        if domain_type == 'live':
            return self.domains.create_new_live_domain(domain_name)
        elif domain_type == 'vod':
            return self.domains.create_new_vod_domain(domain_name)
        elif domain_type == 'vads':
            return self.domains.create_new_vads_domain(domain_name)
        else:
            raise ApiError('You Just Need To Specify A Type Of Domain (live, vod, vads)')


    # Channels APIs
    def get_channels(self, params: QueryParams = None):
        """
        Get a list of channels.

        Parameters:
            params (QueryParams): A Optional Dictionary To Apply Some Changes
        """
        return self.channel.get_channels(params=params)

    def get_channel_info(self, channel_id: str = ''):
        """
        Get a channel info.

        Parameters:
            channel_id (str): The ID Of Your Target Channel
        """
        return self.channel.get_single_channel(channel_id)

    def remove_channel(self, channel_id: str = ''):
        """
        Remove a channel.

        Parameters:
            channel_id (str): The ID Of Your Target Channel
        """
        return self.channel.remove_single_channel(channel_id)

    def create_channel(self, data: Channel):
        """
        Create a channel.

        Parameters:
            data (Channel): A New Channel Input Dictionary
        """
        return self.channel.create_new_channel(data)

    def update_channel(self, channel_id: str = None, data: Channel = None):
        """
        Update a channel.

        Parameters:
            channel_id (str): The ID Of Your Target Channel
            data (Channel): A New Channel Input Dictionary
        """
        return self.channel.update_single_channel(channel_id=channel_id, data=data)


    # Video APIs
    def get_single_channel_videos(self, channel_id: str = None, params: QueryParams = None):
        """
        Get a list of videos of a channel.

        Parameters:
            channel_id (str): The ID Of Your Target Channel
            params (QueryParams): A Optional Dictionary To Apply Some Changes
        """
        return self.videos.get_single_channel_videos(channel_id=channel_id, params=params)

    def remove_video(self, video_id: str = None):
        """
        Remove a video.

        Parameters:
            video_id (str): The ID Of Your Target Video
        """
        return self.videos.remove_single_video_from_channel(video_id)

    def save_new_video(self, channel_id: str = None, data: Video = None):
        """
        Save a new video

        Parameters:
            channel_id (str): The ID Of Your Target Channel
            data (Video): The Video Information's
        """
        return self.videos.save_file_as_video(channel_id=channel_id, data=data)


    # Subtitle APIs
    def get_video_subtitles(self, video_id: str = None):
        """
        Get a video subtitles.

        Parameters:
            video_id (str): The ID Of Your Target Video
        """
        return self.videos.get_all_video_subtitles(video_id)

    def add_video_subtitle(self, video_id: str = None, lang: str = None, subtitle_file: str = None):
        """
        Add a subtitle to a video.

        Parameters:
            video_id (str): The ID Of Your Target Video
            lang (str): The Subtitle Language
            subtitle_file (str): The Subtitle File Path
        """
        return self.videos.add_subtitle_to_single_video(
            video_id=video_id,
            lang=lang,
            subtitle_file=subtitle_file
        )

    def remove_video_subtitle(self, subtitle_id: str = None):
        """
        Remove a subtitle.

        Parameters:
            subtitle_id (str): The ID Of Your Target Subtitle
        """
        return self.videos.remove_subtitle_from_single_video(subtitle_id=subtitle_id)


    # SoundTrack APIs
    def get_video_sounds(self, video_id: str = None):
        """
        Get a video sounds.

        Parameters:
            video_id (str): The ID Of Your Target Video
        """
        return self.videos.get_all_video_sound_tracks(video_id)

    def add_video_sound(self, video_id: str = None, lang: str = None, sound_file: str = None):
        """
        Add a sound to a video.

        Parameters:
            video_id (str): The ID Of Your Target Video
            lang (str): The Subtitle Language
            sound_file (str): The Sound File Path
        """
        return self.videos.add_sound_track_to_single_video(
            video_id=video_id,
            lang=lang,
            sound_track_file=sound_file
        )

    def remove_video_sound(self, sound_id: str = None):
        """
        Remove a sound.

        Parameters:
            sound_id (str): The ID Of Your Target Audio Track
    """
        return self.videos.remove_sound_track_from_single_video(sound_id)


    # Audios APIs
    def get_single_channel_audios(self, channel_id: str = None, params: QueryParams = None):
        """
        Get a list of audios of a channel.

        Parameters:
            channel_id (str): The ID Of Your Target Channel
            params (QueryParams): A Optional Dictionary To Apply Some Changes
        """
        return self.audios.get_single_channel_audios(channel_id=channel_id, params=params)

    def remove_audio(self, audio_id: str = None):
        """
        Remove an audio.

        Parameters:
            audio_id (str): The ID Of Your Target Audio
        """
        return self.audios.remove_single_audio_from_channel(audio_id)

    def save_new_audio(self, channel_id: str = None, data: Audio = None):
        """
        Save a new audio.

        Parameters:
            channel_id (str): The ID Of Your Target Channel
            data (Video): The Audio Information's
        """
        return self.audios.save_file_as_audio(channel_id=channel_id, data=data)


    # Video Watermarks APIs
    def get_single_channel_watermarks(self, channel_id: str = None, params: QueryParams = None):
        """
        Get a list of watermarks of a channel.

        Parameters:
            channel_id (str): The ID Of Your Target Channel
            params (QueryParams): A Optional Dictionary To Apply Some Changes
        """
        return self.watermarks.get_single_channel_watermarks(channel_id=channel_id, params=params)

    def get_video_watermark(self, watermark_id: str = None):
        """
        Get a watermark.

        Parameters:
            watermark_id (str): The ID Of Your Target Video Watermark
        """
        return self.watermarks.get_single_watermark(watermark_id)

    def remove_video_watermark(self, watermark_id: str = None):
        """
        Remove a watermark.

        Parameters:
            watermark_id (str): The ID Of Your Target Video Watermark
        """
        return self.watermarks.remove_single_watermark_from_channel(watermark_id=watermark_id)

    def add_video_watermark(self, channel_id: str = None, watermark_file: str = None, data: Watermark = None):
        """
        Create a watermark.

        Parameters:
            channel_id (str): The ID Of Your Target Channel
            watermark_file (str): The Watermark File Path
            data (dict): Watermark Information
        """
        return self.watermarks.create_new_watermark_for_specific_channel(
            channel_id=channel_id,
            watermark_file=watermark_file,
            data=data
        )

    def update_video_watermark(self, watermark_id: str = None, data: Watermark = None):
        """
        Update a watermark.

        Parameters:
            watermark_id (str): The ID Of Your Target Video Watermark
            data (dict): Watermark Information
        """
        return self.watermarks.update_single_watermark(
            watermark_id=watermark_id,
            data=data,
        )


    # Live Watermarks APIs
    def get_live_watermarks(self, params: QueryParams = None):
        """
        Get a list of watermarks of a channel.

        Parameters:
            params (QueryParams): A Optional Dictionary To Apply Some Changes
        """
        return self.watermarks.get_all_live_watermarks(params=params)

    def get_live_watermark(self, watermark_id: str = None):
        """
        Get a watermark.

        Parameters:
            watermark_id (str): The ID Of Your Target Watermark
        """
        return self.watermarks.get_single_live_watermark(watermark_id=watermark_id)

    def remove_live_watermark(self, watermark_id: str = None):
        """
        Remove a watermark.

        Parameters:
            watermark_id (str): The ID Of Your Target Live Watermark
        """
        return self.watermarks.remove_single_live_watermark(watermark_id)

    def create_live_watermark(self, watermark_file: str = None, data: Watermark = None):
        """
        Create a watermark.

        Parameters:
            watermark_file (str): The Watermark File Path
            data (dict): Watermark Information
        """
        return self.watermarks.create_new_live_watermark(
            watermark_file=watermark_file,
            data=data,
        )

    def update_live_watermark(self, watermark_id: str = None, data: Watermark = None):
        """
        Update a watermark.

        Parameters:
            watermark_id (str): The ID Of Your Target Video Watermark
            data (dict): Watermark Information
        """
        return self.watermarks.update_single_live_watermark(
            watermark_id=watermark_id,
            data=data
        )


    # Profiles APIs
    def get_single_channel_profiles(self, channel_id: str = None, params: QueryParams = None):
        """
        Get a list of profiles of a channel.

        Parameters:
            channel_id (str): The ID Of Your Target Channel
            params (QueryParams): A Optional Dictionary To Apply Some Changes
        """
        return self.profiles.get_profiles(channel_id=channel_id, params=params)

    def remove_profile(self, profile_id: str = None):
        """
        Remove Single Channel Profile

        Parameters:
            profile_id (str): The ID Of Your Target Profile
        """
        return self.profiles.remove_single_profile_from_channel(profile_id)

    def get_media_profile(self, profile_id: str = None):
        """
        Get Single Media Profile

        Parameters:
            profile_id (str): The ID Of Your Target Profile
        """
        return self.profiles.get_single_profile(profile_id)

    def create_profile(self, channel_id: str = None, data: Profile = None):
        """
        Create a profile.

        Parameters:
            channel_id (str): The ID Of Your Target Channel
            data (dict): Profile Information's
        """
        return self.profiles.create_new_profile_for_channel(
            channel_id=channel_id,
            data=data
        )

    def update_profile(self, profile_id: str = None, data: Profile = None):
        """
        Update a profile.

        Parameters:
            profile_id (str): The ID Of Your Target Profile
            data (dict): Profile Information's
        """
        return self.profiles.update_single_profile(profile_id=profile_id, data=data)


    # Files APIs
    def get_single_channel_files( self, channel_id: str = None, params: QueryParams = None):
        """
        Get a list of files of a channel.

        Parameters:
            channel_id (str): The ID Of Your Target Channel
            params (QueryParams): A Optional Dictionary To Apply Some Changes
        """
        return self.files.get_files(channel_id=channel_id, params=params)

    def remove_file(self, file_id: str = None):
        """
        Remove a file.

        Parameters:
            file_id (str): The ID Of Your Target File
        """
        return self.files.remove_single_file_from_channel(file_id)

    def get_file(self, file_id: str = None):
        """
        Get a file.

        Parameters:
            file_id (str): The ID Of Your Target File
        """
        return self.files.get_single_file(file_id)

    def upload_single_file( self, channel_id: str = None, file_path: str = None):
        """
        Upload a file.

        Parameters:
            channel_id (str): The ID Of Your Target Channel
            file_path (str): The File Path
        """
        return self.files.create_new_file_for_specific_channel(
            channel_id=channel_id,
            file_path=file_path,
        )


    # Live Stream APIs
    def get_streams( self, params: QueryParams = None):
        """
        Get a list of streams

        Parameters:
            params (QueryParams): A Optional Dictionary To Apply Some Changes
        """
        return self.live.get_all_streams(params=params)

    def get_stream_info(self, stream_id: str = None):
        """
        Get a single stream

        Parameters:
            stream_id (str): A Target Stream ID
        """
        return self.live.get_single_stream(stream_id)

    def remove_stream(self, stream_id: str = None):
        """
        Remove a stream

        Parameters:
            stream_id (str): A Target Stream ID
        """
        return self.live.remove_single_stream(stream_id)

    def update_stream(self, stream_id: str = None, data: Stream = None):
        """
        Update a stream

        Parameters:
            stream_id (str): Target Stream ID
            data (Stream): Stream Data Information's
        """
        return self.live.update_single_stream(stream_id=stream_id, data=data)

    def create_stream(self, data: Stream = None,):
        """
        Create a stream

        Parameters:
            data (Stream): Stream Data Information's
        """
        return self.live.create_new_stream(data=data)

    def start_stream_record(self, stream_id: str = None):
        """
        Start a stream record

        Parameters:
            stream_id (str): Target Stream ID
        """
        return self.live.start_record_single_stream(stream_id)

    def stop_stream_record(self, stream_id: str = None):
        """
        Stop a stream record

        Parameters:
            stream_id (str): Target Stream ID
        """
        return self.live.stop_record_single_stream(stream_id)


    # Vads Channel APIs
    def get_vads_channels(self, params: QueryParams = None):
        """
        Get a list of VideoAds channels

        Parameters:
            params (QueryParams): A Optional Dictionary To Apply Some Changes
        """
        return self.channel.get_all_vads_channels(params=params)

    def get_vads_channel_info(self, channel_id: str = None):
        """
        Get a single vads channel

        Parameters:
            channel_id (str): The Target Channel ID
        """
        return self.channel.get_single_vads_channels(channel_id)

    def remove_vads_channel(self, channel_id: str = None):
        """
        Remove a VideoAds channel

        Parameters:
            channel_id (str): The Target Channel ID
        """
        return self.channel.remove_single_vads_channel(channel_id)

    def create_vads_channel(self, data: VadsChannel = None):
        """
        Create a vads channel

        Parameters:
            data (Stream): Stream Data Information's
        """
        return self.channel.create_single_vads_channel(data=data)

    def update_vads_channel(self, channel_id: str = None, data: VadsChannel = None):
        """
        Update a vads channel

        Parameters:
            channel_id (str): Target Channel ID
            data (Stream): Stream Data Information's
        """
        return self.channel.update_single_vads_channel(channel_id=channel_id, data=data)


    # Vads Campaign APIs
    def get_vads_channel_campaigns(self, channel_id: str = None, params: QueryParams = None):
        """
        Get a list of Video Ads campaigns

        Parameters:
            channel_id (str): An ADS Channel ID
            params (QueryParams): A Optional Dictionary To Apply Some Changes
        """
        return self.campaign.get_single_channel_campaigns(channel_id=channel_id, params=params)

    def get_campaign_info(self, campaign_id: str = None):
        """
        Get a single campaign

        Parameters:
            campaign_id (str): Target Campaign ID
        """
        return self.campaign.get_single_campaign_info(campaign_id)

    def remove_campaign(self, campaign_id: str = None):
        """
        Remove a campaign

        Parameters:
            campaign_id (str): Target Campaign ID
        """
        return self.campaign.remove_single_campaign(campaign_id)

    def create_campaign(self, channel_id: str = None, data: Campaign = None):
        """
        Create a campaign

        Parameters:
            channel_id (str): Target Channel ID
            data (Stream): Campaign Data Information's
        """
        return self.campaign.create_single_campaign(channel_id=channel_id, data=data)

    def update_campaign(self, campaign_id: str = None, data: Campaign = None):
        """
        Update a campaign

        Parameters:
            campaign_id (str): Target Campaign ID
            data (Stream): Campaign Data Information's
        """
        return self.campaign.update_single_campaign(campaign_id=campaign_id, data=data)


    # Vads Ads Campaign APIs
    def get_campaign_ads(self, campaign_id: str = None):
        """
        Get a list of ads

        Parameters:
            campaign_id (str): Target Campaign ID
        """
        return self.campaign.get_all_ads_inside_campaign(campaign_id)

    def get_campaign_ad_info(self, campaign_id: str = None, ad_id: str = None):
        """
        Get a single ad

        Parameters:
            campaign_id (str): Target Campaign ID
            ad_id (str): Campaign Ad's ID
        """
        return self.campaign.get_single_ad_in_single_campaign(
            campaign_id=campaign_id,
            ad_id=ad_id,
        )

    def remove_campaign_ad(self, campaign_id: str = None, ad_id: str = None):
        """
        Remove an ad from campaign

        Parameters:
            campaign_id (str): Target Campaign ID
            ad_id (str): Campaign Ad's ID

        """
        return self.campaign.remove_single_ad_from_single_campaign(
            campaign_id=campaign_id,
            ad_id=ad_id,
        )

    def create_campaign_ad(self, campaign_id: str = None, data: CampaignAd = None):
        """
        Create am ad

        Parameters:
            campaign_id (str): Target Campaign ID
            data (dict): Ad Information
        """
        return self.campaign.add_single_ad_to_single_campaign(
            campaign_id=campaign_id,
            data=data,
        )

    def update_campaign_ad(self, campaign_id: str = None, ad_id: str = None, data: CampaignAd = None):
        """
        Update an ad

        Parameters:
            campaign_id (str): Target Campaign ID
            ad_id (str): Target Ad ID
            data (dict): Ad Information
        """
        return self.campaign.update_single_ad_in_single_campaign(
            campaign_id=campaign_id,
            ad_id=ad_id,
            data=data,
        )


    # Vads Ads APIs
    def get_channels_ads(self, channel_id: str = None, params: QueryParams = None):
        """
        Get a list of ads

        Parameters:
            channel_id (str): An ADS Channel ID
            params (QueryParams): A Optional Dictionary To Apply Some Changes
        """
        return self.ads.get_all_channel_ads(channel_id=channel_id, params=params)

    def get_ad_info(self, ad_id: str = None):
        """
        Get a single ad Info

        Parameters:
            ad_id (str): Target Ad ID
        """
        return self.ads.get_single_ad(ad_id)

    def remove_ad(self, ad_id: str = None):
        """
        Remove an ad

        Parameters:
            ad_id (str): Target Ad's ID
        """
        return self.ads.remove_single_ad(ad_id)

    def update_ad(self, ad_id: str = None, data: Ad = None):
        """
        Update an ad

        Parameters:
            ad_id (str): Target Ad ID
            data (dict): Ad Information
        """
        return self.ads.update_single_ad(ad_id, data)

    def create_ad(self, channel_id: str = None, data: Ad = None):
        """
        Create a ad

        Parameters:
            channel_id (str): Target Channel ID
            data (dict): Ad Information
        """
        return self.ads.create_single_ad(channel_id, data)
