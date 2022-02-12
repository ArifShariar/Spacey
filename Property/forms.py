from django.forms import ModelForm

from .models import *


class HostPersonalRoomForm(ModelForm):
    class Meta:
        model = Personal
        fields = '__all__'


class CreateRoomForm(ModelForm):
    class Meta:
        model = Room
        fields = ['room_type', 'room_description']
