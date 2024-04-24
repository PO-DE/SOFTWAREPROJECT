# Inside your app's urls.py (e.g., management/booking/urls.py)

from django.urls import path
<<<<<<< HEAD
<<<<<<< HEAD
from .views import book_package, booking_success,confirm_booking
from management.user_profile.views import my_orders
from management.booking import views
=======
from .views import book_package, booking_success
from management.user_profile.views import my_orders
>>>>>>> b596ea709e2ce38bd15e80908b9797e5e12a6072
=======
from .views import book_package, booking_success,confirm_booking
from management.user_profile.views import my_orders
from management.booking import views
>>>>>>> 7420c6dc11a4ccfbcbebce10ece905ac56cb2a63

urlpatterns = [
    path('book/', book_package, name='book_package'),
    path('booking/success/<int:booking_id>/', booking_success, name='booking_success'),
    # path('user_profile/my_orders', my_orders, name='my_order'),
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 7420c6dc11a4ccfbcbebce10ece905ac56cb2a63
    path('book hotel/', views.book_hotel, name='book_hotel'),
    path('book flight/', views.book_flight, name='book_flight'),
    path('hotels/', views.hotels_list, name='hotels_list'),
    path('flights/', views.flights_list, name='flights_list'),
    path('confirm-booking/', confirm_booking, name='confirm_booking'),
<<<<<<< HEAD
    # Add URL pattern for booking flights
    path('book/flight/', views.book_flight, name='book_flight'),


    path('activities/', views.activity_list, name='activity_list'),
    path('add_activity/', views.add_activity, name='add_activity'),

=======

    # Add URL pattern for booking flights
    path('book/flight/', views.book_flight, name='book_flight'),
>>>>>>> 7420c6dc11a4ccfbcbebce10ece905ac56cb2a63
]



<<<<<<< HEAD
=======
]
>>>>>>> b596ea709e2ce38bd15e80908b9797e5e12a6072
=======
>>>>>>> 7420c6dc11a4ccfbcbebce10ece905ac56cb2a63
