# app/__init__.py
from flask import Flask
from flask_restful import Api
from .routes import ExampleResource

def create_app():
    app = Flask(__name__)
    api = Api(app)

    # Register routes
    api.add_resource(ExampleResource, '/api/example')

    return app
