#!/usr/bin/python3

from flask import Flask, jsonify


def create_app():
    # Create a Flask application instance
    app = Flask(__name__)

    # Import routes inside the function to avoid circular imports
    from views.route_finder_view import route_finder_view
    from views.my_location_view import my_location_view
    from views.nearby_places_view import nearby_places_view

    # Register the Blueprint with the app
    app.register_blueprint(route_finder_view)
    app.register_blueprint(my_location_view)
    app.register_blueprint(nearby_places_view)

    # Global error handler
    @app.errorhandler(500)
    def handle_500_error(e):
        return jsonify(error=str(e)), 500

    # You can include additional initialization code here if needed
    # For example, connecting to a database, setting configurations, etc.

    return app


app = create_app()

# You can include additional initialization code here if needed
# For example, connecting to a database, setting configurations, etc.
