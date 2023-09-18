# Generated by Django 4.2.4 on 2023-09-09 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0027_remove_room_room_name_room_room_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='check_in',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='booking',
            name='check_out',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='room',
            name='room_number',
            field=models.IntegerField(default=1001),
        ),
    ]