# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField(default=0)),
                ('nombre', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Partido',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField(default=0)),
                ('nombre', models.CharField(max_length=200)),
                ('codcas', models.CharField(max_length=20, default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
