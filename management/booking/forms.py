from django import forms
from management.booking.models import Booking
from management.package.models import Package
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
        widgets = {
            'start_Date': forms.DateInput(attrs={'type': 'date', 'class': 'datepicker', 'id': 'start_date'}),
            'end_Date': forms.DateInput(attrs={'type': 'date', 'class': 'datepicker', 'id': 'end_date'}),
        }

    def __init__(self, *args, **kwargs):
        package = kwargs.pop('package', None)
        super(BookingForm, self).__init__(*args, **kwargs)
        if package is not None:
            self.fields['Package'].initial = package