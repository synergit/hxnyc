# Generated by Django 3.1.2 on 2020-11-14 04:08

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentExt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=135, verbose_name='student name')),
                ('contact_name', models.CharField(max_length=135, verbose_name='contact name')),
                ('address', models.CharField(max_length=135, verbose_name='address')),
                ('phone', models.CharField(max_length=135, verbose_name='phone')),
                ('email', models.EmailField(max_length=135, verbose_name='email')),
                ('enrolled_course', models.CharField(max_length=135, verbose_name='enrolled course')),
                ('student_dob', models.CharField(max_length=135, verbose_name='student DOB')),
                ('created_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='created date')),
                ('modified_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='modified data')),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='creator')),
            ],
        ),
    ]
