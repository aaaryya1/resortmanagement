# Generated by Django 4.2.4 on 2023-09-09 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0031_alter_room_room_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=200)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
    ]