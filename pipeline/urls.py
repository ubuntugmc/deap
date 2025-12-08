from django.urls import path
from .views import run_pipeline

urlpatterns = [
    path('run/', run_pipeline, name='run_pipeline'),
]
