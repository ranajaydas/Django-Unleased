from django.urls import path
from .views import (PostList, PostArchiveYear, PostArchiveMonth,
                    PostDetail, PostCreate, PostUpdate, PostDelete)

urlpatterns = [
    path('', PostList.as_view(), name='blog_post_list'),
    path('create/', PostCreate.as_view(), name='blog_post_create'),
    path('<year>/', PostArchiveYear.as_view(), name='blog_post_archive_year'),
    path('<year>/<month>/', PostArchiveMonth.as_view(), name='blog_post_archive_month'),
    path('<year>/<month>/<slug>/', PostDetail.as_view(), name='blog_post_detail'),
    path('<year>/<month>/<slug>/update', PostUpdate.as_view(), name='blog_post_update'),
    path('<year>/<month>/<slug>/delete', PostDelete.as_view(), name='blog_post_delete'),
]
