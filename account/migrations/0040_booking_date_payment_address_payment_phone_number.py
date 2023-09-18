# Generated by Django 4.2.4 on 2023-09-14 13:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0039_remove_booking_address_remove_booking_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='payment',
            name='address',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='phone_number',
            field=models.IntegerField(null=True),
        ),
    ]
