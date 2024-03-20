#!/usr/bin/python3

from flask import Blueprint, jsonify, request
from services.route_finder import optimize_route

# Blueprint for handling route finding related views
route_finder_view = Blueprint('route_finder_view', __name__)


# Route for finding an optimized route
@route_finder_view.route('/find-route', methods=['POST'])
def route_finder():
    # Extracting data from JSON payload
    data = request.get_json()
    start_location = data.get('start')
    end_location = data.get('end')

    # Checking for missing start or end location parameters
    if not start_location or not end_location:
        return jsonify({"error": "Missing start & end location param"}), 400

    try:
        # Finding an optimized route between the provided start and end location
        route = optimize_route(start_location, end_location)

        # Returning the optimized route as JSON
        return jsonify(route)
    except Exception as e:
        # If an error occurs, return an error message with status code 500
        return jsonify({"error": "Failed to find route"}), 500
