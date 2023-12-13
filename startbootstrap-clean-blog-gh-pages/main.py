import datetime
import requests
from flask import Flask, render_template

from post import Post

app = Flask(__name__)


@app.route('/')
def home():
    response = requests.get("https://api.npoint.io/aa831263b7b9ed2bfe31")
    posts = response.json()
    date = datetime.datetime.now().date()
    author = "Panther"
    return render_template("index.html", posts=posts, date=date, author=author)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/sample_post')
def post():
    return render_template("post.html")


@app.route('/blog_post/<int:id>')
def s_post(id):
    post = Post().get_post(id)
    date = datetime.datetime.now().date()
    author = "Panther"
    return render_template("single_post.html", img=post['img'], date=date, id=id, title=post['title'],
                           subtitle=post['subtitle'], body=post['body'], author=author)


@app.route('/contact')
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
