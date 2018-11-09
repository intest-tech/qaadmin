from flask import request, session, render_template, redirect, flash, url_for
from apps.libs.mongo import User
from apps.libs.auth import login_required, check_sk
from . import main


@main.route("/register", methods=["GET", "POST"])
def register():
    """
    用户注册接口
    输入正确的secret_key才能注册用户
    :return: 
    """
    if request.method == "GET":
        return render_template('register.html')
    else:
        secret_key = request.form.get('secret_key', "")
        username = request.form.get('username', "")
        password = request.form.get('password', "")
        if secret_key and check_sk(secret_key):
            if username and len(password) > 6 and not User().exists(username):
                User().new(username, password)
                session['username'] = username
                return redirect('/', code=302)
            else:
                error = "Username or password error!"
        else:
            error = "Secret key error!"
        flash(error)
        return redirect('/register', code=302)


@main.route("/login", methods=['GET', 'POST'])
def login():
    """
    /login接口
    GET: 获取登录页面
    POST: 发送登录请求
    :return: 
    """
    next_url = request.args.get('next', "main.index")
    if request.method == 'GET':
        if 'username' in session:
            return redirect('/', code=302)
        return render_template('login.html')
    else:
        username = request.form.get('username', "")
        password = request.form.get('password', "")
        if User().check(username, password):
            # todo: never clear textbox
            session['username'] = username
            return redirect(url_for(next_url))
        flash("Username or password error!")
        return redirect('/login', code=302)


@main.route("/logout")
@login_required
def logout():
    session.pop('username', None)
    return redirect('/login', code=302)
