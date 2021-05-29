import re
from django.shortcuts import redirect, render
from . import models
from django.contrib import messages
import bcrypt
import dateutil.parser as parser
import datetime
# Create your views here.
def index(request):
    if 'Userid' in request.session:#if the user logged in already rediret him/her to the welcome page without the need to re-access the website
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
            request.session['user']=email
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
        request.session['user']=email
        if user:
            if bcrypt.checkpw(password.encode(), user.password.encode()):
                request.session['Userid']= user.id
                request.session['fname']= user.first_name
                request.session['lname']= user.last_name
                return redirect('/welcome') 
    return redirect('/')         

def wall(request):
    context={
       'messages':models.get_all_messages(),
       'comments':models.get_all_comments(),
    }
    return render(request, 'wall.html',context)

def process_messages(request):
    if request.method =='POST':
        message=request.POST['message']
        msg=models.create_message(message,request.session['user'])
        request.session['messageId']=msg.id
    return redirect('/wall')       


def process_comments(request):
    if request.method =='POST':
        comment=request.POST['comment']
        new_comment=models.create_comment(comment,request.session['user'], request.POST['messageId'])
        request.session['msgid']=request.POST['messageId']
    return redirect('/wall') 

def delete_message(request):
    if request.method == 'POST':
        message_id=request.POST['messageIdDelete']
        created_at_date=request.POST['created_at_date']
        Currenttime = datetime.datetime.now()
        CreatedAt=parser.parse(created_at_date)
        print("the created minutes are:",CreatedAt.minute)
        print("the current minutes are: ",Currenttime.minute)
        print(Currenttime.hour - CreatedAt.hour)
        print(Currenttime.minute - CreatedAt.minute)
        # if ((Currenttime.hour - CreatedAt.hour) ==0 and (Currenttime.minute - CreatedAt.minute)==30) or ((Currenttime.hour - CreatedAt.hour) ==1 and (Currenttime.minute - CreatedAt.minute)== -30): #means that the elapsed time i30 mintues after posting the message 
            #if the above if statment achieved then call the delete function from the models.py
        models.delete_message(message_id,request.session['user'])
        return redirect('/wall')
