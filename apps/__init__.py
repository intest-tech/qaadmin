from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '123456'

    from .main import (main as main_blueprint, proj as project_blueprint)
    app.register_blueprint(main_blueprint)
    app.register_blueprint(project_blueprint, url_prefix='/project')

    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')

    return app
