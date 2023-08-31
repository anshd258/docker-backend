# Generated by Django 4.0.4 on 2023-08-27 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PackageItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package_item', models.CharField(max_length=300)),
                ('priority', models.IntegerField()),
                ('max_guests', models.IntegerField()),
                ('cost_price', models.IntegerField()),
                ('duration', models.FloatField()),
                ('min_buffer_percent', models.FloatField()),
                ('margin_percent', models.FloatField()),
                ('sales_price', models.FloatField()),
                ('comments', models.TextField(blank=True)),
            ],
        ),
    ]
