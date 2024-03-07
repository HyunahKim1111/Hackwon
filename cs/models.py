from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='questions') 
    photo = models.ImageField(upload_to='cs_photo/%Y/%m/%d', null=True, blank=True)
    subject = models.CharField(max_length=200)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated']  

    def __str__(self):
        author_name = self.author.username if self.author else 'Unknown Author'
        created_time = self.created.strftime('%Y-%m-%d %H:%M:%S')
        return f"{author_name} - {self.subject} ({created_time})"


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='admin_answers')  # 관리자에 의한 답변
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Answer to '{self.question.subject[:50]}' by {self.author.username} on {self.created.strftime('%Y-%m-%d %H:%M')}"