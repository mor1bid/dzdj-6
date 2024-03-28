from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from datetime import datetime
from .models import *
from .forms import *

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
            context = {'ware': wlist[i], 'date': ymd[j], 'mydate': mydate[j], 'n': j}
            if ymd[j] < mydate[j] or mydate[j] - ymd[j] >= 7:
                print(context)
                return render(request, 'filter.html', context)
def add_wim(request):
    if request.method == 'POST':
        form = WareForm(request.POST, request.FILES)
        waresize = Ware.objects.count()
        if form.is_valid():
            myid = form.cleaned_data['wid']
            image = form.cleaned_data['image']
            for i in range(1, waresize):
                wares = Ware.objects.get(pk=i)
                wid = wares.pk
                if myid == wid:
                    fs = FileSystemStorage()
                    fs.save(image.name, image)
                    wares.image = str(request.FILES['image'])
                    wares.save()
                    print('Готово')
                elif i == waresize or myid > waresize:
                    print('Ошибка')
    else:
        form = WareForm()
    return render(request, 'addwim.html', {'form': form })



# Create your views here.
