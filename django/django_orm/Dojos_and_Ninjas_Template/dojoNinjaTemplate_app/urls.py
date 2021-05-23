from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('create_dojo', views.create_dojo),
    path('create_ninja', views.create_ninja),
]
