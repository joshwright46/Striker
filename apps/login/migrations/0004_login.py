# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-07-26 20:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_remove_user_confirm_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
