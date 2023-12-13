from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired, ValidationError
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.secret_key = 'your_secret_key'

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''


def length_check(form, field):
    if len(field.data) < 8:
        raise ValidationError("Enter a strong password with at least 8 characters")


def email_check(form, field):
    if '@' not in field.data or '.' not in field.data:
        raise ValidationError("Enter a valid Email ID")


class LoginForm(FlaskForm):
    email = EmailField(label="Email", validators=[DataRequired(), email_check])
    password = PasswordField(label="Password", validators=[DataRequired(), length_check])
    submit = SubmitField("Login")


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()

    if request.method == "POST" and form.validate_on_submit():
        if form.email.data == "admin@email.com" and form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)
