from flask import request, render_template, redirect, flash
from apps.libs.mongo import User
from . import main


@main.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form.get('username', '')
        password = request.form.get('password', "")
        print(username, password)
        if User().check(username, password):
            # todo: never clear textbox
            # todo: set session
            return redirect('/', code=302)
        flash("Username or password error!")
        return redirect('/login', code=302)

# @main.route("/logout")
# def logout():
#     # todo: remove session
#     id = request.args.get('id', '')
#     if not id:
#         return json_response("", status='fail', error_msg='id required')
#     project_info = Project().get(id, filter={'detail': 1, 'pipeline': 1, 'token': 1})
#     if not project_info:
#         return json_response("", status='fail', error_msg='id invalid')
#     return json_response(project_info)
