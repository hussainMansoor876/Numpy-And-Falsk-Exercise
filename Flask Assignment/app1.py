from flask import Flask , render_template ,request
from flask_pymongo import PyMongo

app=Flask(__name__) 
app.config['MONGO_DBNAME']='mansoor'
app.config['MONGO_URI']='mongodb://mansoor:mansoor@ds117858.mlab.com:17858/mansoor'

mongo=PyMongo(app)

@app.route("/login")
def index():
    return render_template('index.html')
@app.route("/submit", methods=['GET','POST'])
def submit():
    add=mongo.db.log
    if request.method=="GET":
        add.insert({'name':request.args.get('user'),'email':request.args.get('email'),\
        'password':request.args.get('password')})
        return "Sucessfully add from GET method"
    else:
        add.insert({'name':request.form['user'],'email':request.form['email'],\
        'password':request.form['password']})
        return "Sucessfully add from POST method"
app.run(debug=True)