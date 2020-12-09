from django import forms
from .models import Dataset

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = Dataset
        fields = ('name','description','data')
    #title = forms.CharField(max_length=50)
    #file = forms.FileField()
