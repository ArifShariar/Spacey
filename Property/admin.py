from django.contrib import admin

from . models import *

admin.site.register(PersonalPropertyFacilities)
admin.site.register(BusinessPropertyFacilities)
admin.site.register(ClimateControlledPropertyFacilities)
admin.site.register(GaragePropertyFacilities)
admin.site.register(Personal)
admin.site.register(Room)
admin.site.register(Business)
admin.site.register(BusinessRooms)
admin.site.register(ClimateControlled)
admin.site.register(Machinery)
admin.site.register(Garage)
admin.site.register(Vehicle)

