from django import forms
from django.forms import ModelForm
from .models import Item

class InputAddItem(forms.ModelForm):
    class Meta:
        model = Item  # Specify the model to be used with this form
        fields =  ["name", "item_type", "amount", "power", "price", "unique_skill", "description"]

class InputRemoveItem(forms.Form):
    Nama = forms.CharField(required=True, max_length=100)

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ["name", "item_type", "amount", "power", "price", "unique_skill", "description"]

class IncreaseAmountForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['amount']

    def clean_amount(self):
        return self.cleaned_data['amount'] + 1

class DecreaseAmountForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['amount']

    def clean_amount(self):
        return max(self.cleaned_data['amount'] - 1, 0)
