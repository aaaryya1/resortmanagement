# Generated by Django 4.2.4 on 2023-09-01 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0013_room_room_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='room_name',
            new_name='r_name',
        ),
    ]
