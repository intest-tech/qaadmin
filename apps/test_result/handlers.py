from apps.basehandler import BaseHandler
from libs.mongo import get_test_result_page, get_test_result
from bson import json_util, ObjectId
import bson.errors


class ListResultHandler(BaseHandler):
    """
    列出某项目下的所有测试数据
    """

    def get(self):
        project_id = self.get_argument('pro_id', "")
        result_id = self.get_argument('id', '')
        page_index = int(self.get_argument('p', 1))
        page_size = int(self.get_argument('ps', 30))
        if result_id:
            result_data = get_test_result(self.mongo, result_id)
        elif not project_id:
            return self.json_response(status='fail', error_msg='id required')
        else:
            result_data = get_test_result_page(self.mongo,
                                               project_id,
                                               page_index,
                                               page_size)
        result_data = json_util._json_convert(result_data)
        return self.json_response(result_data)


class UploadResultHandler(BaseHandler):
    def post(self, *args, **kwargs):
        token = self.get_argument('token')
        result = self.mongo.Project.find_one({'token': token})
        if not token or not result:
            return self.json_response(status='forbidden', error_msg='token error')
        new_result = self.get_formdatas()
        # todo: check arguments
        # []
        new_result['project'] = result['_id']
        new_result = self.update_doc_info(new_result)
        insert_result = self.mongo.TestResult.insert_one(new_result)
        return self.json_response({'inserted_id': str(insert_result.inserted_id)})


class DeleteResultHandler(BaseHandler):
    def delete(self, id):
        return self.mongo['TestResult'].delete_one({'_id': ObjectId(id)})

    def post(self, *args, **kwargs):
        id = self.get_argument('id')
        if not id:
            return self.json_response(status='fail', error_msg='id required')
        try:
            result = self.delete(id).raw_result
            if result['n'] == 0:
                return self.json_response(status='fail', error_msg='no such id')
            return self.json_response(result)
        except bson.errors.InvalidId:
            return self.json_response(status='fail', error_msg='id invalid')
