from django.urls import path

from .views import blog_detail_view


urlpatterns = [
    path('', blog_detail_view),
]
