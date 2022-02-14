from django import forms

from .models import *


class HostPersonalRoomForm(forms.ModelForm):
    class Meta:
        model = Personal
        fields = ('user_id', 'property_name', 'description', 'location', 'size',
                  'facilities', 'price_per_day', 'rooms')
        # the widgets are used to display the form in the html page
        # much harder to control in this method than in the raw html code ( i think )

        # widgets = {
        #     'name': forms.TextInput(attrs={'class': 'form-control',
        #                                    'placeholder': 'Property Name',
        #                                    'required': 'required'}),
        #     'description': forms.Textarea(attrs={'class': 'form-control',
        #                                          'placeholder': 'Property Description'}),
        #     'location': forms.TextInput(attrs={'class': 'form-control',
        #                                        'placeholder': 'Property Location'}),
        #     'size': forms.NumberInput(attrs={'class': 'form-control',
        #                                      'placeholder': 'Floor Size'}),
        #     'facilities': forms.SelectMultiple(attrs={'class': 'form-control'}),
        #     'price_per_day': forms.NumberInput(attrs={'class': 'form-control',
        #                                               'placeholder': 'Price Per Day'}),
        #     'rooms': forms.SelectMultiple(attrs={'class': 'form-control'}),
        # }


class HostBusinessStorageForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ('user_id', 'property_name', 'description', 'location', 'size',
                  'facilities', 'price_per_day', 'rooms')


class HostClimateControlledStorageForm(forms.ModelForm):
    class Meta:
        model = ClimateControlled
        fields = ('user_id', 'property_name', 'description', 'location', 'size',
                  'facilities', 'price_per_day', 'machinery')


class HostGarageForm(forms.ModelForm):
    class Meta:
        model = Garage
        fields = ('user_id', 'property_name', 'description', 'location', 'size',
                  'facilities', 'price_per_hour', 'vehicles')
