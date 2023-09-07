from django.db import models

# Create your models here.
class Item(models.Model):
    char_name = models.CharField(max_length=100, default="Kernel")
    name = models.CharField(max_length=100)
    item_id = models.IntegerField(default=0)
    power = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    unique_skill = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)