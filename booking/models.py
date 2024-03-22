

from django.db import models
from django.contrib.auth.models import User

class Package(models.Model):
    # Define your Package model fields here
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Booking(models.Model):  # Changed from 'booking' to 'Booking'
    customer_name = models.CharField(max_length=255)
    customer_email = models.EmailField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    package = models.ForeignKey(Package, on_delete=models.CASCADE)

    def __str__(self):
        return f"Booking for {self.customer_name}"
