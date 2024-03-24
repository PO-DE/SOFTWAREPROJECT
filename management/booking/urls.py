# Inside your app's urls.py (e.g., management/booking/urls.py)

from django.urls import path
from .views import book_package, booking_success

urlpatterns = [
    path('package/<int:package_id>/book/', book_package, name='book_package'),
    path('booking/success/<int:booking_id>/', booking_success, name='booking_success'),
]
