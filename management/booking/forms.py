from django import forms
from django.db.models import Q
from management.booking.models import Booking
from django.contrib.auth.models import User, Group
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
        agent_group = Group.objects.filter(name="Agent").first()
        if agent_group:
            self.fields['user'].queryset = User.objects.filter(
                Q(groups=agent_group) | Q(is_staff=True)
            )
        else:
            self.fields['user'].queryset = User.objects.filter(is_staff=True)