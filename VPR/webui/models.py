from django.db import models

class Dataset(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=128)
    index = models.BinaryField()

    def __str__(self):
        return self.name


class Model(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=128)
    model = models.TextField()

    def __str__(self):
        return self.name
