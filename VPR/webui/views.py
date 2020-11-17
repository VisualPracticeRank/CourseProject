from django.shortcuts import render
from django.views.generic import TemplateView, ListView

class SearchView(TemplateView):
    template_name = 'search.html'
