from typing import Literal
from ..resources.PlaylistResource import PlaylistListReponse, PlaylistResource
from googleapiclient.discovery import Resource

PlaylistPartType = Literal["content_details", "id", "localizations", 
            "player", "snippet", "status"] | list[
                Literal["content_details", "id", "localizations", 
                        "player", "snippet", "status"]]
        
class Playlist:
    def __init__(self, client: Resource) -> None:
        self.client = client
    
    def list(self, *, part: PlaylistPartType,
             channel_id : str = None, id: list[str] | str = None, mine: bool = None,
             max_results: int = 5, page_token: str = ""
             ):
        """
        Returns a collection of playlists. 
        """
        if len([x for x in (channel_id, id, mine) if x != None]) != 1: 
            raise Exception("No/too many filters specified.")
        
        if type(part) == list:
            part = ",".join(part)
        
        response = self.client.playlists().list(part=part,
                                     channelId=channel_id,
                                     id=id,
                                     mine=mine,
                                     maxResults=max_results,
                                     pageToken=page_token).execute()
        return PlaylistListReponse(response)
    
    def insert(self, body: PlaylistResource, *, part: PlaylistPartType):
        if not body.snippet.title: raise Exception("Playlist title not provided")
        request_body = {
            "snippet": {
                "title": body.snippet.title,
                "description": body.snippet.description
            }
        }
        
        if type(part) == list:
            part = ",".join(part)
        
        req = self.client.playlists().insert(body=request_body, part=part)
        res = PlaylistResource()
        res._from_resource_dict(req.execute())
        
        return res
        ...
    
