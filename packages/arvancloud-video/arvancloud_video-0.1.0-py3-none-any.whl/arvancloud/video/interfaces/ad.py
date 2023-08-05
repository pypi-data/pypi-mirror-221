from typing import TypedDict, Optional


class Ad(TypedDict):
    title: str
    description: Optional[str]
    ad_type: str
    skip_type: str
    skip_offset: Optional[int]
    click_through: str
