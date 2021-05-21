from django.db import models
from . import views
# Create your models here.
class User_template(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return f"<User object: {self.first_name} {self.last_name} {self.email_address} {self.age} {self.created_at} {self.updated_at} > "


def create_user(fname, lname, email, age):
    new_user = User_template.objects.create( first_name=fname,last_name=lname,email_address=email, age=age)

def get_all():
    return User_template.objects.all() #it wll return a query set that contains all users objects that we added