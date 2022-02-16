from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),

    path('login/', views.loginUser, name='login'),
    path('register/', views.register, name='register'),
    path('<str:pk>/homepage/', views.homepage, name='homepage'),
    path('<str:pk>/profile/', views.user_profile, name='profile'),
]
