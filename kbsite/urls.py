"""kbsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path

from pages.views import home_view, contact_view, work_view, hire_me_view, blog_view
from blog.views import blog_detail_view, blog_create_view, blog_modify_view


urlpatterns = [
    path('', home_view, name='home'),
    path('blog/', blog_detail_view),
    path('blogcreate/', blog_create_view),
    path('blogmodify/<int:id>/', blog_modify_view),
    path('contact/', contact_view),
    path('work/', work_view),
    path('hireme/', hire_me_view),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)