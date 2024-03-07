from django import forms
from .models import *


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['subject', 'content']
        widgets = {
            'subject': forms.TextInput(attrs={'placeholder': '제목을 입력하세요.', 'class': 'form-control'}),
            'content': forms.Textarea(attrs={'placeholder': '내용을 입력하세요.', 'class': 'form-control', 'rows': 5}),
        }

        labels = {
            'subject': '제목',
            'content': '내용',
        }  

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'placeholder': '내용을 입력하세요.', 'class': 'form-control', 'rows': 5}),
        }
        labels = {
            'content': '답변내용',
        }

        