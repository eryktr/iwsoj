# Generated by Django 2.2.6 on 2019-10-25 21:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tasks', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Passed', 'OK'), ('Rejected', 'REJECTED'), ('Pending', 'PENDING')], default='Pending', max_length=12)),
                ('sourceCode', models.TextField()),
                ('language', models.CharField(choices=[('C', 'C'), ('C++', 'CPP'), ('GO', 'GO'), ('Python', 'PYTHON'), ('Java', 'JAVA')], max_length=8)),
                ('createdate', models.DateTimeField(default=django.utils.timezone.now)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.Task')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
