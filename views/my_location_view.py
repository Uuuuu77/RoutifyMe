#!/usr/bin/python3

from flask import Blueprint, jsonify
from services.my_location import get_location

# Blueprint for handling user's location-related views
my_location_view = Blueprint('my_location_view', __name__)


# Route for retrieving user's location
@my_location_view.route('/my-location', methods=['GET'])
def my_location():
    try:
        # Retrieve user's location using a service function
        location = get_location()

        # Return the location data as JSON
        return jsonify(location)
    except Exception as e:
        # If an error occurs, return an error message with status code 500
        return jsonify({"error": "Failed to get location"}), 500
