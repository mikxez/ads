from django import forms
from .models import Ad
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class AdForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = ['title', 'description', 'price', 'category', 'condition', 'image']


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', max_length=150)
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']