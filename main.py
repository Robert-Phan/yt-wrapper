from src.client import Client
from src.resources.PlaylistResource import PlaylistResource

if __name__ == '__main__':
    yt = Client.from_client_secrets("client_secrets.json", ["https://www.googleapis.com/auth/youtube"])
    request_body = PlaylistResource()
    request_body.snippet.description = ''
    request_body.snippet.title = "Until it's vegas everywhere we are"
    res = yt.playlist.insert(request_body, part="snippet")
    print(res.snippet.channel_title)