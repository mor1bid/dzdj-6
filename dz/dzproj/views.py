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
    print(me)
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
            if j == 1 and mydate[j] - ymd[j] >= 7:
                return render(request, 'filterweek.html', {'date': dlist[0], 'wlist': wlist[i]})
            elif ymd[j] < mydate[j]:
                if j == 0:
                    return render(request, 'filteryear.html', {'date': dlist[0], 'wlist': wlist[i]})
                else:
                    return render(request, 'filtermonth.html', {'date': dlist[0], 'wlist': wlist[i]})
        # return render(request, 'filter.html', {'ware': wlist, 'date': map(int, ymd), 'mydate': map(int, mydate)})



# Create your views here.
