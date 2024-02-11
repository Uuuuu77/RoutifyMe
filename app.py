#!/usr/bin/python3

<<<<<<< HEAD
# Create a Flask application instance
app = Flask("__name__"):
=======
from flask import Flask
from app.views.my_location_view import my_location_view
from app.views.nearby_places_view import nearby_places_view
from app.views.route_finder_view import route_finder_view
>>>>>>> 7e3380c6109ab3390bc6bef16cd429e6bc92cf03

def create_app():
    app = Flask(__name__)

    # Register blueprints
    app.register_blueprint(my_location_view, url_prefix='/api')
    app.register_blueprint(nearby_places_view, url_prefix='/api')
    app.register_blueprint(route_finder_view, url_prefix='/api')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
