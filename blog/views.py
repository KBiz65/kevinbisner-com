from django.shortcuts import render
from .models import Post


def post_list(request):
    posts = list(Post.objects.all().order_by('-published_on'))
    context = {
        'posts': posts
    }

    return render(request, "blogs/post_list.html", context)
