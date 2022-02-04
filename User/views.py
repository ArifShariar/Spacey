from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate


def login(request):
    return render(request, 'auth/login.html')


def register(request):
    return render(request, 'auth/register.html')
