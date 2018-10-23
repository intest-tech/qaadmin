import uuid
from flask import render_template, request, flash, redirect
from apps.libs.mongo import Project, init_document
from apps.libs.auth import login_required
from . import main


@main.route('/', methods=['GET'])
@login_required
def index():
    return render_template('index.html')


@main.route('/project/<pro_id>')
@login_required
def project_with_id(pro_id):
    return render_template('index.html', id=pro_id)


@main.route('/project/<pro_id>/setting')
@login_required
def project_setting(pro_id):
    return render_template('setting.html', id=pro_id)


@main.route('/project/<pro_id>/job/<job_id>')
@login_required
def project_job_with_id(pro_id, job_id):
    print(pro_id, job_id)
    return render_template('job.html', pro_id=pro_id, job_id=job_id)


@main.route('/project/create', methods=['GET', 'POST'])
@login_required
def project_create():
    if request.method == 'POST':
        project_name = request.form.get('name')
        project_detail = request.form.get('detail')
        error = None
        if not project_name:
            error='error project name'
        else:
            project_info = Project().is_exist(project_name)
            if project_info:
                error='project exist'
        if error is None:
            new_project = {
                '_id': project_name,
                "detail": project_detail,
                "token": uuid.uuid4().hex
            }
            new_project = init_document(new_project)
            # todo: update Project class
            new_project_id = Project().col.insert_one(new_project).inserted_id
            # return json_response({'inserted_id': str(new_project_id)})
            return redirect('/project/'+project_name, code=302)
        flash(error)
    return render_template('create-project.html')