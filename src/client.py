import os
import pickle
import Playlists

import google_auth_oauthlib.flow
import googleapiclient.discovery
from googleapiclient.discovery import Resource
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

class Client:
    def __init__(self) -> None:
        self.client: Resource = ...
        
    def init_resources(self):
        self.playlist = Playlists.Playlist(self.client)
        
    def _fetch_new_creds(self, client_secrets_file: str, scopes: list[str], token_store: str):
        """Fetches new credentials"""
        
        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
        credentials = flow.run_console()
        
        # Saves the credentials for the next run
        with open(token_store, 'wb') as f:
            print('Saving Credentials for Future Use...')
            pickle.dump(credentials, f)
                
        return credentials
    
    @classmethod
    def from_client_secrets(cls, client_secrets_file: str, scopes: list[str], 
                            token_store: str = "token.pickle"):
        """
        Returns a youtube client.\n
        Parameters:
            `client_secrets_file`: the path to your client secrets file. 
            `scopes`: the scopes of this client.
            `token_store`: the file the program will use to store credentials for later use.
        Returns:
            An instance of the Youtube client, with OAuth2 access.
        """
        
        inst = cls()
        
        credentials: Credentials = ...
        # * Fetches stored credentials
        if os.path.exists(token_store):
            print("Loading credentials from file...")
            with open(token_store, 'rb') as token:
                credentials = pickle.load(token)
        
        # * Tries to refresh creds/get new creds if expired
        if not credentials or not credentials.valid:
            if credentials and credentials.expired and credentials.refresh_token:
                print('Refreshing acess token...')
                # try:
                request = Request()
                credentials.refresh(request)
                print("Access token refreshed!")
                # except:
                #     print("Refresh token expired!")
                #     credentials = fetch_new_creds(client_secrets_file, scopes)
            else:
                print("Fetching new credentials...")
                credentials = inst._fetch_new_creds(client_secrets_file, scopes)
                print("New credentails fetched!")
        
        youtube = googleapiclient.discovery.build(
            "youtube", "v3", credentials=credentials)
        
        inst.client = youtube
        inst.init_resources()
        return inst
    
if __name__ == '__main__':
    yt = Client.from_client_secrets("client_secrets.json", ["https://www.googleapis.com/auth/youtube"])
    req = yt.playlist.list(part=["snippet","content_details"], id="PLjgIcMBGNp1cHfSM65iO2uUOU_lmxxPHs")
