from django.db import models


# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
    nidNumber = models.IntegerField()
    dateOfBirth = models.DateField()
    phoneNumber = models.CharField(max_length=50)

    def __str__(self):
        return self.name
