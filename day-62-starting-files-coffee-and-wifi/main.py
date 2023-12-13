from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired
import csv, pandas as pd

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
bootstrap = Bootstrap5(app)

coffee_choice = ['☕', '☕☕', '☕☕☕', '☕☕☕☕', '☕☕☕☕☕']
wifi_choice = ['✘', '💪', '💪💪', '💪💪💪', '💪💪💪💪', '💪💪💪💪💪']
power_choice = ['✘', '🔌', '🔌🔌', '🔌🔌🔌', '🔌🔌🔌🔌', '🔌🔌🔌🔌🔌']


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    open = StringField('Open', validators=[DataRequired()])
    close = StringField('Close', validators=[DataRequired()])
    coffee_rating = SelectField('Coffee', validators=[DataRequired()], choices=coffee_choice)
    wifi_rating = SelectField('Wifi', validators=[DataRequired()], choices=wifi_choice)
    power_rating = SelectField('Power', validators=[DataRequired()], choices=power_choice)

    submit = SubmitField('Submit')


# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
# e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        file = open("cafe-data.csv", 'a', encoding='utf-8')
        file.write(f"\n{form.cafe.data},"
                   f"{form.location.data},"
                   f"{form.open.data},"
                   f"{form.close.data},"
                   f"{form.coffee_rating.data},"
                   f"{form.wifi_rating.data},"
                   f"{form.power_rating.data}")
        file.close()
        return redirect(url_for('cafes'))
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
        # print(list_of_rows)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
