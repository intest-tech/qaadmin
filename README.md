## 项目描述

测试报告归档与分享平台，服务端使用[Flask](https://github.com/pallets/flask)驱动。

## 环境

- Python 3.6
- Ubuntu 16.04
- MongoDB 4.0

## 使用

1. 安装依赖：

```
pip install pipenv
pipenv install
```

2. 启动服务：
```
python manager.py runserver
```

## 测试

1. 安装依赖：
```
pipenv install --dev
```

2. 执行测试
```
nosetests tests
```