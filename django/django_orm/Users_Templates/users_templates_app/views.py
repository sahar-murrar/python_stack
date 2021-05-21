from django.shortcuts import render,redirect
from . import models
# Create your views here.
def root(request):
      
    context={
        "all_user": models.get_all()
    }
    return render(request, 'index.html',context)

def process_data(request):
    if request.method == "POST":
        request.session['first_name']=request.POST['firstname']
        request.session['last_name']=request.POST['lastname']
        request.session['email']=request.POST['email']
        request.session['age']=request.POST['age']
        models.create_user(request.session['first_name'], request.session['last_name'],request.session['email'],request.session['age'])
        # request.session['all_user']=models.get_all()
        

    return redirect('/')    
