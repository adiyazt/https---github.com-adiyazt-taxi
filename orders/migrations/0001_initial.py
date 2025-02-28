# Generated by Django 5.0.1 on 2024-01-31 13:33

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryOrder',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.CharField(max_length=120, verbose_name='Клиент')),
                ('recipient', models.CharField(max_length=120, verbose_name='Получатель')),
                ('courier', models.CharField(max_length=120, verbose_name='Курьер')),
                ('number', models.CharField(max_length=12, unique=True, verbose_name='Номер')),
                ('distance', models.FloatField(verbose_name='Расстояние')),
                ('price', models.FloatField(verbose_name='Цена')),
                ('rating', models.FloatField(blank=True, default=5.0, verbose_name='Рейтинг')),
            ],
            options={
                'verbose_name': 'Заказ доставки',
                'verbose_name_plural': 'Заказы доставки',
                'ordering': ['-price'],
            },
        ),
        migrations.CreateModel(
            name='TaxiOrder',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.CharField(max_length=120, verbose_name='Клиент')),
                ('taxist', models.CharField(max_length=120, verbose_name='Таксист')),
                ('number', models.CharField(max_length=12, unique=True, verbose_name='Номер')),
                ('distance', models.FloatField(verbose_name='Расстояние')),
                ('price', models.FloatField(verbose_name='Цена')),
                ('rating', models.FloatField(blank=True, default=5.0, verbose_name='Рейтинг')),
            ],
            options={
                'verbose_name': 'Заказ такси',
                'verbose_name_plural': 'Заказы такси',
                'ordering': ['-price'],
            },
        ),
    ]
