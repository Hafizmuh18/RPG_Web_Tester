from django.db import models
import uuid
from django.contrib.auth.models import User
# Create your models here.

class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    item_type = models.CharField(max_length=100, null=True, blank=True)
    amount = models.IntegerField(default=1)
    power = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    unique_skill = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)