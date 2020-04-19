from django.shortcuts import render
from .models import Post


class PostList(ListView):
    queryset = Post.objects.filter(published=True).order_by("-published_at")
    context_object_name = "posts"
