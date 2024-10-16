# Generated by Django 5.1.2 on 2024-10-16 07:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_store', '0004_car_city_en_car_city_ky_car_city_ru_car_city_tr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='add_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Время'),
        ),
        migrations.AlterField(
            model_name='car',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='models', to='car_store.model'),
        ),
    ]