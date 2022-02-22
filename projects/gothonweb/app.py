from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    greeting = "Hello World"
    return render_template("index.html", greeting=greeting)

@app.route('/salut')
def salut_monde():
    francais = "Salut tout le monde"
    return render_template("foo.html", greeting=francais)
if __name__ == "__main__":
    app.run()
