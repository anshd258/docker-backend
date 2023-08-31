# Generated by Django 4.0.4 on 2023-08-27 07:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('service', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('earnings', models.DecimalField(decimal_places=2, default=0.0, max_digits=8)),
                ('rating', models.DecimalField(decimal_places=2, default=0.0, max_digits=8)),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'Available'), (2, 'Assigned'), (3, 'On The Way')], default=1)),
                ('deliveries_today', models.IntegerField(default=0)),
                ('total_deliveries', models.IntegerField(default=0)),
                ('commission_today', models.DecimalField(decimal_places=2, default=0.0, max_digits=8, null=True)),
                ('total_commission', models.DecimalField(decimal_places=2, default=0.0, max_digits=8, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('service_areas', models.ManyToManyField(to='service.location')),
                ('user_info', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.userinfo')),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commission', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('unique_link', models.CharField(max_length=100, null=True, unique=True)),
                ('otp', models.IntegerField(null=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gig_jobs', to='service.order')),
                ('worker', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='jobs', to='gig.worker')),
            ],
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_type', models.PositiveSmallIntegerField(choices=[(1, 'Food Delivery'), (2, 'Transport')], default=1)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateTimeField(auto_now=True)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gig.job')),
            ],
            options={
                'verbose_name_plural': 'Deliveries',
            },
        ),
        migrations.CreateModel(
            name='Commission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_type', models.PositiveSmallIntegerField(choices=[(1, 'Food Delivery'), (2, 'Transport')], default=1)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateTimeField(auto_now=True)),
                ('jobref', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commissions', to='gig.job')),
            ],
        ),
    ]
