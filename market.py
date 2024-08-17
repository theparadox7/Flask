from flask import Flask

app = Flask(__name__)

@app.route("/")
def hellow_world():
    return "<h1> Namaste!! </h1>"

@app.route('/about/<username>')
def about_page(username):
    return f'<h1> This is about page of {username}</h1>'
