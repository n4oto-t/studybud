from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("login/", views.loginPage, name="login"),
    path("", views.home, name="home"),
    # name='room'とすることでurlが"room_hoge/<str:pk>/"に変わっても、template側でも同様にroom_hogeと変更する必要がなくなる。
    path("room/<str:pk>/", views.room, name="room"),
    path("create_room/", views.create_room, name="create_room"),
    path("update_room/<str:pk>", views.update_room, name="update_room"),
    path("delete_room/<str:pk>", views.delete_room, name="delete_room"),
]
