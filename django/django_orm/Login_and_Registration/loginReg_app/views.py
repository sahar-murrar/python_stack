import re
from django.shortcuts import redirect, render
from . import models
from django.contrib import messages
import bcrypt
# Create your views here.
def index(request):
    if 'Userid' in request.session:
        return render(request, 'welcome.html')
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
                # for user in all_users:
                #     if user.email == email:
                #         print("this email is already used by another account !!")
                #         return redirect('/')
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
        # context={
        #     'cars': models.get_user_cars(request.session['Userid'])
        # }
        return render(request, 'welcome.html') 
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
                request.session['Bday']=user.Bdate
                return redirect('/welcome') 
    return redirect('/')         
