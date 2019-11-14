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
from django.views.generic import RedirectView, TemplateView
from django.urls import path, include
from user import urls as user_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(pattern_name='blog_post_list')),
    path('tag/', include('organizer.urls.tag')),
    path('startup/', include('organizer.urls.startup')),
    path('blog/', include('blog.urls')),
    path('contact/', include('contact.urls')),
    path('about/', TemplateView.as_view(template_name='site/about.html'), name='about_site'),
    path('user/', include(user_urls)),
]
