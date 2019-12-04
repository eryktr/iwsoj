# Generated by Django 2.2.6 on 2019-12-02 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_auto_20191029_1004'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='input',
            new_name='input_hidden',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='output',
            new_name='output_hidden',
        ),
        migrations.AddField(
            model_name='task',
            name='input_public',
            field=models.TextField(default='changeme'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='output_public',
            field=models.TextField(default='changeme'),
            preserve_default=False,
        ),
    ]
