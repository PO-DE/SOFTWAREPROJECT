from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from management.booking.models import Booking
from django.db.models import Sum


@login_required
def view_profile(request, user_id):
    user_profile = get_object_or_404(User, id=user_id)

    is_special_user = request.user.is_staff or request.user.groups.filter(name='agent').exists()

    # Choose the template based on the user's role
    if is_special_user:
        # For staff users or users in the agent group, use a specific template
        template_name = 'user_profile/agent_profile.html'
    else:
        # Default template for other users
        template_name = 'user_profile/user_profile.html'

    # Render the template with the user profile context
    return render(request, template_name, {'user_profile': user_profile})


@login_required
def my_orders(request, filter_by=None):
    # my_bookings = Booking.objects.filter(user=request.user)
    my_bookings = Booking.objects.filter(customer_email=request.user.email)

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


@login_required
def all_bookings(request):
    filter_by_agent = request.GET.get('user', '')

    if filter_by_agent:
        # Assuming there's an 'agent_name' field in your Booking model
        # Adjust the query to match your actual data structure
        bookings = Booking.objects.filter(user__username__icontains=filter_by_agent)
    else:
        bookings = Booking.objects.all()
    #
    # context = {'bookings': bookings}
    # return render(request, 'user_profile/all_bookings.html', context)
    # query = Q()
    #
    # # Dynamically build the query based on GET parameters
    # filters = {
    #     'booking_date': 'start_Date',
    #     'username': 'user__username__icontains',
    #     'destination': 'Package__destination__icontains',
    #     'customer_name': 'customer_name__icontains',
    #     'customer_email': 'customer_email__icontains',
    # }
    #
    # for param, field in filters.items():
    #     value = request.GET.get(param, '')
    #     if value:
    #         kwargs = {field: value}
    #         query &= Q(**kwargs)

    # bookings = Booking.objects.filter(query)
    total_amount = bookings.aggregate(total=Sum('Package__price'))['total'] or 0
    context = {'bookings': bookings, 'total_amount': total_amount}
    return render(request, 'user_profile/all_bookings.html', context)
    # return render(request, 'user_profile/all_bookings.html', {'bookings': bookings})
