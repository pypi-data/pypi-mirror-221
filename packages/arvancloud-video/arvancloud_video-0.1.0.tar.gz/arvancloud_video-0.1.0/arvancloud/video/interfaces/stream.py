from typing import TypedDict, Optional


class Stream(TypedDict):
    title: str
    description: Optional[str]
    type: str
    mode: str
    input_url: Optional[str]
    slug: str
    timeshift: Optional[str]
    fps_mode: Optional[str]
    fps: int
    archive_enabled: Optional[bool]
    catchup_enabled: Optional[bool]
    catchup_period: Optional[int]
    archive_mode: Optional[str]
    channel_id: Optional[str]
    watermark_id: Optional[str]
    watermark_area: Optional[str]
    convert_info: list
    secure_link_enabled: Optional[bool]
    secure_link_key: Optional[str]
    secure_link_with_ip: Optional[bool]
    ads_enabled: Optional[bool]
    present_type: Optional[str]
    campaign_id: Optional[str]
