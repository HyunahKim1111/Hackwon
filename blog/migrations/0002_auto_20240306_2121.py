# Generated by Django 3.1.7 on 2024-03-06 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-updated']},
        ),
    ]
