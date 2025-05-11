from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Person, License, Car

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ["name", "birth_date",  "address"]

class LicenseForm(forms.ModelForm):
    class Meta:
        model = License
        fields = ["number", "issue_date", "expiry_date"]

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ["number", "manufacturer", "model", "color"]
