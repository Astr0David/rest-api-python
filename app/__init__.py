from flask import Flask
from app.config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.json.sort_keys = False

    from app.api import character_data

    app.register_blueprint(character_data)

    return app
