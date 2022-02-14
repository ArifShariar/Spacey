from django.shortcuts import render, redirect
from .forms import *


# Create your views here.


def host(request):
    context = {}
    return render(request, 'host/host.html', context)


def hosting_successful(request):
    return render(request, 'host/hosting_success.html')


def host_personal_room(request):
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
            return redirect(hosting_successful)
    return render(request, 'host/personal_room_host.html', context)


def host_business_storage(request):
    form = HostBusinessStorageForm()
    context = {'form': form}

    if request.method == 'POST':
        form = HostBusinessStorageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(hosting_successful)
    return render(request, 'host/business_storage_host.html', context)


def host_climate_controlled_storage(request):
    form = HostClimateControlledStorageForm()
    context = {'form': form}

    if request.method == 'POST':
        form = HostClimateControlledStorageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(hosting_successful)
    return render(request, 'host/climate_controlled_storage_host.html', context)


def host_garage(request):
    form = HostGarageForm()
    context = {'form': form}

    if request.method == 'POST':
        form = HostGarageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(hosting_successful)
    return render(request, 'host/garage_host.html', context)
