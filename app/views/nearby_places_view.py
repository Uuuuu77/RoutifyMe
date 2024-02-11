#!/usr/bin/python3

from flask import Blueprint, jsonify, request
from app.services.nearby_places import get_nearby_places

nearby_places_view = Blueprint('nearby_places_view', __name__)

@nearby_places_view.route('/nearby-places', methods=['GET'])
def nearby_places():
    location = request.args.get('location')
    places = get_nearby_places(location)
    return jsonify(places)