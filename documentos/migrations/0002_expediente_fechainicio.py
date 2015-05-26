# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('documentos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='expediente',
            name='fechaInicio',
            field=models.DateField(verbose_name='FechaInicio', default=1),
            preserve_default=False,
        ),
    ]
