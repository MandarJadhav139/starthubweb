from django import forms
from django.contrib.auth import get_user_model
from app1.models import Application


class SignupForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password')


class LoginForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'password')


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ('name', 'email', 'github', 'resume')
