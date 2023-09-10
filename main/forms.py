from django import forms

class InputAddItem(forms.Form):
    inp_name = forms.CharField(required=True, max_length=100)
    inp_item_type = forms.CharField(required=False, max_length=100)
    inp_amount = forms.IntegerField(required=True)
    inp_power = forms.IntegerField(required=True)
    inp_price = forms.IntegerField(required=True)
    inp_unique_skill = forms.CharField(required=False)
    inp_description = forms.CharField(required=False)