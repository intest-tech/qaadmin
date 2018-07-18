from tornado.web import authenticated
from apps.basehandler import BaseHandler
from libs.mongo import get_project_list
import json


class ListProjectHandler(BaseHandler):
    # @authenticated
    async def get(self):
        # res = await get_project_list(self.mongo)
        # self.build_output(res)
        project_list = await get_project_list(self.mongo)
        self.render('index.html', project_list=project_list)

class CreateProjectHandler(BaseHandler):
    async def project_exist(self, project_name: str) -> bool:
        """
        Check project existence
        :param project_name:
        :return: True: pass; False: error
        """
        return bool(await self.mongo['Project'].find_one({'name': project_name}))

    async def get(self):
        self.render('create-project.html')

    @authenticated
    async def post(self, *args, **kwargs):
        project_name = self.get_argument('name')
        project_detail = self.get_argument('detail')
        if not project_name:
            self.write("<script language='javascript'>alert('请输入项目名');window.location.href='create';</script>")
        else:
            project_info = await self.project_exist(project_name)
            if project_info:
                print(project_name )
                self.write("<script language='javascript'>alert('项目已存在');window.location.href='create';</script>")

            new_project = {
                'name': project_name,
                "detail": project_detail
            }
            new_project = self.update_doc_info(new_project)
            result = await self.mongo.Project.insert_one(new_project)
            self.write("<script language='javascript'>alert('新建成功');window.location.href='create';</script>")


class UpdateProjectHandler(BaseHandler):
    @authenticated
    async def post(self, *args, **kwargs):
        pass


class DeleteProjectHandler(BaseHandler):
    @authenticated
    async def post(self, *args, **kwargs):
        pass


class GenTokenHandler(BaseHandler):
    @authenticated
    async def get(self):
        pass
