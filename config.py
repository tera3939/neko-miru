from pymongo import MongoClient
from mastodon import Mastodon


MASTODON_HOST = "mastodon.cloud"
BASE_URL = "https://" + MASTODON_HOST
APP_NAME = "neko-miru"
SECRET_NAME = APP_NAME+".secret"

DATABASE_NAME = "neko-miru"
TOOTS_COLLECTION = "toots"
FAVORITES_COLLECTION = "favorites"

CACHE_FOLDER = "cache/"


def create_app():
    global MASTODON_HOST
    global BASE_URL
    global SECRET_NAME

    Mastodon.create_app(
        APP_NAME,
        api_base_url=BASE_URL,
        to_file=SECRET_NAME
    )


def create_db():
    global DATABASE_NAME
    global TOOTS_COLLECTION
    global FAVORITES_COLLECTION

    con = MongoClient()
    db = con[DATABASE_NAME]
    db.create_collection(TOOTS_COLLECTION)
    db.create_collection(FAVORITES_COLLECTION)
    db[TOOTS_COLLECTION].create_index([("id", 1)], unique=True)
    db[FAVORITES_COLLECTION].create_index([("id", 1)], unique=True)
    con.close()


def main():
    create_app()
    create_db()


if __name__ == "__main__":
    main()
