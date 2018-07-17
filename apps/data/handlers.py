from tornado.web import authenticated
from apps.basehandler import BaseHandler
from libs.mongo import get_data_list
from pyecharts import Pie

REMOTE_HOST = "https://pyecharts.github.io/assets/js"


class ListDataHandler(BaseHandler):
    """
    列出某项目下的所有测试数据
    """
    @authenticated
    async def get(self):
        pro_id = self.get_argument('pro_id', "")
        data_list = await get_data_list(self.mongo, pro_id)
        # self.build_output(res)
        self.render('datalist.html', project=pro_id, data_list=data_list)


class DetailDataHandler(BaseHandler):
    """

    """
    @authenticated
    async def get(self):
        pass

class UploadDataHandler(BaseHandler):
    @authenticated
    async def post(self, *args, **kwargs):
        pass


class DeleteDataHandler(BaseHandler):
    @authenticated
    async def post(self, *args, **kwargs):
        pass


# TODO: 分页

class DrawPieHandler(BaseHandler):
    async def get(self):
        attr = ['成功', "失败", "错误", "跳过"]
        v2 = [55, 3, 16, 20]
        area_color = ["#008B00",
                      "#CD950C",
                      "#CD0000",
                      "#838B8B"]
        line = Pie("测试结果统计")
        line.add("测试结果", attr, v2,
                 label_color=area_color,
                 is_smooth=True,
                 mark_line=["max", "average"])

        s3d = line
        render_em = s3d.render_embed()
        print(render_em)
        self.render('piechart.html',
                    myechart=render_em,
                    host=REMOTE_HOST,
                    script_list=s3d.get_js_dependencies(), )
