from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime


class Package(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE ,default=None)
    source= models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    seats = models.IntegerField(default=0)
    # hotels= models.CharField(max_length=100,default=0)
    room= models.IntegerField(default=0)
    description= models.TextField(max_length=100,default=None)
    price= models.IntegerField(default=None)
    date= models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.source + "|" + self.destination + "|" + str(self.user)


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # booking = models.ForeignKey('bookings.Booking', on_delete=models.CASCADE)
    message = models.CharField(max_length=255)

    # created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}: {self.message}'


# booking code
class Booking(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    # created_at = models.DateTimeField(auto_now_add=True)
