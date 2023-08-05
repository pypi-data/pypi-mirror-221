from typing import TypedDict, Optional


class Audio(TypedDict):
    title: str
    description: Optional[str]
    audio_url: Optional[str]
    file_id: Optional[str]
    convert_mode: str
    profile_id: Optional[str]
    parallel_convert: Optional[bool]
    convert_info: Optional[list]
