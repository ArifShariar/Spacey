from django import forms

from .models import *


class HostPersonalRoomForm(forms.ModelForm):
    class Meta:
        model = Personal
        fields = ('user_id', 'property_name', 'description', 'location', 'size', 'facilities',
                  'price_per_day', 'rooms')


class HostBusinessStorageForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ('user_id', 'property_name', 'description', 'location', 'size', 'facilities',
                  'price_per_day', 'rooms')


class HostClimateControlledStorageForm(forms.ModelForm):
    class Meta:
        model = ClimateControlled
        fields = ('user_id', 'property_name', 'description', 'location', 'size', 'facilities',
                  'price_per_day', 'machinery')


class HostGarageForm(forms.ModelForm):
    class Meta:
        model = Garage
        fields = ('user_id', 'property_name', 'description', 'location', 'size', 'facilities',
                  'price_per_hour', 'vehicles')
