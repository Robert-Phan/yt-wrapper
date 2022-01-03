from typing import Literal
from ..resources.PlaylistItemsResource import PlaylistItemResource, PlaylistItemListResponse
from googleapiclient.discovery import Resource

PlaylistItemPartType = Literal["content_details", "id", 
                               "snippet", "status"] | list[
                                   Literal["content_details", "id", 
                                           "snippet", "status"]]
                               
class PlaylistItem:
    def __init__(self, client: Resource) -> None:
        self.client: Resource = client
        
    def list(self, *, part: PlaylistItemPartType, 
             id: str = None, playlist_id: str = None,
             max_results: int = 5, page_token: str = "",
             video_id: str = ""
             ):
        
        if len([x for x in (playlist_id, id) if x != None]) != 1: 
            raise Exception("No/too many filters specified.")

        if type(part) == list:
            part = ",".join(part)
        
        req = self.client.playlistItems()\
        .list(part=part, 
              playlistId=playlist_id, id=id,
              maxResults=max_results, pageToken=page_token,
              videoId=video_id)
        
        return PlaylistItemListResponse(req.execute())

        ...
    ...