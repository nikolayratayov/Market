from django.shortcuts import render
from .models import Item
# Create your views here.


def homepage(request):
    return render(request, template_name='main/home.html')


def itemspage(request):
    items = Item.objects.all()
    return render(request, template_name='main/items.html', context={'items': items})


def loginpage(request):
    return render(request, template_name='main/login.html')


def logoutpage(request):
    pass


def registerpage(requesst):
    return render(requesst, 'main/register.html')