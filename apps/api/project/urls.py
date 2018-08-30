from .handlers import *

url = [
    ("/project/create", CreateProjectHandler),
    # (r"/project/list", UpdateProjectHandler),
    ("/project/delete", DeleteProjectHandler),
    ("/project/gen-token", GenTokenHandler),
    ("/api/project", ListProjectHandler),
    ("/api/project/info", ProjectInfoHandler),
    ("/api/project/get-tags", ProjectTagsHandler),
]