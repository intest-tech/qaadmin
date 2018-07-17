from apps.project.handlers import *

url = [
    (r"/project/create", CreateProjectHandler),
    (r"/project/list", ListProjectHandler),
    # (r"/project/list", UpdateProjectHandler),
    # (r"/project/list", DeleteProjectHandler),
]