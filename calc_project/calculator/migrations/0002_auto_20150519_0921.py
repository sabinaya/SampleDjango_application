# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Operators',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('plus', models.CharField(unique=True, max_length=1)),
                ('minus', models.CharField(unique=True, max_length=1)),
                ('divide', models.CharField(unique=True, max_length=1)),
                ('multiply', models.CharField(unique=True, max_length=1)),
                ('equal', models.CharField(unique=True, max_length=1)),
                ('dot', models.CharField(unique=True, max_length=1)),
                ('operators', models.ForeignKey(to='calculator.Calculator_machine')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='calculator_machine',
            name='result',
            field=models.CharField(max_length=100),
        ),
    ]
