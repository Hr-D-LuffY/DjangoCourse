# Generated by Django 4.2.7 on 2023-12-26 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_alter_post_author'),
        ('author', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Author',
        ),
    ]
