# Generated by Django 4.2.4 on 2023-09-15 06:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0043_booking_email_alter_booking_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='address',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='email',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='name',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='phone_number',
        ),
    ]
