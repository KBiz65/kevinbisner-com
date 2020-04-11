from django.shortcuts import render, get_object_or_404

from .forms import BlogpostForm

from .models import Blogpost

# Create your views here.
def blog_create_view(request):
    form = BlogpostForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = BlogpostForm()

    context = {
        'form': form
        }

    return render(request, "blogs/blog_create_view.html", context)

def blog_modify_view(request, id):
    # obj = Blogpost.objects.get(id=1)
    obj = get_object_or_404(Blogpost, id=id)
    form = BlogpostForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form,
        }

    return render(request, "blogs/blog_modify_view.html", context)

def blog_detail_view(request):
    posts = list(Blogpost.objects.all().order_by('-id'))
    #obj = Blogpost.objects.get()
    context = {
        #'object': obj,
        'posts': posts
        }

    return render(request, "blogs/blog_detail.html", context)
