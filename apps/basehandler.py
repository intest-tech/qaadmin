# import tornado.web
# import flask.views
from flask import make_response, request
from flask_restful import Resource
import json
import datetime
# import time


def set_headers(response, origin):
    response.headers['Access-Control-Allow-Origin'] = origin
    response.headers['Access-Control-Allow-Methods'] = 'POST, GET, OPTIONS'
    response.headers['Access-Control-Allow-Credentials'] = "true"
    response.headers['Access-Control-Max-Age'] = 1678000
    response.headers['Access-Control-Allow-Headers'] = 'origin, x-csrftoken, content-type, accept'
    response.headers['Server'] = 'PHP'
    return response


class BaseHandler(Resource):
    # def get_current_user(self) -> str:
    #     """
    #     根据cookie获取当前用户
    #     :return: username in cookie
    #     """
    #     user = self.get_secure_cookie("user")
    #     return user.decode('utf8') if user else ""

    @property
    def mongo(self):
        from libs.mongo import qa_db
        return qa_db

    def get_argument(self, args, default=None):
        """
        获取Query String中的请求参数
        :param args: 
        :param default: 
        :return: 
        """
        return request.args.get(args, default)

    def get_formdata(self, args, default=None):
        """
        获取Form Data中的请求参数
        :param args: 
        :param default: 
        :return: 
        """
        return request.form.get(args, default)

    def get_formdatas(self):
        """
        获取Form Data中的JSON请求参数
        :return: 
        """
        # req = request.form
        # json_args = request.get_json()
        return request.get_json()

    def json_response(self, data={}, status='success', error_msg='', **kwargs):
        """
        构建易处理的HTTP输出
        :param status: 
        :param error_msg: 
        :param data: 
        :param kwargs: 
        :return: 
        """
        if isinstance(data, dict):
            data.update(kwargs)
        response = dict(
            data=data,
            status=status,
            message=error_msg
        )
        return response

    def update_doc_info(self, document: dict) -> dict:
        """
        为document字典添加create_time, is_del 
        :param document: 插入mongo前的document
        :return: 
        """
        document['create_time'] = datetime.datetime.utcnow()
        # document['create_time'] = time.time()
        document['is_del'] = False
        return document
