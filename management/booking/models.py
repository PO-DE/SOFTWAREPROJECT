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
            raise ValidationError(_('The end date cannot be before or the same as the start date.'))