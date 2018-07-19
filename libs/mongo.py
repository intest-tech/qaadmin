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

async def get_data_list(db, pro_id):
    find_condition = {'is_del': False}
    if pro_id:
        pro_id = ObjectId(pro_id)
        find_condition['pro_id'] = pro_id
    cur = db['unit_test_data'].find(find_condition, {'_id': 0, 'pro_version': 1, 'was_successful': 1})
    res = await cur.to_list(10)
    return res

qa_db = conn_mongo()