import bson.errors
from bson import json_util
from flask import request
from apps.libs.response import json_response

from apps.libs.mongo import Project, Result, init_document
from . import api


@api.route('/test-result/get-version')
def get_version_list():
    project_id = request.args.get('project', "", type=str)
    if not project_id:
        return json_response("", status='fail', error_msg='project required')
    result_data = Result().list_version(project_id)
    return json_response(result_data)


@api.route('/test-result/latest')
def get_latest_version():
    result_data = Result().list_detail()
    result_data = json_util._json_convert(result_data)
    return json_response(result_data)


@api.route('/test-result')
def get_test_result():
    project_id = request.args.get('pro_id', "")
    result_id = request.args.get('id', '')
    page_index = request.args.get('p', 1, type=int)
    page_size = request.args.get('ps', 30, type=int)
    tag = request.args.get('tag', None)
    if result_id:
        result_data = Result().get(result_id)
    elif not project_id:
        return json_response("", status='fail', error_msg='id required')
    else:
        result_data = Result().get_page(project_id, tag, page_index, page_size)
    result_data = json_util._json_convert(result_data)
    return json_response(result_data)


@api.route('/test-result/upload', methods=['POST'])
def upload_result():
    token = request.args.get('token')
    result = Project().col.find_one({'token': token})
    if not token or not result:
        return json_response("", status='forbidden', error_msg='token error')
    new_result = request.get_json()
    # todo: check arguments
    # []
    new_result['project'] = result['_id']
    new_result = init_document(new_result)
    insert_result = Result().insert(new_result)
    # todo: update pipeline of project when some stage first created.
    Project().col.update({'_id': result['_id']}, {"$addToSet": {"pipeline": new_result['stage']}})
    return json_response({'inserted_id': str(insert_result.inserted_id)})


@api.route('/test-result/delete')
def delete_result():
    id = request.args.get('id')
    if not id:
        return json_response("", status='fail', error_msg='id required')
    try:
        result = Result().delete(id)
        if result['n'] == 0:
            return json_response("", status='fail', error_msg='no such id')
        return json_response(result)
    except bson.errors.InvalidId:
        return json_response("", status='fail', error_msg='id invalid')
