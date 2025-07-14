from django import forms
from .models import *


class CityForm(forms.ModelForm):
    class Meta:
        model = Weather
        fields = ['city']
        labels = {
            "city": "Город",
        }
