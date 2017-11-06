from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.index),
	url(r'idc',views.idc),
	url(r'server',views.server),
]
