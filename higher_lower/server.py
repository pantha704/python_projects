import random
from flask import Flask, render_template

app = Flask(__name__)

random_no = random.randint(0, 9)

@app.route('/')
def home():
    return '<h1>Guess a number between 0 and 9</h1><img src="/static/home.gif">'

@app.route('/<user_no>')
def guess(user_no):
    if int(user_no) == random_no:
        return ("<h1>Aww you got me >.< </h1>"
                '<img src="/static/gotcha.webp">')
    elif int(user_no) < random_no:
        return ("<h1>Too low, try again!</h1>"
                '<img src="/static/toolow.webp">')
    else:
        return ("<h1>Too high, try again!</h1>"
                '<img src="/static/toohigh.gif">')

if __name__ == '__main__':
    app.run(debug=True)
