# Generated by Django 4.0.4 on 2023-10-06 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0011_alter_discount_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fooditem',
            name='image',
            field=models.TextField(blank=True, null=True),
        ),
    ]