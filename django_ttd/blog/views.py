from django.shortcuts import render
#from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from .models import Entry
# Create your views here.

class HomeView(ListView):
	template_name = 'index.html'
	queryset = Entry.objects.order_by('-created_at')

class EntryDetail(DetailView):
	model = Entry
