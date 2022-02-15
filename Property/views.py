from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from User.models import User
from .forms import *


# Create your views here.


def host(request, pk):
    user = User.objects.get(pk=pk)
    if user:
        print(user.name)
    context = {}
    return render(request, 'host/host.html', context)


def hosting_successful(request, pk):
    user = User.objects.get(pk=pk)
    context = {}
    if user:
        context = {'user': user.name}

    return render(request, 'host/hosting_success.html', context)


def host_personal_room(request, pk):
    user = User.objects.get(pk=pk)
    form = HostPersonalRoomForm(initial={'user_id': user})
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


def host_business_storage(request, pk):
    user = User.objects.get(pk=pk)
    form = HostBusinessStorageForm(initial={'user_id': user})
    context = {'form': form}

    if request.method == 'POST':
        form = HostBusinessStorageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(hosting_successful)
    return render(request, 'host/business_storage_host.html', context)


def host_climate_controlled_storage(request, pk):
    user = User.objects.get(pk=pk)
    form = HostClimateControlledStorageForm(initial={'user_id': user})
    context = {'form': form}

    if request.method == 'POST':
        form = HostClimateControlledStorageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(hosting_successful)
    return render(request, 'host/climate_controlled_storage_host.html', context)


def host_garage(request, pk):
    user = User.objects.get(pk=pk)
    form = HostGarageForm(initial={'user_id': user})
    context = {'form': form}

    if request.method == 'POST':
        form = HostGarageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(hosting_successful)
    return render(request, 'host/garage_host.html', context)
