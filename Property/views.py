from django.shortcuts import render, redirect
from .forms import *


# Create your views here.


def host(request):
    form = HostPersonalRoomForm()
    room = CreateRoomForm()
    context = {'form': form, 'room': room}

    if request.method == 'POST':
        form = HostPersonalRoomForm(request.POST)
        room = CreateRoomForm(request.POST)
        if form.is_valid() and room.is_valid():
            user_id = form.data.get('user_id')
            print(user_id)
    return render(request, 'host/host.html', context)
