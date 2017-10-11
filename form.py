from flask import Flask, render_template, session, request, redirect, url_for, flash

my_app = Flask(__name__)
my_app.secret_key = "this is my secret key"

user = "user"
password = "pass"
u = "Sorry, your username is incorrect"
p = "Sorry, your password is incorrect"

def check(getUser, getPass):
    if user == getUser:
        if password == getPass:
            session["user"] = user
            return 1
        else:
            return 2
    else:
        return 3

@my_app.route('/', methods=["POST", "GET"])
def root():
    if "user" in session and session["user"] == user:
        session['method'] = request.method
        return redirect( url_for('welcome') )
    return render_template("form.html")

@my_app.route("/welcome", methods=["POST", "GET"])
def welcome():
    return render_template('welcome.html', un = session['user'], method = session['method'])

@my_app.route("/check", methods=["POST", "GET"])
def auth():
    m = request.method
    getUser = request.form['username']
    getPass = request.form['password']
    result = check(getUser, getPass)
    if result == 1:
        session['user'] = getUser
        session['method'] = m
        return redirect( url_for("welcome") ) # this become a GET method
    elif result == 2:
        flash("Sorry, your password is incorrect")
        return redirect( url_for("root") )
    else:
        flash("Sorry, your username does not exist")
        return redirect( url_for("root") )

@my_app.route("/logout", methods=["POST","GET"])
def logout():
    if "user" in session:
        session.pop("user")
    return redirect( url_for("root") ) 

if __name__ == "__main__":
    my_app.debug = True
    my_app.run()
