from mongoengine import connect
from flask import current_app


def global_init():
    DB_USER = current_app.config['DB_USER']
    DB_PASSWORD = current_app.config['DB_PASSWORD']
    DB_URI = f'mongodb+srv://{DB_USER}:{DB_PASSWORD}@cluster0.kvp12.mongodb.net/crescendo?retryWrites=true&w=majority'
    connect(host=DB_URI)

