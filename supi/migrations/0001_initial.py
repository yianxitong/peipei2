# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-03-11 14:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('major', models.CharField(max_length=20, verbose_name='专业')),
                ('num_of_men', models.IntegerField(db_column='男生数', verbose_name='男生数')),
                ('num_of_women', models.IntegerField(db_column='女生数', verbose_name='女生数')),
                ('school', models.CharField(db_column='学校', max_length=15, null=True, verbose_name='学校')),
                ('isDelete', models.BooleanField(db_column='是否删除', default=False, verbose_name='是否删除')),
            ],
            options={
                'db_table': 'majors',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_name', models.CharField(db_column='姓名', db_index=True, max_length=20, verbose_name='姓名')),
                ('sid', models.IntegerField(db_column='学号', default='0', primary_key=True, serialize=False, verbose_name='学号')),
                ('school', models.CharField(db_column='学校', max_length=15, null=True, verbose_name='学校')),
                ('gender', models.BooleanField(db_column='性别', default=False, verbose_name='性别')),
                ('isDelete', models.BooleanField(db_column='是否删除', default=False, verbose_name='是否删除')),
                ('major', models.ForeignKey(db_column='专业', null=True, on_delete=django.db.models.deletion.CASCADE, to='supi.Major', verbose_name='专业')),
            ],
            options={
                'db_table': 'students',
                'ordering': ['sid'],
            },
        ),
    ]