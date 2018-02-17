# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-15 02:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('evaluator', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unanswered', models.BooleanField(default=False)),
                ('marks_awarded', models.IntegerField()),
                ('your_response', models.CharField(max_length=1000)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer_related', to='evaluator.Question')),
            ],
        ),
    ]
