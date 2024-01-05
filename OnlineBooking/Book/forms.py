from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Customer

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'username', 'password1', 'password2']

class CustomerForm(forms.ModelForm):
    gen = (('MALE', 'Male'), ('FEMALE', 'Female'))
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=gen)
    areatype = forms.ChoiceField(widget=forms.Select, choices=[('URBAN', 'Urban'), ('RURAL', 'Rural')])
    class Meta:
        model = Customer
        fields = '__all__'

