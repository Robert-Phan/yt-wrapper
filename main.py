from datetime import timezone
from src.client import Client
from src.resources.PlaylistResource import PlaylistResource

if __name__ == '__main__':
    yt = Client.from_client_secrets("client_secrets.json", ["https://www.googleapis.com/auth/youtube"])