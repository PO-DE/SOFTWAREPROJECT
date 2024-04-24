# Inside your app's urls.py (e.g., management/booking/urls.py)

from django.urls import path
from .views import book_package, booking_success,confirm_booking
from management.user_profile.views import my_orders
from management.booking import views

urlpatterns = [
    path('book/', book_package, name='book_package'),
    path('booking/success/<int:booking_id>/', booking_success, name='booking_success'),
    # path('user_profile/my_orders', my_orders, name='my_order'),
    path('book hotel/', views.book_hotel, name='book_hotel'),
    path('book flight/', views.book_flight, name='book_flight'),
    path('hotels/', views.hotels_list, name='hotels_list'),
    path('flights/', views.flights_list, name='flights_list'),
    path('confirm-booking/', confirm_booking, name='confirm_booking'),

    # Add URL pattern for booking flights
    path('book/flight/', views.book_flight, name='book_flight'),
]



