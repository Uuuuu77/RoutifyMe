#!/usr/bin/python3

from flask import Blueprint, jsonify
from app.services.my_location import get_my_location

my_location_view = Blueprint('my_location_view', __name__)


@my_location_view.route('/my-location', methods=['GET'])
def my_location():
    try:
        location = get_my_location()
        return jsonify(location)
    except Exception as e:
        return jsonify({"error": "Failed to get location"}), 500
