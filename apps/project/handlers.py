from tornado.web import authenticated
from apps.basehandler import BaseHandler
from libs.mongo import get_project_list

class ListProjectHandler(BaseHandler):
    # @authenticated
    async def get(self):
        # res = await get_project_list(self.mongo)
        # self.build_output(res)
        project_list = await get_project_list(self.mongo)
        self.render('dashboard.html', project_list=project_list)

