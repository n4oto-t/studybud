from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name=""),
    # name='room'とすることでurlが"room_hoge/<str:pk>/"に変わっても、template側でも同様にroom_hogeと変更する必要がなくなる。
    path("room/<str:pk>/", views.room, name="room"),
]
