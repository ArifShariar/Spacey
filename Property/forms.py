from django.forms import ModelForm

from .models import *


class HostPersonalRoomForm(ModelForm):
    class Meta:
        model = Personal
        fields = '__all__'
