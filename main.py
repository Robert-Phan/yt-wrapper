from src.client import Client
from src.resources import CommentThreadResource

if __name__ == '__main__':
    yt = Client.from_client_secrets("client_secrets.json", ["https://www.googleapis.com/auth/youtube.force-ssl",
                                                            "https://www.googleapis.com/auth/youtube"])
