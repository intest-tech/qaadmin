# from apps import url as main_url
# from apps.user.urls import url as user_url
from apps.project.urls import url as project_url
from apps.test_result.urls import url as test_result_url

# urls = main_url + user_url + project_url + test_result_url
urls = project_url + test_result_url