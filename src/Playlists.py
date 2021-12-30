from dataclasses import dataclass as dtcls
from typing import Literal, Union, Any
from PlaylistResource import PlaylistListReponse
from googleapiclient.discovery import Resource

PlaylistPartType = Union[Literal["content_details", "id", "localizations",
                                "player", "snippet", "status"], 
                    list[Literal["content_details", "id", "localizations",
                                "player", "snippet", "status"]]]
        

class Playlist:
    def __init__(self, client: Resource) -> None:
        self.client = client
    
    def list(self, *, part: PlaylistPartType,
             channel_id : str = None, id: Union[list[str], str] = None, mine: bool = None,
             max_results: int = 5, page_token: str = ""
             ):
        """
        Returns a collection of playlists. 
        More at the [official documentation](https://developers.google.com/youtube/v3/docs/playlists/list).
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
    
