#!/usr/bin/python3

from flask import Blueprint, jsonify, request
from services.route_finder import optimize_route

route_finder_view = Blueprint('route_finder_view', __name__)


@route_finder_view.route('/find-route', methods=['POST'])
def route_finder():
    data = request.get_json()
    start_location = data.get('start')
    end_location = data.get('end')

    if not start_location or not end_location:
        return jsonify({"error": "Missing start & end location param"}), 400

    try:
        route = optimize_route(start_location, end_location)
        return jsonify(route)
    except Exception as e:
        return jsonify({"error": "Failed to find route"}), 500
