from django.shortcuts import render

from django.core import serializers
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView

from .models import Trip

# Create your views here.

class TripListView(ListView):
    model = Trip
    template_name = "index.html"

    def get_queryset(self):
        return Trip.objects.all()

class TripCreateView(CreateView):
    model = Trip
    # form_class= forms.NewTripForm
    # success_url = reverse_lazy('trversal:new-day')

class TripDetailView(DetailView):
    model = Trip

class TripUpdateView(UpdateView):
    model = Trip
    # form_class= forms.NewTripForm

class TripDeleteView(DeleteView):
    model = Trip