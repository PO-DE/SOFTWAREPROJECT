from django.contrib import admin
from .models import Package
# Register your models here.
from django.contrib import admin
from .models import Booking


admin.site.register(Package)

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name' , 'email')
