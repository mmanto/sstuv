# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('publicador', '0002_articulo_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='contenido',
            field=tinymce.models.HTMLField(),
            preserve_default=True,
        ),
    ]
