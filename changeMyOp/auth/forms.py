from django import forms
from django.forms import CharField, PasswordInput


class RegistrationForm(forms.Form):
    """
    Registration form
    """
    username = forms.CharField(label='Username', max_length=50, required=True)
    password = forms.CharField(label='Password', max_length=50, required=True, widget=PasswordInput())
    passwordconf = forms.CharField(label='Password Confirmation', max_length=30, required=True, widget=PasswordInput())
    email = forms.CharField(label='Email', max_length=50, required=True)
    first_name = forms.CharField(label='First Name', max_length=50, required=True)
    last_name = forms.CharField(label='Last Name', max_length=50, required=True)


class SigninForm(forms.Form):
    """
    Signin form
    """
    username = forms.CharField(label='Username', max_length=30, required=True)
    password = forms.CharField(label='Password', max_length=30, required=True, widget=PasswordInput())
