#!/usr/bin/python3

from flask import Blueprint, request
from models.location import Location, db

# Blueprint for location-related views
location_view = Blueprint('location_view', __name__)


# Route for creating a new location
@location_view.route('/create', methods=['POST'])
def create():
    # Extracting name and address from the request form
    name = request.form['name']
    address = request.form['address']

    # Creating a new location object and adding it to the database
    location = Location(name=name, address=address)
    db.session.add(location)
    db.session.commit()

    # Return a success message
    return 'Location created successfully'
