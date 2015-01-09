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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('caracteristica', models.CharField(max_length=200)),
                ('numero', models.CharField(max_length=200)),
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
                ('expediente_ptr', models.OneToOneField(serialize=False, to='documentos.Expediente', parent_link=True, auto_created=True, primary_key=True)),
                ('region', models.CharField(max_length=200)),
                ('partido', models.OneToOneField(to='comun.Partido')),
            ],
            options={
            },
            bases=('documentos.expediente',),
        ),
        migrations.CreateModel(
            name='Pase',
            fields=[
                ('departamento_origen', models.OneToOneField(serialize=False, to='comun.Departamento', primary_key=True)),
                ('fecha', models.DateTimeField(verbose_name='fecha de movimiento')),
                ('expediente', models.ForeignKey(to='documentos.Expediente')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
