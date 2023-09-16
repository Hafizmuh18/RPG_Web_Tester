from django.shortcuts import render, redirect
from .models import Item
from django.http import HttpResponse
from .forms import InputAddItem, InputRemoveItem
from django.http import HttpResponseRedirect
from main.forms import ItemForm
from django.urls import reverse
from django.core import serializers

# Create your views here.
def char_desc(request, id):
    try:
        item = Item.objects.get(item_id=id)
    except:
        return render(request, 'pagenotfound.html', status=404)

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
        return render(request, 'pagenotfound.html', status=404)
    
    context = {
        'cards': items,
        'project' : "RPG WEB TESTER",
        'nama_pembuat' : "Muhammad Hafiz",
        'kelas' : "PBP F",
    }

    return render(request, "main.html", context)

def add_item(request):
    if request.method == 'POST':
        adding = InputAddItem(request.POST)
        if adding.is_valid():
            Item.objects.create(
                name = adding.cleaned_data.get('Name'),
                item_type = adding.cleaned_data.get('Item_Type'),
                amount = adding.cleaned_data.get('Amount'),
                power = adding.cleaned_data.get('Power'),
                price = adding.cleaned_data.get('Price'),
                unique_skill = adding.cleaned_data.get('Unique_Skill'),
                description = adding.cleaned_data.get('Description')
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

def remove_item(request):
    if request.method == 'POST':
        remove_form = InputRemoveItem(request.POST)
        if remove_form.is_valid():
            nama_to_remove = remove_form.cleaned_data.get('Nama')
            try:
                item = Item.objects.get(name=nama_to_remove)
                item.delete()
                return redirect('display_main')
            except Item.DoesNotExist:
                return HttpResponse("Item not Found", status=200)
        else:
            return HttpResponse("Invalid Form Data", status=400)

    context = {
        'remove_form': InputRemoveItem()
    }
    return render(request, 'removeitem.html', context)

def view_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
    
def view_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def view_xml_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def view_json_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")