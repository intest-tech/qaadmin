from flask import request
from libs.mongo import Project, init_document
from libs.response import json_response
from . import api


@api.route("/project/info")
def get_project_info():
    id = request.args.get('id', '')
    if not id:
        return json_response("", status='fail', error_msg='id required')
    project_info = Project().get(id, filter={'detail': 1, 'pipeline': 1, 'token': 1})
    if not project_info:
        return json_response("", status='fail', error_msg='id invalid')
    return json_response(project_info)


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