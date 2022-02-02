from src.ytwrapper.client import Client
# TODO: Add in actual testing, instead of...whatever this is supposed to be.

if __name__ == '__main__':
    yt = Client.from_client_secrets("client_secrets.json", ["https://www.googleapis.com/auth/youtube.force-ssl",
                                                            "https://www.googleapis.com/auth/youtube"])
