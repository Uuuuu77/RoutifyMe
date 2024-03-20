#!/usr/bin/python3

from flask import Blueprint, request
from models.user import User, db

# Blueprint for user-related views
user_view = Blueprint('user_view', __name__)


# Route for user registration
@user_view.route('/register', methods=['POST'])
def register():
    # Extracting email and password from the request form
    email = request.form['email']
    password = request.form['password']

    # Creating a new User object with the provided email and password
    user = User(email=email, password=password)

    # Adding the new user object to the database session
    db.session.add(user)

    # Committing the changes to the database
    db.session.commit()

    # Returning a success message
    return 'User registered successfully'
