from django.urls import path
from .views import *

app_name = 'cs'

urlpatterns = [
    path('', question_list, name='question_list'),
    path('<int:question_id>/', question_detail, name='question_detail'),
    path('question/answer/create/<int:question_id>/', answer_create, name='answer_create'),
    path('answer/delete/<int:answer_id>/', answer_delete, name='answer_delete'),
    path('question/create/', question_create, name='question_create'),
    path('question/<int:question_id>/update/', question_update, name='question_update'),
    path('question/<int:question_id>/delete/', question_delete, name='question_delete'),
]
