from django.shortcuts import redirect, render
import random

# Create your views here.

def guess(request):
    user_num=-1
    if 'flag' in request.session and  request.session['flag']!=1: #if the flag=0
        print("the initial value for the flag:" ,request.session['flag'])
        if request.method == "GET": #if the request is get (which means only when do refresh for the web page)
            request.session['random_num']=random.randint(1,100) #generating a random number between 1 and 100, then save it inside sessio key called random_num.
            print("the random generated number is:",request.session['random_num'])
            request.session['played_times']=0   
    elif 'flag' not in request.session:
            request.session['flag']=0
            request.session['random_num']=random.randint(1,100) #generating a random number between 1 and 100, then save it inside sessio key called random_num.
            print("the random generated number is:",request.session['random_num'])   
            request.session['played_times']=0    
    if 'user_num' in request.session:
        user_num=request.session['user_num'] #set user_num to request.session['user_num'] wheter it is =-1 or the user input.
        # if 'random_num' not in request.session:
        #     request.session['random_num']=random.randint(1,100) #generating a random number between 1 and 100, then save it inside sessio key called random_num.
        #     print("the random generated number is:",request.session['random_num'])
        if request.session['user_num'] !=-1:
            print("user number is:",request.session['user_num']) #printing the user input
            #comparing the generated number with the user input:
            if(request.session['user_num'] == request.session['random_num']): 
                print("sucess")
                print(f"you took {request.session['played_times']} of attempts")
            elif(request.session['user_num'] > request.session['random_num']):
                print("Too High!")
                if request.session['played_times'] < 6: 
                    request.session['played_times']+=1 
                    print("played_times: ",request.session['played_times']) 
            elif(request.session['user_num'] < request.session['random_num']):
                print("Too Low!") 
                if request.session['played_times'] < 6: 
                    request.session['played_times']+=1 
                    print("played_times: ",request.session['played_times']) 
                    
    request.session['user_num']=-1 #setting the value of request.session['user_num'] to -1 and that's why we assigned it's value to user_num variable to make it possible to change the value of the session key wihtout affecting the actual value
    #if the value remained as it, when we refresh the web page it will remain the value of the session as the old value and then it will give a result without entering an input  from the user.
    # user_num=request.session['user_num']
    request.session['flag']=0 #setting the value of the flag to 0.
    # print("flag value:",request.session['flag'])
    context = {
            "user_num":user_num #putting the value of num_user inside the context to use it in the html file
        
    }
    return render(request, 'index1.html', context)

def guess_result(request):
    if request.method == "POST": #only when we have post request (sumbit our data)
        if request.POST['user_num'] !="": #make sure that the user input is not empty
            request.session['user_num']= int(request.POST['user_num']) #setting session key 'user_num' to the submitted data
 
    request.session['flag']=1 #enable the flag by setting it to 1
    return redirect('/')  

def reset(request):
    if 'user_num' in request.session:
        del request.session['user_num']

    if 'random_num' in request.session:    
        del request.session['random_num']  
    #or use :
    # request.session.clear()    
  

    return redirect('/') 


def send_name(request):
    if request.method =='POST':
        request.session['name']=request.POST['username']
        # request.session['name']=[]
        # request.session['name'].append(request.POST['username'])
        # request.session.save()
        return render(request, 'userInfo.html')