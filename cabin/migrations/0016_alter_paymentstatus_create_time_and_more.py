# Generated by Django 4.0.4 on 2023-09-05 17:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cabin', '0015_alter_paymentstatus_create_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentstatus',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 5, 17, 56, 54, 893431)),
        ),
        migrations.AlterField(
            model_name='paymentstatus',
            name='update_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 5, 17, 56, 54, 893453)),
        ),
    ]
