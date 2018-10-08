import os
from pymongo import MongoClient, DESCENDING
from libs.myconfigparser import config
from libs.crypto import encrypt_password
from bson import ObjectId
import datetime


def conn_mongo():
    DOCKER_FLAG = os.environ.get('DOCKER', False)
    if DOCKER_FLAG:
        conn = MongoClient('mongo', 27017)
    else:
        conn = MongoClient(config['mongo']['host'], int(config['mongo']['port']))
        # conn = MongoClient('localhost', 27017)
    db = conn.qaadmin
    return db


def singleton(cls, *args, **kwargs):
    instances = {}

    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return _singleton


qa_db = conn_mongo()


@singleton
class User(object):
    db = qa_db

    def check(self, username: str, password: str) -> bool:
        user_info = self.db['User'].find_one({'username': username, 'is_del': False})
        if user_info and encrypt_password(password, user_info.get('salt', 0)) == user_info.get('password'):
            return True
        return False


@singleton
class Project(object):
    db = qa_db
    col = db['Project']

    def get(self, name: str) -> dict:
        """
        获取某个 project 信息.
        :param name: project name
        :return: 
        """
        result = self.col.find_one({'_id': name})
        return result

    def get_tags(self, name: str) -> list:
        """
        获取某个 project 信息.
        :param name: project name
        :return: 
        """
        result = self.col.find_one({'_id': name}, {'tags': 1})
        return result.get('tags', [])

    def list(self) -> list:
        """
        获取 project 列表.
        :return: 
        """
        cur = self.col.find({'is_del': False}, {'_id': 1})
        return list(cur)

    def is_exist(self, name: str) -> bool:
        """
        Check project existence
        :param name:
        :return: True: pass; False: error
        """
        return bool(self.get(name))


@singleton
class Result(object):
    db = qa_db
    col = qa_db['xUnitResult']

    def insert(self, new_result):
        return self.col.insert_one(new_result)

    def get(self, id):
        """
        获取 test result 详细数据
        :param id: _id of test result
        :return: 
        """
        find_condition = {'_id': ObjectId(id), 'is_del': False}
        filter_condition = {'is_del': 0, '_id': 0}
        result = self.col.find_one(find_condition, filter_condition)
        return result

    def get_page(self, pro_id, tag, page_index: int, page_size: int) -> dict:
        find_condition = {'is_del': False, 'project': pro_id}
        if tag:
            find_condition['tag'] = tag
        filter_condition = {
            '_id': 1,
            'was_successful': 1,
            'version': 1,
            'create_time': 1,
            'failures': 1,
            'errors': 1,
            'success': 1,
            'duration': 1,
            'details': 1,
            'tag': 1
        }
        count = self.col.count_documents(find_condition)
        result = self.col.find(find_condition, filter_condition) \
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

    def list_detail(self) -> list:
        """
        获取project中最新的测试记录, 用于展示project列表
        :return: 
        """
        project_list = []
        cur = self.db['Project'].find({'is_del': False}, {'_id': 1, 'pipeline': 1})
        result = list(cur)
        print(result)
        for item in result:
            project = item.get('_id')
            pipeline = item.get('pipeline')
            print(pipeline)
            project_info = dict(
                project=project,
                has_record=False,
                success=True,
                version=""
            )

            latest_result = self.col.find_one({'project': project}, sort=[('_id', DESCENDING)])

            if latest_result:
                project_info['version'] = version = latest_result.get('version')
                for stage in pipeline:
                    find_condition = {'stage': stage, 'project': project, 'version': version}
                    filter_condition = {'_id': 0, 'was_successful': 1}
                    test_result = self.col.find_one(find_condition, filter_condition)
                    if test_result:
                        project_info['has_record'] = True
                        if test_result.get('was_successful') is False:
                            project_info['success'] = False

            project_list.append(project_info)
        return project_list

    def list_version(self, project_id):
        """
        获取某项目下所有版本与对应的id
        :param project_id:
        :return:
        """
        versions_list = []
        versions_dict = []
        result = self.col.find({'project': project_id},
                               {'version': 1, 'stage': 1, 'was_successful': 1, "duration": 1},
                               sort=[('_id', DESCENDING)])
        for item in result:
            now_version = item['version'].replace("\n", "")
            if now_version in versions_list:
                version_index = versions_list.index(now_version)
                # stage = versions_dict[version_index].get(item['stage'], None)
                if not versions_dict[version_index].get(item['stage'], None):
                    versions_dict[version_index][item['stage']] = dict(
                        id=str(item['_id']),
                        success=item['was_successful'],
                        duration=item['duration']
                    )
                    versions_dict[version_index]['duration'] += versions_dict[version_index][item['stage']]['duration']
                    versions_dict[version_index]['success'] = versions_dict[version_index]['success'] and item[
                        'was_successful']
                    versions_dict[version_index]['count'] += 1
            else:
                versions_list.append(now_version)
                # todo: get pipeline from project documents.
                new_dict = dict(
                    version=now_version,
                    success=item['was_successful'],
                    count=1,
                    duration=item['duration']
                )
                # todo: change duration to duration
                new_dict[item['stage']] = dict(
                    id=str(item['_id']),
                    success=item['was_successful'],
                    duration=item['duration']
                )
                versions_dict.append(new_dict)
        return versions_dict

    def delete(self, id):
        return self.col.delete_one({'_id': ObjectId(id)}).raw_result


def init_document(document: dict) -> dict:
    """
    为document字典添加create_time, is_del 
    :param document: 插入mongo前的document
    :return: 
    """
    document['create_time'] = datetime.datetime.utcnow()
    document['is_del'] = False
    return document


if __name__ == '__main__':
    b = Result()
    print(b.get_page('gt-api-test', None, 1, 20))
