# Generated by Django 4.0.4 on 2023-09-02 21:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_fooditem_alter_discount_to_item_alter_orderitem_item_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Discount',
        ),
    ]
