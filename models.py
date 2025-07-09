from django.db import models
from django.utils import timezone

class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.CharField(max_length=100)
    massage = models.CharField(max_length=1000)  # kept typo consistent
    date = models.DateField()

class booking(models.Model): 
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    persons = models.CharField(max_length=4)
    booking_date = models.DateField()

class veg_item(models.Model):  
    dish = models.CharField(max_length=100)
    price = models.CharField(max_length=4)

class non_veg_item(models.Model): 
    dish = models.CharField(max_length=100)
    price = models.CharField(max_length=4)

class Dessert(models.Model): 
    dish = models.CharField(max_length=100)
    price = models.CharField(max_length=4)

class Cold_Drink(models.Model): 
    dish = models.CharField(max_length=100)
    price = models.CharField(max_length=4)


