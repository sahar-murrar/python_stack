from django.urls import path
from . import views
urlpatterns = [
    # it is required that When we go to localhost:8000 or localhost:8000/time_display the method index should render the current date and time.
    path('',views.index),
    path('time_display',views.index),
]