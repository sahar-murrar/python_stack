from django.shortcuts import redirect, render
from time import strftime
from . import models

# Create your views here.
def show_new(request):
    return render(request, 'index.html')

def process_data(request):
    if request.method=='POST':
        title=request.POST['title'] 
        network=request.POST['network']
        releaseDate=request.POST['date'] 
        desc=request.POST['desc']
        newShow=models.create_show(title, network, releaseDate, desc)
        request.session['id']=newShow.id
        return redirect('shows/'+str(request.session['id']))

def showInfo(request, id):
    show=models.Show_with_Id(id)
    context={
        'id':show.id,
        'title': show.title,
        'network': show.network,
        'releaseDate': show.releaseDate,
        'desc':show.desc,
        'lastupdated':show.updated_at,
    }
    return render(request, 'showInfo.html', context)      

def showAll(request):
    context={
        'All_shows':models.get_all_show(),
    }
    return render(request, 'all_shows.html', context)

def edit(request, id):
    show=models.Show_with_Id(id)
    request.session['ShowId']=id
    date=show.releaseDate
    new_date=date.strftime('%Y-%m-%d')
    context={
        'id':id,
        'title': show.title,
        'network': show.network,
        'releaseDate': new_date,
        'desc':show.desc,
    }
    return render(request, 'EditPage.html', context)   

def process_updated_data(request):
    if request.method=='POST':
        title=request.POST['title'] 
        network=request.POST['network']
        releaseDate=request.POST['date'] 
        desc=request.POST['desc']
        id = request.session['ShowId']
        show=models.Show_with_Id(id)
        models.update(show, title, network, releaseDate, desc)  
        return redirect('shows/'+id)

def destroy(request, id):
    show=models.Show_with_Id(id) 
    models.delete_show(show)  
    return redirect('/shows')

def root(request):
    return redirect('/shows')       
