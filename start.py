#!/usr/bin/env python3
"""
Simple start script for Railway deployment
"""
import os
from wsgi import application

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    
    # Import gunicorn programmatically 
    from gunicorn.app.base import BaseApplication
    
    class StandaloneApplication(BaseApplication):
        def __init__(self, app, options=None):
            self.options = options or {}
            self.application = app
            super().__init__()

        def load_config(self):
            for key, value in self.options.items():
                self.cfg.set(key.lower(), value)

        def load(self):
            return self.application

    options = {
        'bind': f'0.0.0.0:{port}',
        'workers': 1,
        'timeout': 300,
        'keepalive': 2,
        'max_requests': 1000,
        'preload_app': True,
    }

    StandaloneApplication(application, options).run()
