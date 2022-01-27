"""Class representations of the `PlaylistItem` resource."""

from dataclasses import dataclass
from .utils import ResponseResourceBase

@dataclass
class ThumbnailKey:
    url: str = None
    width: int = None
    height: int = None

@dataclass
class Thumbnails:
    default: ThumbnailKey = None
    medium: ThumbnailKey = None
    high: ThumbnailKey = None
    standard: ThumbnailKey = None
    maxres: ThumbnailKey = None
    
@dataclass
class ResourceId:
    kind: str = None
    video_id: str = None

@dataclass
class Snippet:
    published_at: str = None
    channel_id: str = None
    title: str = None
    description: str = None
    thumbnails: Thumbnails = None
    channel_title: str = None
    video_owner_channel_title: str = None
    video_owner_channel_id: str = None
    playlist_id: str = None
    position: int = None
    resource_id: ResourceId = ResourceId()

@dataclass
class ContentDetails:
    video_id: str = None
    note: str = None
    video_published_at: str = None
    
@dataclass
class Status:
    privacy_status: str = None
    
@dataclass
class PlaylistItemResource(ResponseResourceBase):
    id: str = None
    
    snippet: Snippet = Snippet()
    content_details: ContentDetails = ContentDetails()
    status: Status = None
    
@dataclass
class PageInfo:
    total_results: int = None
    results_per_page: int = None
    
@dataclass
class PlaylistItemListResponse(ResponseResourceBase):
    next_page_token: str = None
    prev_page_token: str = None
    page_info: PageInfo = None
    items: list[PlaylistItemResource] = None
