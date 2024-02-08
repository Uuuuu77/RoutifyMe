#!/usr/bin/python3

import requests
from flask import Blueprint, render_template, request, jsonify

# Create a Blueprint for routes
routes_bp = Blueprint('routes', __name__)

# Sample data (replace with actual data or database interactions)
locations = [
    {"id": 1, "name": "Location A", "lat": 37.7749, "lng": -122.4194},
    {"id": 2, "name": "Location B", "lat": 37.7749, "lng": -122.4294},
    {"id": 3, "name": "Location C", "lat": 37.7849, "lng": -122.4194},
]

@routes_bp.route('/')
def index():
    return render_template('index.html', locations=locations)

@routes_bp.route('/optimize', methods=['POST'])
def optimize_route():
    data = request.get_json()
    optimized_route = optimize_with_google_maps(data)
    return jsonify(optimized_route)

def optimize_with_google_maps(data):
    # Google Maps Directions API endpoint
    endpoint = 'https://maps.googleapis.com/maps/api/directions/json?'

    # parameters
    api_key = 'YOUR_API_KEY'  # replace with your own API key
    origin = data['locations'][0]
    destination = data['locations'][-1]
    waypoints = '|'.join(data['locations'][1:-1])
    optimize = 'true'  # to optimize waypoints

    # define the request url
    nav_request = f'origin={origin}&destination={destination}&waypoints=optimize:{optimize}:{waypoints}&key={api_key}'

    # send the request to the Google Maps Directions API
    request_url = endpoint + nav_request
    response = requests.get(request_url)

    # convert the response to json
    directions = response.json()

    # extract the optimized route from the response
    optimized_route = [leg['end_address'] for leg in directions['routes'][0]['legs']]

    return optimized_route