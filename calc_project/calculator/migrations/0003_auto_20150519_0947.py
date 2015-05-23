# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0002_auto_20150519_0921'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='numbers',
            name='calculator_machine',
        ),
        migrations.DeleteModel(
            name='Numbers',
        ),
        migrations.RemoveField(
            model_name='operators',
            name='operators',
        ),
        migrations.DeleteModel(
            name='Operators',
        ),
        migrations.AddField(
            model_name='calculator_machine',
            name='eight',
            field=models.DecimalField(default=b'8', unique=True, max_digits=1, decimal_places=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='calculator_machine',
            name='five',
            field=models.DecimalField(default=b'5', unique=True, max_digits=1, decimal_places=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='calculator_machine',
            name='four',
            field=models.DecimalField(default=b'4', unique=True, max_digits=1, decimal_places=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='calculator_machine',
            name='nine',
            field=models.DecimalField(default=b'9', unique=True, max_digits=1, decimal_places=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='calculator_machine',
            name='one',
            field=models.DecimalField(default=b'1', unique=True, max_digits=1, decimal_places=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='calculator_machine',
            name='seven',
            field=models.DecimalField(default=b'7', unique=True, max_digits=1, decimal_places=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='calculator_machine',
            name='six',
            field=models.DecimalField(default=b'6', unique=True, max_digits=1, decimal_places=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='calculator_machine',
            name='three',
            field=models.DecimalField(default=b'3', unique=True, max_digits=1, decimal_places=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='calculator_machine',
            name='two',
            field=models.DecimalField(default=b'2', unique=True, max_digits=1, decimal_places=0),
            preserve_default=True,
        ),
    ]
