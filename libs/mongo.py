from motor.motor_asyncio import AsyncIOMotorClient as MotorClient
from libs.myconfigparser import config
from bson import ObjectId

async def conn_mongo():
    conn = MotorClient(config['mongo']['host'], int(config['mongo']['port']))
    db = conn.xtest
    # await db.authenticate(
    #     config['mongo']['user'],
    #     config['mongo']['password']
    # )
    return db

async def get_project_list(db):
    cur = db['test_project'].find({'is_del': False}, {'_id': 0, 'project_name': 1}).count()
    res = await cur.to_list(10)
    return res

async def get_data_list(db, pro_id):
    find_condition = {'is_del': False}
    if pro_id:
        pro_id = ObjectId(pro_id)
        find_condition['pro_id'] = pro_id
    cur = db['unit_test_data'].find(find_condition, {'_id': 0, 'pro_version': 1, 'was_successful': 1})
    res = await cur.to_list(10)
    return res