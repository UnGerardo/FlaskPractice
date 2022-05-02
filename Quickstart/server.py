from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}"

@app.route("/blogs/<int:blog_number>")
def blog_by_number(blog_number):
    return f"This is blog {blog_number}"