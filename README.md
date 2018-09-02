## QA Admin

[![Build Status](https://travis-ci.org/intest-tech/qaadmin.svg?branch=master)](https://travis-ci.org/intest-tech/qaadmin)

测试报告归档与分享平台，服务端使用[Flask](https://github.com/pallets/flask)驱动。

## 环境

- Python 3.6
- Ubuntu 16.04
- MongoDB 4.0

## 使用

### 方法一: 本地安装

1. 安装依赖：

```
pip install pipenv
pipenv install
```

2. 启动服务：

```
python manage.py runserver
```

### 方法二: Docker 安装

使用项目: [qaadmin-docker](https://github.com/intest-tech/qaadmin-docker)

## 测试

1. 安装依赖：
```
pipenv install --dev
```

2. 执行测试
```
nosetests tests
```

## SDK

使用下列SDK实现测试结果上传：

- Python unittest: [qaa-sdk-pyunit](https://github.com/intest-tech/qaa-sdk-pyunit)
- Python pyunit: TODO
- Java TestNG: TODO
- Java Junit: TODO

> 欢迎[联系我](mailto:ityoung@foxmail.com)贡献您的SDK!

## 关于

设计&后端开发：严北 | 博客主页：[Shin's Blog](https://intest.tech) | 简书专题：[测试开发实践](https://www.jianshu.com/c/b4b2bd0cb60d)

前端开发：[CroveWang](https://github.com/orgs/intest-tech/people/MinistryWJW)
