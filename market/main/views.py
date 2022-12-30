from django.shortcuts import render, redirect
from .models import Item
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def homepage(request):
    return render(request, template_name='main/home.html')


def itemspage(request):
    if request.method == 'GET':
        items = Item.objects.all()
        return render(request, template_name='main/items.html', context={'items': items})
    if request.method == 'POST':
        pass

def loginpage(request):
    if request.method == 'GET':
        return render(request, template_name='main/login.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('items')
        else:
            return redirect('login')


def logoutpage(request):
    logout(request)
    return redirect('home')


def registerpage(requesst):
    if requesst.method == 'GET':
        return render(requesst, 'main/register.html')
    if requesst.method == 'POST':
        form = UserCreationForm(requesst.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(requesst, user)
            return redirect('/')
        else:

            return redirect('register')