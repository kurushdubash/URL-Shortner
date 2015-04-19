from flask import Flask, request, render_template
from random import randint
import os
from url_fetch import*
app = Flask(__name__)


@app.route("/")
def hello():
    return app.send_static_file('index.html')


@app.route("/shorten", methods=["POST"])
def get_website():
    print(request.form['url'])
    url = request.form['url']


    short_url = "http://Bs.id/" + find_short_url(url)

    #short_url = 'Http://' + url
    return render_template('shorten.html', return_url=short_url)

if __name__ == "__main__":
    app.debug = True
    app.run()