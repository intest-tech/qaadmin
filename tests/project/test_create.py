from tests.base_testcase import BaseTestCase
from unittest import mock


class TestProjectCreate(BaseTestCase):
    def mock_create_project(self):
        self._patch_method(
            'apps.api.project.handlers.CreateProjectHandler.create_project',
            'new_project')

    def create_app(self):
        return BaseTestCase._create_api(self)

    def test_error_project_name(self):
        req_data = {
            'detail': '123'
        }
        response = self.client.post('/project/create', data=req_data)
        response_dict = response.get_json()
        print(response_dict)
        self.assertEqual(response_dict['status'], 'fail', msg='请求状态异常')
        self.assertEqual(response_dict['message'], 'error project name', msg='错误信息不匹配')

    def test_project_exist(self):
        self.mock_project_exist(True)
        req_data = {
            'name': '124565',
            'detail': '123'
        }
        response = self.client.post('/project/create', data=req_data)
        response_dict = response.get_json()
        print(response_dict)
        self.assertEqual(response_dict['status'], 'fail', msg='请求状态异常')
        self.assertEqual(response_dict['message'], 'project exist', msg='错误信息不匹配')

    def test_project_not_exist(self):
        self.mock_project_exist(False)
        self.mock_create_project()
        req_data = {
            'name': '124565',
            'detail': '123'
        }
        response = self.client.post('/project/create', data=req_data)
        response_dict = response.get_json()
        print(response_dict)
        self.assertEqual(response_dict['status'], 'success', msg='请求状态异常')
        self.assertEqual(response_dict['data']['inserted_id'], 'new_project', msg='返回值不匹配')
