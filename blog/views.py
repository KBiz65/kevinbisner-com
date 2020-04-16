from django.shortcuts import render
from .models import Post


def blog_detail_view(request):
    posts = list(Post.objects.all().order_by('-id'))
    context = {
        'posts': posts
    }

    return render(request, "blogs/blog_detail_view.html", context)
