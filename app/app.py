#!/usr/bin/python3

from app import app
from flask import Flask, jsonify, request, abort
from services import nearby_places, route_finder, my_location

app = Flask(__name__)


@app.route('/nearby-places', methods=['GET'])
def get_nearby_places_view():
    location = request.args.get('location')  # Get location from request args

    if not location:
        abort(400, description="Missing location parameter")

    try:
        data = nearby_places.get_nearby_places(location)
    except Exception as e:
        abort(500, description=str(e))

    return jsonify(data)


@app.route('/route-finder', methods=['GET'])
def find_route_view():
    start_location = request.args.get('start_location')  # Get start location
    end_location = request.args.get('end_location')  # Get end location

    if not start_location or not end_location:
        abort(400, description="Missing start_location end_location parameter")

    try:
        data = route_finder.find_route(start_location, end_location)
    except Exception as e:
        abort(500, description=str(e))

    return jsonify(data)


@app.route('/my-location', methods=['GET'])
def get_my_location_view():
    try:
        data = my_location.get_my_location()
    except Exception as e:
        abort(500, description=str(e))

    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
