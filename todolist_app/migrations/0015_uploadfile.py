# Generated by Django 3.0.9 on 2021-11-18 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist_app', '0014_auto_20211118_1645'),
    ]

    operations = [
        migrations.CreateModel(
            name='uploadfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploaded_file', models.BinaryField(null=True)),
            ],
        ),
    ]