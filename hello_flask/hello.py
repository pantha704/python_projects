from flask import Flask

app = Flask(__name__)


def make_bold(fn):
    def wrapper(name):
        return f"<b>{fn(name)}</b>"

    return wrapper


def make_underlined(fn):
    def wrapper(name):
        return f"<u>{fn(name)}</u>"
    return wrapper


def make_emphasis(fn):
    def wrapper(name):
        return f"<em>{fn(name)}</em>"

    return wrapper


@app.route('/<name>')
@make_bold
@make_emphasis
@make_underlined
def hello(name):
    return f'{name.title()}'


if __name__ == "__main__":
    app.run(debug=True)
