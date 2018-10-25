from flask_testing import TestCase
from unittest import mock


class BaseTestCase(TestCase):
    def create_app(self):
        from apps import create_app
        return create_app()


    def setUp(self):
        super(BaseTestCase, self).setUp()
        self._patcher = []

    def tearDown(self):
        super(BaseTestCase, self).tearDown()
        for patcher in self._patcher:
            patcher.stop()

    def _patch_method(self, method: str, result):
        """
        patch 某个方法, 使其返回 result
        :param method: 需要被mock.patch的方法
        :param result: 需要被patch方法返回的值
        :return: None
        """
        patcher = mock.patch(method)
        self._patcher.append(patcher)
        mock_obj = patcher.start()
        mock_obj.return_value = result

    # def mock_project_exist(self, result=True):
    #     patcher = mock.patch('apps.basehandler.BaseHandler.Project')
    #     self._patcher.append(patcher)
    #     mock_obj = patcher.start()
    #     mock_obj.exist.return_value = result
