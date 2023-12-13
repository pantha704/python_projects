import requests
from flask import Flask, render_template
from post import Post

app = Flask(__name__)


@app.route('/')
def home():
    all_posts = Post().output()
    return render_template("index.html", posts=all_posts)


@app.route("/post/<id>")
def blog(id):
    post = Post().output(id)
    return render_template("post.html", post=post)


if __name__ == "__main__":
    app.run(debug=True)
