from dataclasses import dataclass as dtcls
from typing import  Any

@dtcls
class Key:
    url: str
    width: int
    height: int
    
class Thumbnails:
    def __init__(self, thumbnails: dict[str, Key]) -> None:
        self.__thumbnails = thumbnails
    
    def __getitem__(self, index: str):
        return self.__thumbnails[index]

@dtcls
class Localized:
    title: str
    string: str
    
@dtcls
class Snippet:
    published_at: str
    channel_id: str
    title: str
    description: str
    thumbnails: Thumbnails
    channel_title: str
    default_language: str
    localized: Localized
    
@dtcls
class Status:
    privacy_status: str
    
@dtcls
class ContentDetails:
    item_count: str
    
@dtcls
class Player:
    embed_html: str

class PlaylistResource:
    def __init__(self, resource: dict) -> None:
        self.id: str = resource["id"]
        self.etag: Any = resource["etag"]
        self.kind = "youtube#playlist"
        
        
        thumbnails = Thumbnails({k: Key(v["url"], v["width"], v["height"]) 
                                 for (k, v) in resource["snippet"]["thumbnails"].items()})
        
        self.snippet = Snippet(resource["snippet"]["publishedAt"], 
                               resource["snippet"]["channelId"],
                               resource["snippet"]["title"], 
                               resource["snippet"]["description"],
                               thumbnails, 
                               resource["snippet"]["channelTitle"], 
                               resource["snippet"]["defaultLanguage"] 
                               if "defaultLanguage" in resource["snippet"] else None,
                               Localized(
                                   resource["snippet"]["localized"]["title"],
                                   resource["snippet"]["localized"]["description"]
                               ))
        self.status = Status(resource["status"]["privacy_status"] 
                             if "status" in resource else None)
        self.content_details = ContentDetails(resource["contentDetails"]["itemCount"])
        self.player = Player(resource["player"]["embedHtml"]
                             if "player" in resource else None)

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
        self.items = [PlaylistResource(x) for x in response["items"]]
        pass
    

