from functools import wraps
from flask import request, session, redirect, url_for
from .mongo import User
from apps.libs.myconfigparser import MyConfig

config = MyConfig.instance()

def check_sk(secret_key: str) -> bool:
    """
    验证secret_key, 用于注册用户与重置其他用户密码
    :param secret_key: 
    :return: 
    """
    try:
        if secret_key == config['admin']['secret_key']:
            return True
        return False
    except:
        return False


def login_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if config.getboolean('security', 'LOGIN_DISABLED'):
            return func(*args, **kwargs)
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

# todo: token required
