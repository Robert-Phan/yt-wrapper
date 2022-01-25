from typing import Literal
from ..resources.PlaylistItemResources import PlaylistItemResource, PlaylistItemListResponse
from googleapiclient.discovery import Resource

# the type used in the `part` parameter in class methods
PlaylistItemPartType = Literal["content_details", "id", 
                               "snippet", "status"] | list[
                                   Literal["content_details", "id", 
                                           "snippet", "status"]]
# TODO: Add in all the params I missed.
class PlaylistItem:
    """Contains request methods for the `PlaylistItem` resource."""
    def __init__(self, client: Resource) -> None:
        self.client: Resource = client
        
    def list(self, *, part: PlaylistItemPartType, 
             id: str|list[str] = None, playlist_id: str = None,
             max_results: int = 5, page_token: str = "",
             video_id: str = ""
             ):
        """
        Return a collection of playlist items that match the parameters.
        For more info, visit\
[Google's official documentation](https://developers.google.com/youtube/v3/docs/playlistItems/list)
        """
        if len([x for x in (playlist_id, id) if x != None]) != 1: 
            raise Exception("No/too many filters specified.")

        if type(part) == list:
            part = ",".join(part)
        if type(id) == list:
            id = ",".join(part)
        
        req = self.client.playlistItems()\
        .list(part=part, 
              playlistId=playlist_id, id=id,
              maxResults=max_results, pageToken=page_token,
              videoId=video_id)
        
        return PlaylistItemListResponse.init(req.execute())

    def insert(self, *, body: PlaylistItemResource, part: PlaylistItemPartType):
        """
        Adds a resource to a playlist.
        For more info, visit\
[Google's official documentation](https://developers.google.com/youtube/v3/docs/playlistItems/insert)
        """
        if not (body.snippet.playlist_id and body.snippet.resource_id): 
            raise Exception("Playlist Id and Resource Id not provided")
        
        request_body = {
            "snippet": {
                "playlistId": body.snippet.playlist_id,
                "position": body.snippet.position,
                "resourceId": {
                    "kind": "youtube#video",
                    "videoId": body.snippet.resource_id.video_id,
                }
            }
        }
        
        if "content_details" in part:
            request_body["contentDetails"] = {}
            request_body["contentDetails"]["note"] = body.content_details.note

        req = self.client.playlistItems().insert(body=request_body, part=part)
        res = PlaylistItemResource._from_resource_dict(req.execute())
        return res
    
    def update(self, *, body: PlaylistItemResource, part: PlaylistItemPartType):
        """
        Modifies a playlist item. For example, you could update the item's position in the playlist.
        For more info, visit\
[Google's official documentation](https://developers.google.com/youtube/v3/docs/playlistItems/update)
        """
        if not (body.snippet.playlist_id and body.snippet.resource_id ):
            raise Exception(
                "`snippet.playlist_id`, and `snippet.resource_id` properties not provided"
                )
        
        request_body = {
            "snippet": {
                "playlistId": body.snippet.playlist_id,
                "resourceId": {
                    "kind": "youtube#video",
                    "videoId": body.snippet.resource_id.video_id
                },
                "position": body.snippet.position
            }
        }

        if "content_details" in part:
            request_body["contentDetails"] = {}
            request_body["contentDetails"]["note"] = body.content_details.note
            
        req = self.client.playlistItems().insert(body=request_body, part=part)
        res = PlaylistItemResource._from_resource_dict(req.execute())
        return res
    
    def delete(self, id:str):
        """
        Deletes a playlist item.
        For more info, visit\
[Google's official documentation](https://developers.google.com/youtube/v3/docs/playlistItems/update)
        """
        request = self.client.playlistItems().delete(
            id=id
        )
        request.execute()
        