from .handlers import *

url = [
    ("/project/create", CreateProjectHandler),
    ("/api/project", ListProjectHandler),
    # (r"/project/list", UpdateProjectHandler),
    ("/project/delete", DeleteProjectHandler),
    ("/project/gen-token", GenTokenHandler),
]