## Description

Platform used for collecting and sharing testing result. Powered by [Flask](https://github.com/pallets/flask).

## Environment

- Python 3.6
- Ubuntu 16.04
- MongoDB 4.0

## How to

1. Install requirement:
```
pip install pipenv
pipenv install
```

2. Run server:
```
python manager.py runserver
```

## Testing

1. Install requirement:
```
pipenv install --dev
```

2. Run test:
```
nosetests tests
```