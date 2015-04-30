from flask import *
from random import randint
import os

# Custom URL and Database handlers
import url_fetch as url
import database as db

app = Flask(__name__)

# New User Login
@app.route("/")
def welcome():
    return render_template('index.html', return_url="")

# Created a shortened URL
@app.route("/", methods=["POST"])
def added_website():
    print(request.form['url'])
    url = request.form['url']
    stripped_url = strip_url(url[url.index(".") + len("."):])
    current = request.url_root
    short_url = current + str(find_short_url(url, stripped_url))

    return render_template('index.html', return_url=short_url)

# Returning a shortened URL
@app.route("/<url>/")
def forward(url):
	send = db.check_database(url)
	return redirect(send)

if __name__ == "__main__":
    app.debug = True
    app.run()