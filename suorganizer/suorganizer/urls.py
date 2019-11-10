"""suorganizer URL Configuration

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
from django.contrib import admin
from django.contrib.flatpages import urls as flatpages_urls
from django.urls import path, include
from .views import redirect_root


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', redirect_root),
    path('tag/', include('organizer.urls.tag')),
    path('startup/', include('organizer.urls.startup')),
    path('newslink/', include('organizer.urls.newslink')),
    path('blog/', include('blog.urls')),
    path('contact/', include('contact.urls')),
    path('', include(flatpages_urls)),  # Used for the About page at /about
]
