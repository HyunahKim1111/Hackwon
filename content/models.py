from django.db import models
from django.urls import reverse
import os
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name='course_category')
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('content:hackwon_in_category', args=[self.id])

class Hackwon(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='hackwons')
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)
    image = models.ImageField(upload_to='hackwons/%Y/%m/%d', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    region = models.CharField(max_length=200, db_index=True, null=True)
    tuition = models.CharField(max_length=200, db_index=True, null=True)
    course = models.CharField(max_length=200, db_index=True, null=True)
    dormitory_available = models.BooleanField(default=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True) 
    latitude = models.FloatField(null=True, blank=True)  # 위도
    longitude = models.FloatField(null=True, blank=True)  # 경도
    voter = models.ManyToManyField(User, related_name='voted_hackwons') # 좋아요기능

    class Meta:
        index_together = [['id', 'slug']]

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('content:hackwon_detail', args=[self.id])
    


    



