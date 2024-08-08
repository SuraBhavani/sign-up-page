from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Name', 'id': 'name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email', 'id': 'email'}),
            'password1': forms.PasswordInput(attrs={'placeholder': 'Password', 'id': 'password'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}),
        }
