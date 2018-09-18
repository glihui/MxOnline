# _*_ encoding:utf-8 _*_
__author__ = 'bobby'
__date__ = '18-9-18 下午3:28'

from django.urls import path, include, re_path

from .views import CourseListView, CourseDetailView

urlpatterns = [
    # 课程列表页
    path('list/', CourseListView.as_view(), name="course_list"),
    re_path('detail/(?P<course_id>.*)/', CourseDetailView.as_view(), name="course_detail"),
]

app_name = 'course'