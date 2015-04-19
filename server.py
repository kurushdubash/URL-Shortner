from flask import Flask, request, render_template
from random import randint
import os
from url_fetch import *
app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('index.html', return_url="")


@app.route("/", methods=["POST"])
def get_website():
    print(request.form['url'])
    url = request.form['url']


    stripped_url = strip_url(url[url.index(".") + len("."):])
    short_url = "http://bs.id/" + str(find_short_url(url, stripped_url))

    return render_template('index.html', return_url=short_url)

if __name__ == "__main__":
    app.debug = True
    app.run()