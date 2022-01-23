"""Class representations of the `PlaylistItem` resource."""

from dataclasses import dataclass
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
    resource_id = ResourceId()

@dataclass
class ContentDetails:
    video_id: str = None
    note: str = None
    video_published_at: str = None
    
@dataclass
class Status:
    privacy_status: str = None
    

class PlaylistItemResource:
    """
    The class representation for the `PlaylistItem` JSON resource during request bodies and responses.
    """
    def __init__(self) -> None:
        self.id: str = None
        self.etag: str = None
        self.kind = "youtube#playlistItem"
        
        # ? Some of these attrs are init as None, whilst some are init as a class.
        # ? This is becaause those that are init as a class are intended to be assigned by users
        # ? when they use the insert or any other methods that needs to provide a resource body.
        self.snippet = Snippet()
        self.content_details = ContentDetails()
        self.status: Status = None
    
    @classmethod
    def _from_resource_dict(cls, resource: dict):
        """
        Creates a resource from a returned resource dictionary.
        """
        inst = cls()
        inst.id = resource['id']
        inst.etag = resource['etag']
        
        # * assigns the attrs snippet, status, contentDetails
        # * the program has to check whether the props got requested or not
        # * in the case that the user didn't request them in the `part` param
        
        snippet: dict = resource.get('snippet')
        if snippet != None:
            # goes through all of the simple attrs and assign them
            snippetAttrs = ['publishedAt', 'title', 'description', 
                            'channelTitle', 'channelId',
                            'videoOwnerChannelTitle', 'videoOwnerChannelId',
                            'playlistId', 'position']
            for x in snippetAttrs:
                inst.snippet.__setattr__(camel_snake_converter(x),
                                         snippet.get(x))
            
            # goes through the thumbnails to assign them 
            for x in ['default', 'medium', 'high', 'standard', 'maxres']:
                key = ThumbnailKey()
                key.url = snippet["thumbnails"].get(x, {}).get("url")
                key.height = snippet["thumbnails"].get(x, {}).get("height")
                key.width = snippet["thumbnails"].get(x, {}).get("width")
                inst.snippet.thumbnails.__setattr__(x, key)
            
            inst.snippet.resource_id.kind = snippet["resourceId"]["kind"]
            inst.snippet.resource_id.video_id = snippet["resourceId"]["videoId"]
        else: inst.snippet = None
        
        content_details: dict = resource.get("contentDetails")
        if content_details != None:
            for x in ["videoId", "note", "videoPublishedAt"]:
                inst.content_details.__setattr__(camel_snake_converter(x),
                                                 content_details.get(x))
        else: inst.content_details = None
        
        if "status" in resource:
            inst.status.privacy_status = resource.get("status").get("privacyStatus")
        
        return inst

@dataclass
class PageInfo:
    total_results: int
    results_per_page: int

class PlaylistItemListResponse:
    """The response of a `list` method from the `PlaylistItem` class."""
    def __init__(self, response: dict) -> None:
        self.kind = "youtube#playlistListResponse"
        self.etag = response["etag"]
        
        self.next_page_token: str = response.get("nextPageToken")
        self.prev_page_token: str = response.get("prevPageToken")
        
        self.page_info = PageInfo(response["pageInfo"]["totalResults"],
                                  response["pageInfo"]["resultsPerPage"])
        
        self.items: list[PlaylistItemResource] = [PlaylistItemResource._from_resource_dict(x) 
                                              for x in response["items"]]
    
    