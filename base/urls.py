from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [path("", views.home, name=""), path("room/", views.room, name="room")]
