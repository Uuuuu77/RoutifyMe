#!/usr/bin/python3

import os
from flask import Flask, jsonify, request, abort, render_template
from models.user import db, User
from models.location import Location
from services import nearby_places, route_finder, my_location
from __init__ import create_app

app = create_app()


@app.route('/')
def index():
    bing_maps_key = os.getenv('Bing_Maps_Key')
    return render_template('index.html', bing_maps_key=bing_maps_key)


@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user = User(**data)
    db.session.add(user)
    db.session.commit()
    return jsonify(user.to_dict()), 201


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if user is None:
        abort(404, description="User not found")
    return jsonify(user.to_dict())


@app.route('/locations', methods=['POST'])
def create_location():
    data = request.get_json()
    location = Location(**data)
    db.session.add(location)
    db.session.commit()
    return jsonify(location.to_dict()), 201


@app.route('/locations/<int:location_id>', methods=['GET'])
def get_location(location_id):
    location = Location.query.get(location_id)
    if location is None:
        abort(404, description="Location not found")
    return jsonify(location.to_dict())


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
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=8000)
