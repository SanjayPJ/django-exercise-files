from django.conf.urls import url, include
from app0 import views

urlpatterns = [
    url(r'^$', views.app0, name='app0')
]
