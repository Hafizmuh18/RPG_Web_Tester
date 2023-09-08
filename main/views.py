from django.shortcuts import render
from .models import Item
from django.http import HttpResponse

# Create your views here.
def char_desc(request, id):
    try:
        item = Item.objects.get(item_id=id)
    except:
        return HttpResponse("not found", status=404)

    # context = {
    #     'name' : 'Death Sytche',
    #     'item_id' : '101',
    #     'item_type' : 'Weapon (Sword)',
    #     'amount' : '1',
    #     'power' : '250',
    #     'price' : '100000000000000',
    #     'unique_skill' : 'The more enemy killed by this weapon, its power increase',
    #     'description' : 'The sycthe of a Grim Reaper that has an ability of Soul Eater, it said that the weapon killed its own owner if it think that the user is not strong enough'
    # }

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
        for item in items:
            print(item.item_id)
    except:
        return HttpResponse('not found', status=404)
    
    context = {
        'cards': items,
        'list': [1,2,3]
    }

    return render(request, "main.html", context)
    
