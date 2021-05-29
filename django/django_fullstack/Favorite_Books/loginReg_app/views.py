import re
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from . import models
from django.contrib import messages
import bcrypt
# Create your views here.
def index(request):
    if 'Userid' in request.session: #if the user logged in already rediret him/her to the welcome page without the need to re-access the website
        return redirect('/welcome')
    return render(request, 'index.html')

def register(request):
    if request.method == "POST":
        all_users=models.get_all_users()
        errors = models.User.objects.registration_validator(request.POST, all_users)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:    
            fname=request.POST['fname']
            lname=request.POST['lname']
            email=request.POST['email']
            password=request.POST['password']
            confirmpassword= request.POST['confirmpassword'] 
            Bday=request.POST['Bday']
            if(password == confirmpassword): #even if we didn't enter a password and hit register it will render the welcome page because both password and it's confirmation are the same (they are empty)!!
                hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
                new_user=models.create_user(fname, lname, email,Bday, hashed_password)
                request.session['Userid']= new_user.id
                request.session['fname']= new_user.first_name
                request.session['lname']= new_user.last_name
                request.session['Bday']=new_user.Bdate
                return redirect('/welcome') #it is not preferable to render inside the method that check for post, we have to to redirect ot a new method and make that method to render what we want.
    return redirect('/')          

def welcome(request):
    if 'Userid' in request.session: #to make sure that if we tried to access the /welcome routes from the url to see the welcome page to not open it if we are not logged in/saved to the session
        books=models.get_all_books()
        userId=request.session['Userid']
        Liked_books=models.get_books_for_auser(userId)
        context={
            'books': books,
            "loggedUser_id":userId,
            "liked_books":Liked_books,
        }
        return render(request, 'welcome.html',context) 
    return redirect('/')    

def logout(request):
    request.session.clear()
    return redirect('/')   

def login(request):
    if request.method == "POST": 
        email=request.POST['email']
        password=request.POST['password'] 
        user=models.get_user(email)  
        if user:
            if bcrypt.checkpw(password.encode(), user.password.encode()):
                request.session['Userid']= user.id
                request.session['fname']= user.first_name
                request.session['lname']= user.last_name
                return redirect('/welcome') 
    return redirect('/') 

def process_fav_book(request):
    if request.method == "POST":
        errors = models.Books.objects.book_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/welcome')
        else:    
            title=request.POST['title']
            desc=request.POST['desc']
            userId=request.session['Userid']
            book=models.create_book(title, desc,userId)
            models.add_to_favorites(book.id, userId)
            return redirect('/welcome')

def book_info(request, id):
    book =models.get_book_with_id(id)
    users=models.get_users_for_abook(id)
    userId=request.session['Userid']
    Liked_books=models.get_books_for_auser(userId)
    context={
        'book':book,
        'users':users,
        'liked_books':Liked_books,
        'logged_user':models.get_user_withId(userId),
        }
    if (book.uploaded_by.id != userId): #means that the logged user is not the uploader of the book
        return render(request, 'bookInfo.html',context)    
    elif (book.uploaded_by.id == userId): #means that the logged user is the uploader of the book 
        return render(request, 'editBookInfo.html', context) 



def favorite_book(request, id):
    userId=request.session['Userid']
    models.add_to_favorites(id, userId)
    return redirect('/book_info/'+id)

def unfavorite_book(request, id):
    userId=request.session['Userid'] 
    models.remove_from_favorites(id, userId)
    return redirect('/book_info/'+id)

def edit_book_info(request, id):
    if request.method == "POST":
        if request.POST['button'] == 'Update':
            errors = models.Books.objects.book_validator(request.POST)
            if len(errors) > 0:
                for key, value in errors.items():
                    messages.error(request, value)
                return redirect('/book_info/'+id)
            else:    
                title=request.POST['title']
                desc=request.POST['desc']
                models.update_book_info(id, title, desc)
                return redirect('/book_info/'+id)
        elif request.POST['button'] == 'Delete':
            models.delete_book(id)
            return redirect('/welcome')  
            
def view_all_Favorites(request, id):
    user= models.get_user_withId(id)
    favorite_books=models.get_books_for_auser(id)
    context={
        'list_of_FavoriteBooks':favorite_books,
        'user':user,
    }
    return render(request, 'UserFavoriteBooks_list.html', context)


