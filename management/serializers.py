<<<<<<< HEAD
# from rest_framework import serializers
# from .models import Package, Booking
#
#
# class PackageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Package
#         fields = '__all__'
#
# class BookingSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Booking
#         fields = '__all__'
#
#
=======
from rest_framework import serializers
from .models import Package, Booking


class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'


>>>>>>> 7534b29360cfcec71acd477de69076415c82222d
