


from rest_framework import serializers
from .models import Package, Booking  # Ensure correct case

class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking  # Corrected from 'booking' to 'Booking'
        fields = '__all__'
