from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from .models import User
auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                # flash('Logged in successfully!', category='success')
                print("logged in succesed")
                # login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                # flash('Incorrect password, try again.')
                print("incorret password")
        else:
            # flash('Email does not exist.')
            print("email n'existe pas")
    return render_template("login.html")


@auth.route('/logout')
def logout():
    return "u will logout shortly"


@auth.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        FirstName = request.form.get('FirstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('email doit contenir plus que 4 element', category="error")
        if len(FirstName) < 2:
            flash('votre nom doit contenir plus que 2 caractere ', category="error")
        if password1 != password2:
            flash("mot de pass est pas le meme", category="error")
        else:
            new_user = User(email=email, first_name=FirstName,
                            password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash("compt cree avec succes", category="success")
            return redirect(url_for('views.home'))
    elif request.method == "GET":
        return render_template("signup.html")
