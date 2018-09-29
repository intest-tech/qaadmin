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

    @property
    def User(self):
        from libs.mongo import User
        return User()

    @property
    def Project(self):
        from libs.mongo import Project
        return Project()

    @property
    def Result(self):
        from libs.mongo import Result
        return Result()

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
