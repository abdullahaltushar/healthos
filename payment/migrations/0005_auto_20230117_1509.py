# Generated by Django 3.2.15 on 2023-01-17 09:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0004_auto_20230117_1508'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='payment_ammount',
            field=models.CharField(default=1, max_length=12),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='payment',
            name='expire_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 16, 15, 9, 47, 73613)),
        ),
        migrations.AlterField(
            model_name='payment',
            name='expire_year',
            field=models.DateField(default=datetime.datetime(2024, 1, 17, 15, 9, 47, 73613)),
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment',
            field=models.DateField(default=datetime.datetime(2023, 1, 17, 15, 9, 47, 73613)),
        ),
    ]
