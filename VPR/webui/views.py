from django.shortcuts import render
from django.views.generic import TemplateView, ListView, FormView, UpdateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic.list import ListView
from django.core.files.storage import default_storage
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UploadFileForm
from .models import Model, Dataset, Document
from django.urls import reverse
import subprocess
import uuid
import os
from django.conf import settings

class DatasetDelete(DeleteView):
    model = Dataset
    template_name = 'delete.html'

    def get_success_url(self):
        return reverse('dataset')

class DatasetUpdate(UpdateView):
    model = Dataset
    fields = ['name', 'description']
    template_name = 'update.html'

    def get_success_url(self):
        return reverse('dataset')

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
        datasets = []
        for dataset in Dataset.objects.all():
            datasets.append({'id': dataset.id, 'name': dataset.name})
        context['datasets'] = datasets

        # build context for models
        models = []
        for model in Model.objects.all():
            models.append({'id': model.id, 'name': model.name})
        #context['models'] = [{'id': 0, 'name': 'test'}, {'id': 1, 'name': 'test2'}]
        context['models'] = models

        if "query" in self.request.GET:
            results = eval(subprocess.run(["python3", "search_eval.py", self.request.GET.get("query")], stdout=subprocess.PIPE).stdout.decode("utf-8"))
            print(results)
            list = []
            counter = 1
            for x in results:
                list.append({'body': Document.objects.get(document_id=x[0]).body[0 : 120], 'score': x[1], 'rank': counter})
                counter += 1
            context['results'] = list
        return context

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            test = form.save()
            file_id = Dataset.objects.get(id=test.id)
            mfile = open(os.path.join(settings.MEDIA_ROOT, "datasets/{}/dataset/dataset.dat".format(file_id.id)), 'r')
            counter = 0
            for line in mfile.readlines():
                Document.objects.create(body=line,document_id=counter,dataset=file_id)
                counter += 1
            return HttpResponseRedirect('/')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form,'object_list': Dataset.objects.all()})
