#!/usr/bin/env python
#coding:utf-8
 
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ECproject.settings")
 
'''
Django 版本大于等于1.7的时候，需要加上下面两句
import django
django.setup()
否则会抛出错误 django.core.exceptions.AppRegistryNotReady: Models aren't loaded yet.
'''
 
import django
if django.VERSION >= (1, 7):#自动判断版本
    django.setup()
 
 
def main():
    from goodslib.models import Goods
    f = open('goods.txt')
    for line in f:
        def __unicode__(self):
            title,content = line.split('*')
            Goods.objects.create(goods_num_id=goods_num_id,\
			         goods_name=goods_name,\
			         is_new=is_new,\
			         is_hot=is_hot,\
			         is_recommend=is_recommend,\
			         is_free=is_free,\
			         add_date=add_date,\
			         brand_id=brand_id,\
			         goods_kind_id=goods_kind_id,\
			         goods_attr_id=goods_attr_id)
            Goods.save()
    f.close()
 
if __name__ == "__main__":
    main()
    print('Done!')
