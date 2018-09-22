# _*_ encoding:utf-8 _*_
__author__ = 'bobby'
__date__ = '18-9-21 下午2:56'

from django.urls import path, include, re_path

from .views import UserinfoView, UploadImageView, UpdatePwdView

urlpatterns = [
    # 用户信息
    path('info/', UserinfoView.as_view(), name="user_info"),

    # 用户头像上传
    path('image/upload/', UploadImageView.as_view(), name="image_upload"),

    # 用户个人中心修改密码
    path('update/pwd/', UpdatePwdView.as_view(), name="update_pwd"),
]

app_name = 'users'