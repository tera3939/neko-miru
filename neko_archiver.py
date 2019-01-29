from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
from mastodon import Mastodon
import requests
import config


class NekoArchiver:
    def __init__(self):
        self.__con = MongoClient()
        self.__db = self.__con[config.DATABASE_NAME]
        self.toots = self.__db[config.TOOTS_COLLECTION]

        self.mastodon = Mastodon(
            client_id=config.SECRET_NAME,
            api_base_url=config.BASE_URL
        )

    def get_toots(self):
        nekos = self.mastodon.timeline_hashtag("cat", only_media=True)
        for neko in nekos:
            neko = self.__cache_image(neko)
            try:
                self.toots.insert_one(neko)
            except DuplicateKeyError:
                # TODO: 良い感じにログ取りたい
                pass

    def get_nekos(self):
        return self.toots.find({})

    def close(self):
        self.__con.close()

    def __cache_image(self, toot):
        media = toot["media_attachments"]
        for i, medium in enumerate(media):
            url = medium["preview_url"]
            filename = url.split("/")[-1]
            res = requests.get(url)
            with open("./static/" + config.CACHE_FOLDER + filename, "wb") as f:
                f.write(res.content)
            toot["media_attachments"][i]["cache_path"] = config.CACHE_FOLDER + filename
        toot["cached"] = True
        return toot
