# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-11 22:26
from __future__ import unicode_literals

from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=128)),
                ('suburb', models.CharField(max_length=128)),
                ('current_employer', models.CharField(blank=True, max_length=128, null=True)),
                ('current_job_title', models.CharField(blank=True, max_length=128, null=True)),
                ('industries', models.CharField(blank=True, max_length=512, null=True)),
                ('job_titles', models.CharField(blank=True, max_length=512, null=True)),
                ('perm_salary', models.CharField(blank=True, max_length=128, null=True)),
                ('languages', models.CharField(blank=True, max_length=512, null=True)),
                ('qualifications', models.CharField(blank=True, max_length=512, null=True)),
                ('notice_period', models.PositiveIntegerField()),
                ('owning_consultant', models.CharField(max_length=128)),
                ('randstad_id', models.IntegerField()),
                ('status', models.CharField(max_length=32)),
                ('created', models.DateTimeField()),
                ('follow_up', models.DateTimeField(blank=True, null=True)),
                ('last_contact', models.DateTimeField(blank=True, null=True)),
                ('last_electronic_contact', models.DateTimeField(blank=True, null=True)),
                ('last_interview', models.DateTimeField(blank=True, null=True)),
                ('updated', models.DateTimeField()),
            ],
        ),
    ]