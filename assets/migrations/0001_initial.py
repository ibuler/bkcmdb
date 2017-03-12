# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ip', models.GenericIPAddressField(unique=True, verbose_name=b'IP')),
                ('port', models.IntegerField(default=22, verbose_name=b'\xe7\xab\xaf\xe5\x8f\xa3')),
                ('username', models.CharField(max_length=20, verbose_name=b'\xe7\xae\xa1\xe7\x90\x86\xe7\x94\xa8\xe6\x88\xb7\xe5\x90\x8d')),
                ('password', models.CharField(max_length=32, verbose_name=b'\xe7\xae\xa1\xe7\x90\x86\xe5\xaf\x86\xe7\xa0\x81')),
                ('os', models.CharField(max_length=2, verbose_name=b'\xe7\xb3\xbb\xe7\xbb\x9f\xe5\xb9\xb3\xe5\x8f\xb0', choices=[(b'C', b'CentOS'), (b'U', b'Ubuntu'), (b'D', b'Debian'), (b'R', b'Redhat'), (b'B', b'BSD')])),
                ('is_active', models.BooleanField(default=True, verbose_name=b'\xe6\xbf\x80\xe6\xb4\xbb')),
            ],
        ),
    ]
