from flask import Blueprint,render_template
auth=Blueprint('auth',__name__)

@auth.route('/login')
def  login():
    return render_template("login.html", text=True)

@auth.route('/logout')
def logout():
    return "u will logout shortly"
@auth.route('/signup')
def signup():
    return render_template("signup.html")