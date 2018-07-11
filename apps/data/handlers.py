from apps.basehandler import BaseHandler
from libs.mongo import get_data_list


class ListDataHandler(BaseHandler):
    async def get(self):
        pro_id = self.get_argument('pro_id', "")
        data_list = await get_data_list(self.mongo, pro_id)
        # self.build_output(res)
        self.render('datalist.html', project=pro_id, data_list=data_list)

# TODO: 分页
