# Generated by Django 5.1.2 on 2024-10-16 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_store', '0003_car_car_name_en_car_car_name_ky_car_car_name_ru_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='city_en',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='city_ky',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='city_ru',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='city_tr',
            field=models.CharField(max_length=32, null=True),
        ),
    ]
