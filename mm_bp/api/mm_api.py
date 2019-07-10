
from mm_bp import measurements_api
from flask_restplus import Resource
from flask import request
from werkzeug.exceptions import Forbidden
from functools import wraps
from config import Config
from flask import request
from schemas import CreateMeasurement

def authentication_required(f):
    @wraps(f)
    def wrapped(*args, **kwargs):

        if not request.authorization:
            raise Forbidden
        
        if request.authorization["username"] != Config.BASIC_AUTH_USERNAME or request.authorization["password"] != Config.BASIC_AUTH_PASSWORD:
            raise Forbidden

        return f(*args, **kwargs)

    return wrapped

@measurements_api.route('/measurements', methods=['POST'])
class Measurements(Resource):

    @authentication_required
    def post(self):
    
        valid_data = CreateMeasurement().load(request.get_json(force=True))

        return valid_data 
