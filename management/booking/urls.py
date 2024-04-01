# Inside your app's urls.py (e.g., management/booking/urls.py)

from django.urls import path
from .views import book_package, booking_success
from management.user_profile.views import my_orders

urlpatterns = [
    path('book/', book_package, name='book_package'),
    path('booking/success/<int:booking_id>/', booking_success, name='booking_success'),
    # path('user_profile/my_orders', my_orders, name='my_order'),
]
