from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug':('name', )}

admin.site.register(Category, CategoryAdmin)

class HackwonAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category', 'course', 'tuition', 'dormitory_available', 'phone_number', 'latitude', 'longitude']
    list_filter = ['category', 'course', 'dormitory_available']
    prepopulated_fields = {'slug': ('name',)}
    # 필드셋을 사용하여 양식 필드의 순서나 구조를 더 세밀하게 조정할 수 있습니다. (옵션)
    fieldsets = (
        (None, {
            'fields': ('name', 'slug', 'category', 'image', 'description', 'meta_description', 'region', 'tuition', 'course')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('dormitory_available', 'phone_number', 'latitude', 'longitude'),
        }),
    )

admin.site.register(Hackwon, HackwonAdmin)
