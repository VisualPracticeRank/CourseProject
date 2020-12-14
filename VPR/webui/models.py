from django.db import models
import uuid
import os

def dataset_id_path(instance, filename):
    return 'datasets/{0}/dataset/dataset.dat'.format(instance.id)

def qrels_id_path(instance, filename):
    return 'datasets/{0}/dataset/qrels.txt'.format(instance.id)

def queries_id_path(instance, filename):
    return 'datasets/{0}/dataset/queries.txt'.format(instance.id)

class Dataset(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=32,  unique=True)
    description = models.CharField(max_length=128)
    data = models.FileField(upload_to=dataset_id_path)
    qrels = models.FileField(upload_to=qrels_id_path)
    queries = models.FileField(upload_to=queries_id_path)
    unique_terms = models.IntegerField(null=True)
    avg_dl =  models.FloatField(null=True)
    num_docs = models.IntegerField(null=True)


    def __str__(self):
        return self.name

class Document(models.Model):
    document_id = models.IntegerField()
    body = models.TextField()
    doc_size = models.IntegerField(null=True)
    doc_unique_terms = models.IntegerField(null=True)
    dataset = models.ForeignKey(
        'Dataset',
        on_delete=models.CASCADE,
    )

class Model(models.Model):
    name = models.CharField(max_length=32, unique=True)
    description = models.CharField(max_length=128)
    model = models.TextField()

    def __str__(self):
        return self.name
