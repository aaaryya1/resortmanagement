# Generated by Django 4.2.4 on 2023-09-15 04:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0040_booking_date_payment_address_payment_phone_number'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Payment',
        ),
    ]