# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comun', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expediente',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('organismo', models.IntegerField()),
                ('numero', models.CharField(max_length=200)),
                ('anio', models.IntegerField()),
                ('caracteristica', models.CharField(max_length=200)),
                ('fecha', models.DateField(verbose_name='Fecha')),
#                 ('fechaInicio', models.DateField(verbose_name='FechaInicio')),
                ('alcance', models.CharField(max_length=200)),
                ('cuerpo', models.CharField(max_length=200)),
                ('extracto', models.CharField(max_length=5000)),
                ('cant_fojas', models.IntegerField(default=0)),
                ('observacion', models.CharField(max_length=10000)),
                ('consolidacion', models.BooleanField(default=False)),
                ('usuarioAlta', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ExpedienteLey',
            fields=[
                ('expediente_ptr', models.OneToOneField(primary_key=True, parent_link=True, auto_created=True, to='documentos.Expediente', serialize=False)),
                ('region', models.CharField(max_length=200)),
                ('partido', models.ForeignKey(to='comun.Partido')),
            ],
            options={
            },
            bases=('documentos.expediente',),
        ),
        migrations.CreateModel(
            name='Pase',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('numero', models.IntegerField()),
                ('fecha', models.DateTimeField(verbose_name='fecha de movimiento')),
                ('estado', models.CharField(max_length='50')),
                ('departamento_destino', models.ForeignKey(to='comun.Departamento', related_name='destino')),
                ('departamento_origen', models.ForeignKey(to='comun.Departamento', related_name='origen')),
                ('expediente', models.ForeignKey(to='documentos.Expediente', related_name='pase_set')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
