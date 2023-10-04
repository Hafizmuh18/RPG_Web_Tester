from django.urls import path
from .views import test_page, logout_user ,login_user, register, view_json_id, view_xml_id, view_json, view_xml, char_desc, display_main, add_item, remove_item
from django.http import HttpResponse
from django.core import serializers

app_name = 'main'

urlpatterns = [
    path('', display_main, name="display_main"),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('add_item/', add_item, name="add_item"),
    path('remove_item/', remove_item, name="remove_item"),
    path('xml/', view_xml, name='view_xml'),
    path('json/', view_json, name='view_json'),
    path('xml/<int:id>/', view_xml_id, name='view_xml_id'),
    path('json/<int:id>/', view_json_id, name='view_json_id'), 
    path('<str:id>/', char_desc, name='char_desc'),
    path('/test/', test_page, name='test_page'),
]