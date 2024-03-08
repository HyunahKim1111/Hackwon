from django.urls import path
from .views import *

app_name = 'content'

urlpatterns = [
    path('', hackwon_in_category, name='hackwon_all'),
    path('detail/<int:pk>/', hackwon_detail, name='hackwon_detail'),
    path('category/<int:category_id>/', hackwon_in_category, name='hackwon_in_category'),
    path('vote/<int:hackwon_id>/', hackwon_vote, name='hackwon_vote'),
]
