#!/usr/bin/python3

from models.user import User, db
from sqlalchemy.exc import IntegrityError


# Function to create a new user
def create_user(email, password):
    new_user = User(email=email, password=password)
    db.session.add(new_user)
    try:
        db.session.commit()
        return new_user
    except IntegrityError:
        db.session.rollback()
        return None


# Function to get a user by its id
def get_user_by_id(user_id):
    try:
        return User.query.get(user_id)
    except Exception as e:
        print(f"Error occurred: {e}")
        return None


# Function to get a user by its email
def get_user_by_email(email):
    try:
        return User.query.filter_by(email=email).first()
    except Exception as e:
        print(f"Error occurred: {e}")
        return None


# Function to update a user's email and/or password
def update_user(user_id, email=None, password=None):
    user = get_user_by_id(user_id)
    if user is None:
        return None
    if email is not None:
        user.email = email
    if password is not None:
        user.password = password
    try:
        db.session.commit()
        return user
    except IntegrityError:
        db.session.rollback()
        return None


# Function to delete a user
def delete_user(user_id):
    user = get_user_by_id(user_id)
    if user is None:
        return None
    db.session.delete(user)
    try:
        db.session.commit()
        return user
    except IntegrityError:
        db.session.rollback()
        return None
