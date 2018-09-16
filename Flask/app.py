from flask import Flask ,render_template
from flask import url_for

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World"
@app.route("/calendar")
def index1():
    return render_template("index.html")
@app.route("/about")
def about():
    return render_template("about.html")
    # return '''<h1>My Name is Mansoor Hussain</h1>'''


app.run(debug=True)