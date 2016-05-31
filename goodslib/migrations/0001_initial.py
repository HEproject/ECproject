# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Good_brand',
            fields=[
                ('brand_id', models.PositiveIntegerField(serialize=False, primary_key=True)),
                ('brand_name', models.CharField(max_length=20)),
                ('brand_desc', models.CharField(max_length=20)),
                ('brand_imgurl', models.CharField(max_length=20)),
                ('is_view', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('goods_num_id', models.PositiveIntegerField(serialize=False, primary_key=True)),
                ('goods_name', models.CharField(max_length=20)),
                ('is_new', models.BooleanField(default=True)),
                ('is_hot', models.BooleanField(default=True)),
                ('is_recommend', models.SmallIntegerField(default=0)),
                ('is_free', models.CharField(max_length=20)),
                ('add_date', models.DateTimeField(auto_now=True, auto_now_add=True)),
                ('brand_id', models.ForeignKey(to='goodslib.Good_brand')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Goods_attr',
            fields=[
                ('goods_attr_id', models.PositiveIntegerField(serialize=False, primary_key=True)),
                ('good_attr', models.CharField(max_length=20)),
                ('is_descard', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Goods_color',
            fields=[
                ('goods_color_id', models.PositiveIntegerField(serialize=False, primary_key=True)),
                ('good_color', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Goods_kind',
            fields=[
                ('goods_kind_id', models.PositiveIntegerField(serialize=False, primary_key=True)),
                ('good_kind', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Goods_lib',
            fields=[
                ('goods_id', models.PositiveIntegerField(serialize=False, primary_key=True)),
                ('goods_cost', models.IntegerField(default=0)),
                ('goods_price', models.IntegerField(default=0)),
                ('goods_size', models.IntegerField(default=0)),
                ('goods_color_id', models.ForeignKey(to='goodslib.Goods_color')),
                ('goods_num_id', models.ForeignKey(to='goodslib.Goods')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='goods',
            name='goods_attr_id',
            field=models.ForeignKey(to='goodslib.Goods_attr'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='goods',
            name='goods_kind_id',
            field=models.ForeignKey(to='goodslib.Goods_kind'),
            preserve_default=True,
        ),
    ]
