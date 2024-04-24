from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from management.booking.forms import BookingForm
from .models import Booking
from rest_framework import viewsets
from .serializers import BookingSerializer
from management.package.models import Package
from django.core.mail import send_mail
from django.conf import settings
from django.utils.dateformat import format
from django.urls import reverse



@login_required
def book_package(request):
    # package = get_object_or_404(Package, id=package_id)
    if request.method == 'POST':
        form = BookingForm(request.POST, package=Package)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            # booking.Package = package
            booking.save()

            start_date_formatted = format(booking.start_Date, 'd-m-Y')
            end_date_formatted = format(booking.end_Date, 'd-m-Y')

            subject = 'Booking Confirmation'
            message = f"""Dear {booking.customer_name},

            Thank you for booking with us! Your trip from Montreal to {booking.Package.destination} from {start_date_formatted} to {end_date_formatted} is now confirmed.

            We wish you an incredible journey ahead. May your travel be filled with exciting adventures and unforgettable memories. Our goal is to provide you with the best experience possible, and we're here to assist with any part of your travel plans.

            Safe travels,
            Clumsy Coders"""
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [booking.customer_email]

            # Send the email
            send_mail(subject, message, email_from, recipient_list)

            return redirect('booking_success', booking_id=booking.id)  # Ensure this redirects to an existing view
    else:
        form = BookingForm(package=Package)
    return render(request, 'booking/bookingform.html', {'form': form, 'package': Package})  # Correct the template name as needed

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()  # Corrected from 'booking' to 'Booking'
    serializer_class = BookingSerializer

def booking_success(request, booking_id):

    is_staff_or_agent = request.user.is_staff or request.user.groups.filter(name='agent').exists()

    # Determine the redirect URL based on the user's status
    if is_staff_or_agent:
        redirect_url = reverse('index')  # Use the name of your home page view
    else:
        redirect_url = reverse('my_orders')  # Use the namespaced URL for "my orders"

    context = {
        'booking_id': booking_id,
        'redirect_url': redirect_url,
    }
    return render(request, 'booking/booking_success.html', context)


from .models import Hotels, Flights

def hotels_list(request):
    # Use Hotel.objects.all() to get all hotels from the database.
    hotels = Hotels.objects.all()
    return render(request, 'hotels/hotels_list.html', {'hotels': hotels})

def flights_list(request):
    flights = Flights.objects.all()
    return render(request, 'flights/flights_list.html', {'flights': flights})



def book_hotel(request):
    hotel = Hotels.objects.all()
    context = {
        'hotel': hotel
    }
    # Add additional context or booking logic if necessary
    return render(request, 'hotels/book_hotel.html', {'hotel': hotel})

def book_flight(reqest):
    flight = Flights.objects.all()
    return render(request, 'flights/book_flight.html', {'flight': flight})

from django.shortcuts import render

def book_flight(request):
    if request.method == 'POST':
        # Handle the flight booking logic here
        return render(request, 'flights/booking_confirmation.html')
    else:
        return render(request, 'flights/book_flight.html')


# views.py

from django.shortcuts import render
from django.http import HttpResponse

def confirm_booking(request):
    if request.method == 'POST':
        # You can add logic here to process the dates or save the booking
        check_in_date = request.POST.get('check_in')
        check_out_date = request.POST.get('check_out')

        # For now, we'll just pretend we processed the booking and return a simple response
        return HttpResponse('Booking successful!')
    else:
        # If not a POST request, just redirect to the form or show an error
        return render(request, 'book_hotel.html', {'error': 'Invalid method'})


# Add a view for the confirmation page

