# Generated by Django 2.1 on 2019-04-13 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantApp', '0005_auto_20190411_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='url',
            field=models.URLField(blank=True),
        ),
    ]
