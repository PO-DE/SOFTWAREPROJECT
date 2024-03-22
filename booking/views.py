
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .forms import BookingForm  # Ensure correct form name
from .models import Booking
from rest_framework import viewsets
from .serializers import BookingSerializer

@login_required
def book_package(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking_instance = form.save(commit=False)
            booking_instance.user = request.user
            booking_instance.save()
            return redirect('some_view_name')  # Ensure this redirects to an existing view
    else:
        form = BookingForm()
    return render(request, 'your_template_name.html', {'form': form})  # Correct the template name as needed

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()  # Corrected from 'booking' to 'Booking'
    serializer_class = BookingSerializer
