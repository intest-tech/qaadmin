import os
from flask import Flask, render_template, send_from_directory
from flask_restful import Api
from flask_script import Manager, Server
from apps.route import urls

app = Flask(__name__)

api = Api(app)
for url in urls:
    api.add_resource(url[1], url[0])


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route('/project')
def project():
    return render_template('project-list.html')


@app.route('/project/<pro_id>')
def project_with_id(pro_id):
    return render_template('project-with-id.html', id=pro_id)


manager = Manager(app)
manager.add_command('runserver', Server(use_debugger=True))

if __name__ == '__main__':
    manager.run()
