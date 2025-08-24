#!/usr/bin/env python3
"""
WSGI Entry Point for Plant Disease Detection App
This file serves as the main entry point for WSGI servers like Gunicorn, uWSGI, or cloud platforms.
"""

import os
import sys

# Add the src directory to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, 'src')
sys.path.insert(0, src_dir)

# Import the Flask app
from app import app

# This is what WSGI servers will look for
application = app

if __name__ == "__main__":
    # For local development
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=False)
