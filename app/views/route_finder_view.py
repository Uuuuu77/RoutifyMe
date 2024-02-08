#!/usr/bin/python3

from flask import Blueprint, jsonify, request
from app.services.route_finder import find_route

route_finder_view = Blueprint('route_finder_view', __name__)

@route_finder_view.route('/find-route', methods=['POST'])
def route_finder():
    data = request.get_json()
    start_location = data.get('start')
    end_location = data.get('end')
    route = find_route(start_location, end_location)
    return jsonify(route)