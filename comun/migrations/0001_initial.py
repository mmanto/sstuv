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
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
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
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('codigo', models.IntegerField(default=0)),
                ('nombre', models.CharField(max_length=200)),
                ('codcas', models.CharField(default=0, max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
