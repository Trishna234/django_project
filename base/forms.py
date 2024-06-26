from django import forms
from base.models import ToDo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']


class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = '__all__'
        # exclude = ['user'] #to delete
