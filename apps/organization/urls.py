# _*_ encoding:utf-8 _*_
__author__ = 'bobby'
__date__ = '18-9-17 下午3:23'


from django.urls import path, include, re_path
from .views import OrgView, AddUserAskView, OrgHomeView, OrgCourseView, OrgDescView, OrgTeacherView, AddFavView

urlpatterns = [
    # 课程机构列表页
    path('list/', OrgView.as_view(), name="org_list"),
    path('add_ask/', AddUserAskView.as_view(), name="add_ask"),
    re_path('home/(?P<org_id>.*)/', OrgHomeView.as_view(), name="org_home"),
    re_path('course/(?P<org_id>.*)/', OrgCourseView.as_view(), name="org_course"),
    re_path('desc/(?P<org_id>.*)/', OrgDescView.as_view(), name="org_desc"),
    re_path('teacher/(?P<org_id>.*)/', OrgTeacherView.as_view(), name="org_teacher"),

    # 机构收藏
    path('add_fav/', AddFavView.as_view(), name="add_fav"),
]

app_name = 'org'
