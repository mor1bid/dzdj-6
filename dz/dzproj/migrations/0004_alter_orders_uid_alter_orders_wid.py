# Generated by Django 5.0.3 on 2024-03-18 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dzproj', '0003_orders_delete_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='uid',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='orders',
            name='wid',
            field=models.IntegerField(default=0),
        ),
    ]
