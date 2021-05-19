from django.shortcuts import redirect, render
import random
import datetime
# Create your views here.
def ninja(request):
    return render(request, 'index.html')

def process_money(request):
    if request.method == "POST":
        if 'golds' not in request.session:
            request.session['golds'] =0 # the golds initially are 0
        if 'activities' not in request.session: 
            request.session['activities'] =[]
        if request.POST['which_form'] == 'farm':
            num=random.randint(10,20)
            request.session['golds']+=num
            request.session['activities'].append('Earned '+str(num)+ ' golds from the farm! ('+
                '{:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now()))
            request.session.save()    
            return redirect('/')

        elif request.POST['which_form'] == 'cave':
            num=random.randint(5,10)
            request.session['golds']+=num
            request.session['activities'].append('Earned '+str(num)+ ' golds from the cave! ('+
                '{:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now()))
            request.session.save()    
            return redirect('/') 
        elif request.POST['which_form'] == 'house':
            num=random.randint(2,5)
            request.session['golds']+=num
            request.session['activities'].append('Earned '+str(num)+ ' golds from the house! ('+
                '{:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now()))
            request.session.save()    
            return redirect('/') 
        elif request.POST['which_form'] == 'casino':
            num=random.randint(-50,50)
            request.session['golds']+=num
            if num < 0:
                num*=-1
                request.session['activities'].append('Entered a casino and lost '+str(num)+ ' golds...Ouch. ('+
                '{:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now()))
                request.session.save()  
            elif num >0:    
                request.session['activities'].append('Earned '+str(num)+ ' golds from the casino! ('+
                    '{:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now()))
                request.session.save()    
            return redirect('/')          

def destroy(request):
    request.session.clear()
    return redirect('/')            