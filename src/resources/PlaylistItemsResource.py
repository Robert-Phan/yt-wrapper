from dataclasses import dataclass as dtcls

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
class ResourceId:
    kind: str = None
    video_id: str = None

@dtcls
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
    resource_id: ResourceId = None

@dtcls
class ContentDetails:
    video_id: str = None
    note: str = None
    video_published_at: str = None
    
@dtcls
class Status:
    privacy_status: str = None
    

class PlaylistItemResource:
    def __init__(self) -> None:
        self.id: str = None
        self.etag: str = None
        self.kind = "youtube#playlistItem"
        
        self.snippet = Snippet()
        self.content_details = ContentDetails()
        self.status = Status()
    
    @classmethod
    def _from_resource_dict(cls, resource: dict):
        inst = cls()
        inst.id = resource['id']
        inst.etag = resource['etag']
        
        snippet = resource.get('snippet')
        if snippet != None:
            thumbnails = Thumbnails()
            for x in ['default', 'medium', 'high', 'standard', 'maxres']:
                key = ThumbnailKey()
                key.url = snippet["thumbnails"].get(x, {}).get("url")
                key.height = snippet["thumbnails"].get(x, {}).get("height")
                key.width = snippet["thumbnails"].get(x, {}).get("width")
                thumbnails.__setattr__(x, key)
            inst.snippet.thumbnails =  thumbnails
            
            inst.snippet.published_at = snippet['publishedAt']
            inst.snippet.channel_id = snippet['channelId']
            inst.snippet.title = snippet['title']
            inst.snippet.description = snippet['description']
            inst.snippet.channel_title = snippet['channelTitle']
            inst.snippet.video_owner_channel_title = snippet['videoOwnerChannelTitle']
            inst.snippet.video_owner_channel_id = snippet['videoOwnerChannelId']
            inst.snippet.playlist_id = snippet['playlistId']
            inst.snippet.position = snippet['position']
            
            resource_id = ResourceId()
            resource_id.kind = snippet["resourceId"]["kind"]
            resource_id.video_id = snippet["resourceId"]["videoId"]
            inst.snippet.resource_id = resource_id
            
        
        content_details = resource.get("contentDetails")
        if content_details != None:
            
            inst.content_details.video_id = content_details["videoId"]
            inst.content_details.note = content_details["note"]
            inst.content_details.video_published_at = content_details["videoPublisedAt"]
            
        inst.status = resource.get("status", {}).get("privacyStatus")
        return inst

@dtcls
class PageInfo:
    total_results: int
    results_per_page: int

class PlaylistItemListResponse:
    def __init__(self, response: dict) -> None:
        self.kind = "youtube#playlistListResponse"
        self.etag = response["etag"]
        
        self.next_page_token: str = response.get("nextPageToken")
        self.prev_page_token: str = response.get("prevPageToken")
        
        self.page_info = PageInfo(response["pageInfo"]["totalResults"],
                                  response["pageInfo"]["resultsPerPage"])
        
        self.items: list[PlaylistItemResource] = [PlaylistItemResource._from_resource_dict(x) 
                                              for x in response["items"]]
    
    