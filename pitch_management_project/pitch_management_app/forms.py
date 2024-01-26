from django.forms import ModelForm
from .models import Pitch
from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'


class PitchForm(ModelForm):
    class Meta:
        model = Pitch
        fields = '__all__'
        widgets = {
            'last_maintenance_date': DateInput(),
            'next_maintenance_date': DateInput(),
        }