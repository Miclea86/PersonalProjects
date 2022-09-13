from django import forms
from django.forms import TextInput, Select

from car.models import Car


class CarsForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
        widgets = {
            'brand': Select(attrs={'class': 'form-control'}),
            'type_of_car': TextInput(attrs={'placeholder': 'Enter the model of the car', 'class': 'form-control'}),
            'num_plate': TextInput(attrs={'placeholder': 'Enter the plate of the car', 'class': 'form-control'}),
            'year': TextInput(attrs={'placeholder': 'Enter the year of the car', 'class': 'form-control'}),
            'user': Select(attrs={'placeholder': 'Select user', 'class': 'form-control'})
        }
