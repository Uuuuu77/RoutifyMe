#!/usr/bin/python3

from models.location import Location, db
from sqlalchemy.exc import IntegrityError


# Function to create a new location
def create_location(name, address):
    new_location = Location(name=name, address=address)
    db.session.add(new_location)
    try:
        db.session.commit()
        return new_location
    except IntegrityError:
        db.session.rollback()
        return None


# Function to get a location by its id
def get_location_by_id(location_id):
    try:
        return Location.query.get(location_id)
    except Exception as e:
        print(f"Error occurred: {e}")
        return None


# Function to get a location by its name
def get_location_by_name(name):
    try:
        return Location.query.filter_by(name=name).first()
    except Exception as e:
        print(f"Error occurred: {e}")
        return None


# Function to update a location's name and/or address
def update_location(location_id, name=None, address=None):
    location = get_location_by_id(location_id)
    if location is None:
        return None
    if name is not None:
        location.name = name
    if address is not None:
        location.address = address
    try:
        db.session.commit()
        return location
    except IntegrityError:
        db.session.rollback()
        return None


# Function to delete a location
def delete_location(location_id):
    location = get_location_by_id(location_id)
    if location is None:
        return None
    db.session.delete(location)
    try:
        db.session.commit()
        return location
    except IntegrityError:
        db.session.rollback()
        return None
