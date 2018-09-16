from flask import Flask, jsonify

app=Flask(__name__)

@app.route("/")
def index():
    stud=[{'name':'mansoor','age':19},
    {'name':'Qasim','age':23}]
    return jsonify({'stud':stud})
app.run(host='0.0.0.0' , port='3000' debug=True)