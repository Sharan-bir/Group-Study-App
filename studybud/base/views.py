from django.http import HttpRequest,HttpResponse
from django.shortcuts import render
from .models import *

def home(request:HttpRequest) -> HttpResponse:
    rooms = Room.objects.all()
    context = {'rooms':rooms}
    return render(request,'base/home.html',context)

def room(request:HttpRequest) -> HttpResponse:
    rooms = Room.objects.all()
    context = {'rooms':rooms}
    return render(request,'base/room.html',context)

def createRoom(request:HttpRequest) -> HttpResponse:
    if request.method == "POST":
        # room_name = request.POST.get('room_name')
        pass
