# Generated by Django 4.0.4 on 2023-08-31 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_userinfo_otp'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='username',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
