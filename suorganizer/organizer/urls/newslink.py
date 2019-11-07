from django.urls import path
from ..views import NewsLinkCreate, NewsLinkUpdate, NewsLinkDelete


urlpatterns = [
    path('create', NewsLinkCreate.as_view(), name='organizer_newslink_create'),
    path('update/<pk>', NewsLinkUpdate.as_view(), name='organizer_newslink_update'),
    path('delete/<pk>', NewsLinkDelete.as_view(), name='organizer_newslink_delete'),
]
