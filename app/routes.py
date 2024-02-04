# app/routes.py
from flask import Blueprint, render_template, jsonify

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
    # Extract data from the frontend (e.g., selected locations)
    data = request.get_json()

    # Implement logic to optimize the route using Google Maps API
    # Replace the following with actual Google Maps API calls
    optimized_route = optimize_with_google_maps(data)

    return jsonify({"optimized_route": optimized_route})

# Function to simulate Google Maps API call for optimization
def optimize_with_google_maps(data):
    # Your implementation here
    # This could involve making requests to Google Maps Directions API
    # and processing the response to get the optimized route.
    # For simplicity, we are just returning a reversed list of locations.
    return list(reversed(data['locations']))
