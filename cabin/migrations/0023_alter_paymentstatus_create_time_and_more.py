# Generated by Django 4.0.4 on 2023-09-10 16:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cabin', '0022_alter_paymentstatus_create_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentstatus',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 10, 16, 34, 49, 68732)),
        ),
        migrations.AlterField(
            model_name='paymentstatus',
            name='update_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 10, 16, 34, 49, 68745)),
        ),
    ]