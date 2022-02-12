from django.shortcuts import render
from .forms import *


# Create your views here.


def host(request):
    form = HostPersonalRoomForm()
    context = {'form': form}

    if request.method == 'POST':
        print(request.POST)
    return render(request, 'host/host.html', context)
