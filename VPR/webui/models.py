from django.db import models
import uuid
import os

def dataset_id_path(instance, filename):
    return 'datasets/{0}/dataset/dataset.dat'.format(instance.id)

class Dataset(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=128)
    data = models.FileField(upload_to=dataset_id_path)

    def __str__(self):
        return self.name

class Model(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=128)
    model = models.TextField()

    def __str__(self):
        return self.name
