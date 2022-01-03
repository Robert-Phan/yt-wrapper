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
        self.id: str = None
        self.etag: Any = None
        self.kind = "youtube#playlist"

        self.snippet = Snippet()
        
        self.status = Status()
        self.content_details = ContentDetails()
        self.player = Player()
        pass
    
    @classmethod
    def _from_resource_dict(cls, resource: dict):
        inst = cls()
        inst.id = resource["id"]
        inst.etag = resource["etag"]
        inst.kind = "youtube#playlist"
        
        snippet = resource.get("snippet")
        if snippet != None:
            thumbnails = Thumbnails()
            for x in ['default', 'medium', 'high', 'standard', 'maxres']:
                key = ThumbnailKey()
                key.url = snippet["thumbnails"].get(x, {}).get("url")
                key.height = snippet["thumbnails"].get(x, {}).get("height")
                key.width = snippet["thumbnails"].get(x, {}).get("width")
                thumbnails.__setattr__(x, key)
            inst.snippet.thumbnails =  thumbnails
            
            inst.snippet.published_at =  snippet["publishedAt"]
            inst.snippet.channel_id =  snippet["channelId"]
            inst.snippet.title =  snippet["title"]
            inst.snippet.description =  snippet["description"]
            inst.snippet.channel_title =  snippet["channelTitle"]
            inst.snippet.default_language =  snippet.get("defaultLanguage")

            local = Localized()
            local.title = snippet["localized"]["title"]; 
            local.description = snippet["localized"]["description"]
            inst.snippet.localized = local
            
        inst.status = Status(resource.get("status", {}).get("privacyStatus"))
        inst.content_details = ContentDetails(resource.get("contentDetails", {}).get("itemCount"))
        inst.player = Player(resource.get("player", {}).get("embedHtml"))
        
        return inst

@dtcls
class PageInfo:
    total_results: int
    results_per_page: int

class PlaylistListReponse:
    def __init__(self, response: dict) -> None:
        self.kind = "youtube#playlistListResponse"
        self.etag = response["etag"]
        
        self.next_page_token: str = response.get("nextPageToken")
        self.prev_page_token: str = response.get("prevPageToken")
        
        self.page_info = PageInfo(response["pageInfo"]["totalResults"],
                                  response["pageInfo"]["resultsPerPage"])
        
        self.items: list[PlaylistResource] = [PlaylistResource._from_resource_dict(x) 
                                              for x in response["items"]]

