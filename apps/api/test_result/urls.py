from .handlers import *

url = [
    (r"/test-result", ListResultHandler),
    (r"/test-result/upload", UploadResultHandler),
    (r"/test-result/delete", DeleteResultHandler),
]