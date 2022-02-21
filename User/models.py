from django.db import models

# Create your models here.

location_choices = [
    ('Bogura', 'Bogura'),
    ('Cox\'s Bazar', 'Cox\'s Bazar'),
    ('Dhaka', 'Dhaka'),
    ('Chittagong', 'Chittagong'),
    ('Khulna', 'Khulna'),
    ('Rajshahi', 'Rajshahi'),
    ('Sylhet', 'Sylhet'),
    ('Rangpur', 'Rangpur'),
    ('Mymensingh', 'Mymensingh'),
    ('Barisal', 'Barisal'),
    ('Dinajpur', 'Dinajpur'),
    ('Comilla', 'Comilla'),

]


class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
    nid_number = models.IntegerField()
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=50)
    location = models.CharField(max_length=50, choices=location_choices, blank=True)

    def __str__(self):
        return self.name
