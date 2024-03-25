from django.shortcuts import render, get_list_or_404
from django.urls import path
from datetime import datetime
from .models import *

def index(request):
    return render(request, 'index.html', {'title':'Index'})
def about(request):
    return render(request, 'about.html', {'title': 'About'})
def regdate_filter(request, myid):
    me = Client.objects.get(pk=myid)
    me = me.name
    mydate = str(datetime.now().date()).split('-')
    mydate = list(map(int, mydate))
    dates = Orders.objects.values_list('regdate', flat=True)
    wares = Orders.objects.values_list('wid', flat=True)
    for i in range(Orders.objects.count()):
        dlist = str(dates[i]).split()
        wlist = str(wares[i]).split()
        ymd = dlist[0].split('-')
        ymd = list(map(int, ymd))
        for j in range(len(ymd)):
            print(j)
            context = {'ware': wlist[i], 'date': ymd[j], 'mydate': mydate[j], 'n': j}
            if ymd[j] < mydate[j] or mydate[j] - ymd[j] >= 7:
                print(context)
                return render(request, 'filter.html', context)



# Create your views here.
