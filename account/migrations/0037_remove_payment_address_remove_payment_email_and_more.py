# Generated by Django 4.2.4 on 2023-09-14 04:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0036_booking_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='address',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='email',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='name',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='phone_number',
        ),
        migrations.AddField(
            model_name='booking',
            name='address',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='phone_number',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='booking',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='account.booking'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='booking',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('canceled', 'Canceled')], default='confirmed', max_length=20),
        ),
    ]
