from functools import wraps
from flask import request, session, redirect, url_for
from .mongo import User


def login_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        # if current_app.config.get('LOGIN_DISABLED'):
        #     return func(*args, **kwargs)
        user = session.get('username')
        if user and User().exists(user):
            return func(*args, **kwargs)
        else:
            return redirect(url_for('main.login', next=request.endpoint))

    return decorated_function


# todo: admin required
# todo: permission system
# def admin_required(func):
#     @wraps(func)
#     def decorated_function(*args, **kwargs):
#         # if current_app.config.get('LOGIN_DISABLED'):
#         #     return func(*args, **kwargs)
#         user = session.get('username')
#         if user and User().exists(user):
#             return func(*args, **kwargs)
#         else:
#             return redirect(url_for('main.login', next=request.endpoint))
#
#     return decorated_function
