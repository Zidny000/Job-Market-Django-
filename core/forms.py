from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'block bg-[#18debb] bg-opacity-20 w-96 rounded-xl px-3 py-2 focus:outline-none placeholder:text-gray-400'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'block bg-[#18debb] bg-opacity-20 w-96 rounded-xl px-3 py-2 focus:outline-none placeholder:text-gray-400'
    }))

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'block bg-[#18debb] bg-opacity-20 w-96 rounded-xl px-3 py-2 focus:outline-none placeholder:text-gray-400'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your email address',
        'class': 'block bg-[#18debb] bg-opacity-20 w-96 rounded-xl px-3 py-2 focus:outline-none placeholder:text-gray-400'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'block bg-[#18debb] bg-opacity-20 w-96 rounded-xl px-3 py-2 focus:outline-none placeholder:text-gray-400'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repeat password',
        'class': 'block bg-[#18debb] bg-opacity-20 w-96 rounded-xl px-3 py-2 focus:outline-none placeholder:text-gray-400'
    }))