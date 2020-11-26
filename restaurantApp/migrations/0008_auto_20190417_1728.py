# Generated by Django 2.1 on 2019-04-17 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantApp', '0007_auto_20190414_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dishes', to='restaurantApp.Restaurant'),
        ),
    ]
