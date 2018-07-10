import tornado.web
from libs.crypto import encrypt_password


class LoginHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.mongo = self.settings['mongo']

    async def login_check(self, username: str, password: str) -> bool:
        """
        Check username and password
        :param username: 
        :param password: 
        :return: True: pass; False: error
        """
        user_info = await self.mongo['g_users'].find_one({'user_id': username})
        if user_info and encrypt_password(password, user_info.get('salt', 0)) == user_info.get('passwd'):
            return True
        return False

    async def post(self, *args, **kwargs):
        user = self.get_argument('username')
        pwd = self.get_argument('password')
        if await self.login_check(user, pwd):
            # todo: redirect to dashboard
            self.write('ok')
        else:
            # todo: redirect to login page
            self.write('no')

    def get(self):
        self.render('login.html')
