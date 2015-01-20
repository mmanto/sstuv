# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('documentos', '0004_auto_20150119_1714'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='keyvaluepair',
            name='container',
        ),
        migrations.DeleteModel(
            name='Dictionary',
        ),
        migrations.DeleteModel(
            name='KeyValuePair',
        ),
    ]
