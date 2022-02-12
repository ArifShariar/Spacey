from django.shortcuts import render
from .models import User


def welcome(request):
    return render(request, 'home/welcome.html')


def login(request):
    return render(request, 'auth/login.html')


def register(request):
    return render(request, 'auth/register.html')


# remember, pk has to be same as the url
def homepage(request, pk):
    user = User.objects.get(pk=pk)
    context = {
        'user': user,
    }
    return render(request, 'home/homepage.html', context)


def user_profile(request, pk):
    user = User.objects.get(pk=pk)
    context = {
        'user': user,
    }
    return render(request, 'home/user_profile.html', context)
