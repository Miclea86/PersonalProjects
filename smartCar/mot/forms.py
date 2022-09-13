from django import forms
from django.forms import Select, NumberInput, DateInput


from mot.models import Mot


class MotForm(forms.ModelForm):
    class Meta:
        model = Mot
        fields = '__all__'
        widgets = {
            'sum': NumberInput(attrs={'placeholder': 'M.O.T cost', 'class': 'form-control'}),
            'start_date': DateInput(attrs={'placeholder': 'Start date', 'class': 'form-control',
                                           'type': 'date'}),
            'end_date': DateInput(attrs={'placeholder': 'End date', 'class': 'form-control',
                                         'type': 'date'}),
            'car': Select(attrs={'placeholder': 'Choose car', 'class': 'form-control'})
        }
