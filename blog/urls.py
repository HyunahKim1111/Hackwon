from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('', blog_list, name='blog_list'),
]