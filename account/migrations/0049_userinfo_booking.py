# Generated by Django 4.2.4 on 2023-09-15 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0048_remove_userinfo_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='booking',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.booking'),
        ),
    ]