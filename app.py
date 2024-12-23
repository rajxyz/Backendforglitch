from flask import Flask
from flask_cors import CORS
from api import api_blueprint  # Import API routes from api.py

app = Flask(__name__)
CORS(app)

# Register API routes
app.register_blueprint(api_blueprint)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)  # Glitch-compatible host and port