from django.http import HttpRequest,HttpResponse
from django.shortcuts import render,redirect
from .models import *
from .forms import *

def home(request:HttpRequest) -> HttpResponse:
    rooms = Room.objects.all()
    context = {'rooms':rooms}
    return render(request,'base/home.html',context)

def room(request:HttpRequest,pk:int) -> HttpResponse:
    room = Room.objects.get(id=pk)
    context = {'room':room}
    return render(request,'base/room.html',context)

def createRoom(request:HttpRequest) -> HttpResponse:
    form = RoomForm()
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form}
    return render(request,'base/room_form.html',context)

def updateRoom(request:HttpRequest,pk:int) -> HttpResponse:
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.method == "POST":
        form = RoomForm(request.POST,instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form}
    return render(request,'base/room_form.html',context)

def deleteRoom(request:HttpRequest,pk:int) -> HttpResponse:
    room = Room.objects.get(id=pk)
    if request.method == "POST":
        room.delete()
        return redirect('home')
    return render(request,'base/delete_room.html')

