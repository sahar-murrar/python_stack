from django.shortcuts import render

# Create your views here.
def index(request):
        context = {
            "hi":"hello world!"
        
        }
        return render(request,'index.html', context)

def showInfo(request):
  if request.method == "POST":
        name = request.POST['name']
        gender = request.POST['gender']
        courses=request.POST.getlist('courses')#we used gelist function for checkbox because we may have more than one value for the checkbox so we need to put them in a list. also we set the name attribute in the html file to courses for all checkbox to refer them in the getlist function.
        location=request.POST['location']
        language=request.POST['language']
        comment=request.POST['comment']  

        context = {
            "username":name,
            "usergender":gender,
            "usercourses":courses,
            "userlocation":location,
            "userlanguage":language,
            "usercomment":comment
        
        }
        return render(request,'index1.html', context)

