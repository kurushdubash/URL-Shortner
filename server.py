from flask import *
from random import randint
import os
from url_fetch import *
import database as db
app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('index.html', return_url="")


@app.route("/", methods=["POST"])
def get_website():
    print(request.form['url'])
    url = request.form['url']


    stripped_url = strip_url(url[url.index(".") + len("."):])
    bside = "http://bs.id/"
    current = request.url_root
    short_url = current + str(find_short_url(url, stripped_url))

    return render_template('index.html', return_url=short_url)

@app.route("/<url>/")
def forward(url):
	send = db.check_database(url)
	return redirect(send)


if __name__ == "__main__":
    app.debug = True
    app.run()