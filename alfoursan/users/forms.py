from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    full_name = forms.CharField(max_length=100)
    
    class Meta:
        model = User
        fields = ("username", "password1", "password2", "email", "full_name", )

        labels = {
            'username': '',  
            'password1': '',
            'password2': '',
            'email': '',
            'full_name': '',
        }

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username',}),
            'password1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mot de passe',}),
            'password2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Confirmer Mot de passe',}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email',}),
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name',}),  
        }