# Generated by Django 4.0.4 on 2023-09-27 20:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cabin', '0002_alter_paymentstatus_create_time_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_type', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('available', models.IntegerField()),
                ('_property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cabin.property')),
            ],
        ),
    ]
