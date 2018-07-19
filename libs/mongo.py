from pymongo import MongoClient
from libs.myconfigparser import config
from bson import ObjectId


def conn_mongo():
    conn = MongoClient(config['mongo']['host'], int(config['mongo']['port']))
    db = conn.qaadmin
    return db


def get_project_list(db):
    cur = db['Project'].find({'is_del': False}, {'_id': 1, 'token': 1})
    return list(cur)


def get_test_result(db, id):
    find_condition = {'_id': ObjectId(id), 'is_del': False}
    result = db['TestResult'].find_one(find_condition)
    return result


def get_data_list(db, pro_id):
    find_condition = {'is_del': False}
    if pro_id:
        find_condition['project'] = pro_id
    cur = db['TestResult'].find(find_condition).sort('_id', -1)
    return list(cur)


qa_db = conn_mongo()
