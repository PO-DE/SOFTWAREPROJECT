from django.contrib.auth.models import User
from management.booking.models import Booking
from management.package.forms import PackageForm
from management.package.models import Package
from django.db.models import Sum
from django.shortcuts import render, get_object_or_404, redirect
from management.booking.forms import BookingForm
from django.contrib.auth.decorators import login_required, user_passes_test


@login_required
def view_profile(request, user_id):
    user_profile = get_object_or_404(User, id=user_id)

    is_special_user = request.user.is_staff or request.user.groups.filter(name='agent').exists()

    if is_special_user:
        template_name = 'user_profile/agent_profile.html'
    else:
        template_name = 'user_profile/user_profile.html'

    return render(request, template_name, {'user_profile': user_profile})


@login_required
def my_orders(request, filter_by=None):
    # my_bookings = Booking.objects.filter(user=request.user)
    my_bookings = Booking.objects.filter(customer_email=request.user.email)

    if filter_by == 'a_to_z':
        my_bookings = Booking.objects.order_by('Package__destination')
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




def is_staff_or_agent(user):
    return user.is_staff or user.groups.filter(name='AgentGroup').exists()

@login_required
@user_passes_test(is_staff_or_agent)
def booking_update(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('all_bookings')
    else:
        form = BookingForm(instance=booking)
    return render(request, 'user_profile/booking_edit_form.html', {'form': form})



@login_required
def all_packages(request):
    filter_by_destination = request.GET.get('destination', '')

    if filter_by_destination:
        # Assuming there's an 'agent_name' field in your Booking model
        # Adjust the query to match your actual data structure
        # bookings = Booking.objects.filter(user__username__icontains=filter_by_agent)
        packages = Package.objects.filter(destination__icontains=filter_by_destination)
    else:
        packages = Package.objects.all()
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
    # total_amount = bookings.aggregate(total=Sum('Package__price'))['total'] or 0
    context = {'packages': packages,}
    return render(request, 'user_profile/all_packages.html', context)
    # return render(request, 'user_profile/all_bookings.html', {'bookings': bookings})


def is_staff_or_agent(user):
    return user.is_staff or user.groups.filter(name='AgentGroup').exists()

@login_required
@user_passes_test(is_staff_or_agent)
def package_update(request, pk):
    package = get_object_or_404(Package, pk=pk)
    if request.method == 'POST':
        form = PackageForm(request.POST, instance=package)
        if form.is_valid():
            form.save()
            return redirect('all_packages')
    else:
        form = PackageForm(instance=package)
    return render(request, 'user_profile/package_edit_form.html', {'form': form})