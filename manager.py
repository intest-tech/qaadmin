from flask import Flask, render_template
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


@app.route('/project')
def project():
    return render_template('project.html')


@app.route('/project/<pro_id>')
def project_with_id(pro_id):
    return render_template('project-with-id.html', id=pro_id)


manager = Manager(app)
manager.add_command('runserver', Server(use_debugger=True))

if __name__ == '__main__':
    manager.run()
