from app.config import db


def init_db(app):
    db.init_app(app)
