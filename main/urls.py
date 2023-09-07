from django.urls import path
from main.views import char_desc

app_name = 'main'

urlpatterns = [
    path('', char_desc, name='char_desc'),
]