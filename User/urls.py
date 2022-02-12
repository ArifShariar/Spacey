from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('homepage/<str:pk>/', views.homepage, name='homepage'),
    path('profile/<str:pk>/', views.user_profile, name='profile'),
]
