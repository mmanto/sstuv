# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('publicador', '0003_auto_20150217_1117'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo',
            name='otroContenido',
            field=tinymce.models.HTMLField(default=0),
            preserve_default=False,
        ),
    ]
