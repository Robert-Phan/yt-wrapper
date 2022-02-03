from typing import Literal
from ..resources.ChannelResources import ChannelResource, ChannelListResponse
from googleapiclient.discovery import Resource

ChannelPartType = Literal["auditDetails",
    "brandingSettings", "contentDetails",
    "contentOwnerDetails", "id",
    "localizations", "snippet",
    "statistics", "status",
    "topicDetails"
] | list[
    Literal["auditDetails",
        "brandingSettings", "contentDetails",
        "contentOwnerDetails", "id",
        "localizations", "snippet",
        "statistics", "status",
        "topicDetails"
    ]
]

class Channel:
    def __init__(self, client: Resource) -> None:
        self.client: Resource = client
    
    def list(self, *, part: ChannelPartType,
             for_username: str = None, id: str|list[str] = None, managed_by_me: bool = None, mine: bool = None,
             max_results: int = None, page_token: str = None, 
             on_behalf_of_content_owner: str = None):
        """
        Returns a collection of zero or more `channel` resources that match the request criteria.
        For more info, visit\
        [Google's official documentation](https://developers.google.com/youtube/v3/docs/comments/list)
        """
        
        if len([x for x in (for_username, id, managed_by_me, mine) if x != None]) != 1: 
            raise Exception("No/too many filters specified.")

        if type(part) == list:
            part = ",".join(part)
        if type(id) == list:
            id = ",".join(id)
        
        req = self.client.channels().list(
            part=part,
            forUsername=for_username, id=id, managedByMe=managed_by_me, mine=mine,
            maxResults=max_results, pageToken=page_token,
            onBehalfOfContentOwner=on_behalf_of_content_owner
        )
        
        return ChannelListResponse._from_response_dict(req.execute())
        
