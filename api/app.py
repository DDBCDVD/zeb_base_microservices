from api.core import db
from api.models import test_data

from flask import Flask, request, jsonify, make_response
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, zebrands catalog'


@app.route('/test', methods=['POST'])
def test():
    return 'Test'


@app.route('/create_catalog_website', methods=['POST'])
def create_catalog_website():
    data = request.get_json(request.data)
    return make_response(jsonify(
        {'message': 'Created', 'data': data}), 200)
