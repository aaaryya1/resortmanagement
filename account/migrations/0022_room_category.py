# Generated by Django 4.2.4 on 2023-09-02 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0021_person_roomcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='category',
            field=models.CharField(choices=[('suite', 'suite'), ('deluxe', 'deluxe'), ('club suite', 'club suite')], default=2, max_length=10),
            preserve_default=False,
        ),
    ]
