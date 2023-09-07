from django.shortcuts import render

# Create your views here.
def char_desc(request):
    context = {
        'name' : 'Death Sytche',
        'item_id' : '101',
        'item_type' : 'Weapon (Sword)',
        'amount' : '1',
        'power' : '250',
        'price' : '100000000000000',
        'unique_skill' : 'The more enemy killed by this weapon, its power increase',
        'description' : 'The sycthe of a Grim Reaper that has an ability of Soul Eater, it said that the weapon killed its own owner if it think that the user is not strong enough'
    }

    return render(request, "main.html", context)