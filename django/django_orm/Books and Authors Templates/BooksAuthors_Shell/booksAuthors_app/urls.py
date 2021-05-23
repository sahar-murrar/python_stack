from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('add_book', views.add_book),
    path('books/<book_id>', views.about_book),
    path('addAuthor_toBook', views.addAuthor_toBook),
    path('authors', views.authors),
    path('add_author', views.add_author),
    path('authors/<author_id>', views.about_author),
    path('addBook_toAuthor', views.addBook_toAuthor),
]

