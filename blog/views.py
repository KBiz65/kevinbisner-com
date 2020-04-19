from django.views.generic import ListView
from .models import Post


class PostList(ListView):
    queryset = Post.objects.filter(published=True).order_by("-published_on")
    context_object_name = "posts"
