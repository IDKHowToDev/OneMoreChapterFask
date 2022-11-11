from flask import Blueprint,render_template
auth=Blueprint('auth',__name__)

@auth.route('/login')
def  login():
    return "<h1> this is the login page </h1>"

@auth.route('/logout')
def logout():
    return "<p> you will logout shortly</p>"
@auth.route('/trying')
def trying():
    return render_template("base.html")