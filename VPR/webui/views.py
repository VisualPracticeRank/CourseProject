from django.shortcuts import render
from django.views.generic import TemplateView, ListView, FormView
from django.http import HttpResponse
import search_eval

def test(request):
    search_eval.run_query("test2")
    return HttpResponse("1")

class SearchView(TemplateView):
    template_name = 'search.html'
    def get_context_data(self, *args, **kwargs):
        context = super(SearchView, self).get_context_data(*args, **kwargs)
        test = search_eval.run_query("test1")
        return context
