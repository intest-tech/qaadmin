from flask import jsonify, request
from libs.mongo import Project, init_document
from libs.response import json_response
from . import api

# import uuid
# from apps.basehandler import BaseHandler
# from bson import json_util


@api.route("/project")
def list_project():
    project_list = Project().list()
    return jsonify(project_list)


# @api.route('/project/create', methods=['POST'])
# def create_project():
#     # todo: create with token
#     project_name = request.form.get('name')
#     project_detail = request.form.get('detail')
#     if not project_name:
#         return json_response("", status='fail', error_msg='error project name')
#     else:
#         project_info = Project().is_exist(project_name)
#         if project_info:
#             return json_response("", status='fail', error_msg='project exist')
#
#         new_project = {
#             '_id': project_name,
#             "detail": project_detail
#         }
#         new_project = init_document(new_project)
#         # todo: update Project class
#         new_project_id = Project().col.insert_one(new_project).inserted_id
#         return json_response({'inserted_id': str(new_project_id)})
#         # return redirect('/project/'+project_name, code=302)

# class CreateProjectHandler(BaseHandler):
#     def create_project(self, document):
#         return self.mongo.Project.insert_one(document).inserted_id
#
#     # todo: create with token
#     def post(self):
#         project_name = self.get_formdata('name')
#         project_detail = self.get_formdata('detail')
#         if not project_name:
#             return self.json_response(status='fail', error_msg='error project name')
#         else:
#             project_info = self.Project.is_exist(project_name)
#             if project_info:
#                 return self.json_response(status='fail', error_msg='project exist')
#
#             new_project = {
#                 '_id': project_name,
#                 "detail": project_detail
#             }
#             new_project = self.update_doc_info(new_project)
#             new_project_id = self.create_project(new_project)
#             return self.json_response({'inserted_id': str(new_project_id)})
#

# # todo: update project info
# # class UpdateBaseHandler(BaseHandler):
# #     def post(self, *args, **kwargs):
# #         pass
# #
#
# # todo: update project pipeline
#
# class DeleteProjectHandler(BaseHandler):
#     # todo: bulk delete
#     def post(self, *args, **kwargs):
#         project_name = self.get_formdata('name')
#         if not project_name:
#             return self.json_response(status='fail', error_msg='error project name')
#         else:
#             project_info = self.Project.is_exist(project_name)
#             if not project_info:
#                 return self.json_response(status='fail', error_msg='project not exist')
#             result = self.mongo.Project.delete_one({'_id': project_name})
#             print(result)
#             return self.json_response({'delete_result': result.raw_result})
#
#
# class GenTokenHandler(BaseHandler):
#     """
#     生成token, 用于测试数据上传
#     """
#
#     def post(self):
#         project_name = self.get_formdata('name')
#         if not project_name:
#             return self.json_response(status='fail', error_msg='error project name')
#         else:
#             project_info = self.Project.is_exist(project_name)
#             if not project_info:
#                 return self.json_response(status='fail', error_msg='project not exist')
#             new_token = uuid.uuid4().hex
#             result = self.mongo.Project.update_one({'_id': project_name},
#                                                    {'$set': {'token': new_token}})
#             print(result)
#             return self.json_response({'token': new_token})
#
#
# class ProjectInfoHandler(BaseHandler):
#     def get(self):
#         project = self.get_argument('id')
#         if not project:
#             return self.json_response(status='fail', error_msg='error project id')
#         else:
#             project_info = self.Project.is_exist(project)
#             if not project_info:
#                 return self.json_response(status='fail', error_msg='project not exist')
#             result = self.Project.get(project)
#             print(result)
#             result = json_util._json_convert(result)
#             return self.json_response(result)
#
#
# class ProjectTagsHandler(BaseHandler):
#     """
#     获取Project的tag
#     """
#     def get(self):
#         project = self.get_argument('id')
#         if not project:
#             return self.json_response(status='fail', error_msg='error project id')
#         else:
#             project_info = self.Project.is_exist(project)
#             if not project_info:
#                 return self.json_response(status='fail', error_msg='project not exist')
#             result = self.Project.get_tags(project)
#             print(result)
#             return self.json_response(result)
