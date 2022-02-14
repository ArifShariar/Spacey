from django.shortcuts import render, redirect
from .forms import *

# Create your views here.


def host(request):
    form = HostPersonalRoomForm()
    context = {'form': form}

    if request.method == 'POST':
        form = HostPersonalRoomForm(request.POST)
        if form.is_valid():
            name = form.data.get('property_name')
            description = form.data.get('description')
            location = form.data.get('location')
            size = form.data.get('size')
            facilities = form.data.get('facilities')
            rooms = form.data.get('rooms')
            print(name, description, location, size, facilities, rooms)
            form.save()
    return render(request, 'host/personal_room_host.html', context)
