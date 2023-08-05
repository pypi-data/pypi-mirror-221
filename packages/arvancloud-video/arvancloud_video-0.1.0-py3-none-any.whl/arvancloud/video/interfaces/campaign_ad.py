from typing import TypedDict, Optional


class CampaignAd(TypedDict):
    ad_id: str
    weight: int
    filter_device: Optional[list]
    filter_browser: Optional[list]
    filter_platform: Optional[list]
    quota: Optional[list]
    quota_type: Optional[str]
