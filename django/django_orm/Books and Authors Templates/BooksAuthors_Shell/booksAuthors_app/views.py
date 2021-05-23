from django.shortcuts import redirect, render
from . import models
# Create your views here.
def index(request):
    context={
        'all_books': models.get_all_books()
    }
    return render(request, 'index.html',context)

def add_book(request):
    if request.method=='POST':
        title=request.POST['title']
        desc=request.POST['desc']
        models.create_book(title,desc)
        return redirect('/')

def about_book(request, book_id):
    request.session['book_id']=book_id
    book=models.get_book_withId(book_id)
    authors=models.get_authors_for_bookId(book_id)
    all_authors=models.get_all_authors()
    context={
        "book_id": book_id,
        "book_title": book.title,
        "book_desc": book.desc,
        "authors":authors,
        "all_authors":all_authors,
    }
    return render(request, 'about_book.html', context)   

def addAuthor_toBook(request):
    if request.method=='POST':
        authorName=request.POST['author']
        book_id=request.session['book_id']
        models.addAuthor_toBook(authorName, book_id)
        return redirect('/books/'+book_id)

def authors(request):
    context={
        'all_authors': models.get_all_authors()
    }
    return render(request, 'Allauthors.html', context)

def add_author(request):
        if request.method=='POST':
            fname=request.POST['fname']
            lname=request.POST['lname']
            notes=request.POST['notes']
            models.create_author(fname,lname,notes)
            return redirect('/authors')

def about_author(request, author_id):
    request.session['author_id']=author_id
    author=models.get_author_withId(author_id)
    books=models.get_books_for_authorId(author_id)
    all_books=models.get_all_books()
    context={
        "author_id": author_id,
        "author_fname": author.first_name,
        "author_lname": author.last_name,
        "author_notes": author.notes,
        "books":books,
        "all_books":all_books,
    }
    return render(request, 'about_author.html', context)   

def addBook_toAuthor(request):
    if request.method=='POST':
        title=request.POST['book']
        author_id=request.session['author_id']
        models.addBook_toAuthor(title, author_id)
        return redirect('/authors/'+author_id)