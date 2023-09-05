# Generated by Django 4.0.4 on 2023-08-27 07:55

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('description', models.TextField()),
                ('location_address', models.TextField()),
                ('photo', models.TextField()),
                ('cabin_type', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('description', models.TextField()),
                ('amount', models.BigIntegerField()),
                ('duration', models.FloatField()),
                ('discount', models.IntegerField()),
                ('cabin_type', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('price', models.IntegerField()),
                ('property_address', models.TextField()),
                ('photo', models.TextField()),
                ('property_type', models.TextField()),
                ('rooms', models.IntegerField()),
                ('overallrating', models.PositiveSmallIntegerField(choices=[(1, 'One'), (2, 'Two'), (3, 'Three'), (4, 'Four'), (5, 'Five')], default=5)),
                ('description', models.TextField()),
                ('transportation_cost', models.IntegerField()),
                ('meal_cost', models.IntegerField()),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='property', to='cabin.location')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('adults', models.IntegerField()),
                ('children', models.IntegerField()),
                ('checkin', models.DateTimeField()),
                ('checkout', models.DateTimeField()),
                ('rooms', models.IntegerField()),
                ('mobile', models.CharField(max_length=10, null=True)),
                ('whatsapp', models.CharField(max_length=10, null=True)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservation', to='cabin.property')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_name', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PropertyReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField()),
                ('rating', models.PositiveSmallIntegerField(choices=[(1, 'One'), (2, 'Two'), (3, 'Three'), (4, 'Four'), (5, 'Five')], default=5)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='propertyReview', to='cabin.property')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='propertyReview', to='user.userinfo')),
            ],
        ),
        migrations.CreateModel(
            name='PropertyMetaData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.TextField()),
                ('Value', models.TextField()),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='propertyMetaData', to='cabin.property')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_ref_id', models.CharField(max_length=200)),
                ('status', models.BooleanField(default=False)),
                ('amount', models.IntegerField()),
                ('create_time', models.DateTimeField(default=datetime.datetime(2023, 8, 27, 7, 55, 38, 552793))),
                ('update_time', models.DateTimeField(default=datetime.datetime(2023, 8, 27, 7, 55, 38, 552806))),
                ('reservation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservation', to='cabin.reservation')),
            ],
        ),
        migrations.CreateModel(
            name='LocationMetaData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('overallrating', models.PositiveSmallIntegerField(choices=[(1, 'One'), (2, 'Two'), (3, 'Three'), (4, 'Four'), (5, 'Five')], default=5)),
                ('weather', models.TextField()),
                ('airquality', models.TextField()),
                ('internet', models.TextField()),
                ('accessibility', models.PositiveSmallIntegerField(choices=[(1, 'One'), (2, 'Two'), (3, 'Three'), (4, 'Four'), (5, 'Five')], default=5)),
                ('safety', models.PositiveSmallIntegerField(choices=[(1, 'One'), (2, 'Two'), (3, 'Three'), (4, 'Four'), (5, 'Five')], default=5)),
                ('health', models.PositiveSmallIntegerField(choices=[(1, 'One'), (2, 'Two'), (3, 'Three'), (4, 'Four'), (5, 'Five')], default=5)),
                ('timezone', models.TextField()),
                ('language', models.TextField()),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='location', to='cabin.location')),
            ],
        ),
    ]