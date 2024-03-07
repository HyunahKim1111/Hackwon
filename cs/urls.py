from django.urls import path
from .views import *

app_name = 'cs'

urlpatterns = [
    path('', question_list, name='question_list'),
    path('<int:question_id>/', question_detail, name='question_detail'),
]