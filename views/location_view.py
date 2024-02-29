#!/usr/bin/python3

from flask import Blueprint, request
from models.location import Location, db

location_view = Blueprint('location_view', __name__)

@location_view.route('/create', methods=['POST'])
def create():
    name = request.form['name']
    address = request.form['address']
    location = Location(name=name, address=address)
    db.session.add(location)
    db.session.commit()
    return 'Location created successfully'