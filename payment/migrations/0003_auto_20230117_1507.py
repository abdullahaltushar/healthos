# Generated by Django 3.2.15 on 2023-01-17 09:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_auto_20230117_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='expire_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 16, 15, 7, 21, 384031)),
        ),
        migrations.AlterField(
            model_name='payment',
            name='expire_year',
            field=models.DateField(default=datetime.datetime(2024, 1, 17, 15, 7, 21, 384031)),
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment',
            field=models.DateField(default=datetime.datetime(2023, 1, 17, 15, 7, 21, 384031)),
        ),
    ]
