from typing import TypedDict, Optional


class Video(TypedDict):
    title: str
    description: Optional[str]
    video_url: Optional[str]
    file_id: Optional[str]
    convert_mode: Optional[str]
    profile_id: Optional[str]
    parallel_convert: Optional[bool]
    thumbnail_time: Optional[int]
    watermark_id: Optional[str]
    watermark_area: Optional[str]
    convert_info: Optional[list]
