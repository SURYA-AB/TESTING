# Generated by Django 3.0.9 on 2021-12-17 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist_app', '0032_files'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='file2',
            field=models.BinaryField(blank=True, null=True),
        ),
    ]
