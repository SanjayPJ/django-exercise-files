from django.conf.urls import url, include
from app1 import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
