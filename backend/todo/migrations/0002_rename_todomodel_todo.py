# Generated by Django 4.0.4 on 2022-05-24 08:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TodoModel',
            new_name='Todo',
        ),
    ]
