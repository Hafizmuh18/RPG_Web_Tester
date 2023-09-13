from django.db import models
import uuid
# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=100)
    item_id = models.IntegerField(editable=False, unique=True)
    item_type = models.CharField(max_length=100, null=True, blank=True)
    amount = models.IntegerField(default=1)
    power = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    unique_skill = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.item_id:
            self.item_id = Item.objects.count() + 1
        super(Item, self).save(*args, **kwargs)