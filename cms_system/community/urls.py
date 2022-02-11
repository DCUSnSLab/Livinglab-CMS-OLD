from django.urls import path
from community.views import index, community, posting, new_post, remove_post, reply, edit_post, edit_reply, remove_reply

urlpatterns = [
    path('', index, name='index'),
    path('community/<int:id>/', community, name='community'),
    path('community/<int:id>/<int:pk>', posting, name="posting"),
    path('community/<int:id>/new_post/', new_post, name='new_post'),
    path('community/<int:id>/<int:pk>/edit', edit_post, name='edit_post'),
    path('community/<int:id>/<int:pk>/remove/', remove_post, name='remove_post'),
    path('community/<int:id>/<int:pk>/reply/', reply, name='reply'),
    path('community/<int:id>/<int:pk>/reply/<int:rid>/edit', edit_reply, name='edit_reply'),
    path('community/<int:id>/<int:pk>/reply/<int:rid>/remove', remove_reply, name='remove_reply'),
]
