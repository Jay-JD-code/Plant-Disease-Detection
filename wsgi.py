#!/usr/bin/env python3
"""
Simplified WSGI Entry Point for Vercel Deployment
"""

import os
import sys

# Create Flask app with minimal error handling
try:
    # Import the main app from root directory
    from app import app as main_app
    app = main_app
    print("✅ Main app imported")
except Exception as e:
    print(f"⚠️ Main app import failed: {e}")
    # Create minimal fallback app
    from flask import Flask, jsonify
    app = Flask(__name__)
    
    @app.route('/')
    def index():
        return '''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Plant Disease Detection</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 40px; text-align: center; }
                .container { max-width: 600px; margin: 0 auto; }
                .error { color: #d32f2f; background: #ffebee; padding: 20px; border-radius: 5px; }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>🌱 Plant Disease Detection</h1>
                <div class="error">
                    <h3>Service Temporarily Unavailable</h3>
                    <p>The application is starting up. Please refresh in a moment.</p>
                    <p><strong>Error:</strong> ''' + str(e) + '''</p>
                </div>
            </div>
        </body>
        </html>
        '''
    
    @app.route('/health')
    def health():
        return jsonify({"status": "error", "message": str(e)})

# WSGI application
application = app

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
