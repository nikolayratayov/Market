from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Item(models.Model):
    owner = models.ForeignKey(User, default=None, blank=True, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255, default='')
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=1024, default='')
    image_url = models.CharField(max_length=512, default='')

    def __str__(self):
        return self.name
