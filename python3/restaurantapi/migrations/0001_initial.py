# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(unique=True, max_length=32)),
                ('description', models.CharField(max_length=200)),
                ('available', models.BooleanField(default=False)),
                ('chef', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(unique=True, max_length=32)),
                ('description', models.CharField(max_length=200)),
                ('cost_to_make', models.DecimalField(decimal_places=2, max_digits=5)),
                ('sale_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('available', models.BooleanField(default=False)),
                ('menu', models.ForeignKey(to='restaurantapi.Menu')),
            ],
        ),
    ]
