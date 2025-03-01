from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('room/<int:pk>/',views.room,name="room"),
    path('create_room/',views.createRoom,name="create_room"),
    path('update_room/<int:pk>',views.updateRoom,name="update_room"),
    path('delete_room/<int:pk>',views.deleteRoom,name="delete_room"),
]
