from django.urls import path
from .views import *

app_name = 'content'

urlpatterns = [
    path('', content, name='content')
]