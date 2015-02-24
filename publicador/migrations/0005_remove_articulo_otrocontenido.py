# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publicador', '0004_articulo_otrocontenido'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articulo',
            name='otroContenido',
        ),
    ]
