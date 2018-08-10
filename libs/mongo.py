from pymongo import MongoClient
from libs.myconfigparser import config
from bson import ObjectId


def conn_mongo():
    conn = MongoClient(config['mongo']['host'], int(config['mongo']['port']))
    # conn = MongoClient('localhost', 27017)
    db = conn.qaadmin
    return db


def get_project_list(db):
    cur = db['Project'].find({'is_del': False}, {'_id': 1})
    return list(cur)


def get_test_result(db, id):
    find_condition = {'_id': ObjectId(id), 'is_del': False}
    filter_condition = {'is_del': 0, '_id': 0}
    result = db['TestResult'].find_one(find_condition, filter_condition)
    return result

def get_latest_result_list(db) -> list:
    """
    获取project中最新的测试记录, 用于展示project列表
    :param db: 
    :return: 
    """
    filter_condition = {'is_del': 0, '_id': 0, 'details': 0, 'run_time': 0}
    latest_result_list = []
    cur = db['Project'].find({'is_del': False}, {'_id': 1, 'latest_test': 1})
    result = list(cur)
    for item in result:
        latest_test = item.get('latest_test')
        if latest_test:
            find_condition = {'_id': latest_test}
            result = db['TestResult'].find_one(find_condition, filter_condition)
            latest_result_list.append(result)
        else:
            latest_result_list.append({'project': item['_id']})
    return latest_result_list

def get_test_result_page(db, pro_id, page_index: int, page_size: int):
    find_condition = {'is_del': False, 'project': pro_id}
    filter_condition = {
        '_id': 1,
        'was_successful': 1,
        'version': 1,
        'create_time': 1,
        'failures': 1,
        'errors': 1,
        'success': 1,
        'run_time': 1
    }
    count = db['TestResult'].count_documents(find_condition)
    # todo: 使用查询过滤后再分页, 提高性能
    # last_id = kwargs.get('last_id', '')
    # if last_id:
    #     find_condition['_id'] = {'$lt': ObjectId(last_id)}
    #     result = db['TestResult'].find(find_condition).sort('_id', -1).limit(page_size)
    # else:
    result = db['TestResult'].find(find_condition, filter_condition) \
        .sort('_id', -1) \
        .skip((page_index - 1) * page_size) \
        .limit(page_size)
    page = dict(
        results=list(result),
        p=page_index,
        ps=page_size,
        total=count
    )
    return page


qa_db = conn_mongo()

if __name__ == '__main__':
    get_test_result_page(qa_db, '124565', 1)
