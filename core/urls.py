from django.urls import path, include
from .views import *

urlpatterns = [
    path('', listing, name='listing'),
    path('view_blog/<int:blog_id>/', view_blog, name='view_blog'),
    path('see_request', see_request, name='see_request'),
    path('user_info', user_info, name='user_info'),
    path('private_place', private_place, name='private_place'),
    path('staff_place', staff_place, name='staff_place'),
    path('add_messages', add_messages, name='add_messages'),
]
