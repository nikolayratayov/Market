from django.urls import path
from .views import *


urlpatterns = [
    path('home/', homepage, name='home'),
    path('items/', itemspage, name='items'),
]