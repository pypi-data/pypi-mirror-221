from typing import TypedDict, Optional


class Channel(TypedDict):
    title: str
    description: Optional[str]
    secure_link_enabled: Optional[bool]
    secure_link_key: Optional[str]
    secure_link_with_ip: Optional[bool]
    ads_enabled: Optional[bool]
    present_type: Optional[str]
    campaign_id: Optional[str]
