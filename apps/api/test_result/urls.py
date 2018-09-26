from .handlers import *

url = [
    (r"/api/test-result", ListResultHandler),
    (r"/api/test-result/get-version", ListResultVersionsHandler),
    (r"/api/test-result/latest", LatestResultHandler),
    (r"/api/test-result/upload", UploadResultHandler),
    (r"/test-result/delete", DeleteResultHandler),
]