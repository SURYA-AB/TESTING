# Generated by Django 3.0.9 on 2021-10-27 21:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist_app', '0005_auto_20211027_1751'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='edit_page',
            name='oldid',
        ),
    ]
