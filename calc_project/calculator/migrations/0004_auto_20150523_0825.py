# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0003_auto_20150519_0947'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calculator_machine',
            name='eight',
        ),
        migrations.RemoveField(
            model_name='calculator_machine',
            name='five',
        ),
        migrations.RemoveField(
            model_name='calculator_machine',
            name='four',
        ),
        migrations.RemoveField(
            model_name='calculator_machine',
            name='nine',
        ),
        migrations.RemoveField(
            model_name='calculator_machine',
            name='one',
        ),
        migrations.RemoveField(
            model_name='calculator_machine',
            name='seven',
        ),
        migrations.RemoveField(
            model_name='calculator_machine',
            name='six',
        ),
        migrations.RemoveField(
            model_name='calculator_machine',
            name='three',
        ),
        migrations.RemoveField(
            model_name='calculator_machine',
            name='two',
        ),
    ]
