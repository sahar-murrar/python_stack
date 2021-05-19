from django.urls import path
from . import views
urlpatterns = [
    path('',views.ninja),
    path('process_money', views.process_money),
    path('destroy', views.destroy),
]