from flask import Flask, render_template, request
import requests, smtplib

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)


def send_mail(data):
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user="prathamjaiswal204@gmail.com", password="rhhxzirrnqoisxbi")
    connection.sendmail(from_addr="prathamjaiswal204@gmail.com", to_addrs="prathamjaiswal204@gmail.com", msg=data)
    connection.close()


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        info = f"{data['name']}\n{data['email']}\n{data['phone']}\n{data['message']}"
        send_mail(info)
        return render_template("contact.html", submitted=True)
    else:
        return render_template("contact.html", submitted=False)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
