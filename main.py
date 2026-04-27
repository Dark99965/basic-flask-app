from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hello, world</h1>"


@app.route('/test/<name>')
def test(name):
    return render_template("index.html", person=name)

@app.route('/test')
def test1():
    return render_template("testerror.html")

@app.route("/<url>")
def error(url):
    return render_template("404.html", link=url)