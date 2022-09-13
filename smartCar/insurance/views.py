from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from insurance.forms import InsuranceForm
from insurance.models import Insurance


class InsuranceCreateView(LoginRequiredMixin, CreateView):
    template_name = 'insurance/create_insurance.html'
    model = Insurance
    form_class = InsuranceForm
    success_url = reverse_lazy('home')


class InsuranceListView(LoginRequiredMixin, ListView):
    template_name = 'insurance/list_of_insurances.html'
    model = Insurance
    context_object_name = 'all_insurances'


class InsuranceUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "insurance/update_insurance.html"
    model = Insurance
    form_class = InsuranceForm
    success_url = reverse_lazy('list_of_insurances')


class InsuranceDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "insurance/delete_insurance.html"
    model = Insurance
    success_url = reverse_lazy('list_of_insurances')
