from django.shortcuts import render, redirect
from .forms import *
from django.db.models import Q
from django.contrib import messages


def welcome(request):
    return render(request, 'home/welcome.html')


def loginUser(request):
    context = {}

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        # get user from database by email
        user = User.objects.filter(email=email)
        if user:
            # check if password matches
            if password == user.get().password:
                # print('Password matches')
                return redirect('homepage', pk=user.get().pk)
            else:
                # print('Password does not match')
                messages.error(request, 'Password does not match')
        else:
            # print('Email not found')
            messages.error(request, 'Email not found')

    return render(request, 'auth/login.html', context)


def logoutUser(request):
    return redirect('login')


def register(request):
    form = RegisterForm()
    context = {'form': form}
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user_name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            nid_number = form.cleaned_data['nid_number']
            date_of_birth = form.cleaned_data['date_of_birth']
            phone_number = form.cleaned_data['phone_number']
            location = form.cleaned_data['location']

            existing_user = User.objects.filter(Q(email=email) | Q(nid_number=nid_number))
            if existing_user:
                messages.error(request, 'User already exists')
                return render(request, 'auth/register.html', context)
            else:
                new_user = User(name=user_name, email=email, password=password, nid_number=nid_number,
                                date_of_birth=date_of_birth, phone_number=phone_number, location=location)
                new_user.save()
                messages.success(request, 'User created successfully, please log in to continue')
                return redirect('login')
        else:
            context = {'form': form}
            return render(request, 'auth/register.html', context)
    return render(request, 'auth/register.html', context)


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
