#!/usr/bin/python3

from flask import Blueprint, jsonify, request
from services.nearby_places import get_nearby_places

# Blueprint for handling nearby places related views
nearby_places_view = Blueprint('nearby_places_view', __name__)


# Route for retrieving nearby places
@nearby_places_view.route('/nearby-places', methods=['GET'])
def nearby_places():
    # Retrieve the location parameter from the request
    location = request.args.get('location')

    # Check if location parameter is missing
    if not location:
        return jsonify({"error": "Missing location parameter"}), 400

    try:
        # Retrieve nearby places using the provided location
        places = get_nearby_places(location)

        # Return the nearby places as JSON
        return jsonify(places)
    except Exception as e:
        # If an error occurs, return an error message with status code 500
        return jsonify({"error": "Failed to get nearby places"}), 500
