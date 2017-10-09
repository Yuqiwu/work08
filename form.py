from flask import Flask, render_template, session, request, redirect, url_for

my_app = Flask(__name__)
my_app.secret_key = "this is my secret key"

user = "user"
password = "pass"
u = "Sorry, your username is incorrect"
p = "Sorry, your password is incorrect"

@my_app.route('/', methods=["POST", "GET"])
def root():
    if "user" in session and session["user"] == user:
        m = request.method
        return render_template("welcome.html", un = user, pw = password, method = m)
    return render_template("form.html")

@my_app.route("/welcome", methods=["POST", "GET"])
def welcome():
    m = request.method
    print m
    if user == request.form['username']:
        if password == request.form['password']:
            session["user"] = user
            return render_template("welcome.html",un = user, pw = password, method = m)
        else:
            return render_template("welcome.html",un = user, pw = p)
    else:
        return render_template("welcome.html", un = u, pw = "")

@my_app.route("/logout", methods=["POST","GET"])
def logout():
    if "user" in session:
        session.pop("user")
    return redirect( url_for("root") ) 

if __name__ == "__main__":
    my_app.debug = True
    my_app.run()
