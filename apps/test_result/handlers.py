from apps.basehandler import BaseHandler
from libs.mongo import get_data_list


# from pyecharts import Pie

# REMOTE_HOST = "https://pyecharts.github.io/assets/js"


# class ListResultHandler(BaseHandler):
#     """
#     列出某项目下的所有测试数据
#     """
#     def get(self):
#         pro_id = self.get_argument('pro_id', "")
#         data_list = get_data_list(self.mongo, pro_id)
#         # self.build_output(res)
#         self.render('datalist.html', project=pro_id, data_list=data_list)


# class DetailDataHandler(BaseHandler):
#     """
#
#     """
#     async def get(self):
#         pass

class UploadResultHandler(BaseHandler):
    def post(self, *args, **kwargs):
        token = self.get_argument('token')
        result = self.mongo.Project.find_one({'token': token})
        if not token or not result:
            return self.json_response(status='forbidden', error_msg='token error')
        new_result = self.get_formdatas()
        new_result['project'] = result['_id']
        return self.json_response(new_result)

# class DeleteDataHandler(BaseHandler):
#     def post(self, *args, **kwargs):
#         pass
#
#
# # TODO: 分页
#
# class DrawPieHandler(BaseHandler):
#     def get(self):
#         attr = ['成功', "失败", "错误", "跳过"]
#         v2 = [55, 3, 16, 20]
#         area_color = ["#008B00",
#                       "#CD950C",
#                       "#CD0000",
#                       "#838B8B"]
#         line = Pie("测试结果统计")
#         line.add("测试结果", attr, v2,
#                  label_color=area_color,
#                  is_smooth=True,
#                  mark_line=["max", "average"])
#
#         s3d = line
#         render_em = s3d.render_embed()
#         print(render_em)
#         self.render('piechart.html',
#                     myechart=render_em,
#                     host=REMOTE_HOST,
#                     script_list=s3d.get_js_dependencies(), )
