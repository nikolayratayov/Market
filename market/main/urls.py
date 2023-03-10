from django.urls import path, include
from .views import *


urlpatterns = [
    path('home/', homepage, name='home'),
    path('', homepage, name='home'),
    path('items/', itemspage, name='items'),
    path('login/', loginpage, name='login'),
    path('logout/', logoutpage, name='logout'),
    path('register/', registerpage, name='register'),
    path('my_items/', myitemspage, name='my_items'),
    path('accounts/', include('allauth.urls')),
]