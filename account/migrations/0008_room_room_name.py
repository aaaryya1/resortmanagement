# Generated by Django 4.2.4 on 2023-09-01 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_remove_reservation_is_checked_in_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='room_name',
            field=models.CharField(default=None, max_length=200),
        ),
    ]
