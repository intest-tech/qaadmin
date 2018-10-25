from flask import Blueprint

main = Blueprint('main', __name__)
proj = Blueprint('project', __name__)

from . import views
from . import auth
from . import project
