from django.shortcuts import render
from .models import *


def question_list(request):
    question_list = Question.objects.all()
    return render(request, 'cs/question_list.html', {'question_list':question_list})

def question_detail(request, question_id):
    question_detail = Question.objects.get(id=question_id)
    return render(request, 'cs/question_detail.html', {'question_detail':question_detail})
