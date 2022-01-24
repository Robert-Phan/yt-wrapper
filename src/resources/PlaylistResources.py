"""Class representations of the `Playlist` resource."""

from dataclasses import dataclass
from typing import Any
from .utils import camel_snake_converter 

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
    localized = Localized()
    
@dataclass
class Status:
    privacy_status: str = None
    
@dataclass
class ContentDetails:
    item_count: int = None
    
@dataclass
class Player:
    embed_html: str = None

class PlaylistResource:
    """
    The class representation for the `Playlist` JSON resource during request bodies and responses.
    """    
    def __init__(self) -> None:
        self.id: str = None
        self.etag: Any = None
        self.kind = "youtube#playlist"
        
        # ? Some of these attrs are init as None, whilst some are init as a class.
        # ? This is becaause those that are init as a class are intended to be assigned by users
        # ? when they use the insert or any other methods that needs to provide a resource body.
        self.snippet = Snippet()
        self.status = Status()
        self.content_details: ContentDetails = None
        self.player: Player = None 
        pass
    
    @classmethod
    def _from_resource_dict(cls, resource: dict):
        """
        Creates a resource from a returned resource dictionary.
        """
        inst = cls()
        inst.id = resource["id"]
        inst.etag = resource["etag"]
        inst.kind = "youtube#playlist"
        
        # * assigns the attrs snippet, status, contentDetails, and player
        # * the program has to check whether the props got requested or not
        # * in the case that the user didn't request them in the `part` param
        
        snippet: dict = resource.get("snippet")
        if snippet != None:
            # goes through all of the simple attrs and assign them
            snippetAttrs = ["publishedAt", "channelId", "title", "description", 
                            "defaultLanguage"]
            for x in snippetAttrs:
                inst.snippet.__setattr__(camel_snake_converter(x), snippet.get(x))

            # goes through the thumbnails to assign them 
            thumbnails = Thumbnails()
            for x in ['default', 'medium', 'high', 'standard', 'maxres']:
                key = ThumbnailKey()
                key.url = snippet["thumbnails"].get(x, {}).get("url")
                key.height = snippet["thumbnails"].get(x, {}).get("height")
                key.width = snippet["thumbnails"].get(x, {}).get("width")
                thumbnails.__setattr__(x, key)
            inst.snippet.thumbnails =  thumbnails
            
            inst.snippet.localized.title = snippet["localized"]["title"]; 
            inst.snippet.localized.description = snippet["localized"]["description"]
        else: inst.snippet = None
        
        if "status" in resource:
            inst.status.privacy_status = resource.get("status").get("privacyStatus")
        else: inst.status = None
        
        if "contentDetails" in resource:
            inst.content_details.item_count = resource.get("contentDetails").get("itemCount")
        if "player" in resource:
            inst.player.embed_html = resource.get("player").get("embedHtml")
        
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

