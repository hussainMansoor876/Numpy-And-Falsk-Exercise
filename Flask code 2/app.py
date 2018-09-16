from flask import Flask,render_template,url_for,request
app=Flask(__name__)

@app.route("/<Name>")
def info(Name):
    return ("Hello dear:" +Name)

@app.route("/login")
def index():
    return render_template('index.html')
#     return ''' 
# <form action="/info" method="POST">
# <input type="text" name="user" placeholder="Full Name"><br>
# <input type="email" name="email" placeholder="Email"><br>
# <input type="password" name="pass" placeholder="password"><br>
# <input type="submit" value="Send">
# </form>
# '''

@app.route("/submit", methods=['GET','POST'])
def index1():
    if request.method=="GET":
        return "<h1>Open Method</h1>Hello "+ request.args.get('user') + \
    " Your Email:"+request.args.get('email') +" Your Password:"+request.args.get('password')
    else:
        return "<h1>Secure Method</h1>Hello "+ request.form['user'] + \
    " Your Email:"+request.form['email']
app.run(debug=True)