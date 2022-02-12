from django.shortcuts import render


def welcome(request):
    return render(request, 'home/welcome.html')


def login(request):
    return render(request, 'auth/login.html')


def register(request):
    return render(request, 'auth/register.html')
