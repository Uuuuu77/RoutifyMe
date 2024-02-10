#!/usr/bin/python3

from flask import Flask, jsonify
from services import nearby_places, route_finder, my_location

app = Flask(__name__)

@app.route('/nearby-places', methods=['GET'])
def get_nearby_places_view():
    location = request.args.get('location')  # Get location from the request parameters
    data = nearby_places.get_nearby_places(location)
    return jsonify(data)

@app.route('/route-finder', methods=['GET'])
def find_route_view():
    start_location = request.args.get('start_location')  # Get start location from the request parameters
    end_location = request.args.get('end_location')  # Get end location from the request parameters
    data = route_finder.find_route(start_location, end_location)
    return jsonify(data)

@app.route('/my-location', methods=['GET'])
def get_my_location_view():
    data = my_location.get_my_location()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
