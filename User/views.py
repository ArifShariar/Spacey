from django.shortcuts import render
from .forms import *
from django.contrib.auth.hashers import make_password, check_password


def welcome(request):
    return render(request, 'home/welcome.html')


def login(request):
    return render(request, 'auth/login.html')


def register(request):
    form = RegisterForm()
    context = {'form': form}
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            password = make_password(password)
            nid_number = form.cleaned_data['nid_number']
            date_of_birth = form.cleaned_data['date_of_birth']
            phone_number = form.cleaned_data['phone_number']

            # print(user_name, email, password, nid_number, date_of_birth, phone_number)
            # check if email and nid_number already exists
            # if not, create new user
            # if yes, return error
            existing_user = User.objects.filter(email=email, nid_number=nid_number)
            if existing_user:
                print('User already exists')
                # pass this message to frontend
                return render(request, 'auth/register.html', context)
            else:
                new_user = User(name=user_name, email=email, password=password, nid_number=nid_number, date_of_birth=date_of_birth, phone_number=phone_number)
                new_user.save()

            # redirect to user home page
            return render(request, 'home/welcome.html')
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
