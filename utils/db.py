from flask_pymongo import PyMongo
from flask import Flask
from config import Config

mongo = PyMongo()

def init_db(app: Flask):
    app.config.from_object(Config)
    mongo.init_app(app)
