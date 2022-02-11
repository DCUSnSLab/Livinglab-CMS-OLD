from django.urls import path
from . import views

app_name = "display"

urlpatterns = [
    path('', views.just, name='just'),
    path('signage/', views.signageView, name='signage'),
    path('picture/<int:id>', views.picDetail, name="picture"),
]
