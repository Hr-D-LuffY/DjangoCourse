# Generated by Django 4.2.7 on 2024-01-07 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='category',
            new_name='Bookcategory',
        ),
    ]
