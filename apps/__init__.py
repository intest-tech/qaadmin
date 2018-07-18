from tornado.web import authenticated
from apps.basehandler import BaseHandler
from libs.crypto import encrypt_password
import random


class MainHandler(BaseHandler):
    """
    主页，及系统初始化检查
    """

    async def user_check(self):
        """
        检查是否有admin用户，无则创建用户
        :return:
        """
        collections = await self.mongo.list_collection_names()
        if 'User' not in collections:
            salt = random.randint(10, 99)
            new_user = {
                'salt': salt,
                'username': 'admin',
                "password": encrypt_password('admin', salt)}
            new_user = self.update_doc_info(new_user)
            result = await self.mongo.User.insert_one(new_user)

            print('Create user: admin, inserted id: %s' % repr(result.inserted_id))

    @authenticated
    async def get(self, *args, **kwargs):
        await self.user_check()
        self.redirect('/index')


class IndexHandler(BaseHandler):
    """
    主页
    """
    async def get(self, *args, **kwargs):
        self.render('index.html', project_list=[], report=[])


url = [
    (r'/', MainHandler),
    (r'/index', IndexHandler)
]
