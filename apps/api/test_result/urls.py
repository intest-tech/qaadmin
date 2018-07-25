from .handlers import *

url = [
    (r"/api/test-result", ListResultHandler),
    (r"/test-result/upload", UploadResultHandler),
    (r"/test-result/delete", DeleteResultHandler),
]