from django.conf.urls import url
from . import views,user

urlpatterns = [
        url(r'hello',views.hello),
        url(r'echart',views.echart),
        url(r'index',user.index),
        url(r'reg',user.reg),
        url(r'login',user.login),
        url(r'userlist',user.userlist),
        url(r'update',user.modify),
]
