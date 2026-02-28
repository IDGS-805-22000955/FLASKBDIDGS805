from flask import Blueprint

alumnos = Blueprint('alumnos', __name__, url_prefix='/alumnos')

from . import routes