# Generated by Django 3.1.7 on 2024-03-08 06:10

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_auto_20240306_2121'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='likes',
            field=models.ManyToManyField(related_name='blog_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
