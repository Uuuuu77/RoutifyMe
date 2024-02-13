#!/usr/bin/python3
from flask import Flask

app = Flask(__name__)

from app.views import route_finder_view, my_location_view, nearby_places_view

