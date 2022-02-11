from . import views
from django.urls import path

app_name = "contents"
urlpatterns = [
    path('', views.contents, name='contents'),
    path('upload/', views.UploadView, name="upload"),
    path('dashboard/', views.DashboardView, name="dashboard"),
    path('update/<int:id>', views.UpdateView, name="update"),
    path('delete/<int:id>', views.DeleteView, name="delete"),
]
