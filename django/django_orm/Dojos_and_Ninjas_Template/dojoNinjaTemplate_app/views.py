from django.db import models
from django.shortcuts import redirect, render
from . import models
# Create your views here.
def index(request):
    context={
        'all_dojos': models.get_all_dojos()
    }
    return render(request, 'index.html',context)

def create_dojo(request):
    if request.method == 'POST':
        name=request.POST['name']
        city=request.POST['city']
        state=request.POST['state']
        models.create_new_dojo(name,city,state)
        return redirect('/')


def create_ninja(request):
    fname=request.POST['fname']
    lname=request.POST['lname']
    dojo_name=request.POST['dojo']
    models.create_new_ninja(dojo_name,fname,lname)


    return redirect('/')