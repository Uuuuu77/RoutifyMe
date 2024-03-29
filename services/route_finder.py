#!/usr/bin/python3

import os
import requests
from flask import Blueprint, render_template, request, jsonify
from requests.exceptions import RequestException
from dotenv import load_dotenv

load_dotenv()

# Create a Blueprint for routes
route_finder = Blueprint('route_finder', __name__)

# Sample data
locations = [
    {"id": 1, "name": "Nairobi", "lat": -1.280555, "lng": 36.808945},
    {"id": 2, "name": "Nakuru", "lat": -0.3031, "lng": 36.0800},
    {"id": 3, "name": "Mombasa", "lat": -4.0435, "lng": 39.6682},
]


@route_finder.route('/')
def index():
    return render_template('index.html', locations=locations)


@route_finder.route('/optimize', methods=['POST'])
def optimize_route():
    data = request.get_json()
    if 'locations' not in data or len(data['locations']) < 2:
        return jsonify({"error": "At least two locations are required"}), 400
    optimized_route = optimize_with_bing_maps(data)
    return jsonify(optimized_route)


def optimize_with_bing_maps(data):
    # Bing Maps API endpoint
    endpoint = 'http://dev.virtualearth.net/REST/V1/Routes/Driving?'

    # parameters
    api_key = os.getenv('Bing_Maps_Key')
    origin = data['locations'][0]
    destination = data['locations'][-1]
    waypoints = ';'.join([
        f"{loc['lat']},{loc['lng']}"
        for loc in data['locations'][1:-1]
    ])
    optimize = 'time'  # to optimize waypoints

    # define the request url
    nav_request = (
        f'wp.0={origin}&'
        f'wp.1={waypoints}&'
        f'wp.2={destination}&'
        f'optimize={optimize}&'
        f'key={api_key}'
    )

    # send the request to the Bing Maps API
    request_url = endpoint + nav_request
    try:
        response = requests.get(request_url)
        response.raise_for_status()
    except RequestException as e:
        raise Exception(f"Request to Bing maps API failed: {str(e)}")

    directions = response.json()

    optimized_route = [
        route['routeLegs'][0]['endLocation']
        for route in directions['resourceSets'][0]['resources']
    ]

    return optimized_route
