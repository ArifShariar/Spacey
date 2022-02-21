from django import forms

from .models import *


class HostPersonalRoomForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(HostPersonalRoomForm, self).__init__(*args, **kwargs)
        self.fields['location'].label = 'Location Description'
        self.fields['location_district'].label = 'District'
        self.fields['size'].label = 'Size (sq. ft.)'

    class Meta:
        model = Personal
        fields = ('user_id', 'property_name', 'description', 'location', 'location_district', 'size', 'facilities',
                  'price_per_day', 'rooms')


class HostBusinessStorageForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(HostBusinessStorageForm, self).__init__(*args, **kwargs)
        self.fields['location'].label = 'Location Description'
        self.fields['location_district'].label = 'District'
        self.fields['size'].label = 'Size (sq. ft.)'

    class Meta:
        model = Business
        fields = ('user_id', 'property_name', 'description', 'location', 'location_district', 'size', 'facilities',
                  'price_per_day', 'rooms')


class HostClimateControlledStorageForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(HostClimateControlledStorageForm, self).__init__(*args, **kwargs)
        self.fields['location'].label = 'Location Description'
        self.fields['location_district'].label = 'District'
        self.fields['size'].label = 'Size (sq. ft.)'

    class Meta:
        model = ClimateControlled
        fields = ('user_id', 'property_name', 'description', 'location', 'location_district', 'size', 'facilities',
                  'price_per_day', 'machinery')


class HostGarageForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(HostGarageForm, self).__init__(*args, **kwargs)
        self.fields['location'].label = 'Location Description'
        self.fields['location_district'].label = 'District'
        self.fields['size'].label = 'Size (sq. ft.)'

    class Meta:
        model = Garage
        fields = ('user_id', 'property_name', 'description', 'location', 'location_district', 'size', 'facilities',
                  'price_per_hour', 'vehicles')
