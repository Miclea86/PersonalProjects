from django.contrib.auth.forms import UserCreationForm
from django.forms import TextInput

from user.models import Userextend


class UserForm(UserCreationForm):
    class Meta:
        model = Userextend
        fields = ['username', 'email', 'phone_number']

        widgets = {
            'username': TextInput(attrs={'placeholder': 'Please enter user name', 'class': 'form-control'}),
            'email': TextInput(attrs={'placeholder': 'Please enter email', 'class': 'form-control'}),
            'phone_number': TextInput(attrs={'placeholder': 'Please insert phone number', 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Please enter your password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Please enter your password confirmation'
