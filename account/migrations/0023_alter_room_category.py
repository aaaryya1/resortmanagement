# Generated by Django 4.2.4 on 2023-09-04 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0022_room_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='category',
            field=models.CharField(choices=[('suite', 'suite'), ('deluxe', 'deluxe'), ('club suite', 'club suite'), ('Presidential Suite', 'Presidential Suite')], default='deluxe', max_length=20),
        ),
    ]