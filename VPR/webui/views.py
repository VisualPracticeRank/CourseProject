from django.shortcuts import render
from django.views.generic import TemplateView, ListView, FormView, UpdateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic.list import ListView
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UploadFileForm
from .models import Model
from django.urls import reverse
import subprocess

class ModelDelete(DeleteView):
    model = Model
    template_name = 'delete.html'

    def get_success_url(self):
        return reverse('model')

class ModelUpdate(UpdateView):
    model = Model
    fields = ['name', 'description', 'model']
    template_name = 'update.html'

    def get_success_url(self):
        return reverse('model')

class ModelView(CreateView):
    model = Model
    template_name = "model.html"
    fields = ['name', 'description', 'model']

    def get_context_data(self, **kwargs):
        context = super(ModelView, self).get_context_data(**kwargs)
        context["object_list"] = Model.objects.all()
        return context

    def get_success_url(self):
        return reverse('model')


class SearchView(TemplateView):
    template_name = 'search.html'
    def get_context_data(self, *args, **kwargs):
        context = super(SearchView, self).get_context_data(*args, **kwargs)
        if "query" in self.request.GET:
            context['results'] = eval(subprocess.run(["python3", "search_eval.py", self.request.GET.get("query")], stdout=subprocess.PIPE).stdout.decode("utf-8"))
        return context

def upload_file(request):
    if request.method == 'POST':
        print('test')
        form = UploadFileForm(request.POST, request.FILES)
        print(request.FILES['file'].temporary_file_path())
        if form.is_valid():
            print(request.FILES['file'])
            return HttpResponseRedirect('/')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})
