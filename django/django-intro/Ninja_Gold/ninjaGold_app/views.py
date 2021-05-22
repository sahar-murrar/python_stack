from django.shortcuts import redirect, render
import random
import datetime
# Create your views here.
def ninja(request):
    if 'golds' not in request.session:
            request.session['golds'] =0 # the golds initially are 0
    return render(request, 'index.html')

def process_money(request):
    if request.method == "POST":
        if 'activities' not in request.session: 
            request.session['activities'] =[]
        if request.POST['which_form'] == 'farm':
            num=random.randint(10,20)
            request.session['golds']+=num
            # request.session['activities'].append('Earned '+str(num)+ ' golds from the farm! ('+
            #     '{:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now())) #append will add at the end of the list
            request.session['activities'].insert(0,'Earned '+str(num)+ ' golds from the farm! ('+
                '{:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now())) #insert 0 will add at the end of the list
            request.session.save()    
            return redirect('/')

        elif request.POST['which_form'] == 'cave':
            num=random.randint(5,10)
            request.session['golds']+=num
            request.session['activities'].insert(0,'Earned '+str(num)+ ' golds from the cave! ('+
                '{:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now()))
            request.session.save()    
            return redirect('/') 
        elif request.POST['which_form'] == 'house':
            num=random.randint(2,5)
            request.session['golds']+=num
            request.session['activities'].insert(0,'Earned '+str(num)+ ' golds from the house! ('+
                '{:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now()))
            request.session.save()     
            return redirect('/') 
        elif request.POST['which_form'] == 'casino':
            num=random.randint(-50,50)
            if num < 0:
                request.session['golds']+=num # we added it because the number is already negative
                num*=-1
                request.session['activities'].insert(0,'Entered a casino and lost '+str(num)+ ' golds...Ouch. ('+
                '{:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now()))
                request.session.save()  
            elif num >0:    
                request.session['activities'].insert(0,'Earned '+str(num)+ ' golds from the casino! ('+
                    '{:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now()))
                request.session.save()  
                request.session['golds']+=num   
            return redirect('/')          

def destroy(request):
    request.session.clear()
    return redirect('/')            