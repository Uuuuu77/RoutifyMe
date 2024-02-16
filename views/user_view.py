#!/usr/bin/python3

from flask import Blueprint, request
from models.user import User

user_view = Blueprint('user_view', __name__)

@user_view.route('/register', methods=['POST'])
def register():
    email = request.form['email']
    password = request.form['password']
    user = User(email=email, password=password)
    db.session.add(user)
    db.session.commit()
    return 'User registered successfully'