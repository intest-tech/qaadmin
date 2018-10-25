# import uuid
# from flask import request
# from apps.libs.response import json_response
#
# from apps.libs.mongo import Project
# from apps.libs.auth import login_required
# from . import api
#
#
# @api.route("/project/info")
# @login_required
# def get_project_info():
#     id = request.args.get('id', '')
#     if not id:
#         return json_response("", status='fail', error_msg='id required')
#     project_info = Project().get(id, filter={'detail': 1, 'pipeline': 1, 'token': 1})
#     if not project_info:
#         return json_response("", status='fail', error_msg='id invalid')
#     return json_response(project_info)
#
#
# @api.route("/project/pipeline/update", methods=['POST'])
# @login_required
# def update_project_pipeline():
#     # todo: judge logged in.
#     new_pipeline = request.form.get('pipeline')
#     new_pipeline = new_pipeline.replace(' ', '').split(',') if new_pipeline else []
#     id = request.args.get('id', '')
#     project_info = Project().update(id, pipeline=new_pipeline)
#     if not project_info:
#         return json_response("", status='fail', error_msg='id invalid')
#     return json_response("pipeline updated.")
#
#
# @api.route("/project/gen-token", methods=['POST'])
# @login_required
# def gen_token():
#     project = request.form.get('project')
#     if Project().is_exist(project):
#         new_token = uuid.uuid4().hex
#         Project().update(project, token=new_token)
#         return json_response("token updated.")
#     return json_response("", status='fail', error_msg='project id invalid')
#
# # class DeleteProjectHandler(BaseHandler):
# #     # todo: bulk delete
# #     def post(self, *args, **kwargs):
# #         project_name = self.get_formdata('name')
# #         if not project_name:
# #             return self.json_response(status='fail', error_msg='error project name')
# #         else:
# #             project_info = self.Project.is_exist(project_name)
# #             if not project_info:
# #                 return self.json_response(status='fail', error_msg='project not exist')
# #             result = self.mongo.Project.delete_one({'_id': project_name})
# #             print(result)
# #             return self.json_response({'delete_result': result.raw_result})
# #
# # todo: judge token legal
