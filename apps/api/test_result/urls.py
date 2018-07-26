from .handlers import *

url = [
    (r"/api/test-result", ListResultHandler),
    (r"/api/test-result/latest", LatestResultHandler),
    (r"/test-result/upload", UploadResultHandler),
    (r"/test-result/delete", DeleteResultHandler),
]