from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime


class Package(models.Model):
    # user_id= models.ForeignKey(User, on_delete=models.CASCADE)
    source= models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    seats = models.IntegerField(default=0)
    # hotels= models.CharField(max_length=100,default=0)
    room= models.IntegerField(default=0)
    price= models.IntegerField(default=0)
    date= models.DateTimeField(default=datetime.now)
    def __str__(self):
        return self.source

