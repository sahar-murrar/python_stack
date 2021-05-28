from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('welcome', views.welcome),
    path('logout', views.logout),
    path('login', views.login),
    path('wall', views.wall),
    path('process_messages', views.process_messages),
    path('process_comments', views.process_comments),
    path('delete_message', views.delete_message),

]
