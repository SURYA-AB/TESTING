# Generated by Django 3.0.9 on 2021-11-16 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist_app', '0010_edit_page_blob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edit_page',
            name='blob',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
