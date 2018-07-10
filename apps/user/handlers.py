import tornado.web
import json


class LoginHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.mongo = self.settings['mongo']

    async def post(self, *args, **kwargs):
        user = self.get_argument('username')
        # todo: user in mongo
        print(user)
        if await self.mongo['g_users'].find_one({'user_id': user}):
            self.write('ok')
        else:
            self.write('no')

    def get(self):
        self.render('login.html')
