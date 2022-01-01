from dataclasses import dataclass as dtcls
from typing import  Any

@dtcls
class ThumbnailKey:
    url: str = None
    width: int = None
    height: int = None

@dtcls
class Thumbnails:
    default : ThumbnailKey = None
    medium : ThumbnailKey = None
    high : ThumbnailKey = None
    standard : ThumbnailKey = None
    maxres : ThumbnailKey = None

@dtcls
class Localized:
    title: str = None
    description: str = None
    
@dtcls
class Snippet:
    published_at: str = None
    channel_id: str = None
    title: str = None
    description: str = None
    thumbnails: Thumbnails = None
    channel_title: str = None
    default_language: str = None
    localized: Localized = None
    
@dtcls
class Status:
    privacy_status: str = None
    
@dtcls
class ContentDetails:
    item_count: int = 0
    
@dtcls
class Player:
    embed_html: str = None

class PlaylistResource:
    """Represents a Playlist resource."""
    def __init__(self) -> None:
        self.id: str = ""
        self.etag: Any = None
        self.kind = "youtube#playlist"

        
        self.snippet = Snippet()
        self.snippet.published_at = None 
        self.snippet.channel_id = None 
        self.snippet.title = None
        self.snippet.description = None
        self.snippet.thumbnails =  ThumbnailKey()
        self.snippet.channel_title = None
        self.snippet.default_language = None

        self.snippet.localized = Localized()
        
        self.status = Status()
        self.content_details = ContentDetails()
        self.player = Player()
        pass
    
    def _from_resource_dict(self, resource: dict) -> None:
        self.id: str = resource["id"]
        self.etag: Any = resource["etag"]
        self.kind = "youtube#playlist"
        
        thumbnails = Thumbnails()
        for x in ['default', 'medium', 'high', 'standard', 'maxres']:
            key = ThumbnailKey()
            key.url = resource["snippet"]["thumbnails"].get(x, {}).get("url")
            key.height = resource["snippet"]["thumbnails"].get(x, {}).get("height")
            key.width = resource["snippet"]["thumbnails"].get(x, {}).get("width")
            thumbnails.__setattr__(x, key)
        self.snippet.thumbnails =  thumbnails
        
        self.snippet = Snippet()
        self.snippet.published_at =  resource["snippet"]["publishedAt"]
        self.snippet.channel_id =  resource["snippet"]["channelId"]
        self.snippet.title =  resource["snippet"]["title"]
        self.snippet.description =  resource["snippet"]["description"]
        self.snippet.channel_title =  resource["snippet"]["channelTitle"]
        self.snippet.default_language =  resource["snippet"].get("defaultLanguage")

        local = Localized()
        local.title = resource["snippet"]["localized"]["title"]; 
        local.description = resource["snippet"]["localized"]["description"]
        self.snippet.localized = local
        
        self.status = Status(resource.get("status", {}).get("privacy_status"))
        self.content_details = ContentDetails(resource.get("contentDetails", {}).get("itemCount"))
        self.player = Player(resource.get("player", {}).get("embedHtml"))

@dtcls
class PageInfo:
    total_results: int
    results_per_page: int

class PlaylistListReponse:
    def __init__(self, response: dict) -> None:
        self.kind = "youtube#playlistListResponse"
        self.etag = response["etag"]
        
        self.next_page_token: str = response["nextPageToken"] if "nextPageToken" in response else None
        self.prev_page_token: str = response["prevPageToken"] if "prevPageToken" in response else None
        
        self.page_info = PageInfo(response["pageInfo"]["totalResults"],
                                  response["pageInfo"]["resultsPerPage"])
        
        self.items: list[PlaylistResource] = []
        for x in response["items"]:
            g = PlaylistResource()
            g._from_resource_dict(x)
            self.items.append(g)
            


