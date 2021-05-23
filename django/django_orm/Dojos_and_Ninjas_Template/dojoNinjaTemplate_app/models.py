from django.db import models

# Create your models here.
class Dojos(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    desc=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
class Ninjas(models.Model):
    dojo = models.ForeignKey(Dojos, related_name="ninjas", on_delete = models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def get_all_dojos():
    return Dojos.objects.all()

def create_new_dojo(name,city,state):
    Dojos.objects.create(name=name, city=city,state=state,desc="new dojo")

def create_new_ninja(dojo_name, first_name, last_name):
    Ninjas.objects.create(dojo=Dojos.objects.get(name=dojo_name), first_name=first_name, last_name=last_name)    
