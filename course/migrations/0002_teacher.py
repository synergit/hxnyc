# Generated by Django 3.1.2 on 2020-11-11 02:44

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_name', models.CharField(max_length=250, verbose_name='teacher name')),
                ('teacher_email', models.CharField(max_length=250, verbose_name='teacher email')),
                ('created_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='created date')),
                ('modified_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='modified data')),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='creator')),
            ],
        ),
    ]
