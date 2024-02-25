from django.contrib import admin
from .models import Package
# Register your models here.
from django.contrib import admin
from .models import Booking


admin.site.register(Package)

@admin.register(Booking)
class CustomerBookingAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'customer_email')
