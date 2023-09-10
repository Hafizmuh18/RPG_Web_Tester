from pickle import NONE
from django.shortcuts import render, redirect
from .models import Item
from django.http import HttpResponse
from .forms import InputAddItem

# Create your views here.
def char_desc(request, id):
    try:
        item = Item.objects.get(item_id=id)
    except:
        return HttpResponse("not found", status=404)

    context = {
        'name': item.name,
        'item_type' : item.item_type,
        'amount' : item.amount,
        'power' : item.power,
        'price' : item.price,
        'unique_skill' : item.unique_skill,
        'description' : item.description
    }

    return render(request, "detail.html", context)

def display_main(request):
    try:
        items = Item.objects.all()
    except:
        return HttpResponse('not found', status=404)
    
    context = {
        'cards': items,
    }

    return render(request, "main.html", context)

def add_item(request):
    if request.method == 'POST':
        adding = InputAddItem(request.POST)
        if adding.is_valid():
            new_item = Item.objects.create(
                name = adding.cleaned_data.get('inp_name'),
                item_type = adding.cleaned_data.get('inp_item_type'),
                amount = adding.cleaned_data.get('inp_amount'),
                power = adding.cleaned_data.get('inp_power'),
                price = adding.cleaned_data.get('inp_price'),
                unique_skill = adding.cleaned_data.get('inp_unique_skill'),
                description = adding.cleaned_data.get('inp_description')
            )
            return redirect('display_main')
        context = {
            'item_form' : adding
        }
        return render(request, 'additem.html', context)
    # else:
    #     adding = InputAddItem()
    context={
        'item_form' : InputAddItem
    }
    return render(request, 'additem.html', context)
    
