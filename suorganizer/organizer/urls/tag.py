from django.urls import path
from ..views import TagList, TagPageList, tag_detail, TagCreate, TagUpdate, TagDelete


urlpatterns = [
    path('', TagList.as_view(), name='organizer_tag_list'),
    path('<int:page_number>/', TagPageList.as_view(), name='organizer_tag_page'),
    path('create/', TagCreate.as_view(), name='organizer_tag_create'),
    path('<slug>', tag_detail, name='organizer_tag_detail'),
    path('<slug>/update', TagUpdate.as_view(), name='organizer_tag_update'),
    path('<slug>/delete', TagDelete.as_view(), name='organizer_tag_delete'),
]
