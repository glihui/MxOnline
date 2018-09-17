# _*_ encoding:utf-8 _*_
__author__ = 'bobby'
__date__ = '18-9-17 下午3:23'


from django.urls import path, include, re_path
from .views import OrgView, AddUserAskView

urlpatterns = [
    # 课程机构列表页
    path('list/', OrgView.as_view(), name="org_list"),
    path('add_ask/', AddUserAskView.as_view(), name="add_ask"),
]

app_name = 'org'
