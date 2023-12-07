from django.contrib.auth import authenticate, login, logout
from django.shortcuts import HttpResponse, redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Message, Room, Topic
from django.db.models import Q
from .forms import RoomForm


def registerPage(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'somthing went wrong try again')

    return render(request, 'base/login_register.html', {'form': form})


def loginPage(request):
    context = {'page':  'login'}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except Exception:
            messages.error(request, 'Acount does not exits')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'password does not match!')
    return render(request, 'base/login_register.html', context)


def logoutPage(request):
    logout(request)
    return redirect('home')


def home(request):
    q = request.GET.get('q', '')
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(owner__username__icontains=q)
    )
    room_messages = Message.objects.all().filter(Q(room__topic__name__icontains=q)).order_by('-created')
    context = {
        'rooms': rooms,
        'topics': Topic.objects.all(),
        'room_messages': room_messages}
    return render(request, 'base/home.html', context)


def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    if request.method == "POST":
        message = Message.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get('body')
        )
        message.save()
        room.participants.add(request.user)
        return redirect('room', pk=pk)
    return render(request, 'base/room.html', context)


@login_required(login_url='login')
def createRoom(request):
    form = RoomForm
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save(commit=False)
            room.owner = request.user
            room.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/room_form.html', context)


@login_required(login_url="login")
def updateRoom(request, pk):
    context = {}
    room = Room.objects.get(id=pk)
    if room.owner == request.user:
        form = RoomForm(instance=room)
        context = {'form': form}
        if request.method == 'POST':
            form = RoomForm(request.POST, instance=room)
            if form.is_valid:
                form.save()
                return redirect('home')
    else:
        messages.error(request, 'you don\'t have permission to manage this room')
    return render(request, 'base/room_form.html', context)


@login_required(login_url="login")
def deleteRoom(request, pk):
    if request.method == 'POST':
        room = Room.objects.get(id=pk)
        room.delete()
        return redirect('home')
    return render(request, 'base/delete.html')


def deleteMessage(request):
    q = request.GET.get('q')
    message = Message.objects.get(id=q)
    if request.user == message.user:
        room_id = message.room.id
        message.delete()
        room_url = reverse('room', args=[str(room_id)])
        return redirect(room_url)
    else:
        return HttpResponse('you are not allowd here')


def userProfile(request, pk):
    user = User.objects.get(id=pk)
    rooms = Room.objects.all().filter(owner=user)
    room_messages = Message.objects.all().filter(user=user)
    context = {'user': user,
               'rooms': rooms,
               'topics': Topic.objects.all(),
               'room_messages': room_messages,
               }

    return render(request, 'base/user_profile.html', context)
