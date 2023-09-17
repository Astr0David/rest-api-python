import os
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv()

db = SQLAlchemy()

url = os.getenv("DATABASE_URL")


class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = url
