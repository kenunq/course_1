# Generated by Django 3.2.13 on 2023-04-08 18:04

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0002_bsket'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Bsket',
            new_name='Basket',
        ),
    ]
