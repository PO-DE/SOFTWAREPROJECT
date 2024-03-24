from django.urls import path
from .views import view_profile, my_orders, my_profile

urlpatterns = [
    path('profile/<int:user_id>/', view_profile, name='view_profile'),
    path('my-orders/', my_orders, name='my_orders'),
    path('profile/my_profile/', my_profile, name='my_profile'),
    path('my-orders/<str:filter_by>/', my_orders, name='my-orders-filter'),
]
