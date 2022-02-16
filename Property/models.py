from django.db import models


# Create your models here.
# storage is declared as abstract class
# other classes like personal room ,business storage, garage and climate controlled
# will inherit from this Storage Base class
class Storage(models.Model):
    user_id = models.ForeignKey('User.User', on_delete=models.CASCADE)
    property_name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    size = models.IntegerField()
    # TODO: ADD IMAGE FIELD
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# property facilities table
# will be created in database
class PersonalPropertyFacilities(models.Model):
    facility_type = models.CharField(max_length=100)
    facility_description = models.CharField(max_length=100)

    def __str__(self):
        return self.facility_type

    class Meta:
        verbose_name_plural = 'Personal Property Facilities'


class BusinessPropertyFacilities(models.Model):
    facility_type = models.CharField(max_length=100)
    facility_description = models.CharField(max_length=100)

    def __str__(self):
        return self.facility_type

    class Meta:
        verbose_name_plural = 'Business Property Facilities'


class ClimateControlledPropertyFacilities(models.Model):
    facility_type = models.CharField(max_length=100)
    facility_description = models.CharField(max_length=100)

    def __str__(self):
        return self.facility_type

    class Meta:
        verbose_name_plural = 'Climate Controlled Property Facilities'


class GaragePropertyFacilities(models.Model):
    facility_type = models.CharField(max_length=100)
    facility_description = models.CharField(max_length=100)

    def __str__(self):
        return self.facility_type

    class Meta:
        verbose_name_plural = 'Garage Property Facilities'


# personal room will inherit from Storage class
# table of this field will be created


class Personal(Storage):
    price_per_day = models.IntegerField()
    rooms = models.ManyToManyField('Room')
    facilities = models.ManyToManyField(PersonalPropertyFacilities)

    def __str__(self):
        return self.property_name

    class Meta:
        verbose_name_plural = 'Personal'


# room is for personal storage and business storage
class Room(models.Model):
    room_type = models.CharField(max_length=100)
    room_description = models.CharField(max_length=100)

    def __str__(self):
        return self.room_type

    class Meta:
        verbose_name_plural = 'Rooms'


class Business(Storage):
    price_per_day = models.IntegerField()
    rooms = models.ManyToManyField('BusinessRooms')
    facilities = models.ManyToManyField(BusinessPropertyFacilities)

    def __str__(self):
        return self.property_name

    class Meta:
        verbose_name_plural = 'Business Storages'


class BusinessRooms(models.Model):
    room_type = models.CharField(max_length=100)
    room_description = models.CharField(max_length=100)

    def __str__(self):
        return self.room_type

    class Meta:
        verbose_name_plural = 'Rooms for Business Storage'


class ClimateControlled(Storage):
    price_per_day = models.IntegerField()
    machinery = models.ManyToManyField('Machinery')
    facilities = models.ManyToManyField(ClimateControlledPropertyFacilities)

    def __str__(self):
        return self.property_name

    class Meta:
        verbose_name_plural = 'Climate Controlled'


class Machinery(models.Model):
    machinery_type = models.CharField(max_length=100)
    machinery_description = models.CharField(max_length=100)

    def __str__(self):
        return self.machinery_type

    class Meta:
        verbose_name_plural = 'Machinery'


class Garage(Storage):
    price_per_hour = models.IntegerField()
    vehicles = models.ManyToManyField('Vehicle')
    facilities = models.ManyToManyField(GaragePropertyFacilities)

    def __str__(self):
        return self.property_name

    class Meta:
        verbose_name_plural = 'Garages'


class Vehicle(models.Model):
    vehicle_type = models.CharField(max_length=100)
    vehicle_description = models.CharField(max_length=100)

    def __str__(self):
        return self.vehicle_type

    class Meta:
        verbose_name_plural = 'Vehicles'
