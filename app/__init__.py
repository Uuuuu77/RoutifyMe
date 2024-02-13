#!/usr/bin/python3

from flask import Flask, jsonify


def create_app():
    # Create a Flask application instance
    app = Flask(__name__)

    # Import routes inside the function to avoid circular imports
    from app.views import route_finder_view, my_location_view, nearby_places_view

    # Register the Blueprint with the app
    app.register_blueprint(routes_bp)

    # Global error handler
    @app.errorHandler(500)
    def handle_500_error(e):
        return jsonify(error=str(e)), 500

    # You can include additional initialization code here if needed
    # For example, connecting to a database, setting configurations, etc.

    return app


app = create_app()

# You can include additional initialization code here if needed
# For example, connecting to a database, setting configurations, etc.
