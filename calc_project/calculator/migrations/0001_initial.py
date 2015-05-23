# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calculator_machine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('result', models.DecimalField(max_digits=100, decimal_places=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Numbers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('zero', models.DecimalField(unique=True, max_digits=1, decimal_places=0)),
                ('one', models.DecimalField(unique=True, max_digits=1, decimal_places=0)),
                ('two', models.DecimalField(unique=True, max_digits=1, decimal_places=0)),
                ('three', models.DecimalField(unique=True, max_digits=1, decimal_places=0)),
                ('four', models.DecimalField(unique=True, max_digits=1, decimal_places=0)),
                ('five', models.DecimalField(unique=True, max_digits=1, decimal_places=0)),
                ('six', models.DecimalField(unique=True, max_digits=1, decimal_places=0)),
                ('seven', models.DecimalField(unique=True, max_digits=1, decimal_places=0)),
                ('eight', models.DecimalField(unique=True, max_digits=1, decimal_places=0)),
                ('nine', models.DecimalField(unique=True, max_digits=1, decimal_places=0)),
                ('calculator_machine', models.ForeignKey(to='calculator.Calculator_machine')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
