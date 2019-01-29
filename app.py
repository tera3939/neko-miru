import bson
from flask import Flask, Response, request, render_template
from favorite_archiver import FavoriteArchiver
from neko_archiver import NekoArchiver
from neko_getter import NekoGetter


app = Flask(__name__)
NEKO_ARCHIVER = NekoArchiver()
FAVORITE_ARCHIVER = FavoriteArchiver()


@app.route("/")
def index():
    global NEKO_ARCHIVER
    toots = NEKO_ARCHIVER.get_nekos().sort([("created_at", -1)])
    return render_template("index.html", toots=toots)


@app.route("/favorite_list")
def favorite_list():
    global FAVORITE_ARCHIVER
    return render_template("favorite.html", favorites=FAVORITE_ARCHIVER.tootlist())


@app.route("/operation/favorite", methods=["POST"])
def favorite():
    global FAVORITE_ARCHIVER
    toot_id = bson.Int64(request.form["toot_id"])
    FAVORITE_ARCHIVER.save(toot_id)
    print("saved", toot_id)
    return Response(status=200)


@app.route("/operation/unfavorite", methods=["POST"])
def unfavorite():
    global FAVORITE_ARCHIVER
    toot_id = bson.Int64(request.form["toot_id"])
    FAVORITE_ARCHIVER.remove(toot_id)
    return Response(status=200)


if __name__ == "__main__":
    nekogetter = NekoGetter()
    nekogetter.run()
    app.run(debug=True)
