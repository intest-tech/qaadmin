from flask import request, session, render_template, redirect, flash, url_for
from apps.libs.mongo import User
from apps.libs.auth import login_required
from . import main


@main.route("/login", methods=['GET', 'POST'])
def login():
    next_url = request.args.get('next', "main.index")
    if request.method == 'GET':
        if 'username' in session:
            print("ss", session['username'])
            return redirect('/', code=302)
        return render_template('login.html')
    else:
        username = request.form.get('username', "")
        password = request.form.get('password', "")
        print(username, password)
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
