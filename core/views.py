from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.

# すべての記事を一覧表示する
def listing(request):
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs
    }
    return render(request, 'listing.html', context)

# ブログ記事を閲覧する
def view_blog(request, blog_id):
    blog = get_object_or_404(Blog, blog_id)
    context = {
        'blog': blog
    }
    return render(request, 'view_blog.html', context)
