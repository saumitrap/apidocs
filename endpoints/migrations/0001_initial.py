# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Endpoint',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.CharField(max_length=255)),
                ('method', models.PositiveSmallIntegerField(choices=[(1, b'GET'), (2, b'POST'), (3, b'PUT'), (4, b'DELETE')])),
                ('url', models.CharField(max_length=255)),
                ('descr', models.TextField()),
                ('request_example', models.TextField()),
                ('response_example', models.TextField()),
                ('response_descr', models.TextField()),
                ('order_rank', models.PositiveSmallIntegerField(default=99)),
            ],
        ),
        migrations.CreateModel(
            name='Error',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.PositiveSmallIntegerField(unique=True)),
                ('message', models.CharField(max_length=1000)),
                ('descr', models.TextField(blank=True)),
                ('order_rank', models.PositiveSmallIntegerField(default=99)),
                ('endpoint', models.ForeignKey(to='endpoints.Endpoint')),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.CharField(max_length=255)),
                ('descr', models.TextField()),
                ('order_rank', models.PositiveSmallIntegerField(default=99)),
            ],
        ),
        migrations.CreateModel(
            name='Param',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('param_type', models.PositiveSmallIntegerField(choices=[(1, b'Path Parameter'), (2, b'Request Parameter')])),
                ('key', models.CharField(max_length=255)),
                ('is_required', models.BooleanField(default=True)),
                ('data_type', models.PositiveSmallIntegerField(choices=[(1, b'integer'), (2, b'number'), (3, b'string')])),
                ('descr', models.TextField(blank=True)),
                ('order_rank', models.PositiveSmallIntegerField(default=99)),
                ('endpoint', models.ForeignKey(to='endpoints.Endpoint')),
            ],
        ),
        migrations.AddField(
            model_name='endpoint',
            name='group',
            field=models.ForeignKey(to='endpoints.Group'),
        ),
    ]
