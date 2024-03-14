from django.shortcuts import render
from django.urls import path

def index(request):
    return render(request, 'index.html', {'title':'Главная страница'})
def about(request):
    return render(request)


# Create your views here.
