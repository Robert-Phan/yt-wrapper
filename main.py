from src.client import Client
from resources.PlaylistItemResource import PlaylistItemResource, ResourceId

if __name__ == '__main__':
    yt = Client.from_client_secrets("client_secrets.json", ["https://www.googleapis.com/auth/youtube"])