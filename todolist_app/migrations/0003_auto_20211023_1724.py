# Generated by Django 3.0.9 on 2021-10-23 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist_app', '0002_auto_20211023_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edit_page',
            name='old_id',
            field=models.IntegerField(),
        ),
    ]