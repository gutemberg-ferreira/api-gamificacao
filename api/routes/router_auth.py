from flask_jwt_extended import create_access_token
from flask_login import login_user, logout_user
from app import app
from api.services import helpers
from flasgger import swag_from
from flask import request, render_template, jsonify, flash, redirect, url_for
from api.models.users import user_by_username
from werkzeug.security import check_password_hash

@app.route('/auth', methods=['POST'])
@swag_from('../../api_docs/Auth/Post_Auth.yml')
def authenticate():
    return helpers.auth()


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':  # if the request is a GET we return the login page
        return render_template('login.html')
    else:
        username = user_by_username(request.form.get('HTTP_USERNAME'))
        password = request.form.get('HTTP_PASSWORD')
        remember = True if request.form.get('REMEMBER') else False

    if not username:
        flash('Please sign up before')
    elif not check_password_hash(username.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('login'))

    login_user(username, remember=remember)
    return redirect(url_for('home'))


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))