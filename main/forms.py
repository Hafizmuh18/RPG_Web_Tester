from django import forms

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