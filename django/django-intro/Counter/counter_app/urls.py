from django.urls import path
from . import views
urlpatterns = [
    path('',views.count),
    path('destroy_session',views.destroy),
    path('addTwo', views.addTwo),
]