from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})

def blog_view(request, *args, **kwargs):
    my_context = {
        "my_text": "Welcome to my blog",
        "my_number": 123,
        "my_blog_list": [123, 165, 999, "KBIZ!"]
    }
    return render(request, "blog.html", my_context)

def work_view(request, *args, **kwargs):
    return render(request, "work.html", {})

def hire_me_view(request, *args, **kwargs):
    return render(request, "hireme.html", {})

def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})