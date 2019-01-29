from mastodon import Mastodon


MASTODON_HOST = "mastodon.cloud"
BASE_URL = "https://" + MASTODON_HOST
APP_NAME = "neko-miru"


if __name__ == "__main__":
    Mastodon.create_app(
     APP_NAME,
     api_base_url=BASE_URL,
     to_file=APP_NAME+'.secret'
    )
