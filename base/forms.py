from django import forms
from base.models import ToDo


class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = '__all__'
        # exclude = ['user']


