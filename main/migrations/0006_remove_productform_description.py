# Generated by Django 5.1.1 on 2024-09-25 03:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_remove_product_mood_intensity_product_owner_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productform',
            name='description',
        ),
    ]
