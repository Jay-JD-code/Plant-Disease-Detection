#!/usr/bin/env python3
"""
WSGI Entry Point for Plant Disease Detection App
This file serves as the main entry point for WSGI servers like Gunicorn, uWSGI, or cloud platforms.
Automatically falls back to demo mode if PyTorch dependencies aren't available.
"""

import os
import sys

# Add the src directory to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, 'src')
sys.path.insert(0, src_dir)

# Import the Flask app (will automatically handle PyTorch availability)
try:
    from app import app
    print("✅ Flask app imported successfully")
except ImportError as e:
    print(f"⚠️ Import error: {e}")
    # Create a minimal Flask app as fallback
    from flask import Flask
    app = Flask(__name__)
    
    @app.route('/')
    def fallback():
        return "<h1>Plant Disease Detection</h1><p>App is starting up...</p>"

# This is what WSGI servers will look for
application = app

# For Vercel, we need to export the app
def handler(event, context):
    """AWS Lambda / Vercel handler"""
    return application

if __name__ == "__main__":
    # For local development
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
