import request
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/login', methods=['POST'])
def receive_data():
    name = request.form.get("username")
    passwd = request.form.get("password")
    return f"<h1>Data received!</h1><br><h3>Name: {name}, Password: {passwd}</h3>"


if __name__ == "__main__":
    app.run(debug=True)
