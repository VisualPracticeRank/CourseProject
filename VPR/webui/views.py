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
import base64

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
        models = ['OkapiBM25','PivotedLength','AbsoluteDiscount','JelinekMercer','DirichletPrior']
        default_models = models.copy()
        for model in Model.objects.all():
            models.append(model.name)
        context['models'] = models

        context['default_model'] = self.request.GET.get("model")
        context['default_dataset'] = self.request.GET.get("dataset")

        if "query" in self.request.GET:
            print(self.request.GET)
            obj = Dataset.objects.get(name=self.request.GET.get("dataset")) # find dataset path
            print(obj.id)
            set_model = self.request.GET.get("model")
            if set_model not in default_models:
                set_model = base64.b64encode(Model.objects.get(name=set_model).model.encode())
            print(set_model)
            folder = obj.data.name.split("/")[1]
            results = eval(subprocess.run(["python3", "search_eval.py", folder, set_model, self.request.GET.get("query")], stdout=subprocess.PIPE).stdout.decode("utf-8"))
            #print(results)
            
            list = []
            counter = 1
            
            # results[0] = top k articles and scores
            # results[1] = ndcg score for each query
            # results[3]: 
            #              results[3][0] - avg_dl
            #              results[3][1] - num_docs
            #              results[3][2] - total_terms
            #              results[3][3] - query_length
            #              results[3][4] - corpus_term_count
            #              results[3][5] - corpus_unique_term
            #              results[3][6] - term_doc_count (tuple list)
            #              results[3][0] - corpus_term_count (tuple list)
            # results[3] = average ndcg score
            #for x in results[0][0]:
            #    list.append({'body': Document.objects.filter(dataset_id=obj.id).get(document_id=x[0]).body[0 : 120], 'score': x[1], 'rank': counter})
            
            # MAIN
            for x in results:
                doc = Document.objects.filter(dataset_id=obj.id).get(document_id=x[0])
                list.append({'body': doc.body[0 : 120], 'score': x[1], 'rank': counter, 'doc_size': doc.doc_size, 'unique_terms': doc.doc_unique_terms})
                counter += 1
            
            context['results'] = list
        return context

class IterateView(TemplateView):
    template_name = 'iterate.html'
    def get_context_data(self, *args, **kwargs):
        results = eval(subprocess.run(["python3", ""], stdout=subprocess.PIPE).stdout.decode("utf-8"))
        context = super(IterateView, self).get_context_data(*args, **kwargs)
        return context

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            test = form.save()
            file_id = Dataset.objects.get(id=test.id)
            mfile = open(os.path.join(settings.MEDIA_ROOT, "datasets/{}/dataset/dataset.dat".format(file_id.id)), 'r')
            counter = 0

            results = eval(subprocess.run(["python3", "doc_data.py", str(file_id.id)], stdout=subprocess.PIPE).stdout.decode("utf-8"))
            doc_data = results['doc_data']
            for line in mfile.readlines():
                Document.objects.create(body=line,document_id=counter,dataset=file_id,doc_size=doc_data[counter]['doc_size'],doc_unique_terms=doc_data[counter]['unique_terms'])
                counter += 1

            file_id.unique_terms = results['corpus_data']['unique_terms']
            file_id.avg_dl = results['corpus_data']['avg_dl']
            file_id.num_docs = results['corpus_data']['num_docs']
            file_id.save()

            return HttpResponseRedirect('/')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form,'object_list': Dataset.objects.all()})
