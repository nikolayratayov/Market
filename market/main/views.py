from django.shortcuts import render, redirect
from .models import Item
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


# Create your views here.


def homepage(request):
    return render(request, template_name='main/home.html')


def itemspage(request):
    if request.method == 'GET':
        items = Item.objects.filter(owner=None)
        return render(request, template_name='main/items.html', context={'items': items})
    if request.method == 'POST':
        if not request.user.is_authenticated:
            messages.error(request, f'You have to login to buy items!')
            return redirect('login')
        purchased_item = request.POST.get('purchased-item')
        if purchased_item:
            purchased_item_object = Item.objects.get(name=purchased_item)
            purchased_item_object.owner = request.user
            purchased_item_object.save()
            messages.success(request,
                             f'Congratulations. You just bought {purchased_item_object.name} for {purchased_item_object.price}')
        return redirect('items')


def myitemspage(request):
    if request.method == 'GET':
        if not request.user.is_authenticated:
            messages.error(request, f'You have to login to check your items!')
            return redirect('login')
        my_items = Item.objects.filter(owner=request.user)
        return render(request, template_name='main/my_items.html', context={'my_items': my_items})
    if request.method == 'POST':
        sold_item = request.POST.get('sold-item')
        if sold_item:
            sold_item_object = Item.objects.get(name=sold_item)
            sold_item_object.owner = None
            sold_item_object.save()
            messages.success(request, f'Congratulations. You just sold {sold_item} for {sold_item_object.price}')
        return redirect('my_items')


def loginpage(request):
    if request.method == 'GET':
        return render(request, template_name='main/login.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.info(request, f'You are logged in as {user.username}')
            return redirect('items')
        else:
            messages.error(request, 'The combination of username and password is wrong!')
            return redirect('login')


def logoutpage(request):
    logout(request)
    messages.info(request, f'You have been logged out!')
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
            messages.success(requesst, f'You have registered your account successfully! Logged in as {user.username}')
            return redirect('/')
        else:
            messages.error(requesst, form.errors)
            return redirect('register')
