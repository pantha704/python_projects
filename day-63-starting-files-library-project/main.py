from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''
db = SQLAlchemy()
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books.db"
db.init_app(app)


class Book(db.Model):
    __tablename__ = "books"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    # To represent all books as:
    def __repr__(self):
        return f'<Book {self.title}'


# Since we weren't inside any 'app' request so we create one using app.app_context()
# if we were already inside any 'app' request then it won't be needed
with app.app_context():
    db.create_all()


@app.route('/')
def home():
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars()
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        new_book = Book(
            title=request.form["title"],
            author=request.form["author"],
            rating=request.form["rating"],
        )
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("add.html")


@app.route('/edit', methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        # print(book_to_update)
        book_to_update = db.session.query(Book).get(request.args.get("id"))
        print(book_to_update)
        book_to_update.rating = float(request.form['rating'])
        db.session.commit()
        return redirect(url_for('home'))
    book = db.get_or_404(Book, request.args.get("id"))
    return render_template("edit.html", book=book)


@app.route('/delete/<int:id>', methods=["GET", "POST"])
def delete(id):
    book = db.session.query(Book).get(id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
