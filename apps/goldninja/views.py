from django.shortcuts import render, redirect, HttpResponse
from datetime import datetime
from random import random, randint


# Create your views here.
def index(request):
    return render(request,'goldninja/index.html')

def process(request):
    point=0
    time=datetime.now().strftime('%Y/%m/%d %H:%M:%S')
    itype=(request.POST['building'])
    
    if 'total' and 'earned' and 'lost' not in request.session:
            request.session['total']=0
            request.session['earned']=[]
            request.session['lost']=[]
      
    if request.method == "POST":
        if(itype =='farm'):
            point=randint(10,20)
            request.session['total']= request.session['total'] + point
            message="Earned {} golds golds from the {}! - {}".format(point,itype,time)
            request.session['earned'].append(message)
        elif(itype == 'cave'):
            point=randint(5,10)
            request.session['total']= request.session['total'] + point
            message="Earned {} golds golds from the {}! - {}".format(point,itype,time)
            request.session['earned'].append(message)
        elif(itype == 'house'):
            point=randint(2,5)
            request.session['total']= request.session['total'] + point
            message="Earned {} golds golds from the {}! - {}".format(point,itype,time)
            request.session['earned'].append(message)
        else:
            point=randint(0,50)
            earn_or_take=randint(0,1)
            if(earn_or_take == 0): #takes
                request.session['total']= request.session['total'] - point
                message="Entered {} and lost {} golds - {}".format(itype,point,time)
                request.session['lost'].append(message)
            else: #earn
                request.session['total']= request.session['total'] + point
                message="Entered {} and earned {} golds {}".format(itype,point,time) 
                request.session['earned'].append(message)
    return redirect('/')

def clear(request):
    if request.method == "POST":
        request.session.clear()
    return redirect('/')