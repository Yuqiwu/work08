from flask import Flask, render_template, session, request, redirect, url_for, flash

my_app = Flask(__name__)
my_app.secret_key = "this is my secret key"

user = "user"
password = "pass"
u = "Sorry, your username is incorrect"
p = "Sorry, your password is incorrect"

def check(user, passw):
    if user == request.form['username']:
        if password == request.form['password']:
            session["user"] = user
            return 1
        else:
            return 2
    else:
        return 3

@my_app.route('/', methods=["POST", "GET"])
def root():
    if "user" in session and session["user"] == user:
        return redirect( url_for('welcome') )
    return render_template("form.html")

@my_app.route("/welcome", methods=["POST", "GET"])
def welcome():
    m = request.method
    username = request.form('username')
    password = request.form('password')
    return render_template('welcome.html', un = username, pw = password, method = m)

@my_app.route("check", methods=["POST", "GET"])
def auth():    
    username = request.form('username')
    password = request.form('password')
    result = check(username, password)
    if result == 1:
        redirect( url_for("welcome") )
    else if result == 2:
        flash("Sorry, your password is incorrect")
        redirect( url_for("/") )
    else:
        flash("Sorry, your username does not exist")
        redirect( url_for("/") )

@my_app.route("/logout", methods=["POST","GET"])
def logout():
    if "user" in session:
        session.pop("user")
    return redirect( url_for("root") ) 

if __name__ == "__main__":
    my_app.debug = True
    my_app.run()
