# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comun', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expediente',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('organismo', models.IntegerField()),
                ('numero', models.CharField(max_length=200)),
                ('anio', models.IntegerField()),
                ('caracteristica', models.CharField(max_length=200)),
                ('fecha', models.DateField(verbose_name='Fecha')),
                ('alcance', models.CharField(max_length=200)),
                ('cuerpo', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ExpedienteLey',
            fields=[
                ('expediente_ptr', models.OneToOneField(serialize=False, primary_key=True, to='documentos.Expediente', parent_link=True, auto_created=True)),
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
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
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
