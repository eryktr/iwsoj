# Generated by Django 2.2.6 on 2019-10-25 21:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('statement', models.TextField()),
                ('createdate', models.DateTimeField(default=django.utils.timezone.now)),
                ('complexity', models.IntegerField(choices=[(1, 'EASY'), (2, 'MEDIUM'), (3, 'HARD'), (4, 'COMPETITIVE')])),
                ('definition', models.TextField()),
            ],
        ),
    ]
