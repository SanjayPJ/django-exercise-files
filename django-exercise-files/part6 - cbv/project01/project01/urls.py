"""project01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app00 import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('school-list/', views.SchoolListView.as_view(), name='school-list'),
    path('school-list/<slug:pk>/', views.SchoolDetailView.as_view(), name='school-detail'),
    path('student-list/', views.StudentListView.as_view(), name='student-list'),
    path('student-list/<slug:pk>/', views.StudentDetailView.as_view(), name='student-detail'),
    path('create-student/', views.StudentCreateView.as_view(), name='create-student'),
    path('create-school/', views.SchoolCreateView.as_view(), name='create-school'),
    path('update-school/<slug:pk>/', views.SchoolUpdateView.as_view(), name='update-school'),
    path('update-student/<slug:pk>/', views.StudentUpdateView.as_view(), name='update-student'),
    path('delete-school/<slug:pk>/', views.SchoolDeleteView.as_view(), name='delete-school'),
    path('delete-student/<slug:pk>/', views.StudentDeleteView.as_view(), name='delete-student'),
    path('admin/', admin.site.urls),
]
