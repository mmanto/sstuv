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
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
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

                ('expediente_ptr', models.OneToOneField(to='documentos.Expediente', primary_key=True, serialize=False, parent_link=True, auto_created=True)),
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
<<<<<<< HEAD
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField(verbose_name='fecha de movimiento')),
                ('departamento_destino', models.ForeignKey(to='comun.Departamento', related_name='destino')),
                ('departamento_origen', models.ForeignKey(to='comun.Departamento', related_name='origen')),
                ('expediente', models.ForeignKey(to='documentos.Expediente', related_name='pase_set')),
=======
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField(verbose_name='fecha de movimiento')),
                ('departamento_destino', models.ForeignKey(related_name='destino', to='comun.Departamento')),
                ('departamento_origen', models.ForeignKey(related_name='origen', to='comun.Departamento')),
                ('expediente', models.ForeignKey(related_name='pase_set', to='documentos.Expediente')),
>>>>>>> 10ec905fd09b423b90611b4466510b330841dc11
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
