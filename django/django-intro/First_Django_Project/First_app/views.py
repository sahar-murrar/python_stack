from django.shortcuts import redirect, render, HttpResponse
from django.http import JsonResponse

def root(request):
    return redirect('/blogs')

def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
    return redirect('/') #you have to put the / in the redirect, it will not work if yu put ''

def show(request,number):
    return HttpResponse(f"placeholder to display blog number: {number}")

def edit(request,number):
    return HttpResponse(f"placeholder to edit blog number: {number}")

def destroy(request,number):
    return redirect('/blogs')

def jsonmethod(request):
    data = {
        "title":"My First Blog",
        "content" : "Lorem, ipsum dolor sit amet consectetur adipisicing elit."
    }
    return JsonResponse(data)