from django.urls import path
from community.views import *

urlpatterns = [
    path('', index, name='index'),
    path('<int:id>/', community, name='community'),
    path('<int:id>/<int:pk>', posting, name="posting"),
    path('<int:id>/new_post/', new_post, name='new_post'),
    path('<int:id>/<int:pk>/edit', edit_post, name='edit_post'),
    path('<int:id>/<int:pk>/remove/', remove_post, name='remove_post'),
    path('<int:id>/<int:pk>/reply/', reply, name='reply'),
    path('<int:id>/<int:pk>/reply/<int:rid>/edit', edit_reply, name='edit_reply'),
    path('<int:id>/<int:pk>/reply/<int:rid>/remove', remove_reply, name='remove_reply'),
    path('<int:id>/<int:pk>/rereply/<int:rid>', rereply, name='rereply'),
    path('paint', paint, name='paint'),
]
