from django.db import models

# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=255)
    desc=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
class Author(models.Model):
    book = models.ManyToManyField(Books, related_name="authors")
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    notes=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def get_all_books():
    return Books.objects.all()

def get_book_withId(book_id):
    return Books.objects.get(id=book_id)    

def create_book(title, desc):
    Books.objects.create(title=title, desc=desc)    

def get_authors_for_bookId(book_id):
    b=Books.objects.get(id=book_id)
    authors=b.authors.all()
    return authors
    
def get_all_authors():
    return Author.objects.all()

def addAuthor_toBook(author_name,book_id):
    arr=str(author_name).split(" ")
    print(arr[0])
    a=Author.objects.get(first_name=arr[0])
    # Author.objects.get(last_name=arr[1])
    authorId=a.id
    auth=Author.objects.get(id=authorId)
    b=Books.objects.get(id=book_id)
    for i in Author.objects.all():
        if auth == i.id:
            print("this author is already added to this book!!")
        else:
            auth.book.add(b)       

def create_author(fname,lname,notes):
    Author.objects.create(first_name=fname, last_name=lname, notes=notes)

def get_author_withId(author_id):
    return Author.objects.get(id=author_id)  

def get_books_for_authorId(autho_id):
    a=Author.objects.get(id=autho_id)
    books=a.book.all()
    return books  

def addBook_toAuthor(title, author_id):    
    b=Books.objects.get(title=title)
    bookId=b.id
    bok=Books.objects.get(id=bookId)
    a=Author.objects.get(id=author_id)
    for i in Books.objects.all():
        if bok == i.id:
            print("this book is already added to this author!!")
        else:
            bok.authors.add(a)  