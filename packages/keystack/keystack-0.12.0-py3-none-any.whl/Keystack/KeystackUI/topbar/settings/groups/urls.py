from django.urls import include, path, re_path
from topbar.settings.groups.views import Groups

urlpatterns = [
    re_path('^$', Groups.as_view(), name='groups'),
]

