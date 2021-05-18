from django.shortcuts import render
from time import gmtime, strftime
from datetime import date
from datetime import datetime
import time
import pytz
# Create your views here.
    
def index(request):
    context = {
        #**************the first way to git the time and date**********************************
        #  "ww": strftime("%Y-%m-%d %H:%M %p", gmtime()), #this will display it as 2021-05-17 11:59 AM

        #**************the second way to git the time and date**********************************
         "date": strftime("%b %d, %Y", gmtime()),
         "time": time.strftime("%H:%M %p",time.localtime())

        #**************the third way to git the time and date**********************************

            # "date":datetime.date(datetime.today()),
            # "time":datetime.time(datetime.today())

         #**************************************************************************************    

    }
    return render(request,'index.html', context)
