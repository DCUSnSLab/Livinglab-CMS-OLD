#-*- coding: utf-8 -*-

from . import views
from django.urls import path
from . import views

app_name = "user"

urlpatterns = [
    path('', views.just, name='just'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
]
