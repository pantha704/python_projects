import requests

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/guess/<name>")
def your_name(name):
    response = requests.get(f"https://api.agify.io?name={name}")
    naam = response.json()['name']
    age = response.json()['age']

    response = requests.get(f'https://api.genderize.io?name={name}')
    gender = response.json()['gender']
    return render_template("index.html", gender=gender, name=naam.title(), age=age)


@app.route('/blog/<num>')
def blog(num):
    print(num)
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    return render_template("blog.html", posts=response.json())


app.run(debug=True)
