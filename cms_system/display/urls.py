#-*- coding: utf-8 -*-
from django.conf.urls import url
from . import views
from django.urls import path
from . import views

app_name = "display"

urlpatterns = [
    path('', views.just, name='just'),
    path('signage/', views.signageView, name='signage'),
    path('projector/', views.projectorView, name='projector'),

    path('test/', views.testView, name='test'),
    path('test2/',views.test2,name= "test2"),
    path('test3/',views.test3,name= "test3"),

    # path('signup/', views.signup, name='signup'),
    # path('logout/', views.logout, name='logout'),
]
