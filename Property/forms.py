from django import forms

from .models import *


class HostPersonalRoomForm(forms.ModelForm):
    class Meta:
        model = Personal
        fields = ('name', 'description', 'location', 'size',
                  'facilities', 'price_per_day', 'rooms')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control',
                                           'placeholder': 'Property Name',
                                           'required': 'required'}),
            'description': forms.Textarea(attrs={'class': 'form-control',
                                                 'placeholder': 'Property Description'}),
            'location': forms.TextInput(attrs={'class': 'form-control',
                                               'placeholder': 'Property Location'}),
            'size': forms.NumberInput(attrs={'class': 'form-control',
                                             'placeholder': 'Floor Size'}),
            'facilities': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'price_per_day': forms.NumberInput(attrs={'class': 'form-control',
                                                      'placeholder': 'Price Per Day'}),
            'rooms': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }
