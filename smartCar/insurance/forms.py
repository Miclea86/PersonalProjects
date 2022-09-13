from django import forms
from django.forms import Select, DateInput, NumberInput

from insurance.models import Insurance


class InsuranceForm(forms.ModelForm):
    class Meta:
        model = Insurance
        fields = '__all__'
        widgets = {
            'sum': NumberInput(attrs={'placeholder': 'Insurance cost', 'class': 'form-control'}),
            'start_date': DateInput(attrs={'placeholder': 'Start date', 'class': 'form-control',
                                           'type': 'date'}),
            'end_date': DateInput(attrs={'placeholder': 'End date', 'class': 'form-control',
                                         'type': 'date'}),
            'car': Select(attrs={'placeholder': 'Choose car', 'class': 'form-control'})
        }
