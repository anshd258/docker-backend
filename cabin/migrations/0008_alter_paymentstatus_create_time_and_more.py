# Generated by Django 4.0.4 on 2023-08-31 15:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cabin', '0007_alter_paymentstatus_create_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentstatus',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 31, 15, 5, 36, 132006)),
        ),
        migrations.AlterField(
            model_name='paymentstatus',
            name='update_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 31, 15, 5, 36, 132053)),
        ),
    ]