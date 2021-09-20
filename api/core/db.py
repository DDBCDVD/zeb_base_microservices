import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

FLASK_DATABASE = os.environ.get("FLASK_DATABASE")
app.config['SQLALCHEMY_DATABASE_URI'] = FLASK_DATABASE
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
