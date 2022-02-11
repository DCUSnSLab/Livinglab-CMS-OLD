#-*- coding: utf-8 -*-
from django.conf.urls import url

from . import views
from django.urls import path

app_name = "contents"
urlpatterns = [
    # url(r'^$', views.contents, name='contents'),
    path('', views.contents, name='contents'),
    path('upload/', views.UploadView, name="upload"),
    path('dashboard/', views.DashboardView, name="dashboard"),
    path('update/<int:id>', views.UpdateView, name="update"),
    path('delete/<int:id>', views.DeleteView, name="delete"),
]
