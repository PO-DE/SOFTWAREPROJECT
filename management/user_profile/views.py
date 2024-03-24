from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from management.booking.models import Booking
from django.shortcuts import render
from .models import Order
from django.contrib.auth.decorators import login_required
from management.booking.models import Booking


@login_required
def view_profile(request, user_id):
    user_profile = get_object_or_404(User, id=user_id)
    return render(request, 'user_profile/user_profile.html', {'user_profile': user_profile})


# @login_required
# def my_orders(request):
#     my_bookings = Booking.objects.filter(user=request.user).order_by('start_Date')
#     context = {'orders': my_bookings}
#     return render(request, 'user_profile/my_orders.html', context)
@login_required
def my_orders(request, filter_by=None):
    my_bookings = Booking.objects.filter(user=request.user)

    if filter_by == 'a_to_z':
        my_bookings = Booking.objects.order_by('Package__destination')  # Assuming 'Package' is the related name and 'destination' is a field on Package
    elif filter_by == 'z_to_a':
        my_bookings = Booking.objects.order_by('-Package__destination')
    elif filter_by == 'date_acc':
        my_bookings = Booking.objects.order_by('created_at')
    elif filter_by == 'date_desc':
        my_bookings = Booking.objects.order_by('-created_at')
    context = {'orders': my_bookings}
    return render(request, 'user_profile/my_orders.html', context)
@login_required
def my_profile(request):
    # Assuming you want to display the profile of the currently logged-in user
    user_profile = request.user
    context = {'user': user_profile}
    return render(request, 'user_profile/my_profile.html', context)