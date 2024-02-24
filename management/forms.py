from django import forms
from django.contrib.auth.models import User
from .models import Package
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
import datetime
class PackageForm(forms.ModelForm):
    class Meta:
        model = Package
        fields = ['source', 'destination','seats','room']

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        widgets={
            'username': forms.TextInput(attrs={'class': "form-control"}),
            'first_name': forms.TextInput(attrs={'class': "form-control"}),
            'last_name': forms.TextInput(attrs={"class": "form-control"}),
            'email': forms.EmailInput(attrs={'class': "form-control"}),
            'password1': forms.PasswordInput(attrs={'class':  "form-control"}),
            'password2': forms.PasswordInput(attrs={'class':"form-control"}),
        }

    def clean(self):
        cleaned_data = super(UserCreationForm, self).clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 != password2:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )
class SignInForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')
        widgets ={
            'username': forms.TextInput(attrs={'class': "form-control"}),
            'password': forms.PasswordInput(attrs={'class': "form-control"}),
        }