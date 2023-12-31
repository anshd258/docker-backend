# Generated by Django 4.0.4 on 2023-08-27 07:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.TextField(blank=True, max_length=255, null=True)),
                ('price', models.FloatField(default=0)),
                ('category', models.CharField(blank=True, max_length=255, null=True)),
                ('type', models.CharField(blank=True, max_length=255, null=True)),
                ('options', models.JSONField(blank=True, null=True)),
                ('veg', models.BooleanField(default=False)),
                ('available', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(max_length=255)),
                ('address', models.TextField(max_length=255)),
                ('max_persons', models.IntegerField(default=0)),
                ('location_type', models.TextField()),
                ('base_surge', models.FloatField(default=1.0)),
                ('surge', models.FloatField(default=1.0)),
                ('occupancy', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount', models.FloatField(default=0.0)),
                ('subtotal', models.FloatField(default=0)),
                ('taxes', models.FloatField(default=0)),
                ('charges', models.FloatField(default=0)),
                ('comments', models.TextField(blank=True, max_length=255, null=True)),
                ('total', models.FloatField(default=0.0)),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'Hold'), (2, 'Processing'), (3, 'Confirmed'), (4, 'Ready'), (5, 'Delivered'), (6, 'Completed'), (0, 'Failed')], default=1)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('rating', models.FloatField(blank=True, null=True)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.location')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(max_length=100)),
                ('provider_name', models.CharField(max_length=100)),
                ('max_serving_capacity', models.IntegerField()),
                ('opening_time', models.TimeField()),
                ('closing_time', models.TimeField()),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='location', to='service.location')),
            ],
            options={
                'unique_together': {('business_name', 'provider_name')},
            },
        ),
        migrations.CreateModel(
            name='ServiceArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.location')),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.provider')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.JSONField(blank=True, null=True)),
                ('listed_price', models.FloatField()),
                ('total', models.FloatField()),
                ('discount', models.FloatField(default=0)),
                ('rating', models.FloatField(default=0)),
                ('quantity', models.IntegerField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='service.item')),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='service.order')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='provider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='provider', to='service.provider'),
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100)),
                ('percent', models.FloatField(default=0)),
                ('upto', models.FloatField(default=0)),
                ('min_price', models.FloatField(default=0)),
                ('linked_to', models.PositiveSmallIntegerField(choices=[(1, 'Location'), (2, 'Item'), (3, 'Provider')], default=2)),
                ('to_item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='service.item')),
                ('to_location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='service.location')),
                ('to_provider', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='service.provider')),
            ],
        ),
    ]
