from django.urls import path
from . import views
urlpatterns = [
    path('',views.guess),
    path('guess',views.guess_result),
    path('reset',views.reset),
    path('username',views.send_name),
]