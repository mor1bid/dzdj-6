from django.shortcuts import render, get_list_or_404
from django.urls import path
from .models import Orders

def index(request):
    return render(request, 'index.html', {'title':'Index'})
def about(request):
    return render(request, 'about.html', {'title': 'About'})
def regdate_filter(request):

    for i in range(Orders.objects.count()):
        # obj = Orders.objects.get(pk=i)
        date = get_list_or_404(Orders, regdate=i)
        ware = get_list_or_404(Orders, wid=i)
        dates = Orders.objects.filter(regdate=date)
        return render(request, 'filter.html', {'ware': ware, 'regdates': dates})


# Create your views here.
