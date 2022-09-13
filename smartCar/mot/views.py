from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from mot.forms import MotForm
from mot.models import Mot


class MotCreateView(LoginRequiredMixin, CreateView):
    template_name = 'mot/create_mot.html'
    model = Mot
    form_class = MotForm
    success_url = reverse_lazy('home')


class MotListView(LoginRequiredMixin, ListView):
    template_name = 'mot/list_of_mots.html'
    model = Mot
    context_object_name = 'all_mots'


class MotUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "mot/update_mot.html"
    model = Mot
    form_class = MotForm
    success_url = reverse_lazy('list_of_mots')


class MotDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "mot/delete_mot.html"
    model = Mot
    success_url = reverse_lazy('list_of_mots')
