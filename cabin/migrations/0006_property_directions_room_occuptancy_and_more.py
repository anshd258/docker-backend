# Generated by Django 4.0.4 on 2023-10-14 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cabin', '0005_room_bed_type_room_images_room_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='directions',
            field=models.TextField(default='upar sidha left'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='room',
            name='occuptancy',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='property',
            name='description',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Family'), (2, 'Adventure'), (3, 'Lavish')], default=1),
        ),
    ]
