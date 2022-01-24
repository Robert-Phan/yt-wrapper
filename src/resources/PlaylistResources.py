"""Class representations of the `Playlist` resource."""

from dataclasses import dataclass
from typing import Any
from .utils import camel_snake_converter, assign_resource_dict_to_class

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
class Localized:
    title: str = None
    description: str = None
    
@dataclass
class Snippet:
    published_at: str = None
    channel_id: str = None
    title: str = None
    description: str = None
    thumbnails: Thumbnails = None
    channel_title: str = None
    default_language: str = None
    localized: Localized = Localized()
    
@dataclass
class Status:
    privacy_status: str = None
    
@dataclass
class ContentDetails:
    item_count: int = None
    
@dataclass
class Player:
    embed_html: str = None

@dataclass
class PlaylistResource:
    """
    The class representation for the `Playlist` JSON resource during request bodies and responses.
    """    
    id: str = None
    kind: str = "youtube#playlist"
    etag: str = None
    
    content_details: ContentDetails = None
    player: Player = None 
    snippet: Snippet = Snippet()
    status: Status = Status()

    @classmethod
    def _from_resource_dict(cls, resource: dict):
        """
        Creates a resource from a returned resource dictionary.
        """
        inst = assign_resource_dict_to_class(resource, cls)
        return inst

@dataclass
class PageInfo:
    total_results: int
    results_per_page: int

class PlaylistListReponse:
    """The response of a `list` method from the `Playlist` class."""
    def __init__(self, response: dict) -> None:
        self.kind = "youtube#playlistListResponse"
        self.etag = response["etag"]
        
        self.next_page_token: str = response.get("nextPageToken")
        self.prev_page_token: str = response.get("prevPageToken")
        
        self.page_info = PageInfo(response["pageInfo"]["totalResults"],
                                  response["pageInfo"]["resultsPerPage"])
        
        self.items: list[PlaylistResource] = [PlaylistResource._from_resource_dict(x) 
                                              for x in response["items"]]

