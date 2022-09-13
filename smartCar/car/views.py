from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from car.forms import CarsForm
from car.models import Car


class CarCreateView(LoginRequiredMixin, CreateView):
    template_name = 'car/create_car.html'
    model = Car
    form_class = CarsForm
    success_url = reverse_lazy('home')


class CarListView(LoginRequiredMixin, ListView):
    template_name = 'car/list_of_cars.html'
    model = Car
    # context_object_name = 'all_cars'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CarListView, self).get_context_data(**kwargs)
        var = self.request.user.id
        context["all_cars"] = Car.objects.filter(user_id=var)
        return context


class CarUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "car/update_car.html"
    model = Car
    form_class = CarsForm
    success_url = reverse_lazy('list_of_cars')


class CarDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "car/delete_car.html"
    model = Car
    success_url = reverse_lazy('list_of_cars')


class CarDetailView(LoginRequiredMixin, DetailView):
    template_name = 'car/detail_car.html'
    model = Car
