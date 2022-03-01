from django.urls import path, include
from .views import listing, view_blog

urlpatterns = [
    path('', listing, name='listing'),
    path('view_blog/<int:blog_id>/', view_blog, name='view_blog'),
]
