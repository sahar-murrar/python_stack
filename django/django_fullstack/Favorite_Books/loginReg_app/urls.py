from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('welcome', views.welcome),
    path('logout', views.logout),
    path('login', views.login),
    path('process_fav_book', views.process_fav_book),
    path('book_info/<id>', views.book_info),
    path('favorite_book/<id>', views.favorite_book),
    path('unfavorite_book/<id>', views.unfavorite_book),
    path('edit_book_info/<id>', views.edit_book_info),
    path('view_all_Favorites/<id>', views.view_all_Favorites),

]
