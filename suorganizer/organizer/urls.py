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
from django.urls import path
from .views import (tag_list, tag_detail, TagCreate, TagUpdate, TagDelete,
                    startup_list, startup_detail, StartupCreate, StartupUpdate, StartupDelete,
                    NewsLinkCreate, NewsLinkUpdate, NewsLinkDelete)


urlpatterns = [
    path('tag/', tag_list, name='organizer_tag_list'),
    path('tag/create/', TagCreate.as_view(), name='organizer_tag_create'),
    path('tag/<slug>', tag_detail, name='organizer_tag_detail'),
    path('tag/<slug>/update', TagUpdate.as_view(), name='organizer_tag_update'),
    path('tag/<slug>/delete', TagDelete.as_view(), name='organizer_tag_delete'),
    path('startup/', startup_list, name='organizer_startup_list'),
    path('startup/create/', StartupCreate.as_view(), name='organizer_startup_create'),
    path('startup/<slug>', startup_detail, name='organizer_startup_detail'),
    path('startup/<slug>/update', StartupUpdate.as_view(), name='organizer_startup_update'),
    path('startup/<slug>/delete', StartupDelete.as_view(), name='organizer_startup_delete'),
    path('newslink/create', NewsLinkCreate.as_view(), name='organizer_newslink_create'),
    path('newslink/update/<pk>', NewsLinkUpdate.as_view(), name='organizer_newslink_update'),
    path('newslink/delete/<pk>', NewsLinkDelete.as_view(), name='organizer_newslink_delete'),

]
