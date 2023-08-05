from typing import TypedDict, Optional


class QueryParams(TypedDict):
    filter: Optional[str]
    page: Optional[int]
    per_page: Optional[int]
