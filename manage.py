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
    return render_template('index.html')


@app.route('/project/<pro_id>')
def project_with_id(pro_id):
    return render_template('index.html', id=pro_id)


@app.route('/project/<pro_id>/job/<job_id>')
def job_with_id(pro_id, job_id):
    print(pro_id, job_id)
    return render_template('job.html', pro_id=pro_id, job_id=job_id)


manager = Manager(app)
manager.add_command('runserver', Server(use_debugger=True, host='0.0.0.0'))

if __name__ == '__main__':
    manager.run()
