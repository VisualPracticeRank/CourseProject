from django.urls import path
from .views import SearchView
from . import views


urlpatterns = [
    path('', SearchView.as_view(), name='search'),
    path('search', SearchView.as_view(), name='search'),
    path('search2', views.test, name='hello'),
]
