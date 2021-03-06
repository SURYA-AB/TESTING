# Generated by Django 3.0.9 on 2021-10-28 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todolist_app', '0007_logs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edit_page',
            name='old_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='todolist_app.Tasklist'),
        ),
        migrations.AlterField(
            model_name='logs',
            name='task_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='todolist_app.edit_page'),
        ),
    ]
