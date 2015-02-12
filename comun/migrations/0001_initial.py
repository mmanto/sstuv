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
<<<<<<< HEAD
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
=======
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
>>>>>>> 10ec905fd09b423b90611b4466510b330841dc11
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
<<<<<<< HEAD
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('codigo', models.IntegerField(default=0)),
                ('nombre', models.CharField(max_length=200)),
                ('codcas', models.CharField(max_length=20, default=0)),
=======
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('codigo', models.IntegerField(default=0)),
                ('nombre', models.CharField(max_length=200)),
                ('codcas', models.CharField(default=0, max_length=20)),
>>>>>>> 10ec905fd09b423b90611b4466510b330841dc11
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
