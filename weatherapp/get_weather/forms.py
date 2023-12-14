from django.forms import ModelForm,TextInput
from .models import Place
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class PlaceForm(ModelForm):
    class Meta:
        model=Place
        fields=['name']
        widgets={'name':TextInput(attrs={'class':'input','placeholder':'Place Name'})}

class CreateUserForms(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']
