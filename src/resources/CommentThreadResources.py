"""Class representations of the `CommentThread` resource."""

from dataclasses import dataclass
from .utils import ResponseResourceBase
from .CommentResources import CommentResource

@dataclass
class Snippet:
    channel_id: str = None
    video_id: str = None
    top_level_comment: CommentResource = CommentResource()
    can_reply: bool = None
    total_reply_count: int = None 
    is_public: bool = None
    
@dataclass
class Replies:
    comments: list[CommentResource] = None
    
@dataclass
class CommentThreadResource(ResponseResourceBase):
    id: str = None
    snippet: Snippet = Snippet()
    replies: Replies = None

@dataclass
class PageInfo:
    total_results: int = None
    results_per_page: int = None
    
@dataclass
class CommentThreadListResponse(ResponseResourceBase):
    next_page_token: str = None
    prev_page_token: str = None
    page_info: PageInfo = None
    items: list[CommentThreadResource] = None
