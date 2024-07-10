from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True, help_text='Please provide a valid email address')
    date = forms.DateField(required=True, help_text='Required. Enter a valid date of birth.')
    phone = forms.CharField(max_length=15, required=True, help_text='Required. Enter a valid phone number.')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'date', 'phone')
