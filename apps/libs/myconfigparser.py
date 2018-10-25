import configparser


class MyConfig(object):
    _instance = None

    @staticmethod
    def init(file):
        self = MyConfig()
        self.config = configparser.ConfigParser()
        self.config.read(file)
        MyConfig._instance = self.config
        return MyConfig._instance

    @staticmethod
    def instance():
        if not MyConfig._instance:
            MyConfig.init('config.ini')
        return MyConfig._instance
