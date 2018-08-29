from tests.base_testcase import BaseTestCase
from bson import ObjectId
import datetime
from unittest import mock


class TestProjectInfo(BaseTestCase):
    def mock_mongo(self):
        self._patch_method(
            'apps.api.project.handlers.ProjectInfoHandler.mongo',
            None)

    def mock_get_project_info(self):
        result = {
            "_id": "",
            "detail": "",
            "create_time": datetime.datetime(2018, 2, 11, 2, 56, 13, 380000),
            "is_del": False,
            "latest_test": ObjectId("5b3c697647de9d6725b58d96"),
            "token": "",
            "tags": ""
        }
        patcher = mock.patch('apps.basehandler.BaseHandler.Project')
        self._patcher.append(patcher)
        mock_obj = patcher.start()
        mock_obj.get.return_value = result

    def create_app(self):
        return BaseTestCase._create_api(self)

    def test_no_project_id(self):
        response = self.client.get('/project/info')
        response_dict = response.get_json()
        print(response_dict)
        self.assertEqual(response_dict['status'], 'fail', msg='请求状态异常')
        self.assertEqual(response_dict['message'], 'error project id', msg='错误信息不匹配')

    def test_project_not_exist(self):
        self.mock_project_exist(False)
        response = self.client.get('/project/info?id=notexist')
        response_dict = response.get_json()
        print(response_dict)
        self.assertEqual(response_dict['status'], 'fail', msg='请求状态异常')
        self.assertEqual(response_dict['message'], 'project not exist', msg='返回值不匹配')

    def test_project_normal(self):
        self.mock_mongo()
        self.mock_project_exist(True)
        self.mock_get_project_info()
        response = self.client.get('/project/info?id=exist')
        response_dict = response.get_json()
        print(response_dict)
        self.assertEqual(response_dict['status'], 'success', msg='请求状态异常')
        self.assertEqual(13, len(str(response_dict['data']['create_time']['$date'])), msg='时间戳长度不正确')
        self.assertEqual(24, len(response_dict['data']['latest_test']['$oid']), msg='object id长度不正确')
