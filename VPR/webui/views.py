from django.shortcuts import render
from django.views.generic import TemplateView, ListView, FormView
import search_eval
import subprocess

#class SearchView(TemplateView):
#    template_name = 'search.html'
#
#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        context['query'] = self.request.GET.get("query")
#        #search_eval.run_query(context['query'])
#        return context

class SearchView(TemplateView):
    template_name = 'search.html'
    def get_context_data(self, *args, **kwargs):
        context = super(SearchView, self).get_context_data(*args, **kwargs)
        context['results'] = eval(subprocess.run(["python3", "search_eval.py", self.request.GET.get("query")], stdout=subprocess.PIPE).stdout.decode("utf-8"))
        return context
