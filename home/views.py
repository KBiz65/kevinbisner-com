from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm
from django.views.generic import TemplateView



# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})