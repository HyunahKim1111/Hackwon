# Generated by Django 3.1.7 on 2024-03-10 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academyadminprofile',
            name='academy_image',
            field=models.ImageField(default='academy_images/no_image.png', upload_to='media/academy_images/%Y/%m/%d'),
        ),
    ]
