## QA Admin

[![Build Status](https://travis-ci.org/intest-tech/qaadmin.svg?branch=master)](https://travis-ci.org/intest-tech/qaadmin)

[ EN | [中文](https://github.com/intest-tech/qaadmin/blob/master/README.md) ]

Platform used for collecting and sharing testing result. Powered by [Flask](https://github.com/pallets/flask).

## Environment

- Python 3.6
- Ubuntu 16.04
- MongoDB 4.0

## How to

### Deploy locally

1. Install requirement:
```
pip install pipenv
pipenv install
```

2. Set configure:

Create your configure file `config.ini` refer to `config.ini.example`, or just use the example content with:

```
mv config.ini.example config.ini
```

3. Run server:
```
python manage.py runserver
```

### Deploy with Docker

See: [qaadmin-docker](https://github.com/intest-tech/qaadmin-docker)

## Testing

1. Install requirement:
```
pipenv install --dev
```

2. Run test:
```
nosetests tests
```

## SDK

Choose the SDK you need to upload your test result:

Language|Framework|Repository
---|---|---
Python|unittest|[qaa-sdk-pyunit](https://github.com/intest-tech/qaa-sdk-pyunit)
Python|pytest|TODO
Java|TestNG|TODO
Java|Junit|TODO
JavaScript|Mocha|TODO

> [Contact me](mailto:ityoung@foxmail.com)to contribute your SDK!

## About

Author: Shin | HomePage: [Shin's Blog](https://intest.tech)
