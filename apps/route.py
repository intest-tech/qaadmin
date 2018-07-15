from apps import url as main_url
from apps.user.urls import url as user_url
from apps.project.urls import url as project_url
from apps.data.urls import url as data_url

urls = main_url + user_url + project_url + data_url
