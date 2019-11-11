from django.urls import path
from ..views import TagList, TagCreate, TagUpdate, TagDelete, TagDetail


urlpatterns = [
    path('', TagList.as_view(), name='organizer_tag_list'),
    path('create/', TagCreate.as_view(), name='organizer_tag_create'),
    path('<slug>', TagDetail.as_view(), name='organizer_tag_detail'),
    path('<slug>/update', TagUpdate.as_view(), name='organizer_tag_update'),
    path('<slug>/delete', TagDelete.as_view(), name='organizer_tag_delete'),
]
