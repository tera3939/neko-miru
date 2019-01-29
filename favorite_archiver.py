from pymongo import MongoClient

import config


class FavoriteArchiver:
    def __init__(self):
        connection = MongoClient()
        db = connection[config.DATABASE_NAME]
        self.toots = db[config.TOOTS_COLLECTION]
        self.favs = db[config.FAVORITES_COLLECTION]

    def save(self, toot_id):
        toot = self.toots.find_one({"id": toot_id})
        toot["is_favorited"] = True
        self.favs.insert_one(toot)
        self.toots.update_one({"id": toot_id}, {"$set": {"is_favorited": True}})

    def remove(self, toot_id):
        self.favs.remove_one({"id": toot_id})
        self.toots.update_one({"id": toot_id}, {"$set": {"is_favorited": False}})

    def tootlist(self):
        return self.toots.find({"is_favorited": True}).sort([("created_at", -1)])
