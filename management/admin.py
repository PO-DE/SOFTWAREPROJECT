from django.contrib import admin
from management.package.models import Package
# Register your models here.
from django.contrib import admin
from management.booking.models import Booking


# admin.site.register(Package)

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'customer_email')
    search_fields = ('customer_name' , 'customer_email')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "Package":
            kwargs["queryset"] = Package.objects.all()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

# admin.site.register(Booking, BookingAdmin)

@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ('destination','price')
    list_filter = ('destination','price')
    search_fields = ('destination','price')
