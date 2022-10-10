from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('detailed_collection/', views.detailed_collection)
]