import uuid
from flask import request, render_template, redirect, flash
from apps.libs.response import json_response
from apps.libs.mongo import Project, init_document
from apps.libs.auth import login_required
from . import proj


@proj.route("/info")
@login_required
def get_project_info():
    id = request.args.get('id', '')
    if not id:
        return json_response("", status='fail', error_msg='id required')
    project_info = Project().get(id, filter={'detail': 1, 'pipeline': 1, 'token': 1})
    if not project_info:
        return json_response("", status='fail', error_msg='id invalid')
    return json_response(project_info)


@proj.route("/pipeline/update", methods=['POST'])
@login_required
def update_project_pipeline():
    # todo: judge logged in.
    new_pipeline = request.form.get('pipeline')
    new_pipeline = new_pipeline.replace(' ', '').split(',') if new_pipeline else []
    id = request.args.get('id', '')
    project_info = Project().update(id, pipeline=new_pipeline)
    if not project_info:
        return json_response("", status='fail', error_msg='id invalid')
    return json_response("pipeline updated.")


@proj.route("/gen-token", methods=['POST'])
@login_required
def gen_token():
    project = request.form.get('project')
    if Project().is_exist(project):
        new_token = uuid.uuid4().hex
        Project().update(project, token=new_token)
        return json_response("token updated.")
    return json_response("", status='fail', error_msg='project id invalid')


@proj.route('/<pro_id>')
@login_required
def project_with_id(pro_id):
    return render_template('index.html', id=pro_id)


@proj.route('/<pro_id>/setting')
@login_required
def project_setting(pro_id):
    return render_template('setting.html', id=pro_id)


@proj.route('/<pro_id>/job/<job_id>')
@login_required
def project_job_with_id(pro_id, job_id):
    print(pro_id, job_id)
    return render_template('job.html', pro_id=pro_id, job_id=job_id)


@proj.route('/create', methods=['GET', 'POST'])
@login_required
def project_create():
    if request.method == 'POST':
        project_name = request.form.get('name')
        project_detail = request.form.get('detail')
        error = None
        if not project_name:
            error = 'error project name'
        else:
            project_info = Project().is_exist(project_name)
            if project_info:
                error = 'project exist'
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
            return redirect('/project/' + project_name, code=302)
        flash(error)
    return render_template('create-project.html')
