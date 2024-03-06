from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='course_category')
    meta_description = models.TextField(blank=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True, allow_unicode=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('content:hackwon_in_category', args=[self.slug])

class Hackwon(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='hackwons')
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True, allow_unicode=True)
    image = models.ImageField(upload_to='hackwons/%Y/%m/%d', blank=True, null=True)
    region = models.TextField(blank=True, null=True)
    tuition = models.IntegerField(blank=True, null=True)
    course = models.CharField(max_length=200, db_index=True, null=True)
    dormitory_available = models.BooleanField(default=True)

    class Meta:
        index_together = [['id', 'slug']]

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('content:hackwon_detail', args=[self.id, self.slug])



