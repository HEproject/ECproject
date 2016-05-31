from django.db import models
# Create your models here.

class Good_brand(models.Model):
    brand_id = models.PositiveIntegerField(primary_key=True)
    brand_name = models.CharField(max_length = 20)
    brand_desc = models.CharField(max_length = 20)
    brand_imgurl = models.CharField(max_length = 20)
    is_view = models.BooleanField(default=True)
    def __unicode__(self):
        return self.brand_id


class Goods_kind(models.Model):
    goods_kind_id  = models.PositiveIntegerField(primary_key=True)
    good_kind = models.CharField(max_length = 20)
    def __unicode__(self):
        return self.goods_kind_id

class Goods_attr(models.Model):
    goods_attr_id = models.PositiveIntegerField(primary_key=True)
    good_attr = models.CharField(max_length = 20)
    is_descard = models.BooleanField(default=True)
    def __unicode__(self):
        return self.goods_attr_id

class Goods_color(models.Model):
    goods_color_id =  models.PositiveIntegerField(primary_key=True)
    good_color = models.CharField(max_length = 20)
    def __unicode__(self):
        return self.goods_color_id


class Goods(models.Model):
    goods_num_id = models.PositiveIntegerField(primary_key=True)
    goods_name = models.CharField(max_length = 20)
    is_new = models.BooleanField(default=True)
    is_hot = models.BooleanField(default=True)
    is_recommend =  models.SmallIntegerField(default = 0)
    is_free = models.CharField(max_length = 20)
    add_date = models.DateTimeField(auto_now=True,  auto_now_add=True)
    brand_id = models.ForeignKey(Good_brand)
    goods_kind_id = models.ForeignKey(Goods_kind)
    goods_attr_id = models.ForeignKey(Goods_attr)
    def __unicode__(self):
        return self.goods_num_id


class Goods_lib(models.Model):
    goods_id = models.PositiveIntegerField(primary_key=True)
    goods_price = models.IntegerField(default=0)
    goods_cost = models.IntegerField(default=0)
    market_price = models.IntegerField(default=0)
    goods_size = models.IntegerField(default=0)
    goods_color_id = models.ForeignKey(Goods_color)
    goods_num_id = models.ForeignKey(Goods)
    def __unicode__(self):
        return self.goods_id
