from django.urls import path
from main.views import char_desc, display_main, add_item

app_name = ''

urlpatterns = [
    path('<str:id>', char_desc, name='char_desc'),
    path('', display_main, name="display_main"),
    path('add_item/', add_item, name="add_item")
]