from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse("home page")


def room(request):
    return HttpResponse("Room")
