from django.urls import path , include
from rest_framework import routers
from . import views
from .views import signup, signin, package_list, package_create, package_detail, Logout, search_results, BookingViewSet, \
    forgotpassword

urlpatterns = [
    path('', views.index, name='index'),
    path('packagelist/', package_list, name='package_list'),

    path('package/<int:pk>/', package_detail, name='package_detail'),

    # path('package/<int:pk>/', package_detail, name='package_detail'),

    path('package/create/', package_create, name='package_create'),
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('logout/', Logout, name='logout'),
    path('search/', search_results, name='search_results'),
    path('Booking/', BookingViewSet, name='Bookings'),
    path('forgotpassword/', forgotpassword, name='forgot password'),
    path('package/<int:package_id>/', package_detail, name='package_detail'),

]
