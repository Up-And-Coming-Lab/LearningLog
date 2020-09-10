from  django.urls import path,re_path
from  django.conf.urls import url
from django.contrib.auth.views import LoginView,LogoutView
from . import views
"""为应用程序users定义URL模式"""
urlpatterns = [
   # 登录界面  LoginView.as_view后面要加上()
   url(r'^login/$', LoginView.as_view(template_name='users/login.html'), name='login'),
   # 注销
   url(r'^logout',LogoutView.as_view(template_name='learning_logs/index.html'), name='logout'),
   # 注册页面
   url(r'^register/$',views.register,name='register')

]