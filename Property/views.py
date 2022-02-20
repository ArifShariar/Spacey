from django.db.models import Q
from django.shortcuts import render, redirect
from User.models import User
from Property.models import Storage
from .forms import *
from .models import *


# Create your views here.


def host(request, pk):
    user = User.objects.get(pk=pk)
    if user:
        print(user.name)
    context = {'user': user}
    return render(request, 'host/host.html', context)


def hosting_successful(request, pk):
    user = User.objects.get(pk=pk)
    context = {}
    if user:
        context = {'user': user}

    return render(request, 'host/hosting_success.html', context)


# def openPhotosUI()

def addPhoto(request, pk):
    images = request.POST.getlist('images')
    user_id = request.POST.get('id', False)
    desc = request.POST.get('desc', False)
    loc = request.POST.get('loc', False)
    storage_type = request.POST.get('type', False)
    if storage_type == "Personal":
        storage = Personal.objects.get(Q(user_id=user_id) & Q(description=desc) & Q(location=loc))
    elif storage_type == "Business":
        storage = Business.objects.get(Q(user_id=user_id) & Q(description=desc) & Q(location=loc))
    elif storage_type == "ClimateControlled":
        storage = ClimateControlled.objects.get(Q(user_id=user_id) & Q(description=desc) & Q(location=loc))
    else:
        storage = Garage.objects.get(Q(user_id=user_id) & Q(description=desc) & Q(location=loc))
    print(len(images))
    for image in images:
        photo = Photo(
            image=image,
            storageID=storage.pk,
            storageType=storage_type
        )
        photo.save()
    return render(request, 'host/hosting_success.html')


def host_personal_room(request, pk):
    user = User.objects.get(pk=pk)
    form = HostPersonalRoomForm(initial={'user_id': user})
    context = {'form': form}

    if request.method == 'POST':
        form = HostPersonalRoomForm(request.POST)
        if form.is_valid():
            description = form.data.get('description')
            location = form.data.get('location')
            form.save()
            s_type = "Personal"
            context = {'pk': pk, 'type': s_type, 'description': description, 'location': location}
            return render(request, 'addPhotos.html', context)
    return render(request, 'host/personal_room_host.html', context)


def host_business_storage(request, pk):
    user = User.objects.get(pk=pk)
    form = HostBusinessStorageForm(initial={'user_id': user})
    context = {'form': form}

    if request.method == 'POST':
        form = HostBusinessStorageForm(request.POST)
        if form.is_valid():
            description = form.data.get('description')
            location = form.data.get('location')
            form.save()
            s_type = "Business"
            context = {'pk': pk, 'type': s_type, 'description': description, 'location': location}
            return render(request, 'addPhotos.html', context)
    return render(request, 'host/business_storage_host.html', context)


def host_climate_controlled_storage(request, pk):
    user = User.objects.get(pk=pk)
    form = HostClimateControlledStorageForm(initial={'user_id': user})
    context = {'form': form}

    if request.method == 'POST':
        form = HostClimateControlledStorageForm(request.POST)
        if form.is_valid():
            description = form.data.get('description')
            location = form.data.get('location')
            form.save()
            s_type = "ClimateControlled"
            context = {'pk': pk, 'type': s_type, 'description': description, 'location': location}
            return render(request, 'addPhotos.html', context)
    return render(request, 'host/climate_controlled_storage_host.html', context)


def host_garage(request, pk):
    user = User.objects.get(pk=pk)
    form = HostGarageForm(initial={'user_id': user})
    context = {'form': form}

    if request.method == 'POST':
        form = HostGarageForm(request.POST)
        if form.is_valid():
            description = form.data.get('description')
            location = form.data.get('location')
            form.save()
            s_type = "Garage"
            context = {'pk': pk, 'type': s_type, 'description': description, 'location': location}
            return render(request, 'addPhotos.html', context)
    return render(request, 'host/garage_host.html', context)
