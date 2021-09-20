from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from api.core.db import db


class TestData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

    def __init__(self, name):
        self.name = name


db.create_all()
