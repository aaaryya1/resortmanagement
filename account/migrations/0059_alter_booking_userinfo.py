# Generated by Django 4.2.4 on 2023-09-16 06:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0058_alter_booking_userinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='userinfo',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='account.userinfo'),
        ),
    ]
