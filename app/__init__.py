#!/usr/bin/python3

from flask import Flask, jsonify

# Create a Flask application instance
app = Flask(__name__)

# Import routes
from app.routes import routes_bp

# Register the Blueprint with the app
app.register_blueprint(routes_bp)

@app.errorHandler(500)
def handle_500_error(e):
    return jsonify(error=str(e)), 500

# You can include additional initialization code here if needed
# For example, connecting to a database, setting configurations, etc.
