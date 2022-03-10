from datetime import datetime
import email
from email.policy import default
from xmlrpc.client import DateTime
from django.db import models
from django.db.models.base import Model
from django.db.models.fields import DurationField, EmailField
from django.db.models.fields import related
from django.db.models.fields.related import ForeignKey
from sqlalchemy import null, true


# Create your models here.

class bookings(models.Model):
    bookingId = models.AutoField(primary_key=True)
    name= models.CharField(max_length=150)
    user = models.CharField(max_length= 150)
    email = models.EmailField(default="")
    contact = models.CharField(max_length=100)
    date= models.DateField()
    time= models.TimeField()
    fro = models.CharField(max_length=150)
    destination= models.CharField(max_length=100)
    bill = models.PositiveIntegerField()
class category(models.Model):
    categories = models.CharField(primary_key=True,max_length=150)

class status(models.Model):
    state = models.CharField(primary_key=True,max_length=150)

class bustype(models.Model):
    bustype = models.CharField(primary_key=True,max_length=150)

class employee (models.Model):
    userId = models.AutoField(primary_key=True)
    firstname= models.CharField(max_length=150)
    lastname = models.CharField(max_length= 150)
    languages = models.CharField(max_length=250)
    photo = models.ImageField(default='', upload_to='photos')
    email = models.EmailField()
    jobtype = models.ForeignKey(category, related_name="speciality",on_delete=models.CASCADE)
    contact = models.CharField(max_length=100)
    status = models.ForeignKey(status, related_name="status",on_delete=models.CASCADE)

class route (models.Model):
    routeId = models.AutoField(primary_key=True)
    route= models.CharField(max_length=150)
    fee = models.PositiveIntegerField()
    status = models.ForeignKey(status, related_name="status1",on_delete=models.CASCADE)

class bus (models.Model):
    busId = models.AutoField(primary_key=True)
    platenumber = models.CharField(max_length=150)
    route = models.ForeignKey(route, related_name="route1",on_delete=models.CASCADE)
    bustype = models.ForeignKey(bustype, related_name="type",on_delete=models.CASCADE)
    seats = models.CharField(max_length=50)
    driver = models.ForeignKey(employee, related_name="driverr",on_delete=models.CASCADE)
    status = models.ForeignKey(status, related_name="status2",on_delete=models.CASCADE)
    ratings = models.IntegerField(default=3)