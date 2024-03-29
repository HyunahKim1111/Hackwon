from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Blog(models.Model):
    author = models.ForeignKey(User,on_delete=models.SET_NULL, null=True, related_name='user_blogs')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', default='photos/no_image.png')
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)

    class Meta:
        ordering = ['-updated']

    def __str__(self):
        return self.author.username + " " + self.created.strftime("%Y-%m-%d %H:%M:%S")

    def get_absolute_url(self):
        return reverse('blog:blog_detail', args=[self.id])

    def total_likes(self):
        return self.likes.count()
    
    
