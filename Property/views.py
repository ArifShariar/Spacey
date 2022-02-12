from django.shortcuts import render

# Create your views here.


def host(request):
    context = {}
    return render(request, 'host/host.html')