from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import RoomForm
from .models import Room

# rooms = [
#     {"id": 1, "name": "Lets learn python!"},
#     {"id": 2, "name": "Design with me !"},
#     {"id": 3, "name": "Lets learn golang!"},
# ]


def home(request):
    rooms = Room.objects.all()
    context = {"rooms": rooms}
    return render(request, "base/home.html", context)


def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {"room": room}
    return render(request, "base/room.html", context)


def create_room(request):
    form = RoomForm()
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")  ## urls.pyのpath引数のnameを指定。

    context = {"form": form}
    return render(request, "base/room_form.html", context)


def update_room(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.method == "POST":
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect("home")

    context = {"form": form}
    return render(request, "base/room_form.html", context)


def delete_room(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == "POST":
        room.delete()
        return redirect("home")
    return render(request, "base/delete.html", {"obj": room})
