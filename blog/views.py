from django.views.generic import ListView, DetailView
from .models import Post


class PostList(ListView):
    queryset = Post.objects.filter(published=True).order_by("-published_on")
    context_object_name = "posts"


class PostDetail(DetailView):
    context_object_name = "post"
    queryset = Post.objects.filter(published=True)
