from django import forms
from django.forms import ModelForm
from .models import Item

class InputAddItem(forms.Form):
    Name = forms.CharField(required=True, max_length=100)
    Item_Type = forms.CharField(required=False, max_length=100)
    Amount = forms.IntegerField(required=True)
    Power = forms.IntegerField(required=True)
    Price = forms.IntegerField(required=True)
    Unique_Skill = forms.CharField(required=False)
    Description = forms.CharField(required=False)

class InputRemoveItem(forms.Form):
    Nama = forms.CharField(required=True, max_length=100)

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ["name", "item_type", "amount", "power", "price", "unique_skill", "description"]