from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from management.package.models import Package
from django.utils.translation import gettext_lazy as _

class Booking(models.Model):
    customer_name = models.CharField(max_length=255)
    customer_email = models.EmailField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_Date= models.DateTimeField()
    end_Date = models.DateTimeField()
    created_at = models.DateTimeField(default=datetime.now)
    Package = models.ForeignKey(Package, on_delete=models.CASCADE, default=None)
    def __str__(self):
        return f"Booking for {self.customer_name} on package {self.Package}"

    def clean(self):
        # Don't allow end_date to be before start_date
        if self.end_Date and self.start_Date and self.end_Date <= self.start_Date:
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 7420c6dc11a4ccfbcbebce10ece905ac56cb2a63
            raise ValidationError(_('The end date cannot be before or the same as the start date.'))



class Flights(models.Model):
    name = models.CharField(max_length=100)
    departure_city = models.CharField(max_length=50)
    arrival_city = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)
class Hotels(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    price_per_night = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='hotels', default='path/to/default.jpg')

<<<<<<< HEAD
#---------------------------------- Activity --------------------------------#
class Activities(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='activity_images/')  # Define ImageField
=======
            raise ValidationError(_('The end date cannot be before or the same as the start date.'))
>>>>>>> b596ea709e2ce38bd15e80908b9797e5e12a6072
=======

class Activities(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)
>>>>>>> 7420c6dc11a4ccfbcbebce10ece905ac56cb2a63
