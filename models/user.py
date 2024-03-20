#!/usr/bin/python3

from flask_sqlalchemy import SQLAlchemy

# Initializing SQLAlchemy object
db = SQLAlchemy()


# User model for storing user information
class User(db.Model):
    # Columns for id, email, and password
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
