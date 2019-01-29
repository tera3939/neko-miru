from flask import Flask, render_template
from neko_archiver import NekoArchiver
from neko_getter import NekoGetter


app = Flask(__name__)
NEKO_ARCHIVER = NekoArchiver()


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    nekogetter = NekoGetter()
    nekogetter.run()
    app.run()
