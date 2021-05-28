from django.db import models
from django.db.models.fields.related import ManyToManyField
import re
import datetime

from django.shortcuts import redirect

# Create your models here.

class UserManager(models.Manager):
    def registration_validator(self, postData, all_users):
        errors = {}
        regex = re.compile(r'^[a-zA-Z]+$')
        CurrentDate = datetime.datetime.now()
        # age= str(CurrentDate)- str(postData['Bday'])
        Bdate=datetime.datetime.strptime(postData['Bday'],'%Y-%m-%d')
        age= CurrentDate.year - Bdate.year
        print(age) 
        if age < 13:
             errors["age"]="Your Age should be at least 13 years old!!"
        if len(postData['fname']) <  2 :
                errors["fname"] = "First Name should be at least 2 letters"
        elif not regex.match(postData['fname']):
                errors["fname"] = "First Name should contain only letters!"     
        if len(postData['lname']) < 2: 
            errors["lname"] = "Last Name should be at least 2 letters"
        elif not regex.match(postData['lname']):
                errors["lname"] = "Last Name should contain only letters!"       
        if re.search(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$',postData['email']) is None:
            errors["email"] = "Invaild Email Address!"  
        elif re.search(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$',postData['email']) is not None:
            for user in all_users:
                        if user.email == postData['email']:
                            errors["email"] = "this email is already used by another account !!"
                            print("this email is already used by another account !!")    
        if str(postData['Bday']) > str(CurrentDate) :
            errors['Bday'] = "Birthday date must be a past date!!"   
        if len(postData["password"]) <8:
            errors["password"] = "Your Password should be at least 8 characters!"
        elif postData["password"] !=postData["confirmpassword"]:
            errors["password"] = "Your Password should be the same as the Confirmation password!"

        return errors
#the relation between the car and user is many to many because one user can rent many cars and a car can be rented by many users
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    Bdate=models.DateField(default=datetime.datetime.now())
    password=models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=UserManager()

class Messages(models.Model):
    messageText=models.TextField()
    user = models.ForeignKey(User, related_name="messages", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comments(models.Model):
    commentText=models.TextField()
    user = models.ForeignKey(User, related_name="comments", on_delete = models.CASCADE)
    message = models.ForeignKey(Messages, related_name="comments", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


def create_user(fname, lname, email,birthday, password):
    return User.objects.create(first_name=fname, last_name=lname, email=email, Bdate=birthday, password=password)    

def get_user(email):
    # return User.objects.filter(email=email, password=password)[0] #without [0] it will return all users with this email and password, so [0] it will select only the first user that have these email and password 
    users = User.objects.filter(email=email)
    if len(users)>0: #check if the list is not empty
        return users[0]
    return None 

def get_all_users():
    return User.objects.all()

def create_message(message_text, user_email):
    user= User.objects.get(email=user_email)
    return Messages.objects.create(messageText=message_text, user=user) 

def get_all_messages():
    return Messages.objects.all()    

def create_comment(comment_text, user_email, message_id):
    message= Messages.objects.get(id=message_id)
    user= User.objects.get(email=user_email)
    return Comments.objects.create(commentText=comment_text, user=user, message=message)

def get_all_comments():
    return Comments.objects.all()

def get_all_comments_for_Post(post_id):
    post=Messages.objects.get(id=post_id)
    return post.comments.all()

def delete_message(message_id, user_email):
    user=User.objects.get(email=user_email)
    message=Messages.objects.get(id=message_id) 
    print(message.user.id)
    print(user.id) 
    if(message.user.id == user.id):
        message.delete() 
