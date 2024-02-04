# app/app.py
from flask import Flask, render_template

# Create a Flask application instance
app = Flask(__name__)

# Configuration (add your configuration variables here)

# Sample route to render the index page
@app.route('/')
def index():
    return render_template('index.html')

# Add more routes and logic as needed

if __name__ == '__main__':
    # Run the app in debug mode for development
    app.run(debug=True)
