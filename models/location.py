#!/usr/bin/python3

from flask_sqlalchemy import SQLAlchemy

# Initializing SQLAlchemy object
db = SQLAlchemy()


# Location model for storing location information
class Location(db.Model):
    # Columns for id, name, and address
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(200), nullable=False)
