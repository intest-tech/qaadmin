from apps.project.handlers import *

url = [
    ("/project/create", CreateProjectHandler),
    ("/project", ListProjectHandler),
    # (r"/project/list", UpdateProjectHandler),
    ("/project/delete", DeleteProjectHandler),
    ("/project/gen-token", GenTokenHandler),
]