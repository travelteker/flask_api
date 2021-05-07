from flask import Flask

from .tags import tags


def register_routes(app: Flask):
    app.register_blueprint(tags)
