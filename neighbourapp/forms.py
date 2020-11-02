from django import forms
from django.contrib.auth.models import User
from .models import post, Home, Business 
from users.models import Profile


class HomeForm(forms.ModelForm):
    class Meta:
        model = Home
        exclude = ('admin',)


class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ('user', 'home')


class postForm(forms.ModelForm):
    class Meta:
        model = post
        exclude = ('user', 'hood')