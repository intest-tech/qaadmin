import uuid

from apps.api.project.basehandler import ProjectHandler
from apps.basehandler import BaseHandler
from libs.mongo import get_project_list, get_project_info
from bson import json_util


class ListProjectHandler(BaseHandler):

    def get(self):
        project_list = get_project_list(self.mongo)
        return self.json_response(project_list)


class CreateProjectHandler(ProjectHandler):
    def create_project(self, document):
        return self.mongo.Project.insert_one(document).inserted_id

    # todo: create with token
    def post(self):
        project_name = self.get_formdata('name')
        project_detail = self.get_formdata('detail')
        if not project_name:
            return self.json_response(status='fail', error_msg='error project name')
        else:
            project_info = self.project_exist(project_name)
            if project_info:
                return self.json_response(status='fail', error_msg='project exist')

            new_project = {
                '_id': project_name,
                "detail": project_detail
            }
            new_project = self.update_doc_info(new_project)
            new_project_id = self.create_project(new_project)
            return self.json_response({'inserted_id': str(new_project_id)})


# todo: update project info
# class UpdateProjectHandler(BaseHandler):
#     def post(self, *args, **kwargs):
#         pass
#

class DeleteProjectHandler(ProjectHandler):
    # todo: bulk delete
    def post(self, *args, **kwargs):
        project_name = self.get_formdata('name')
        if not project_name:
            return self.json_response(status='fail', error_msg='error project name')
        else:
            project_info = self.project_exist(project_name)
            if not project_info:
                return self.json_response(status='fail', error_msg='project not exist')
            result = self.mongo.Project.delete_one({'_id': project_name})
            print(result)
            return self.json_response({'delete_result': result.raw_result})


class GenTokenHandler(ProjectHandler):
    """
    生成token, 用于测试数据上传
    """

    def post(self):
        project_name = self.get_formdata('name')
        if not project_name:
            return self.json_response(status='fail', error_msg='error project name')
        else:
            project_info = self.project_exist(project_name)
            if not project_info:
                return self.json_response(status='fail', error_msg='project not exist')
            new_token = uuid.uuid4().hex
            result = self.mongo.Project.update_one({'_id': project_name},
                                                   {'$set': {'token': new_token}})
            print(result)
            return self.json_response({'token': new_token})

class ProjectInfoHandler(ProjectHandler):
    def get(self):
        project = self.get_argument('id')
        if not project:
            return self.json_response(status='fail', error_msg='error project id')
        else:
            project_info = self.project_exist(project)
            if not project_info:
                return self.json_response(status='fail', error_msg='project not exist')
            result = get_project_info(self.mongo, project)
            print(result)
            result = json_util._json_convert(result)
            return self.json_response(result)
