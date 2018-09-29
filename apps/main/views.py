from . import main
from flask import render_template


@main.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@main.route('/project/<pro_id>')
def project_with_id(pro_id):
    return render_template('index.html', id=pro_id)


@main.route('/project/<pro_id>/setting')
def project_setting(pro_id):
    return render_template('setting.html', id=pro_id)


@main.route('/project/<pro_id>/job/<job_id>')
def job_with_id(pro_id, job_id):
    print(pro_id, job_id)
    return render_template('job.html', pro_id=pro_id, job_id=job_id)
