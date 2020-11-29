from django.urls import path
from .views import SearchView, ModelView, ModelUpdate, ModelDelete
from . import views

urlpatterns = [
    path('', SearchView.as_view(), name='search'),
    path('search', SearchView.as_view(), name='search'),
    path('upload', views.upload_file, name='upload'),
    path('model', ModelView.as_view(), name='model'),
    path('model_update/<int:pk>/',ModelUpdate.as_view(),name='ModelUpdate'),
    path('model_delete/<int:pk>/',ModelDelete.as_view(),name='ModelDelete'),
]
