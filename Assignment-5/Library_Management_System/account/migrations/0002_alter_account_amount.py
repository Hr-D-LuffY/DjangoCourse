# Generated by Django 4.2.7 on 2024-01-07 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='amount',
            field=models.IntegerField(default=0),
        ),
    ]
