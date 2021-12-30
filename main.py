from src.client import Client

if __name__ == '__main__':
    yt = Client.from_client_secrets("client_secrets.json", ["https://www.googleapis.com/auth/youtube"])
    req = yt.playlist.list(part=["snippet","content_details"], id="PLjgIcMBGNp1cHfSM65iO2uUOU_lmxxPHs")