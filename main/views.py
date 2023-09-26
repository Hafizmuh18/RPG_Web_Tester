from django.shortcuts import render, redirect
from .models import Item
from django.http import HttpResponse
from .forms import InputAddItem, InputRemoveItem
from django.http import HttpResponseRedirect
from main.forms import ItemForm
from django.urls import reverse
from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Item
from django.shortcuts import get_object_or_404, redirect, render
from .models import Item

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:display_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def char_desc(request, id):
    try:
        if id.isdigit():
            item = Item.objects.get(pk=id)
        else :
            item = Item.objects.get(name=id)
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


@login_required(login_url='/login')
def display_main(request):
    if request.method == "POST":
        try:
            post_request = request.POST.get("action").split('-')
            item_id = int(post_request[1])
            action = post_request[0]
            item = get_object_or_404(Item, pk=item_id)
            

            if action == "increase":
                item.amount += 1
            elif action == "decrease" and item.amount > 0:
                item.amount -= 1

            item.save()

        # Render the same page with updated content
            cards = Item.objects.all()  # Retrieve all items (you can modify this query as needed)
            context = {
                    'cards': cards,
                    'project' : "RPG WEB TESTER",
                    'nama_pembuat' : request.user.username,
                    'kelas' : "PBP F",
                    'last_login': request.COOKIES['last_login'],
                }
            return redirect('main:display_main')
        except:
            return render(request, 'pagenotfound.html', status=404)
    else:
        try:
            items = Item.objects.all()
        except:
            return render(request, 'pagenotfound.html', status=404)
        
        context = {
            'cards': items,
            'project' : "RPG WEB TESTER",
            'nama_pembuat' : request.user.username,
            'kelas' : "PBP F",
            'last_login': request.COOKIES['last_login'],
        }

        return render(request, "main.html", context)

def add_item(request):
    if request.method == 'POST':
        adding = InputAddItem(request.POST)
        if adding.is_valid():
            Item.objects.create(
                user = request.user,
                name = adding.cleaned_data.get('name'),
                item_type = adding.cleaned_data.get('item_type'),
                amount = adding.cleaned_data.get('amount'),
                power = adding.cleaned_data.get('power'),
                price = adding.cleaned_data.get('price'),
                unique_skill = adding.cleaned_data.get('unique_skill'),
                description = adding.cleaned_data.get('description')
            )
            return redirect('main:display_main')
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
                return redirect('main:display_main')
            except Item.DoesNotExist:
                return HttpResponse("Item not Found", status=200)
            except Item.MultipleObjectsReturned:
                items = Item.objects.filter(name=nama_to_remove)
                for item in items:
                    item.delete()
                return redirect('main:display_main')
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
    if not data:
        return render(request, 'pagenotfound.html', status=404)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def view_json_id(request, id):
    data = Item.objects.filter(pk=id)
    if not data:
        return render(request, 'pagenotfound.html', status=404)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")