import tornado.web
import json

class BaseHandler(tornado.web.RequestHandler):
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
        tornado.web.RequestHandler.initialize(self)
        self.mongo = self.settings['mongo']