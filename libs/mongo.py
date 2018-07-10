from motor.motor_asyncio import AsyncIOMotorClient as MotorClient
from libs.myconfigparser import config

async def conn_mongo():
    conn = MotorClient(config['mongo']['host'], int(config['mongo']['port']))
    db = conn.xtest
    await db.authenticate(
        config['mongo']['user'],
        config['mongo']['password']
    )
    return db

