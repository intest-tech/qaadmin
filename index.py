from flask import Flask
from flask_restful import Api
from apps.route import urls

app = Flask(__name__)
api = Api(app)

# app.config.from_object()

@app.route('/')
def hello():
    return 'hello'

if __name__ == '__main__':
    for url in urls:
        api.add_resource(url[1], url[0])
    app.run()