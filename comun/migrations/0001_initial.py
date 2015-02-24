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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.IntegerField(default=0)),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.CharField(max_length=250)),
                ('descripcion2', models.CharField(max_length=250)),
                ('descripcion3', models.CharField(max_length=250)),
                ('descripcion4', models.CharField(max_length=250)),
                ('direccion', models.CharField(max_length=250)),
                ('direccion2', models.CharField(max_length=250)),
                ('direccion3', models.CharField(max_length=250)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Partido',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.IntegerField(default=0)),
                ('nombre', models.CharField(max_length=200)),
                ('codcas', models.CharField(max_length=20, default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
