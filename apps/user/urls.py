from apps.user.handlers import *

url = [
    (r"/login", LoginHandler),
    (r"/logout", LogoutHandler)
]