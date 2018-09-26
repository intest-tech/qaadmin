import pymongo
import uuid
from pymongo.mongo_client import MongoClient

xutest_host = '192.168.1.200'
xutest_port = 27027

qaadmin_host = 'localhost'
qaadmin_port = 27017


def conn_xutest(host, port):
    conn = MongoClient(host, int(port))
    return conn.xtest


def conn_qaadmin(host, port):
    conn = MongoClient(host, int(port))
    return conn.qaadmin


def find_latest_test(xu_db, project):
    result = xu_db.unit_test_data.find_one({'pro_id': project, 'is_del': False},
                                           sort=[('_id', pymongo.DESCENDING)])
    if result:
        return result['_id']
    else:
        return None


def migrate_project(xu_db, qa_db):
    old_project = xu_db.test_project.find()
    for item in old_project:
        if item['is_del'] is True:
            continue
        new_project = {
            "_id": item['project_name'],
            "detail": item['mark'],
            "create_time": item['rc_time'],
            "is_del": item['is_del'],
            # TODO:
            "latest_test": find_latest_test(xu_db, item['_id']),
            "token": uuid.uuid4().hex
        }
        tags = item.get('tags', None)
        if tags:
            new_project['tags'] = tags
        print(new_project)
        qa_db.Project.insert(new_project)


def migrate_result(xu_db, qa_db):
    old_result = xu_db.unit_test_data.find()
    for item in old_result:
        if item['is_del'] is True:
            continue
        total = item['total']
        failures = item['failures']
        errors = item['errors']
        skipped = item['skipped']
        success = total - failures - errors - skipped
        new_result = {
            "_id": item['_id'],
            "was_successful": item['was_successful'],
            "total": total,
            "failures": failures,
            "errors": errors,
            "success": success,
            "skipped": skipped,
            "run_time": item['run_time'],
            "version": item['pro_version'],
            "project": item['pro_name'],
            "create_time": item['rc_time'],
            "is_del": False,
            'tag': item.get('tag', 'default'),
            "details": item.get('details', [])
        }
        print(new_result)
        qa_db.xUnitResult.insert(new_result)


if __name__ == '__main__':
    xu_db = conn_xutest(xutest_host, xutest_port)
    qa_db = conn_qaadmin(qaadmin_host, qaadmin_port)
    migrate_project(xu_db, qa_db)
    migrate_result(xu_db, qa_db)
