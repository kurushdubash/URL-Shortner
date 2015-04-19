from flask import Flask, request, render_template
from random import randint
import os
from data import*
app = Flask(__name__)


@app.route("/")
def hello():
    return app.send_static_file('index.html')


@app.route("/api/lottery", methods=["POST"])
def update_data():
    print(request.form['value'])
    val = request.form['value']
    if(val == 'NY'):
        ny = 'checked'
        pb = ''
    else:
        ny = ''
        pb = 'checked'

    data = frequency_winning_numbers(check(val))
    # mega = frequency_mega(check1(val))
    # bm = best_mega(mega)
    #data = [tester([]),tester([])]


    print (data)
    print(len(data))
    best = best_five(data)

    listoffive = best

    if(len(listoffive) > 0):
        prob = find_probability( probability(data), listoffive)
    else:
        prob = ''


    return render_template('data.html', data=data, best=best, size=len(data), ny=ny, pb=pb, prob=prob)

def tester(data):
    x = 0
    while x < 25:
        data.append(randint(1, 25))
        x+=1
    return data

if __name__ == "__main__":
    app.debug = True
    app.run()