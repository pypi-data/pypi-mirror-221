from typing import TypedDict, Optional


class Campaign(TypedDict):
    title: str
    description: Optional[str]
    skip_type: str
    skip_offset: Optional[int]
    active: Optional[bool]
