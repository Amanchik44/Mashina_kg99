# Generated by Django 5.1.2 on 2024-10-19 04:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car_store', '0003_rename_movie_favoritecar_car'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='parent_review',
        ),
    ]
