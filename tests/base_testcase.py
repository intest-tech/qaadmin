from flask_testing import TestCase
from unittest import mock


class BaseTestCase(TestCase):
    def create_app(self):
        from index import app
        return app

    def _create_api(self):
        from flask import Flask
        from flask_restful import Api
        from apps.route import urls

        app = Flask(__name__)
        api = Api(app)
        for url in urls:
            api.add_resource(url[1], url[0])
        return app

    def setUp(self):
        super(BaseTestCase, self).setUp()
        print(1)
        self._patcher = []

    def tearDown(self):
        super(BaseTestCase, self).tearDown()
        print(2)
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
