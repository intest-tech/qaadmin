import asyncio
from tornado.web import Application
import os
from apps.user.urls import url as user_url


setting = {
    'template_path': os.path.join(os.path.dirname(__file__), "templates")
}

app = Application(
    user_url,
    **setting
)

if __name__ == '__main__':
    from libs.myconfigparser import config
    from libs.mongo import conn_mongo
    app.listen(int(config['server']['port']))
    ioloop = asyncio.get_event_loop()
    app.settings['mongo'] = ioloop.run_until_complete(conn_mongo())
    ioloop.run_forever()