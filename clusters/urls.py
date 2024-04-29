from django.urls import path
from .views import cluster_view

urlpatterns = [
    path('', cluster_view, name='cluster_view'),
]
