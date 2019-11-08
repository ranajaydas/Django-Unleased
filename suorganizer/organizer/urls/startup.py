from django.urls import path
from ..views import StartupList, startup_detail, StartupCreate, StartupUpdate, StartupDelete

urlpatterns = [
    path('', StartupList.as_view(), name='organizer_startup_list'),
    path('create/', StartupCreate.as_view(), name='organizer_startup_create'),
    path('<slug>', startup_detail, name='organizer_startup_detail'),
    path('<slug>/update', StartupUpdate.as_view(), name='organizer_startup_update'),
    path('<slug>/delete', StartupDelete.as_view(), name='organizer_startup_delete'),
]
