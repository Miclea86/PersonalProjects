from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from roadTax.forms import RoadTaxForm
from roadTax.models import RoadTax


class RoadTaxCreateView(LoginRequiredMixin, CreateView):
    template_name = 'roadTax/create_roadTax.html'
    model = RoadTax
    form_class = RoadTaxForm
    success_url = reverse_lazy('home')


class RoadTaxListView(LoginRequiredMixin, ListView):
    template_name = 'roadTax/list_of_roadTaxes.html'
    model = RoadTax
    context_object_name = "all_roadTaxes"


class RoadTaxUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "roadTax/update_roadTax.html"
    model = RoadTax
    form_class = RoadTaxForm
    success_url = reverse_lazy('list_of_roadTaxes')


class RoadTaxDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "roadTax/delete_roadTax.html"
    model = RoadTax
    success_url = reverse_lazy('list_of_roadTaxes')

