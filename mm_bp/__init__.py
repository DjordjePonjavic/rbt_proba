from flask import Blueprint
from flask_restplus import Api

measurements_bp = Blueprint("measurements",__name__)
measurements_api = Api(measurements_bp)

from .api import *
