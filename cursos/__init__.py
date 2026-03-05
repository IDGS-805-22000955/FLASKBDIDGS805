from flask import Blueprint

cursos = Blueprint('cursos', __name__, url_prefix='/cursos')

from . import routes