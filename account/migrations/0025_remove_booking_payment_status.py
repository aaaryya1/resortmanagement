# Generated by Django 4.2.4 on 2023-09-05 08:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0024_delete_roomcategory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='payment_status',
        ),
    ]
