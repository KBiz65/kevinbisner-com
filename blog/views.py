from django.shortcuts import render, get_object_or_404

from .forms import BlogpostForm

from .models import Blogpost

# Create your views here.
def blog_detail_view(request):
    posts = list(Blogpost.objects.all().order_by('-id'))
    context = {
        'posts': posts
        }

    return render(request, "blogs/blog_detail_view.html", context)
