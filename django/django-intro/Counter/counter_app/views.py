from django.shortcuts import redirect, render

# Create your views here.
def count(request):

    if 'flag' in request.session:
        if request.session['flag'] != 1:
            if 'count_times' and 'actual_times' in request.session:
                request.session['count_times'] +=1
                request.session['actual_times']+=1
            else:
                request.session['count_times'] = 1
                request.session['actual_times']= 1 
        elif request.session['flag'] == 1:
            if 'count_times' in request.session:
                request.session['count_times'] +=1
                request.session['flag']=0 #return the value of the flag to 0 becuase without this line it will remain 1 and the actual visit times will be never changed when refresh the url!
            else:
                request.session['count_times'] = 1  
                request.session['flag']=0 #return the value of the flag to 0 becuase without this line it will remain 1 and the actual visit times will be never changed when refresh the url!    
    else:
       request.session['flag']=0
       if 'count_times' and 'actual_times' in request.session:
                request.session['count_times'] +=1
                request.session['actual_times']+=1
       else:
            request.session['count_times'] = 1
            request.session['actual_times']= 1 

    context = {
            "hi":"hello world!"
        
    }
    return render(request,'index.html', context)

def destroy(request):
  if request.method == "POST" or request.method == "GET":     
    if 'count_times' in request.session:
        del request.session['count_times']

    if 'actual_times' in request.session:    
        del request.session['actual_times']    

    return redirect('/')    

def addTwo(request):
    if request.method == "POST":
        if request.POST["button"]=="Add two Visits!":
            request.session["count_times"] += 1 #we added here 1 not 2 because when we redirect it to the root route it will add nother 1, so it will be 3 not 2 as we want, that's why we added 1 becuase after redirecting it will be increamented by another 1 and in total we added 2 to the counter.  
        elif request.POST["button"]=="Increament":
            if request.POST['increamentBy'] != '': #check if the input text is not none/empty
                request.session['increamentBy']= int(request.POST['increamentBy'])
                request.session['count_times'] = request.session['count_times'] + request.session['increamentBy']-1 # -1 because the redirect will add 1 by default
            else:
                request.session['count_times']-=1 #if it empty so decrement by 1 because the redirect will increment by 1 and in the end the count will be the same because count-1+1 = count so it will remain the same value and that what we want.

        request.session['flag']=1
        return redirect("/") #redirect to root route
