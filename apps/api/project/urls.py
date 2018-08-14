from .handlers import *

url = [
    ("/project/create", CreateProjectHandler),
    ("/project/info", ProjectInfoHandler),
    ("/api/project", ListProjectHandler),
    # (r"/project/list", UpdateProjectHandler),
    ("/project/delete", DeleteProjectHandler),
    ("/project/gen-token", GenTokenHandler),
]