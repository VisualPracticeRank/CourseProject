from django.urls import path
from .views import SearchView, ModelView, ModelUpdate, ModelDelete, DatasetUpdate, DatasetDelete
from . import views

urlpatterns = [
    path('', SearchView.as_view(), name='search'),
    path('search', SearchView.as_view(), name='search'),
    path('dataset', views.upload_file, name='dataset'),
    path('model', ModelView.as_view(), name='model'),
    path('model_update/<int:pk>/',ModelUpdate.as_view(),name='ModelUpdate'),
    path('model_delete/<int:pk>/',ModelDelete.as_view(),name='ModelDelete'),
    path('dataset_update/<uuid:pk>/',DatasetUpdate.as_view(),name='DatasetUpdate'),
    path('dataset_delete/<uuid:pk>/',DatasetDelete.as_view(),name='DatasetDelete'),
]
