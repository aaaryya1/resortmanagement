# Generated by Django 4.2.4 on 2023-09-15 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0054_rename_booking_userinfo_booking'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='booking',
        ),
    ]
