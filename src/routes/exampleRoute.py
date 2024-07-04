from flask import make_response, request, Blueprint, jsonify
from src.controllers.sampleEngine import *

bp = Blueprint('bp', __name__)

API_URL = "/example-route/"


@bp.route(API_URL + 'post-example', methods=['POST'])
def sample_return():
    """ Sample api end point, return a string """
    try:
        paras = request.get_json()
        response = sample_engine(paras)
        return make_response(response)
    except Exception as e:
        return make_response(str(e), 500)


@bp.route(API_URL + 'get-example', methods=['GET'])
def sample_get():
    """ Sample api end point, return a string """
    try:
        s = request.args.get('para')
        print(s)
        response = sample_engine(s)
        return make_response(response)
    except Exception as e:
        return make_response(str(e), 500)
