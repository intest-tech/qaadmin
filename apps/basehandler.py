import tornado.web
import json
import datetime


class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self) -> str:
        """
        根据cookie获取当前用户
        :return: username in cookie
        """
        user = self.get_secure_cookie("user")
        return user.decode('utf8') if user else ""

    def build_output(self, data):
        """
        构建易处理的HTTP输出
        :param data: 
        :return: 
        """
        response = dict(
            data=data,
            code=200,
            message="success"
        )
        response_json = json.dumps(response)
        self.write(response_json)

    def initialize(self):
        """
        Tornado 初始化 Handler 时执行, 将 mongo 赋值为类属性
        :return: 
        """
        tornado.web.RequestHandler.initialize(self)
        self.mongo = self.settings['mongo']

    def update_doc_info(self, document: dict) -> dict:
        """
        为document字典添加create_time, is_del 
        :param document: 插入mongo前的document
        :return: 
        """
        document['create_time'] = datetime.datetime.utcnow()
        document['is_del'] = False
        return document
