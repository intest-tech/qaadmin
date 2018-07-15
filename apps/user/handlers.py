from apps.basehandler import BaseHandler
from libs.crypto import encrypt_password
from libs.mongo import get_project_list


class LoginHandler(BaseHandler):
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
            # todo: set cookies
            project_list = await get_project_list(self.mongo)
            self.render('index.html', project_list=project_list)
        else:
            # todo: never clear textbox
            self.write("<script language='javascript'>alert('登录失败, 请检查用户名或密码');window.location.href='login';</script>")

    def get(self):
        self.render('login.html')
