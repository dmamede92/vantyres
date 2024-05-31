from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Brand


class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ('name', 'description')

        labels = {
            'name': 'Nome:',
            'description': 'Descrição:'
        }

class BrandFormEdit(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ('name', 'description')

        labels = {
            'name': 'Nome:',
            'description': 'Descrição:'
        }