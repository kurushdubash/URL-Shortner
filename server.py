from flask import *
from random import randint
import os

# Custom URL and Database handlers
import url_fetch as fetch
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

    stripped_url = fetch.strip_url(url[url.index(".") + len("."):])
    short_url = fetch.find_short_url(url, stripped_url)
    return_url = request.url_root + str(short_url)

    return render_template('index.html', return_url = return_url)

# Returning a shortened URL
@app.route("/<url>/")
def forward(url):
    send = db.check_database(url)
    if send != None:
	   return redirect(send, code=301)
    else:
        return render_template('index.html', return_url="Page Not Found")

if __name__ == "__main__":
    app.debug = True
    app.run()

