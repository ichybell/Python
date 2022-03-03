#This is the app.py module from exercise 51

from flask import Flask
from flask import render_template
from flask import request
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/')
def hello_world():
    greeting = "Hello World"
    return render_template("index.html", greeting=greeting)

@app.route('/upload', methods = ['GET', 'POST'])
def upload_file():
    if request.method == "POST":
        f = request.files['file']
        f.save(f.filename)
        name = f.filename
        return f'{name} uploaded successfully'
    else:
        return render_template('upload.html')
@app.route('/salut')
def salut_monde():
    francais = "Salut tout le monde"
    return render_template("foo.html", greeting=francais)

@app.route('/hello', methods = ['GET', 'POST'])
def index():

    if request.method == "POST":
        name = request.form['name']
        greet = request.form['greet']
# The line below is an addition to check if user fills the form and if not,
# returns a message back to the user requiring the form to be filled
        if name and greet:
            greeting = f"{greet}, {name}"
            return render_template("index.html", greeting=greeting)
        else:
            return render_template("hello_form_error.html")
    else:
        return render_template("hello_form.html")
#    name = request.args.get('name', 'Nobody')
#    greet = request.args.get('greet', 'Hello')

#    if name:
#        greeting = f"{greet}, {name}"
#    else:
#        greeting = "Hello World"

#    return render_template("index.html", greeting=greeting)


if __name__ == "__main__":
    app.run()
