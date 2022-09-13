from django import forms
from django.forms import Select, DateInput, NumberInput

from roadTax.models import RoadTax


class RoadTaxForm(forms.ModelForm):
    class Meta:
        model = RoadTax
        fields = '__all__'
        widgets = {
            'sum': NumberInput(attrs={'placeholder': 'Road tax cost', 'class': 'form-control'}),
            'start_date': DateInput(attrs={'placeholder': 'Start date', 'class': 'form-control',
                                           'type': 'date'}),
            'end_date': DateInput(attrs={'placeholder': 'End date', 'class': 'form-control',
                                         'type': 'date'}),
            'car': Select(attrs={'placeholder': 'Choose car', 'class': 'form-control'})
        }
