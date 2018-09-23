from flask import Flask, render_template
from flask_restful import Api
from apps.route import urls

app = Flask(__name__)
api = Api(app)


# app.config.from_object()

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/project')
def project():
    return render_template('project-list.html')


@app.route('/project/<pro_id>')
def project_with_id(pro_id):
    return render_template('project-with-id.html', id=pro_id)


if __name__ == '__main__':
    for url in urls:
        api.add_resource(url[1], url[0])
    app.run()
