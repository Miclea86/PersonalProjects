from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from user.forms import UserForm
from user.models import Userextend


class UserCreateView(CreateView):
    template_name = 'user/register_user.html'
    model = Userextend
    form_class = UserForm
    success_url = reverse_lazy('home')
