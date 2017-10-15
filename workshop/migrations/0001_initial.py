# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-02 03:01
from __future__ import unicode_literals

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
            name='Workshop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('overview', models.TextField()),
                ('course_details', models.TextField(blank=True)),
                ('project', models.TextField(blank=True)),
                ('link', models.URLField(blank=True)),
                ('other_info', models.TextField(blank=True)),
                ('level', models.CharField(blank=True, max_length=100)),
                ('number_of_seats', models.IntegerField()),
                ('poster', models.ImageField(blank=True, null=True, upload_to='workshop/poster/')),
                ('contact_info', models.CharField(blank=True, max_length=200, null=True)),
                ('start_date_time', models.DateTimeField()),
                ('end_date_time', models.DateTimeField()),
                ('price', models.FloatField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WorkshopFeedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('comment', models.CharField(max_length=500)),
                ('workshop', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='workshop.Workshop')),
            ],
        ),
        migrations.CreateModel(
            name='WorkshopGallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='workshop/images/')),
                ('workshop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workshop.Workshop')),
            ],
        ),
        migrations.CreateModel(
            name='WorkshopRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('roll_number', models.CharField(max_length=100)),
                ('batch', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=50)),
                ('paid', models.BooleanField(default=False)),
                ('male_or_female', models.CharField(blank=True, max_length=20)),
                ('hostel_details', models.CharField(blank=True, max_length=200)),
                ('course', models.CharField(blank=True, max_length=50)),
                ('section', models.CharField(blank=True, max_length=50)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('workshop', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='workshop.Workshop')),
            ],
        ),
    ]
