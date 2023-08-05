from typing import TypedDict, Optional


class Profile(TypedDict):
    title: str
    description: Optional[str]
    convert_mode: str
    thumbnail_time: Optional[int]
    watermark_id: Optional[str]
    watermark_area: Optional[str]
    convert_info: Optional[list]
